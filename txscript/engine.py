import copy
import logging
import hashlib
import wire
from .stack import *
from .sig_cache import *
from .hash_cache import *
from .standard import *


_logger = logging.getLogger(__name__)

# MaxStackSize is the maximum combined height of stack and alt stack
# during execution.
MaxStackSize = 1000






class ScriptFlag(Enum):
    # ScriptBip16 defines whether the bip16 threshold has passed and thus
    # pay-to-script hash transactions will be fully validated.
    ScriptBip16 = 1 << 0

    # ScriptStrictMultiSig defines whether to verify the stack item
    # used by CHECKMULTISIG is zero length.
    ScriptStrictMultiSig = 1 << 1

    # ScriptDiscourageUpgradableNops defines whether to verify that
    # NOP1 through NOP10 are reserved for future soft-fork upgrades.  This
    # flag must not be used for consensus critical code nor applied to
    # blocks as this flag is only for stricter standard transaction
    # checks.  This flag is only applied when the above opcodes are
    # executed.
    ScriptDiscourageUpgradableNops = 1 << 2

    # ScriptVerifyCheckLockTimeVerify defines whether to verify that
    # a transaction output is spendable based on the locktime.
    # This is BIP0065.
    ScriptVerifyCheckLockTimeVerify = 1 << 3

    # ScriptVerifyCheckSequenceVerify defines whether to allow execution
    # pathways of a script to be restricted based on the age of the output
    # being spent.  This is BIP0112.
    ScriptVerifyCheckSequenceVerify = 1 << 4

    # ScriptVerifyCleanStack defines that the stack must contain only
    # one stack element after evaluation and that the element must be
    # true if interpreted as a boolean.  This is rule 6 of BIP0062.
    # This flag should never be used without the ScriptBip16 flag nor the
    # ScriptVerifyWitness flag.
    ScriptVerifyCleanStack = 1 << 5

    # ScriptVerifyDERSignatures defines that signatures are required
    # to compily with the DER format.
    ScriptVerifyDERSignatures = 1 << 6

    # ScriptVerifyLowS defines that signtures are required to comply with
    # the DER format and whose S value is <= order / 2.  This is rule 5
    # of BIP0062.
    ScriptVerifyLowS = 1 << 7

    # ScriptVerifyMinimalData defines that signatures must use the smallest
    # push operator. This is both rules 3 and 4 of BIP0062.
    ScriptVerifyMinimalData = 1 << 8

    # ScriptVerifyNullFail defines that signatures must be empty if
    # a CHECKSIG or CHECKMULTISIG operation fails.
    ScriptVerifyNullFail = 1 << 9

    # ScriptVerifySigPushOnly defines that signature scripts must contain
    # only pushed data.  This is rule 2 of BIP0062.
    ScriptVerifySigPushOnly = 1 << 10

    # ScriptVerifyStrictEncoding defines that signature scripts and
    # public keys must follow the strict encoding requirements.
    ScriptVerifyStrictEncoding = 1 << 11

    # ScriptVerifyWitness defines whether or not to verify a transaction
    # output using a witness program template.
    ScriptVerifyWitness = 1 << 12

    # ScriptVerifyDiscourageUpgradeableWitnessProgram makes witness
    # program with versions 2-16 non-standard.
    ScriptVerifyDiscourageUpgradeableWitnessProgram = 1 << 13

    # ScriptVerifyMinimalIf makes a script with an OP_IF/OP_NOTIF whose
    # operand is anything other than empty vector or [0x01] non-standard.
    ScriptVerifyMinimalIf = 1 << 14

    # ScriptVerifyWitnessPubKeyType makes a script within a check-sig
    # operation whose public key isn't serialized in a compressed format
    # non-standard.
    ScriptVerifyWitnessPubKeyType = 1 << 15


