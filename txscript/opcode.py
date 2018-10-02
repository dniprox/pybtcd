from .error import *

# These constants are the values of the official opcodes used on the btc wiki,
# in bitcoin core and in most if not all other references and software related
# to handling BTC scripts
OP_0 = 0x00  # 0
OP_FALSE = 0x00  # 0 - AKA OP_0
OP_DATA_1 = 0x01  # 1
OP_DATA_2 = 0x02  # 2
OP_DATA_3 = 0x03  # 3
OP_DATA_4 = 0x04  # 4
OP_DATA_5 = 0x05  # 5
OP_DATA_6 = 0x06  # 6
OP_DATA_7 = 0x07  # 7
OP_DATA_8 = 0x08  # 8
OP_DATA_9 = 0x09  # 9
OP_DATA_10 = 0x0a  # 10
OP_DATA_11 = 0x0b  # 11
OP_DATA_12 = 0x0c  # 12
OP_DATA_13 = 0x0d  # 13
OP_DATA_14 = 0x0e  # 14
OP_DATA_15 = 0x0f  # 15
OP_DATA_16 = 0x10  # 16
OP_DATA_17 = 0x11  # 17
OP_DATA_18 = 0x12  # 18
OP_DATA_19 = 0x13  # 19
OP_DATA_20 = 0x14  # 20
OP_DATA_21 = 0x15  # 21
OP_DATA_22 = 0x16  # 22
OP_DATA_23 = 0x17  # 23
OP_DATA_24 = 0x18  # 24
OP_DATA_25 = 0x19  # 25
OP_DATA_26 = 0x1a  # 26
OP_DATA_27 = 0x1b  # 27
OP_DATA_28 = 0x1c  # 28
OP_DATA_29 = 0x1d  # 29
OP_DATA_30 = 0x1e  # 30
OP_DATA_31 = 0x1f  # 31
OP_DATA_32 = 0x20  # 32
OP_DATA_33 = 0x21  # 33
OP_DATA_34 = 0x22  # 34
OP_DATA_35 = 0x23  # 35
OP_DATA_36 = 0x24  # 36
OP_DATA_37 = 0x25  # 37
OP_DATA_38 = 0x26  # 38
OP_DATA_39 = 0x27  # 39
OP_DATA_40 = 0x28  # 40
OP_DATA_41 = 0x29  # 41
OP_DATA_42 = 0x2a  # 42
OP_DATA_43 = 0x2b  # 43
OP_DATA_44 = 0x2c  # 44
OP_DATA_45 = 0x2d  # 45
OP_DATA_46 = 0x2e  # 46
OP_DATA_47 = 0x2f  # 47
OP_DATA_48 = 0x30  # 48
OP_DATA_49 = 0x31  # 49
OP_DATA_50 = 0x32  # 50
OP_DATA_51 = 0x33  # 51
OP_DATA_52 = 0x34  # 52
OP_DATA_53 = 0x35  # 53
OP_DATA_54 = 0x36  # 54
OP_DATA_55 = 0x37  # 55
OP_DATA_56 = 0x38  # 56
OP_DATA_57 = 0x39  # 57
OP_DATA_58 = 0x3a  # 58
OP_DATA_59 = 0x3b  # 59
OP_DATA_60 = 0x3c  # 60
OP_DATA_61 = 0x3d  # 61
OP_DATA_62 = 0x3e  # 62
OP_DATA_63 = 0x3f  # 63
OP_DATA_64 = 0x40  # 64
OP_DATA_65 = 0x41  # 65
OP_DATA_66 = 0x42  # 66
OP_DATA_67 = 0x43  # 67
OP_DATA_68 = 0x44  # 68
OP_DATA_69 = 0x45  # 69
OP_DATA_70 = 0x46  # 70
OP_DATA_71 = 0x47  # 71
OP_DATA_72 = 0x48  # 72
OP_DATA_73 = 0x49  # 73
OP_DATA_74 = 0x4a  # 74
OP_DATA_75 = 0x4b  # 75
OP_PUSHDATA1 = 0x4c  # 76
OP_PUSHDATA2 = 0x4d  # 77
OP_PUSHDATA4 = 0x4e  # 78
OP_1NEGATE = 0x4f  # 79
OP_RESERVED = 0x50  # 80
OP_1 = 0x51  # 81 - AKA OP_TRUE
OP_TRUE = 0x51  # 81
OP_2 = 0x52  # 82
OP_3 = 0x53  # 83
OP_4 = 0x54  # 84
OP_5 = 0x55  # 85
OP_6 = 0x56  # 86
OP_7 = 0x57  # 87
OP_8 = 0x58  # 88
OP_9 = 0x59  # 89
OP_10 = 0x5a  # 90
OP_11 = 0x5b  # 91
OP_12 = 0x5c  # 92
OP_13 = 0x5d  # 93
OP_14 = 0x5e  # 94
OP_15 = 0x5f  # 95
OP_16 = 0x60  # 96
OP_NOP = 0x61  # 97
OP_VER = 0x62  # 98
OP_IF = 0x63  # 99
OP_NOTIF = 0x64  # 100
OP_VERIF = 0x65  # 101
OP_VERNOTIF = 0x66  # 102
OP_ELSE = 0x67  # 103
OP_ENDIF = 0x68  # 104
OP_VERIFY = 0x69  # 105
OP_RETURN = 0x6a  # 106
OP_TOALTSTACK = 0x6b  # 107
OP_FROMALTSTACK = 0x6c  # 108
OP_2DROP = 0x6d  # 109
OP_2DUP = 0x6e  # 110
OP_3DUP = 0x6f  # 111
OP_2OVER = 0x70  # 112
OP_2ROT = 0x71  # 113
OP_2SWAP = 0x72  # 114
OP_IFDUP = 0x73  # 115
OP_DEPTH = 0x74  # 116
OP_DROP = 0x75  # 117
OP_DUP = 0x76  # 118
OP_NIP = 0x77  # 119
OP_OVER = 0x78  # 120
OP_PICK = 0x79  # 121
OP_ROLL = 0x7a  # 122
OP_ROT = 0x7b  # 123
OP_SWAP = 0x7c  # 124
OP_TUCK = 0x7d  # 125
OP_CAT = 0x7e  # 126
OP_SUBSTR = 0x7f  # 127
OP_LEFT = 0x80  # 128
OP_RIGHT = 0x81  # 129
OP_SIZE = 0x82  # 130
OP_INVERT = 0x83  # 131
OP_AND = 0x84  # 132
OP_OR = 0x85  # 133
OP_XOR = 0x86  # 134
OP_EQUAL = 0x87  # 135
OP_EQUALVERIFY = 0x88  # 136
OP_RESERVED1 = 0x89  # 137
OP_RESERVED2 = 0x8a  # 138
OP_1ADD = 0x8b  # 139
OP_1SUB = 0x8c  # 140
OP_2MUL = 0x8d  # 141
OP_2DIV = 0x8e  # 142
OP_NEGATE = 0x8f  # 143
OP_ABS = 0x90  # 144
OP_NOT = 0x91  # 145
OP_0NOTEQUAL = 0x92  # 146
OP_ADD = 0x93  # 147
OP_SUB = 0x94  # 148
OP_MUL = 0x95  # 149
OP_DIV = 0x96  # 150
OP_MOD = 0x97  # 151
OP_LSHIFT = 0x98  # 152
OP_RSHIFT = 0x99  # 153
OP_BOOLAND = 0x9a  # 154
OP_BOOLOR = 0x9b  # 155
OP_NUMEQUAL = 0x9c  # 156
OP_NUMEQUALVERIFY = 0x9d  # 157
OP_NUMNOTEQUAL = 0x9e  # 158
OP_LESSTHAN = 0x9f  # 159
OP_GREATERTHAN = 0xa0  # 160
OP_LESSTHANOREQUAL = 0xa1  # 161
OP_GREATERTHANOREQUAL = 0xa2  # 162
OP_MIN = 0xa3  # 163
OP_MAX = 0xa4  # 164
OP_WITHIN = 0xa5  # 165
OP_RIPEMD160 = 0xa6  # 166
OP_SHA1 = 0xa7  # 167
OP_SHA256 = 0xa8  # 168
OP_HASH160 = 0xa9  # 169
OP_HASH256 = 0xaa  # 170
OP_CODESEPARATOR = 0xab  # 171
OP_CHECKSIG = 0xac  # 172
OP_CHECKSIGVERIFY = 0xad  # 173
OP_CHECKMULTISIG = 0xae  # 174
OP_CHECKMULTISIGVERIFY = 0xaf  # 175
OP_NOP1 = 0xb0  # 176
OP_NOP2 = 0xb1  # 177
OP_CHECKLOCKTIMEVERIFY = 0xb1  # 177 - AKA OP_NOP2
OP_NOP3 = 0xb2  # 178
OP_CHECKSEQUENCEVERIFY = 0xb2  # 178 - AKA OP_NOP3
OP_NOP4 = 0xb3  # 179
OP_NOP5 = 0xb4  # 180
OP_NOP6 = 0xb5  # 181
OP_NOP7 = 0xb6  # 182
OP_NOP8 = 0xb7  # 183
OP_NOP9 = 0xb8  # 184
OP_NOP10 = 0xb9  # 185
OP_UNKNOWN186 = 0xba  # 186
OP_UNKNOWN187 = 0xbb  # 187
OP_UNKNOWN188 = 0xbc  # 188
OP_UNKNOWN189 = 0xbd  # 189
OP_UNKNOWN190 = 0xbe  # 190
OP_UNKNOWN191 = 0xbf  # 191
OP_UNKNOWN192 = 0xc0  # 192
OP_UNKNOWN193 = 0xc1  # 193
OP_UNKNOWN194 = 0xc2  # 194
OP_UNKNOWN195 = 0xc3  # 195
OP_UNKNOWN196 = 0xc4  # 196
OP_UNKNOWN197 = 0xc5  # 197
OP_UNKNOWN198 = 0xc6  # 198
OP_UNKNOWN199 = 0xc7  # 199
OP_UNKNOWN200 = 0xc8  # 200
OP_UNKNOWN201 = 0xc9  # 201
OP_UNKNOWN202 = 0xca  # 202
OP_UNKNOWN203 = 0xcb  # 203
OP_UNKNOWN204 = 0xcc  # 204
OP_UNKNOWN205 = 0xcd  # 205
OP_UNKNOWN206 = 0xce  # 206
OP_UNKNOWN207 = 0xcf  # 207
OP_UNKNOWN208 = 0xd0  # 208
OP_UNKNOWN209 = 0xd1  # 209
OP_UNKNOWN210 = 0xd2  # 210
OP_UNKNOWN211 = 0xd3  # 211
OP_UNKNOWN212 = 0xd4  # 212
OP_UNKNOWN213 = 0xd5  # 213
OP_UNKNOWN214 = 0xd6  # 214
OP_UNKNOWN215 = 0xd7  # 215
OP_UNKNOWN216 = 0xd8  # 216
OP_UNKNOWN217 = 0xd9  # 217
OP_UNKNOWN218 = 0xda  # 218
OP_UNKNOWN219 = 0xdb  # 219
OP_UNKNOWN220 = 0xdc  # 220
OP_UNKNOWN221 = 0xdd  # 221
OP_UNKNOWN222 = 0xde  # 222
OP_UNKNOWN223 = 0xdf  # 223
OP_UNKNOWN224 = 0xe0  # 224
OP_UNKNOWN225 = 0xe1  # 225
OP_UNKNOWN226 = 0xe2  # 226
OP_UNKNOWN227 = 0xe3  # 227
OP_UNKNOWN228 = 0xe4  # 228
OP_UNKNOWN229 = 0xe5  # 229
OP_UNKNOWN230 = 0xe6  # 230
OP_UNKNOWN231 = 0xe7  # 231
OP_UNKNOWN232 = 0xe8  # 232
OP_UNKNOWN233 = 0xe9  # 233
OP_UNKNOWN234 = 0xea  # 234
OP_UNKNOWN235 = 0xeb  # 235
OP_UNKNOWN236 = 0xec  # 236
OP_UNKNOWN237 = 0xed  # 237
OP_UNKNOWN238 = 0xee  # 238
OP_UNKNOWN239 = 0xef  # 239
OP_UNKNOWN240 = 0xf0  # 240
OP_UNKNOWN241 = 0xf1  # 241
OP_UNKNOWN242 = 0xf2  # 242
OP_UNKNOWN243 = 0xf3  # 243
OP_UNKNOWN244 = 0xf4  # 244
OP_UNKNOWN245 = 0xf5  # 245
OP_UNKNOWN246 = 0xf6  # 246
OP_UNKNOWN247 = 0xf7  # 247
OP_UNKNOWN248 = 0xf8  # 248
OP_UNKNOWN249 = 0xf9  # 249
OP_SMALLINTEGER = 0xfa  # 250 - bitcoin core internal
OP_PUBKEYS = 0xfb  # 251 - bitcoin core internal
OP_UNKNOWN252 = 0xfc  # 252
OP_PUBKEYHASH = 0xfd  # 253 - bitcoin core internal
OP_PUBKEY = 0xfe  # 254 - bitcoin core internal
OP_INVALIDOPCODE = 0xff  # 255 - bitcoin core internal


