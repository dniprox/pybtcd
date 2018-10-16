from enum import Enum
import io
from .opcode import *
from .error import *
from wire.msg_tx import MsgTx, write_tx_out
from chainhash import *

MaxOpsPerScript = 201  # Max number of non-push operations.
MaxPubKeysPerMultiSig = 20  # Multisig can't have more sigs than this.
MaxScriptElementSize = 520  # Max bytes pushable to the stack.

# payToWitnessPubKeyHashDataSize is the size of the witness program's
# data push for a pay-to-witness-pub-key-hash output.
payToWitnessPubKeyHashDataSize = 20

# payToWitnessScriptHashDataSize is the size of the witness program's
# data push for a pay-to-witness-script-hash output.
payToWitnessScriptHashDataSize = 32


# SigHashType represents hash type bits at the end of a signature.
class SigHashType(Enum):
    SigHashOld = 0x0
    SigHashAll = 0x1
    SigHashNone = 0x2
    SigHashSingle = 0x3
    SigHashAnyOneCanPay = 0x80


# is_small_int returns whether or not the opcode is considered a small integer,
# which is an OP_0, or OP_1 through OP_16.
def is_small_int(op) -> bool:
    if op.value == OP_0 or OP_1 <= op.value <= OP_16:
        return True
    else:
        return False


# isWitnessPubKeyHash returns true if the passed script is a
# pay-to-witness-pubkey-hash, and false otherwise.
def is_witness_pub_key_hash(pops) -> bool:
    return len(pops) == 2 and pops[0].opcode.value == OP_0 and pops[1].opcode.value == OP_DATA_20


# isScriptHash returns true if the script passed is a pay-to-script-hash
# transaction, false otherwise.
def is_script_hash(pops) -> bool:
    return len(pops) == 3 and \
           pops[0].opcode.value == OP_HASH160 and \
           pops[1].opcode.value == OP_DATA_20 and \
           pops[2].opcode.value == OP_EQUAL


# IsPayToScriptHash returns true if the script is in the standard
# pay-to-script-hash (P2SH) format, false otherwise.
def is_pay_to_script_hash(script) -> bool:
    try:
        pops = parse_script(script)
    except ScriptError:
        return False
    return is_script_hash(pops)


# isWitnessScriptHash returns true if the passed script is a
# pay-to-witness-script-hash transaction, false otherwise.
def is_witness_script_hash(pops) -> bool:
    return len(pops) == 2 and pops[0].opcode.value == OP_0 and pops[1].opcode.value == OP_DATA_32


# isPushOnly returns true if the script only pushes data, false otherwise.
def is_push_only(pops) -> bool:
    # NOTE: This function does NOT verify opcodes directly since it is
    # internal and is only called with parsed opcodes for scripts that did
    # not have any parse errors.  Thus, consensus is properly maintained.

    for pop in pops:
        if pop.opcode.value > OP_16:
            return False
    return True


# IsPushOnlyScript returns whether or not the passed script only pushes data.
#
# False will be returned when the script does not parse
def is_push_only_script(script: bytes) -> bool:
    pops = parse_script(script)
    return is_push_only(pops)


# IsWitnessProgram returns true if the passed script is a valid witness
# program which is encoded according to the passed witness program version. A
# witness program must be a small integer (from 0-16), followed by 2-40 bytes
# of pushed data.
def is_script_witness_program(script: bytes) -> bool:
    # The length of the script must be between 4 and 42 bytes. The
    # smallest program is the witness version, followed by a data push of
    # 2 bytes.  The largest allowed witness program has a data push of
    # 40-bytes.
    if len(script) < 4 or len(script) > 42:
        return False

    pops = parse_script(script)
    return is_pops_witness_program(pops)