class ScriptFlags:
    def __init__(self, data=None):
        if type(data) is ScriptFlag:
            self._data = data.value
        elif type(data) is int:
            self._data = data
        elif type(data) is ScriptFlags:
            self._data = ScriptFlags.value
        else:
            self._data = 0

    @property
    def value(self):
        return self._data

    def has_flag(self, flag):
        return (self._data & flag.value) == flag.value


# Engine is the virtual machine that executes scripts.
class Engine:
    def __init__(self, scripts=None, script_idx=None, script_off=None, last_code_sep=None,
                 dstack=None, astack=None, tx=None, tx_idx=None, cond_stack=None, num_ops=None,
                 flags=None, sig_cache=None, hash_cache=None, bip16=None, saved_first_stack=None,
                 witness_version=None, witness_program=None, inptut_amount=None):
        """

        :param [][]parsedOpcode scripts:
        :param int script_idx:
        :param int script_off:
        :param int last_code_sep:
        :param Stack dstack:
        :param Stack astack:
        :param wire.MsgTx tx:
        :param int tx_idx:
        :param []int cond_stack:
        :param int num_ops:
        :param ScriptFlags flags:
        :param SigCache sig_cache:
        :param TxSigHashes hash_cache:
        :param bool bip16:
        :param [][]byte saved_first_stack:
        :param int witness_version:
        :param []byte witness_program:
        :param int64 inptut_amount:
        """
        self.scripts = scripts or []
        self.script_idx = script_idx or 0
        self.script_off = script_off or 0
        self.last_code_sep = last_code_sep or 0
        self.dstack = dstack or Stack()
        self.astack = astack or Stack()
        self.tx = tx or wire.MsgTx()
        self.tx_idx = tx_idx or 0
        self.cond_stack = cond_stack or []
        self.num_ops = num_ops or 0
        self.flags = flags or ScriptFlags()
        self.sig_cache = sig_cache or SigCache()
        self.hash_cache = hash_cache or HashCache()
        self.bip16 = bip16 or False
        self.saved_first_stack = saved_first_stack or []
        self.witness_version = witness_version or 0
        self.witness_program = witness_program or bytes()
        self.inptut_amount = inptut_amount or 0

    # has_flag returns whether the script engine instance has the passed flag set.
    def has_flag(self, flag: ScriptFlag) -> bool:
        return self.flags.has_flag(flag)

    # is_branch_executing returns whether or not the current conditional branch is
    # actively executing.  For example, when the data stack has an OP_FALSE on it
    # and an OP_IF is encountered, the branch is inactive until an OP_ELSE or
    # OP_ENDIF is encountered.  It properly handles nested conditionals.
    def is_branch_executing(self) -> bool:
        if len(self.cond_stack) == 0:
            return True
        return self.cond_stack[-1] == OpCondTrue

    # executeOpcode peforms execution on the passed opcode.  It takes into account
    # whether or not it is hidden by conditionals, but some rules still must be
    # tested in this case.
    def execute_opcode(self, pop: ParsedOpcode):
        """This method do some necessary check then call pop's opfunc to execute"""
        # Disabled opcodes are fail on program counter.
        if pop.is_disabled():
            desc = "attempt to execute disabled opcode %s" % pop.opcode.name
            raise ScriptError(ErrorCode.ErrDisabledOpcode, desc=desc)

        # Always-illegal opcodes are fail on program counter.
        if pop.always_illegal():
            desc = "attempt to execute reserved opcode %s" % pop.opcode.name
            raise ScriptError(ErrorCode.ErrReservedOpcode, desc=desc)

        # Note that this includes OP_RESERVED which counts as a push operation.
        if pop.opcode.value > OP_16:
            self.num_ops += 1
            if self.num_ops > MaxOpsPerScript:
                desc = "exceeded max operation limit of %d" % MaxOpsPerScript
                raise ScriptError(ErrorCode.ErrTooManyOperations, desc=desc)
        elif len(pop.data) > MaxScriptElementSize:
            desc = "element size %d exceeds max allowed size %d" % (len(pop.data), MaxScriptElementSize)
            raise ScriptError(ErrorCode.ErrTooManyOperations, desc=desc)

        # Nothing left to do when this is not a conditional opcode and it is
        # not in an executing branch.
        if not self.is_branch_executing() and not pop.is_conditional():
            return

        # Ensure all executed data push opcodes use the minimal encoding when
        # the minimal data verification flag is set.
        if self.dstack.verify_minimal_data and self.is_branch_executing() and 0 <= pop.opcode.value <= OP_PUSHDATA4:
            pop.check_minimal_data_push()

        return pop.opcode.opfunc(pop, self)

    # disasm is a helper function to produce the output for DisasmPC and
    # DisasmScript.  It produces the opcode prefixed by the program counter at the
    # provided position in the script.  It does no error checking and leaves that
    # to the caller to provide a valid offset.
    def disasm(self, script_idx: int, script_off: int) -> str:
        return "%02x:%04x: %s" % (script_idx, script_off, self.scripts[script_idx][script_off].print(one_line=False))

    # DisasmPC returns the string for the disassembly of the opcode that will be
    # next to execute when Step() is called.
    def disasm_pc(self):
        script_idx, script_off = self.cur_pc()
        return self.disasm(script_idx, script_off)

    # DisasmScript returns the disassembly string for the script at the requested
    # offset index.  Index 0 is the signature script and 1 is the public key
    # script.
    def disasm_script(self, idx: int) -> str:

        if idx >= len(self.scripts):
            desc = "script index %d >= total scripts %d" % (idx, len(self.scripts))
            raise ScriptError(ErrorCode.ErrInvalidIndex, desc=desc)

        dis_str = ""
        for i in self.scripts[idx]:
            dis_str = dis_str + self.disasm(idx, i) + "\n"

        return dis_str

    # validPC returns an error if the current script position is valid for
    # execution, nil otherwise.
    def valid_pc(self):
        if self.script_idx >= len(self.scripts):
            desc = "past input scripts %s:%s %s:xxxx" % (self.script_idx, self.script_off, len(self.scripts))
            raise ScriptError(ErrorCode.ErrInvalidProgramCounter, desc=desc)
        if self.script_off >= len(self.scripts[self.script_idx]):
            desc = "past input scripts %s:%s %s:%04d" % (
                self.script_idx, self.script_off, self.script_idx, len(self.scripts[self.script_idx]))
            raise ScriptError(ErrorCode.ErrInvalidProgramCounter, desc=desc)
        return

    # curPC returns either the current script and offset, or an error if the
    # position isn't valid.
    def cur_pc(self):
        self.valid_pc()
        return self.script_idx, self.script_off

    # isWitnessVersionActive returns true if a witness program was extracted
    # during the initialization of the Engine, and the program's version matches
    # the specified version.
    def is_witness_version_active(self, version: int) -> bool:
        return self.witness_program and self.witness_version == version

    # verifyWitnessProgram validates the stored witness program using the passed
    # witness as input.
    def verify_witness_program(self, witness: list):
        if self.is_witness_version_active(version=0):
            witness_program_len = len(self.witness_program)
            if witness_program_len == payToWitnessPubKeyHashDataSize:  # P2WKH
                # The witness stack should consist of exactly two
                # items: the signature, and the pubkey.
                if len(witness) != 2:
                    desc = "should have exactly two items in witness, instead have %s" % len(witness)
                    raise ScriptError(ErrorCode.ErrWitnessProgramMismatch, desc=desc)

                # Now we'll resume execution as if it were a regular
                # p2pkh transaction.
                pk_script = pay_to_pub_key_hash_script(self.witness_program)
                pops = parse_script(pk_script)

                # Set the stack to the provided witness stack, then
                # append the pkScript generated above as the next
                # script to execute.
                self.scripts.append(pops)
                self.set_stack(witness)

            elif witness_program_len == payToWitnessScriptHashDataSize:  # P2WSH
                # Additionally, The witness stack MUST NOT be empty at
                # this point.
                if len(witness) == 0:
                    desc = "witness program empty passed empty witness"
                    raise ScriptError(ErrorCode.ErrWitnessProgramEmpty, desc=desc)

                # Obtain the witness script which should be the last
                # element in the passed stack. The size of the script
                # MUST NOT exceed the max script size.
                witness_script = witness[-1]
                if len(witness_script) > MaxScriptSize:
                    desc = "witnessScript size %d is larger than max allowed size %d" % (
                        len(witness_script), MaxScriptSize)
                    raise ScriptError(ErrorCode.ErrScriptTooBig, desc=desc)

                # Ensure that the serialized pkScript at the end of
                # the witness stack matches the witness program.
                witness_hash = hashlib.sha256(witness_script).digest()
                if witness_hash != self.witness_program:
                    desc = "witness program hash mismatch"
                    raise ScriptError(ErrorCode.ErrWitnessProgramMismatch, desc=desc)

                # With all the validity checks passed, parse the
                # script into individual op-codes so w can execute it
                # as the next script.
                pops = parse_script(witness_script)

                # The hash matched successfully, so use the witness as
                # the stack, and set the witnessScript to be the next
                # script executed.
                self.scripts.append(pops)
                self.set_stack(witness[:-1])

            else:
                desc = "length of witness program must either be %s or %s bytes, instead is %s bytes" % (
                    payToWitnessPubKeyHashDataSize, payToWitnessScriptHashDataSize, len(self.witness_program))
                raise ScriptError(ErrorCode.ErrWitnessProgramWrongLength, desc=desc)


        elif self.has_flag(ScriptFlag.ScriptVerifyDiscourageUpgradeableWitnessProgram):
            desc = "new witness program versions invalid: %s" % self.witness_program
            raise ScriptError(ErrorCode.ErrDiscourageUpgradableWitnessProgram, desc=desc)
        else:
            # If we encounter an unknown witness program version and we
            # aren't discouraging future unknown witness based soft-forks,
            # then we de-activate the segwit behavior within the VM for
            # the remainder of execution.
            self.witness_program = bytes()

        if self.is_witness_version_active(version=0):
            # All elements within the witness stack must not be greater
            # than the maximum bytes which are allowed to be pushed onto
            # the stack.
            for wit_element in self.get_stack():
                if len(wit_element) > MaxScriptElementSize:
                    desc = "element size %d exceeds max allowed size %d" % (len(wit_element), MaxScriptElementSize)
                    raise ScriptError(ErrorCode.ErrElementTooBig, desc=desc)

        return

    # CheckErrorCondition returns nil if the running script has ended and was
    # successful, leaving a a true boolean on the stack.  An error otherwise,
    # including if the script has not finished.
    def check_error_condition(self, final_script: bool):
        # Check execution is actually done.  When pc is past the end of script
        # array there are no more scripts to run.
        if self.script_idx < len(self.scripts):
            desc = "error check when script unfinished"
            raise ScriptError(ErrorCode.ErrScriptUnfinished, desc=desc)

        # If we're in version zero witness execution mode, and this was the
        # final script, then the stack MUST be clean in order to maintain
        # compatibility with BIP16.
        if final_script and self.is_witness_version_active(0) and self.dstack.depth() != 1:
            desc = "witness program must have clean stack"
            raise ScriptError(ErrorCode.ErrEvalFalse, desc=desc)

        if final_script and self.has_flag(ScriptFlag.ScriptVerifyCleanStack) and self.dstack.depth() != 1:
            desc = "stack contains %d unexpected items" % (self.dstack.depth() - 1)
            raise ScriptError(ErrorCode.ErrEvalFalse, desc=desc)
        elif self.dstack.depth() < 1:
            desc = "stack empty at end of script execution"
            raise ScriptError(ErrorCode.ErrEmptyStack, desc=desc)

        v = self.dstack.pop_bool()
        if not v:
            # Do some log
            dis0 = self.disasm_script(0)
            dis1 = self.disasm_script(1)
            _logger.error("scripts failed: script0: %s\n script1: %s" % (dis0, dis1))

            desc = "false stack entry at end of script execution"
            raise ScriptError(ErrorCode.ErrEvalFalse, desc=desc)

        return

    # Step will execute the next instruction and move the program counter to the
    # next opcode in the script, or the next script if the current has ended.  Step
    # will return true in the case that the last opcode was successfully executed.
    #
    # The result of calling Step or any other method is undefined if an error is
    # returned.
    def step(self):
        # Verify that it is pointing to a valid script address.
        self.valid_pc()

        # Get next opcode to run, and set the offset +1
        opcode = self.scripts[self.script_idx][self.script_off]
        self.script_off += 1

        # # Execute it
        # Execute the opcode while taking into account several things such as
        # disabled opcodes, illegal opcodes, maximum allowed operations per
        # script, maximum script element sizes, and conditionals.
        self.execute_opcode(opcode)

        # # After execution, check status
        # The number of elements in the combination of the data and alt stacks
        # must not exceed the maximum number of stack elements allowed.
        combined_stack_size = self.dstack.depth() + self.astack.depth()
        if combined_stack_size > MaxStackSize:
            desc = "combined stack size %d > max allowed %d" % (combined_stack_size, MaxStackSize)
            raise ScriptError(ErrorCode.ErrStackOverflow, desc=desc)

        # Prepare for next instraction
        if self.script_off >= len(self.scripts[self.script_idx]):
            # Illegal to have an `if' that straddles two scripts.
            if len(self.cond_stack) != 0:
                desc = "end of script reached in conditional execution"
                raise ScriptError(ErrorCode.ErrUnbalancedConditional, desc=desc)


            # Alt stack doesn't persists
            # TOCONSIDER maybe we can first check self.astack.depth()
            # then decide whether to use drop, not the try catch style
            try:
                self.astack.dropN(self.astack.depth())
            except ScriptError as e:
                _logger.debug("dropN cause ScriptError: %s" % e)
                pass

            self.num_ops = 0  # number of ops is per script.
            self.script_off = 0

            if self.script_idx == 0 and self.bip16:
                self.script_idx += 1
                self.saved_first_stack = self.get_stack()
            elif self.script_idx == 1 and self.bip16:
                # Put us past the end for check_error_condition()
                self.script_idx += 1
                
                # Check script ran successfully and pull the script
			    # out of the first stack and execute that.
                self.check_error_condition(final_script=False)

                script = self.saved_first_stack[-1]
                pops = parse_script(script)
                self.scripts.append(pops)

                # Set stack to be the stack from first script minus the
			    # script itself
                self.set_stack(self.saved_first_stack[:-1])
            elif self.script_idx ==1 and self.witness_program or (
                self.script_idx == 2 and self.witness_program and self.bip16
            ):
                self.script_idx += 1
                witness = self.tx.tx_ins[self.tx_idx].witness
                self.verify_witness_program(witness)
            else:
                self.script_idx += 1

            # there are zero length scripts in the wild
            # self.script_off >= len(self.scripts[self.script_idx]) is True only when self.scripts[self.script_idx] is empty
            # So this mean, if next scripts is empty, increase script_idx
            if self.script_idx < len(self.scripts) and self.script_off >= len(self.scripts[self.script_idx]):
                self.script_idx += 1

            self.last_code_sep = 0

            if self.script_idx >= len(self.scripts):
                return True

        return False


    # Execute will execute all scripts in the script engine and return either nil
    # for successful validation or an error if one occurred.
    def execute(self):
        done = False
        while not done:
            # Do some log # TOCHANGE I think I can use better solution here
            try:
                dis = self.disasm_pc()
                _logger.info("stepping %s" % (dis))
            except Exception as e:
                _logger.info("stepping (%s)" % (e))

            done = self.step()

            # Do some log  # TOCHANGE I think I can use better solution here
            dstr = ""
            astr = ""
            if self.dstack.depth() != 0:
                dstr = "Stack:\n" + str(self.dstack)
            if self.astack.depth() != 0:
                astr = "Atack:\n" + str(self.astack)

            _logger.info("%s" % (dstr + astr))

        return self.check_error_condition(final_script=True)

    # subScript returns the script since the last OP_CODESEPARATOR.
    def sub_script(self):
        return self.scripts[self.script_idx][self.last_code_sep:]

    # checkHashTypeEncoding returns whether or not the passed hashtype adheres to
    # the strict encoding requirements if enabled.
    def check_hash_type_encoding(self, hash_type):
        pass

    def check_pub_key_encoding(self, pub_key):
        pass

    def check_signature_encoding(self, sig):
        pass

    # GetStack returns the contents of the primary stack as an array. where the
    # last item in the array is the top of the stack.
    def get_stack(self):
        return get_stack(self.dstack)

    # SetStack sets the contents of the primary stack to the contents of the
    # provided array where the last item in the array will be the top of the stack.
    def set_stack(self, data):
        set_stack(self.dstack, data)

    # GetAltStack returns the contents of the alternate stack as an array where the
    # last item in the array is the top of the stack.
    def get_alt_stack(self):
        return get_stack(self.astack)

    # SetAltStack sets the contents of the alternate stack to the contents of the
    # provided array where the last item in the array will be the top of the stack.
    def set_alt_stack(self, data):
        set_stack(self.astack, data)