# An opcode defines the information related to a txscript opcode.  opfunc, if
# present, is the function to call to perform the opcode on the script.  The
# current script is passed in as a slice with the first member being the opcode
# itself.
class OpCode:
    def __init__(self, value=None, name=None, length=None, opfunc=None):
        """

        :param byte value:
        :param string name:
        :param int length:
        :param func opfunc:
        """
        self.value = value or 0x00
        self.name = name or ""
        self.length = length or 0
        self.opfunc = opfunc or None  # TOCHECK

    def __eq__(self, other):
        return self.value == other.value and \
               self.name == other.name and \
               self.length == other.length and \
               self.opfunc == other.opfunc

    def __repr__(self):
        return self.name


class ParsedOpcode:
    def __init__(self, opcode=None, data=None):
        """

        :param OpCode opcode:
        :param []byte data:
        """
        self.opcode = opcode
        self.data = data or bytes()

    def __eq__(self, other):
        return self.opcode == other.opcode and \
               self.data == other.data

    def bytes(self):
        script = []
        if self.opcode.length == 1:
            script.append(self.opcode.value)
            if len(self.data) != 0:
                desc = "internal consistency error - parsed opcode %s has data length %d when %d was expected".format(
                    self.opcode.name, len(self.data), 0)
                raise ScriptError(c=ErrorCode.ErrInternal, desc=desc)
        elif self.opcode.length > 1:
            script.append(self.opcode.value)
            if len(self.data) != self.opcode.length - 1:
                desc = "internal consistency error - parsed opcode %s has data length %d when %d was expected".format(
                    self.opcode.name, len(self.data), self.opcode.length - 1)
                raise ScriptError(c=ErrorCode.ErrInternal, desc=desc)
            script.append(self.data)
        elif self.opcode.length < 0:
            script.append(self.opcode.value)
            l = len(self.data)
            if self.opcode.length == -1:
                try:
                    script.append(l.to_bytes(1, "little"))
                except OverflowError:
                    desc = "internal consistency error - parsed opcode %s has data length %d, but overflow".format(
                        self.opcode.name, len(self.data))
                    raise ScriptError(c=ErrorCode.ErrInternal, desc=desc)
                script.append(self.data)
            elif self.opcode.length == -2:
                try:
                    script.append(l.to_bytes(2, "little"))
                except OverflowError:
                    desc = "internal consistency error - parsed opcode %s has data length %d, but overflow".format(
                        self.opcode.name, len(self.data))
                    raise ScriptError(c=ErrorCode.ErrInternal, desc=desc)
                script.append(self.data)
            elif self.opcode.length == -4:
                try:
                    script.append(l.to_bytes(4, "little"))
                except OverflowError:
                    desc = "internal consistency error - parsed opcode %s has data length %d, but overflow".format(
                        self.opcode.name, len(self.data))
                    raise ScriptError(c=ErrorCode.ErrInternal, desc=desc)
                script.append(self.data)
            else:
                desc = "internal consistency error - parsed opcode %s has opcode length %s, not one of -1, -2, -4".format(
                    self.opcode.name, self.opcode.length)
                raise ScriptError(c=ErrorCode.ErrInternal, desc=desc)

        else:
            desc = "opcode: %s,  length: %s is illegal".format(
                self.opcode.name, self.opcode.length)
            raise ScriptError(c=ErrorCode.ErrInternal, desc=desc)

        return script