# isWitnessProgram returns true if the passed script is a witness program, and
# false otherwise. A witness program MUST adhere to the following constraints:
# there must be exactly two pops (program version and the program itself), the
# first opcode MUST be a small integer (0-16), the push data MUST be
# canonical, and finally the size of the push data must be between 2 and 40
# bytes.
def is_pops_witness_program(pops):
    return len(pops) == 2 and \
           is_small_int(pops[0].opcode) and \
           canonical_push(pops[1]) and \
           2 <= len(pops[1].data) <= 40


# ExtractWitnessProgramInfo attempts to extract the witness program version,
# as well as the witness program itself from the passed script.
def extract_witness_program_info(script: bytes):
    pops = parse_script(script)

    # If at this point, the scripts doesn't resemble a witness program,
    # then we'll exit early as there isn't a valid version or program to
    # extract.
    if not is_pops_witness_program(pops):
        # desc = "script is not a witness program, unable to extract version or witness program"
        raise NotWitnessProgramError

    witness_version = as_small_int(pops[0].opcode)
    witness_program = pops[1].data
    return witness_version, witness_program


# asSmallInt returns the passed opcode, which must be true according to
# isSmallInt(), as an integer.
def as_small_int(op) -> int:
    if op.value == OP_0:
        return 0
    return int(op.value - (OP_1 - 1))


# getSigOpCount is the implementation function for counting the number of
# signature operations in the script provided by pops. If precise mode is
# requested then we attempt to count the number of operations for a multisig
# op. Otherwise we use the maximum.
def _get_sig_op_count(pops, precise) -> int:
    nsigs = 0
    for i, pop in enumerate(pops):
        value = pop.opcode.value
        if value in (OP_CHECKSIG, OP_CHECKSIGVERIFY):
            nsigs += 1
        elif value in (OP_CHECKMULTISIG, OP_CHECKMULTISIGVERIFY):
            if precise and i > 0 and OP_1 <= pops[i - 1].opcode.value <= OP_16:
                nsigs += as_small_int(pops[i - 1].opcode)
            else:
                nsigs += MaxPubKeysPerMultiSig
        else:
            # not a sigop
            pass
    return nsigs


# GetSigOpCount provides a quick count of the number of signature operations
# in a script. a CHECKSIG operations counts for 1, and a CHECK_MULTISIG for 20.
# If the script fails to parse, then the count up to the point of failure is
# returned.
def get_sig_op_count(script: bytes):
    pops = parse_script_no_err(script)
    return _get_sig_op_count(pops, False)


# GetPreciseSigOpCount returns the number of signature operations in
# scriptPubKey.  If bip16 is true then scriptSig may be searched for the
# Pay-To-Script-Hash script in order to find the precise number of signature
# operations in the transaction.  If the script fails to parse, then the count
# up to the point of failure is returned.
def get_precise_sig_op_count(script_sig, script_pub_key, bip16):
    pops = parse_script_no_err(script_pub_key)

    # Treat non P2SH transactions as normal.
    if not (bip16 and is_script_hash(pops)):
        return _get_sig_op_count(pops, precise=True)

    # The public key script is a pay-to-script-hash, so parse the signature
    # script to get the final item.  Scripts that fail to fully parse count
    # as 0 signature operations.
    try:
        sig_pops = parse_script(script_sig)
    except ScriptError:
        return 0

    # The signature script must only push data to the stack for P2SH to be
    # a valid pair, so the signature operation count is 0 when that is not
    # the case.
    if (not is_push_only(sig_pops)) or len(sig_pops) == 0:
        return 0

    # The P2SH script is the last item the signature script pushes to the
    # stack.  When the script is empty, there are no signature operations.
    sh_script = sig_pops[-1].data
    if len(sh_script) == 0:
        return 0

    # Parse the P2SH script and don't check the error since parseScript
    # returns the parsed-up-to-error list of pops and the consensus rules
    # dictate signature operations are counted up to the first parse
    # failure.
    sh_pops = parse_script_no_err(sh_script)
    return _get_sig_op_count(sh_pops, precise=True)


