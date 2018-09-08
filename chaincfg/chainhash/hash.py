import copy

# HashSize of array used to store hashes.  See Hash.
HashSize = 32

# MaxHashStringSize is the maximum length of a Hash hash string.
MaxHashStringSize = HashSize * 2


# TOCHANGE ErrHashStrSize describes an error that indicates the caller specified a hash
# string that has too many characters.
class Err(Exception):
    def __init__(self, msg=None):
        self.msg = msg


class HashInitErr(Err):
    pass


class HashStrSizeErr(Err):
    def __init__(self, msg=None):
        if not msg:
            msg = "max hash string length is %{} bytes".format(MaxHashStringSize)
        super(HashStrSizeErr, self).__init__(msg=msg)


# bytes  <  >  Hash  <=>  str
#     \                      /
#       -------->    <-------

class Hash:
    def __init__(self, data):
        if type(data) is bytes:
            self._data = data
        elif type(data) is str:
            self._data = self.str_to_bytes(data)
        else:
            raise HashInitErr()

    def to_bytes(self):
        return self._data

    def to_str(self):
        b = bytearray(self._data)
        for i in range(0, int(HashSize / 2)):
            b[i], b[HashSize - 1 - i] = b[HashSize - 1 - i], b[i]
        return b.hex()

    @staticmethod
    def str_to_bytes(s):
        if len(s) > MaxHashStringSize:
            raise HashStrSizeErr

        if len(s) % 2 != 0:
            s = '0' + s

        # TOCHECK check if the reversed_hash correct here. make sure it's len is HashSize
        # TOCLEAN Please refer to origin
        reversed_s = bytes.fromhex(s)
        reversed_s = bytearray(reversed_s)

        for i in range(0, int(HashSize / 2)):
            reversed_s[i], reversed_s[HashSize - 1 - i] = reversed_s[HashSize - 1 - i], reversed_s[i]
        return reversed_s

    @staticmethod
    def bytes_to_str(b):
        b = bytearray(b)
        for i in range(0, int(HashSize / 2)):
            b[i], b[HashSize - 1 - i] = b[HashSize - 1 - i], b[i]
        return b.hex()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return self.to_str()

    def __repr__(self):
        return self._data.hex()

    def __eq__(self, other: 'Hash') -> bool:
        return self._data == other._data

    def copy_bytes(self):
        return copy.deepcopy(self._data)

    def set_bytes(self, b):
        self._data = copy.deepcopy(b)