# *******************************************
# Opcode implementation functions start here.
# *******************************************

# opcodeDisabled is a common handler for disabled opcodes.  It returns an
# appropriate error indicating the opcode is disabled.  While it would
# ordinarily make more sense to detect if the script contains any disabled
# opcodes before executing in an initial parse step, the consensus rules
# dictate the script doesn't fail until the program counter passes over a
# disabled opcode (even when they appear in a branch that is not executed).
def opcodeDisabled(op, vm):
    pass


def opcodeFalse(op, vm):
    pass


def opcodePushData(op, vm):
    pass


def opcode1Negate(op, vm):
    pass


def opcodeReserved(op, vm):
    pass


def opcodeN(op, vm):
    pass


def opcodeNop(op, vm):
    pass


def opcodeIf(op, vm):
    pass


def opcodeNotIf(op, vm):
    pass


def opcodeElse(op, vm):
    pass


def opcodeEndif(op, vm):
    pass


def opcodeVerify(op, vm):
    pass


def opcodeReturn(op, vm):
    pass


def opcodeCheckLockTimeVerify(op, vm):
    pass


def opcodeCheckSequenceVerify(op, vm):
    pass


def opcodeToAltStack(op, vm):
    pass


def opcodeFromAltStack(op, vm):
    pass


def opcode2Drop(op, vm):
    pass