def get_witness_sig_op_count(sig_script, pk_script, witness) -> int:
    # If this is a regular witness program, then we can proceed directly
    # to counting its signature operations without any further processing.
    if is_script_witness_program(pk_script):
        return _get_witness_sig_op_count(pk_script, witness)

    # Next, we'll check the sigScript to see if this is a nested p2sh
    # witness program. This is a case wherein the sigScript is actually a
    # datapush of a p2wsh witness program.
    try:
        sig_pops = parse_script(sig_script)
    except:
        return 0

    if is_pay_to_script_hash(pk_script) and is_push_only(sig_pops) and is_script_witness_program(sig_script[1:]):
        return _get_witness_sig_op_count(sig_script[1:], witness)

    return 0


# getWitnessSigOps returns the number of signature operations generated by
# spending the passed witness program wit the passed witness. The exact
# signature counting heuristic is modified by the version of the passed
# witness program. If the version of the witness program is unable to be
# extracted, then 0 is returned for the sig op count.
def _get_witness_sig_op_count(pk_script, witness) -> int:
    # Attempt to extract the witness program version.
    try:
        witness_version, witness_program = extract_witness_program_info(pk_script)
    except Exception:
        return 0

    if witness_version == 0:
        if len(witness_program) == payToWitnessPubKeyHashDataSize:
            return 1
        elif len(witness_program) == payToWitnessScriptHashDataSize and len(witness) > 0:
            witness_script = witness[-1]
            pops = parse_script_no_err(witness_script)
            return _get_sig_op_count(pops, precise=True)

    return 0


# removeOpcode will remove any opcode matching ``opcode'' in the pops
def remove_opcode(pops, opcode):
    ret_pops = []
    for pop in pops:
        if pop.opcode.value != opcode:
            ret_pops.append(pop)
    return ret_pops


# canonicalPush returns true if the object is either not a push instruction
# or the push instruction contained wherein is matches the canonical form
# or using the smallest instruction to do the job. False otherwise.
def canonical_push(pop):
    opcode = pop.opcode.value
    data = pop.data
    data_len = len(pop.data)

    # opcode > OP_16 don't worry about canonical push
    if opcode > OP_16:
        return True

    # if you have one byte to push and it's value <= 16, use OP_2 - OP_16 to push
    # don't use OP_DATA_1 - OP_DATA_75
    if OP_0 < opcode < OP_PUSHDATA1 and data_len == 1 and data[0] <= 16:
        return False

    # if data_len < OP_PUSHDATA1, no need to use OP_PUSHDATA1, use OP_DATA1-OP_DATA_75
    if opcode == OP_PUSHDATA1 and data_len < OP_PUSHDATA1:
        return False

    # if push data len <= 0xffff(1 bytes max), no need to use OP_PUSHDATA2
    if opcode == OP_PUSHDATA2 and data_len <= 0xff:
        return False

    # if push data len <= 0xffff(2 bytes max), no need to use OP_PUSHDATA4
    if opcode == OP_PUSHDATA4 and data_len <= 0xffff:
        return False

    return True