# getStack returns the contents of stack as a byte array bottom up
def get_stack(stack):
    return list(reversed(copy.deepcopy(stack.stk)))


def set_stack(stack, data):
    stack.dropN(stack.depth())
    for each in data:
        stack.push_byte_array(each)
    return


# NewEngine returns a new script engine for the provided public key script,
# transaction, and input index.  The flags modify the behavior of the script
# engine according to the description provided by each flag.
def new_engine(script_pub_key, tx, tx_idx, flags, sig_cache, hash_cache, input_amount):
    """

    :param script_pub_key:
    :param tx:
    :param tx_idx:
    :param flags:
    :param sig_cache:
    :param hash_cache:
    :param input_amount:
    :return:
    """

    # The provided transaction input index must refer to a valid input.
    if tx_idx < 0 or tx_idx >= len(tx.tx_ins):
        desc = "transaction input index %d is negative or >= %d" % (tx_idx, len(tx.tx_ins))
        raise ScriptError(ErrorCode.ErrInvalidIndex, desc=desc)

    script_sig = tx.tx_ins[tx_idx].signature_script

    # When both the signature script and public key script are empty the
    # result is necessarily an error since the stack would end up being
    # empty which is equivalent to a false top element.  Thus, just return
    # the relevant error now as an optimization.
    if len(script_sig) == 0 and len(script_pub_key) == 0:
        desc = "false stack entry at end of script execution"
        raise ScriptError(ErrorCode.ErrEvalFalse, desc=desc)

    vm = Engine(flags=flags,
                sig_cache=sig_cache,
                hash_cache=hash_cache,
                inptut_amount=input_amount)

    # The clean stack flag (ScriptVerifyCleanStack) is not allowed without
    # either the pay-to-script-hash (P2SH) evaluation (ScriptBip16)
    # flag or the Segregated Witness (ScriptVerifyWitness) flag.
    #
    # Recall that evaluating a P2SH script without the flag set results in
    # non-P2SH evaluation which leaves the P2SH inputs on the stack.
    # Thus, allowing the clean stack flag without the P2SH flag would make
    # it possible to have a situation where P2SH would not be a soft fork
    # when it should be. The same goes for segwit which will pull in
    # additional scripts for execution from the witness stack.
    if vm.has_flag(ScriptFlag.ScriptVerifyCleanStack) and (not vm.has_flag(ScriptFlag.ScriptBip16)) and \
            (not vm.has_flag(ScriptFlag.ScriptVerifyWitness)):
        desc = "invalid flags combination"
        raise ScriptError(ErrorCode.ErrInvalidFlags, desc=desc)

    # The signature script must only contain data pushes when the
    # associated flag is set.
    if vm.has_flag(ScriptFlag.ScriptVerifySigPushOnly) and (not is_push_only_script(script_sig)):
        desc = "signature script is not push only"
        raise ScriptError(ErrorCode.ErrNotPushOnly, desc=desc)

    # The engine stores the scripts in parsed form using a slice.  This
    # allows multiple scripts to be executed in sequence.  For example,
    # with a pay-to-script-hash transaction, there will be ultimately be
    # a third script to execute.
    scripts = [script_sig, script_pub_key]
    for scr in scripts:
        if len(scr) > MaxScriptSize:
            desc = "script size %d is larger than max allowed size %d" % (len(scr), MaxScriptSize)
            raise ScriptError(ErrorCode.ErrScriptTooBig, desc=desc)

        vm.scripts.append(parse_script(scr))

    # Advance the program counter to the public key script if the signature
    # script is empty since there is nothing to execute for it in that
    # case.
    if len(scripts[0]) == 0:
        vm.script_idx += 1

    if vm.has_flag(ScriptFlag.ScriptBip16) and is_script_hash(vm.scripts[1]):
        # Only accept input scripts that push data for P2SH.
        if not is_push_only(vm.scripts[0]):
            desc = "pay to script hash is not push only"
            raise ScriptError(ErrorCode.ErrNotPushOnly, desc=desc)
        vm.bip16 = True

    if vm.has_flag(ScriptFlag.ScriptVerifyMinimalData):
        vm.dstack.verify_minimal_data = True
        vm.astack.verify_minimal_data = True

    # Check to see if we should execute in witness verification mode
    # according to the set flags. We check both the pkScript, and sigScript
    # here since in the case of nested p2sh, the scriptSig will be a valid
    # witness program. For nested p2sh, all the bytes after the first data
    # push should *exactly* match the witness program template.
    if vm.has_flag(ScriptFlag.ScriptVerifyWitness):

        # If witness evaluation is enabled, then P2SH MUST also be
        # active.
        if not vm.has_flag(ScriptFlag.ScriptBip16):
            desc = "P2SH must be enabled to do witness verification"
            raise ScriptError(ErrorCode.ErrInvalidFlags, desc=desc)

        wit_program = None
        if is_pops_witness_program(scripts[1]):
            # The scriptSig must be *empty* for all native witness
            # programs, otherwise we introduce malleability.
            if len(script_sig) != 0:
                desc = "native witness program cannot also have a signature script"
                raise ScriptError(ErrorCode.ErrWitnessMalleated, desc=desc)

            wit_program = script_pub_key

        elif len(tx.tx_ins[tx_idx].witness) != 0 and vm.bip16:
            # The sigScript MUST be *exactly* a single canonical
            # data push of the witness program, otherwise we
            # reintroduce malleability.
            sig_pops = vm.scripts[0]
            if len(sig_pops) == 1 and canonical_push(sig_pops[0]) and \
                    is_script_witness_program(sig_pops[0].data):
                wit_program = sig_pops[0].data
            else:
                desc = "signature script for witness nested p2sh is not canonical"
                raise ScriptError(ErrorCode.ErrWitnessMalleatedP2SH, desc=desc)

        if wit_program:
            vm.witness_version, vm.witness_program = extract_witness_program_info(wit_program)
        else:
            # If we didn't find a witness program in either the
            # pkScript or as a datapush within the sigScript, then
            # there MUST NOT be any witness data associated with
            # the input being validated.
            if not vm.witness_program and len(tx.tx_ins[tx_idx].witness) != 0:
                desc = "non-witness inputs cannot have a witness"
                raise ScriptError(ErrorCode.ErrWitnessUnexpected, desc=desc)

    vm.tx = tx
    vm.tx_idx = tx_idx
    return vm