def opcode2Dup(op, vm):
    pass


def opcode3Dup(op, vm):
    pass


def opcode2Over(op, vm):
    pass


def opcode2Rot(op, vm):
    pass


def opcode2Swap(op, vm):
    pass


def opcodeIfDup(op, vm):
    pass


def opcodeDepth(op, vm):
    pass


def opcodeDrop(op, vm):
    pass


def opcodeDup(op, vm):
    pass


def opcodeNip(op, vm):
    pass


def opcodeOver(op, vm):
    pass


def opcodePick(op, vm):
    pass


def opcodeRoll(op, vm):
    pass


def opcodeRot(op, vm):
    pass


def opcodeSwap(op, vm):
    pass


def opcodeTuck(op, vm):
    pass


def opcodeSize(op, vm):
    pass


def opcodeEqual(op, vm):
    pass


def opcodeEqualVerify(op, vm):
    pass


def opcode1Add(op, vm):
    pass


def opcode1Sub(op, vm):
    pass


def opcodeNegate(op, vm):
    pass


def opcodeAbs(op, vm):
    pass


def opcodeNot(op, vm):
    pass


def opcode0NotEqual(op, vm):
    pass


def opcodeAdd(op, vm):
    pass


def opcodeSub(op, vm):
    pass


def opcodeBoolAnd(op, vm):
    pass


def opcodeBoolOr(op, vm):
    pass


def opcodeNumEqual(op, vm):
    pass


def opcodeNumEqualVerify(op, vm):
    pass


def opcodeNumNotEqual(op, vm):
    pass


def opcodeLessThan(op, vm):
    pass


def opcodeGreaterThan(op, vm):
    pass


def opcodeLessThanOrEqual(op, vm):
    pass


def opcodeGreaterThanOrEqual(op, vm):
    pass


def opcodeMin(op, vm):
    pass


def opcodeMax(op, vm):
    pass


def opcodeWithin(op, vm):
    pass


def opcodeRipemd160(op, vm):
    pass


def opcodeSha1(op, vm):
    pass


def opcodeSha256(op, vm):
    pass


def opcodeHash160(op, vm):
    pass


def opcodeHash256(op, vm):
    pass


def opcodeCodeSeparator(op, vm):
    pass


def opcodeCheckSig(op, vm):
    pass


def opcodeCheckSigVerify(op, vm):
    pass


def opcodeCheckMultiSig(op, vm):
    pass


def opcodeCheckMultiSigVerify(op, vm):
    pass


def opcodeInvalid(op, vm):
    pass