def parse_script_template(script, opcodes):
    """
    Parse script to ParsedOpcode list
    :param []byte script: bytes of script to parse
    :param [] opcodes:  opcode_array, contains all OpCode
    :return:
    """

    return_script = []

    i = 0
    while i < len(script):
        instruction = script[i]
        op = opcodes[instruction]
        pop = ParsedOpcode(opcode=op)

        if op.length == 1:
            i += 1

        elif op.length > 1:
            if len(script[i:]) < op.length:  # TODO check if this len(script[i+1:]) or len(script[i:]?)
                desc = "opcode {} requires {} bytes, but script only has {} remaining".format(op.name, op.length,
                                                                                              len(script[i:]))
                raise ScriptError(c=ErrorCode.ErrMalformedPush, desc=desc, extra_data=return_script)

            pop.data = script[i + 1: i + op.length]
            i += op.length

        elif op.length < 0:
            off = i + 1
            if len(script[off:]) < -op.length:  # TODO check if this len(script[i+1:]) or len(script[i:]?)
                desc = "opcode {} requires {} bytes, but script only has {} remaining".format(op.name, op.length,
                                                                                              len(script[i:]))
                raise ScriptError(c=ErrorCode.ErrMalformedPush, desc=desc, extra_data=return_script)

            if op.length == -1:
                l = script[off]
            elif op.length == -2:
                l = script[off] | (script[off + 1] << 8)
            elif op.length == -4:
                l = script[off] | (script[off + 1] << 8) | (script[off + 2] << 16) | (script[off + 3] << 24)
            else:
                desc = "invalid opcode length {}".format(op.length)
                raise ScriptError(c=ErrorCode.ErrMalformedPush, desc=desc, extra_data=return_script)

            off += -op.length

            if l < 0 or l > len(script[off:]):  # TOCHANGE Consider to split l<0 error
                desc = "opcode {} pushes {} bytes, but script only has {} remaining".format(op.name, op.length,
                                                                                            len(script[off:]))
                raise ScriptError(c=ErrorCode.ErrMalformedPush, desc=desc, extra_data=return_script)

            pop.data = script[off: off + l]
            i += (1 - op.length + l)

        return_script.append(pop)
    return return_script


def parse_script_no_err(script):
    try:
        pops = parse_script_template(script, opcode_array)
    except ScriptError as e:
        pops = e.extra_data
    return pops


def parse_script(script):
    return parse_script_template(script, opcode_array)


def unparse_script(pops):
    script = bytearray()
    for pop in pops:
        script.extend(pop.bytes())
    return script


# calcHashPrevOuts calculates a single hash of all the previous outputs
# (txid:index) referenced within the passed transaction. This calculated hash
# can be re-used when validating all inputs spending segwit outputs, with a
# signature hash type of SigHashAll. This allows validation to re-use previous
# hashing computation, reducing the complexity of validating SigHashAll inputs
# from  O(N^2) to O(N).
def calc_hash_prevouts(tx: MsgTx):
    """

    :param wire.MsgTx tx:
    :return:
    """
    buffer = io.BytesIO()
    for tx_in in tx.tx_ins:
        # First write out the 32-byte transaction ID one of whose
        # outputs are being referenced by this input.
        buffer.write(tx_in.previous_out_point.hash.to_bytes())

        # Next, we'll encode the index of the referenced output as a
        # little endian integer.
        buffer.write(tx_in.previous_out_point.index.to_bytes(4, byteorder="little"))

    return double_hash_h(buffer.getvalue())


# calcHashSequence computes an aggregated hash of each of the sequence numbers
# within the inputs of the passed transaction. This single hash can be re-used
# when validating all inputs spending segwit outputs, which include signatures
# using the SigHashAll sighash type. This allows validation to re-use previous
# hashing computation, reducing the complexity of validating SigHashAll inputs
# from O(N^2) to O(N).
def calc_hash_sequence(tx: MsgTx):
    """

    :param wire.MsgTx tx:
    :return:
    """
    buffer = io.BytesIO()
    for tx_in in tx.tx_ins:
        buffer.write(tx_in.sequence.to_bytes(4, byteorder="little"))

    return double_hash_h(buffer.getvalue())


# calcHashOutputs computes a hash digest of all outputs created by the
# transaction encoded using the wire format. This single hash can be re-used
# when validating all inputs spending witness programs, which include
# signatures using the SigHashAll sighash type. This allows computation to be
# cached, reducing the total hashing complexity from O(N^2) to O(N).
def calc_hash_outputs(tx: MsgTx):
    """

    :param wire.MsgTx tx:
    :return:
    """
    buffer = io.BytesIO()
    for tx_out in tx.tx_outs:
        write_tx_out(buffer, 0, 0, tx_out)

    return double_hash_h(buffer.getvalue())
