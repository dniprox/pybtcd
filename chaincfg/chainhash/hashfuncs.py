import hashlib
from .hash import Hash


# HashB calculates hash(b) and returns the resulting bytes.
# TOCLEAN equal to  golang :sha256.Sum256([]byte("hello world\n"))
def hash_b(b: bytes) -> bytes:
    # print('B is', b)
    sha256 = hashlib.sha256()
    sha256.update(b)
    # print('sha256.hexdigest() is', sha256.hexdigest())
    return sha256.digest()


# HashH calculates hash(b) and returns the resulting bytes as a Hash.
def hash_h(b: bytes) -> Hash:
    return Hash(hash_b(b))


# DoubleHashB calculates hash(hash(b)) and returns the resulting bytes.
def double_hash_b(b: bytes) -> bytes:
    return hash_b(hash_b(b))


# DoubleHashH calculates hash(hash(b)) and returns the resulting bytes as a
# Hash.
def double_hash_h(b: bytes) -> Hash:
    return Hash(double_hash_b(b))
