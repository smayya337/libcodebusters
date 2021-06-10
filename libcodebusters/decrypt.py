from numpy import array, matmul
from libcodebusters import utils
import math
from sympy import Matrix


def rot(ciphertext: str, val: int) -> str:
    ciphertext = ciphertext.upper()
    return utils.rot(ciphertext, 26 - val)


def vigenere(ciphertext: str, key: str) -> str:
    plaintext: str = ""
    ciphertext = ciphertext.upper()
    key = key.upper()
    cipher_char: list = [ord(l) for l in ciphertext]
    key_char: list = utils.vig_key_array(key, cipher_char)
    for i in range(0, len(cipher_char)):
        if utils.is_letter(cipher_char[i]):
            plaintext += chr((cipher_char[i] - key_char[i] + 26) % 26 + 65)
        else:
            plaintext += chr(cipher_char[i])
    return plaintext


def rail_fence(ciphertext: str, val: int) -> str:
    ciphertext = ciphertext.upper()
    return utils.rail(ciphertext, val, "decrypt")


def atbash(ciphertext: str) -> str:
    return utils.atbash(ciphertext)


def affine(ciphertext: str, a: int, b: int) -> str:
    mapped: list = []
    for i in range(0, 26):
        new_val: int = (pow(a, -1, 26) * (i - b)) % 26
        while new_val < 0:
            new_val += 26
        mapped[i] = chr(new_val + 65)
    return utils.convert(ciphertext, mapped)


def hill(ciphertext: str, key: str) -> str:
    ciphertext = utils.letters_only(ciphertext.upper())
    key = utils.letters_only(key.upper())
    len_val: int = math.ceil(math.sqrt(len(key)))
    square_val: int = int(math.pow(len_val, 2))
    while len(key) < square_val:
        key += "Z"
    while len(ciphertext) % len_val != 0:
        ciphertext += "Z"
    plain_matrix: array = array(list(ciphertext)).reshape((int(len(ciphertext) / len_val), len_val)).T
    key_matrix: array = array(list(key)).reshape(len_val, len_val)
    inv_key = Matrix(utils.char_to_num_matrix(key_matrix)).inv_mod(26)
    product_matrix = matmul(inv_key, utils.char_to_num_matrix(plain_matrix))
    return utils.num_to_string(product_matrix)