opcode_array = [
    # Data push opcodes.
    OpCode(OP_FALSE, "OP_0", 1, opcodeFalse),
    OpCode(OP_DATA_1, "OP_DATA_1", 2, opcodePushData),
    OpCode(OP_DATA_2, "OP_DATA_2", 3, opcodePushData),
    OpCode(OP_DATA_3, "OP_DATA_3", 4, opcodePushData),
    OpCode(OP_DATA_4, "OP_DATA_4", 5, opcodePushData),
    OpCode(OP_DATA_5, "OP_DATA_5", 6, opcodePushData),
    OpCode(OP_DATA_6, "OP_DATA_6", 7, opcodePushData),
    OpCode(OP_DATA_7, "OP_DATA_7", 8, opcodePushData),
    OpCode(OP_DATA_8, "OP_DATA_8", 9, opcodePushData),
    OpCode(OP_DATA_9, "OP_DATA_9", 10, opcodePushData),
    OpCode(OP_DATA_10, "OP_DATA_10", 11, opcodePushData),
    OpCode(OP_DATA_11, "OP_DATA_11", 12, opcodePushData),
    OpCode(OP_DATA_12, "OP_DATA_12", 13, opcodePushData),
    OpCode(OP_DATA_13, "OP_DATA_13", 14, opcodePushData),
    OpCode(OP_DATA_14, "OP_DATA_14", 15, opcodePushData),
    OpCode(OP_DATA_15, "OP_DATA_15", 16, opcodePushData),
    OpCode(OP_DATA_16, "OP_DATA_16", 17, opcodePushData),
    OpCode(OP_DATA_17, "OP_DATA_17", 18, opcodePushData),
    OpCode(OP_DATA_18, "OP_DATA_18", 19, opcodePushData),
    OpCode(OP_DATA_19, "OP_DATA_19", 20, opcodePushData),
    OpCode(OP_DATA_20, "OP_DATA_20", 21, opcodePushData),
    OpCode(OP_DATA_21, "OP_DATA_21", 22, opcodePushData),
    OpCode(OP_DATA_22, "OP_DATA_22", 23, opcodePushData),
    OpCode(OP_DATA_23, "OP_DATA_23", 24, opcodePushData),
    OpCode(OP_DATA_24, "OP_DATA_24", 25, opcodePushData),
    OpCode(OP_DATA_25, "OP_DATA_25", 26, opcodePushData),
    OpCode(OP_DATA_26, "OP_DATA_26", 27, opcodePushData),
    OpCode(OP_DATA_27, "OP_DATA_27", 28, opcodePushData),
    OpCode(OP_DATA_28, "OP_DATA_28", 29, opcodePushData),
    OpCode(OP_DATA_29, "OP_DATA_29", 30, opcodePushData),
    OpCode(OP_DATA_30, "OP_DATA_30", 31, opcodePushData),
    OpCode(OP_DATA_31, "OP_DATA_31", 32, opcodePushData),
    OpCode(OP_DATA_32, "OP_DATA_32", 33, opcodePushData),
    OpCode(OP_DATA_33, "OP_DATA_33", 34, opcodePushData),
    OpCode(OP_DATA_34, "OP_DATA_34", 35, opcodePushData),
    OpCode(OP_DATA_35, "OP_DATA_35", 36, opcodePushData),
    OpCode(OP_DATA_36, "OP_DATA_36", 37, opcodePushData),
    OpCode(OP_DATA_37, "OP_DATA_37", 38, opcodePushData),
    OpCode(OP_DATA_38, "OP_DATA_38", 39, opcodePushData),
    OpCode(OP_DATA_39, "OP_DATA_39", 40, opcodePushData),
    OpCode(OP_DATA_40, "OP_DATA_40", 41, opcodePushData),
    OpCode(OP_DATA_41, "OP_DATA_41", 42, opcodePushData),
    OpCode(OP_DATA_42, "OP_DATA_42", 43, opcodePushData),
    OpCode(OP_DATA_43, "OP_DATA_43", 44, opcodePushData),
    OpCode(OP_DATA_44, "OP_DATA_44", 45, opcodePushData),
    OpCode(OP_DATA_45, "OP_DATA_45", 46, opcodePushData),
    OpCode(OP_DATA_46, "OP_DATA_46", 47, opcodePushData),
    OpCode(OP_DATA_47, "OP_DATA_47", 48, opcodePushData),
    OpCode(OP_DATA_48, "OP_DATA_48", 49, opcodePushData),
    OpCode(OP_DATA_49, "OP_DATA_49", 50, opcodePushData),
    OpCode(OP_DATA_50, "OP_DATA_50", 51, opcodePushData),
    OpCode(OP_DATA_51, "OP_DATA_51", 52, opcodePushData),
    OpCode(OP_DATA_52, "OP_DATA_52", 53, opcodePushData),
    OpCode(OP_DATA_53, "OP_DATA_53", 54, opcodePushData),
    OpCode(OP_DATA_54, "OP_DATA_54", 55, opcodePushData),
    OpCode(OP_DATA_55, "OP_DATA_55", 56, opcodePushData),
    OpCode(OP_DATA_56, "OP_DATA_56", 57, opcodePushData),
    OpCode(OP_DATA_57, "OP_DATA_57", 58, opcodePushData),
    OpCode(OP_DATA_58, "OP_DATA_58", 59, opcodePushData),
    OpCode(OP_DATA_59, "OP_DATA_59", 60, opcodePushData),
    OpCode(OP_DATA_60, "OP_DATA_60", 61, opcodePushData),
    OpCode(OP_DATA_61, "OP_DATA_61", 62, opcodePushData),
    OpCode(OP_DATA_62, "OP_DATA_62", 63, opcodePushData),
    OpCode(OP_DATA_63, "OP_DATA_63", 64, opcodePushData),
    OpCode(OP_DATA_64, "OP_DATA_64", 65, opcodePushData),
    OpCode(OP_DATA_65, "OP_DATA_65", 66, opcodePushData),
    OpCode(OP_DATA_66, "OP_DATA_66", 67, opcodePushData),
    OpCode(OP_DATA_67, "OP_DATA_67", 68, opcodePushData),
    OpCode(OP_DATA_68, "OP_DATA_68", 69, opcodePushData),
    OpCode(OP_DATA_69, "OP_DATA_69", 70, opcodePushData),
    OpCode(OP_DATA_70, "OP_DATA_70", 71, opcodePushData),
    OpCode(OP_DATA_71, "OP_DATA_71", 72, opcodePushData),
    OpCode(OP_DATA_72, "OP_DATA_72", 73, opcodePushData),
    OpCode(OP_DATA_73, "OP_DATA_73", 74, opcodePushData),
    OpCode(OP_DATA_74, "OP_DATA_74", 75, opcodePushData),
    OpCode(OP_DATA_75, "OP_DATA_75", 76, opcodePushData),
    OpCode(OP_PUSHDATA1, "OP_PUSHDATA1", -1, opcodePushData),
    OpCode(OP_PUSHDATA2, "OP_PUSHDATA2", -2, opcodePushData),
    OpCode(OP_PUSHDATA4, "OP_PUSHDATA4", -4, opcodePushData),
    OpCode(OP_1NEGATE, "OP_1NEGATE", 1, opcode1Negate),
    OpCode(OP_RESERVED, "OP_RESERVED", 1, opcodeReserved),
    OpCode(OP_TRUE, "OP_1", 1, opcodeN),
    OpCode(OP_2, "OP_2", 1, opcodeN),
    OpCode(OP_3, "OP_3", 1, opcodeN),
    OpCode(OP_4, "OP_4", 1, opcodeN),
    OpCode(OP_5, "OP_5", 1, opcodeN),
    OpCode(OP_6, "OP_6", 1, opcodeN),
    OpCode(OP_7, "OP_7", 1, opcodeN),
    OpCode(OP_8, "OP_8", 1, opcodeN),
    OpCode(OP_9, "OP_9", 1, opcodeN),
    OpCode(OP_10, "OP_10", 1, opcodeN),
    OpCode(OP_11, "OP_11", 1, opcodeN),
    OpCode(OP_12, "OP_12", 1, opcodeN),
    OpCode(OP_13, "OP_13", 1, opcodeN),
    OpCode(OP_14, "OP_14", 1, opcodeN),
    OpCode(OP_15, "OP_15", 1, opcodeN),
    OpCode(OP_16, "OP_16", 1, opcodeN),

    # Control opcodes.
    OpCode(OP_NOP, "OP_NOP", 1, opcodeNop),
    OpCode(OP_VER, "OP_VER", 1, opcodeReserved),
    OpCode(OP_IF, "OP_IF", 1, opcodeIf),
    OpCode(OP_NOTIF, "OP_NOTIF", 1, opcodeNotIf),
    OpCode(OP_VERIF, "OP_VERIF", 1, opcodeReserved),
    OpCode(OP_VERNOTIF, "OP_VERNOTIF", 1, opcodeReserved),
    OpCode(OP_ELSE, "OP_ELSE", 1, opcodeElse),
    OpCode(OP_ENDIF, "OP_ENDIF", 1, opcodeEndif),
    OpCode(OP_VERIFY, "OP_VERIFY", 1, opcodeVerify),
    OpCode(OP_RETURN, "OP_RETURN", 1, opcodeReturn),
    # # As same of OP_NOP2 and OP_NOP3
    # OpCode(OP_CHECKLOCKTIMEVERIFY, "OP_CHECKLOCKTIMEVERIFY", 1, opcodeCheckLockTimeVerify),
    # OpCode(OP_CHECKSEQUENCEVERIFY, "OP_CHECKSEQUENCEVERIFY", 1, opcodeCheckSequenceVerify),

    # Stack opcodes.
    OpCode(OP_TOALTSTACK, "OP_TOALTSTACK", 1, opcodeToAltStack),
    OpCode(OP_FROMALTSTACK, "OP_FROMALTSTACK", 1, opcodeFromAltStack),
    OpCode(OP_2DROP, "OP_2DROP", 1, opcode2Drop),
    OpCode(OP_2DUP, "OP_2DUP", 1, opcode2Dup),
    OpCode(OP_3DUP, "OP_3DUP", 1, opcode3Dup),
    OpCode(OP_2OVER, "OP_2OVER", 1, opcode2Over),
    OpCode(OP_2ROT, "OP_2ROT", 1, opcode2Rot),
    OpCode(OP_2SWAP, "OP_2SWAP", 1, opcode2Swap),
    OpCode(OP_IFDUP, "OP_IFDUP", 1, opcodeIfDup),
    OpCode(OP_DEPTH, "OP_DEPTH", 1, opcodeDepth),
    OpCode(OP_DROP, "OP_DROP", 1, opcodeDrop),
    OpCode(OP_DUP, "OP_DUP", 1, opcodeDup),
    OpCode(OP_NIP, "OP_NIP", 1, opcodeNip),
    OpCode(OP_OVER, "OP_OVER", 1, opcodeOver),
    OpCode(OP_PICK, "OP_PICK", 1, opcodePick),
    OpCode(OP_ROLL, "OP_ROLL", 1, opcodeRoll),
    OpCode(OP_ROT, "OP_ROT", 1, opcodeRot),
    OpCode(OP_SWAP, "OP_SWAP", 1, opcodeSwap),
    OpCode(OP_TUCK, "OP_TUCK", 1, opcodeTuck),

    # Splice opcodes.
    OpCode(OP_CAT, "OP_CAT", 1, opcodeDisabled),
    OpCode(OP_SUBSTR, "OP_SUBSTR", 1, opcodeDisabled),
    OpCode(OP_LEFT, "OP_LEFT", 1, opcodeDisabled),
    OpCode(OP_RIGHT, "OP_RIGHT", 1, opcodeDisabled),
    OpCode(OP_SIZE, "OP_SIZE", 1, opcodeSize),

    # Bitwise logic opcodes.
    OpCode(OP_INVERT, "OP_INVERT", 1, opcodeDisabled),
    OpCode(OP_AND, "OP_AND", 1, opcodeDisabled),
    OpCode(OP_OR, "OP_OR", 1, opcodeDisabled),
    OpCode(OP_XOR, "OP_XOR", 1, opcodeDisabled),
    OpCode(OP_EQUAL, "OP_EQUAL", 1, opcodeEqual),
    OpCode(OP_EQUALVERIFY, "OP_EQUALVERIFY", 1, opcodeEqualVerify),
    OpCode(OP_RESERVED1, "OP_RESERVED1", 1, opcodeReserved),
    OpCode(OP_RESERVED2, "OP_RESERVED2", 1, opcodeReserved),

    # Numeric related opcodes.
    OpCode(OP_1ADD, "OP_1ADD", 1, opcode1Add),
    OpCode(OP_1SUB, "OP_1SUB", 1, opcode1Sub),
    OpCode(OP_2MUL, "OP_2MUL", 1, opcodeDisabled),
    OpCode(OP_2DIV, "OP_2DIV", 1, opcodeDisabled),
    OpCode(OP_NEGATE, "OP_NEGATE", 1, opcodeNegate),
    OpCode(OP_ABS, "OP_ABS", 1, opcodeAbs),
    OpCode(OP_NOT, "OP_NOT", 1, opcodeNot),
    OpCode(OP_0NOTEQUAL, "OP_0NOTEQUAL", 1, opcode0NotEqual),
    OpCode(OP_ADD, "OP_ADD", 1, opcodeAdd),
    OpCode(OP_SUB, "OP_SUB", 1, opcodeSub),
    OpCode(OP_MUL, "OP_MUL", 1, opcodeDisabled),
    OpCode(OP_DIV, "OP_DIV", 1, opcodeDisabled),
    OpCode(OP_MOD, "OP_MOD", 1, opcodeDisabled),
    OpCode(OP_LSHIFT, "OP_LSHIFT", 1, opcodeDisabled),
    OpCode(OP_RSHIFT, "OP_RSHIFT", 1, opcodeDisabled),
    OpCode(OP_BOOLAND, "OP_BOOLAND", 1, opcodeBoolAnd),
    OpCode(OP_BOOLOR, "OP_BOOLOR", 1, opcodeBoolOr),
    OpCode(OP_NUMEQUAL, "OP_NUMEQUAL", 1, opcodeNumEqual),
    OpCode(OP_NUMEQUALVERIFY, "OP_NUMEQUALVERIFY", 1, opcodeNumEqualVerify),
    OpCode(OP_NUMNOTEQUAL, "OP_NUMNOTEQUAL", 1, opcodeNumNotEqual),
    OpCode(OP_LESSTHAN, "OP_LESSTHAN", 1, opcodeLessThan),
    OpCode(OP_GREATERTHAN, "OP_GREATERTHAN", 1, opcodeGreaterThan),
    OpCode(OP_LESSTHANOREQUAL, "OP_LESSTHANOREQUAL", 1, opcodeLessThanOrEqual),
    OpCode(OP_GREATERTHANOREQUAL, "OP_GREATERTHANOREQUAL", 1, opcodeGreaterThanOrEqual),
    OpCode(OP_MIN, "OP_MIN", 1, opcodeMin),
    OpCode(OP_MAX, "OP_MAX", 1, opcodeMax),
    OpCode(OP_WITHIN, "OP_WITHIN", 1, opcodeWithin),

    # Crypto opcodes.
    OpCode(OP_RIPEMD160, "OP_RIPEMD160", 1, opcodeRipemd160),
    OpCode(OP_SHA1, "OP_SHA1", 1, opcodeSha1),
    OpCode(OP_SHA256, "OP_SHA256", 1, opcodeSha256),
    OpCode(OP_HASH160, "OP_HASH160", 1, opcodeHash160),
    OpCode(OP_HASH256, "OP_HASH256", 1, opcodeHash256),
    OpCode(OP_CODESEPARATOR, "OP_CODESEPARATOR", 1, opcodeCodeSeparator),
    OpCode(OP_CHECKSIG, "OP_CHECKSIG", 1, opcodeCheckSig),
    OpCode(OP_CHECKSIGVERIFY, "OP_CHECKSIGVERIFY", 1, opcodeCheckSigVerify),
    OpCode(OP_CHECKMULTISIG, "OP_CHECKMULTISIG", 1, opcodeCheckMultiSig),
    OpCode(OP_CHECKMULTISIGVERIFY, "OP_CHECKMULTISIGVERIFY", 1, opcodeCheckMultiSigVerify),

    # Reserved opcodes.
    OpCode(OP_NOP1, "OP_NOP1", 1, opcodeNop),
    OpCode(OP_CHECKLOCKTIMEVERIFY, "OP_CHECKLOCKTIMEVERIFY", 1, opcodeCheckLockTimeVerify),
    OpCode(OP_CHECKSEQUENCEVERIFY, "OP_CHECKSEQUENCEVERIFY", 1, opcodeCheckSequenceVerify),
    OpCode(OP_NOP4, "OP_NOP4", 1, opcodeNop),
    OpCode(OP_NOP5, "OP_NOP5", 1, opcodeNop),
    OpCode(OP_NOP6, "OP_NOP6", 1, opcodeNop),
    OpCode(OP_NOP7, "OP_NOP7", 1, opcodeNop),
    OpCode(OP_NOP8, "OP_NOP8", 1, opcodeNop),
    OpCode(OP_NOP9, "OP_NOP9", 1, opcodeNop),
    OpCode(OP_NOP10, "OP_NOP10", 1, opcodeNop),

    # Undefined opcodes.
    OpCode(OP_UNKNOWN186, "OP_UNKNOWN186", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN187, "OP_UNKNOWN187", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN188, "OP_UNKNOWN188", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN189, "OP_UNKNOWN189", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN190, "OP_UNKNOWN190", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN191, "OP_UNKNOWN191", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN192, "OP_UNKNOWN192", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN193, "OP_UNKNOWN193", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN194, "OP_UNKNOWN194", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN195, "OP_UNKNOWN195", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN196, "OP_UNKNOWN196", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN197, "OP_UNKNOWN197", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN198, "OP_UNKNOWN198", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN199, "OP_UNKNOWN199", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN200, "OP_UNKNOWN200", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN201, "OP_UNKNOWN201", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN202, "OP_UNKNOWN202", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN203, "OP_UNKNOWN203", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN204, "OP_UNKNOWN204", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN205, "OP_UNKNOWN205", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN206, "OP_UNKNOWN206", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN207, "OP_UNKNOWN207", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN208, "OP_UNKNOWN208", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN209, "OP_UNKNOWN209", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN210, "OP_UNKNOWN210", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN211, "OP_UNKNOWN211", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN212, "OP_UNKNOWN212", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN213, "OP_UNKNOWN213", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN214, "OP_UNKNOWN214", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN215, "OP_UNKNOWN215", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN216, "OP_UNKNOWN216", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN217, "OP_UNKNOWN217", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN218, "OP_UNKNOWN218", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN219, "OP_UNKNOWN219", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN220, "OP_UNKNOWN220", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN221, "OP_UNKNOWN221", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN222, "OP_UNKNOWN222", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN223, "OP_UNKNOWN223", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN224, "OP_UNKNOWN224", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN225, "OP_UNKNOWN225", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN226, "OP_UNKNOWN226", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN227, "OP_UNKNOWN227", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN228, "OP_UNKNOWN228", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN229, "OP_UNKNOWN229", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN230, "OP_UNKNOWN230", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN231, "OP_UNKNOWN231", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN232, "OP_UNKNOWN232", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN233, "OP_UNKNOWN233", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN234, "OP_UNKNOWN234", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN235, "OP_UNKNOWN235", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN236, "OP_UNKNOWN236", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN237, "OP_UNKNOWN237", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN238, "OP_UNKNOWN238", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN239, "OP_UNKNOWN239", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN240, "OP_UNKNOWN240", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN241, "OP_UNKNOWN241", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN242, "OP_UNKNOWN242", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN243, "OP_UNKNOWN243", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN244, "OP_UNKNOWN244", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN245, "OP_UNKNOWN245", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN246, "OP_UNKNOWN246", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN247, "OP_UNKNOWN247", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN248, "OP_UNKNOWN248", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN249, "OP_UNKNOWN249", 1, opcodeInvalid),

    # Bitcoin Core internal use opcode.  Defined here for completeness.
    OpCode(OP_SMALLINTEGER, "OP_SMALLINTEGER", 1, opcodeInvalid),
    OpCode(OP_PUBKEYS, "OP_PUBKEYS", 1, opcodeInvalid),
    OpCode(OP_UNKNOWN252, "OP_UNKNOWN252", 1, opcodeInvalid),
    OpCode(OP_PUBKEYHASH, "OP_PUBKEYHASH", 1, opcodeInvalid),
    OpCode(OP_PUBKEY, "OP_PUBKEY", 1, opcodeInvalid),

    OpCode(OP_INVALIDOPCODE, "OP_INVALIDOPCODE", 1, opcodeInvalid),

]
