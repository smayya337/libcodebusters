import numpy
import Utils
import math
import sympy


def rot(ciphertext: str, val: int):
    ciphertext = ciphertext.upper()
    return Utils.rot(ciphertext, 26 - val)


def vigenere(ciphertext: str, key: str):
    plaintext: str = ""
    ciphertext = ciphertext.upper()
    key = key.upper()
    cipherChar: list = [ord(l) for l in ciphertext]
    keyChar: list = Utils.vigKeyArr(key, cipherChar)
    for i in range(0, len(cipherChar)):
        if Utils.isLetter(cipherChar[i]):
            plaintext += chr((cipherChar[i] - keyChar[i] + 26) % 26 + 65)
        else:
            plaintext += chr(cipherChar[i])
    return plaintext


def railFence(ciphertext: str, val: int):
    ciphertext = ciphertext.upper()
    return Utils.rail(ciphertext, val, "decrypt")


def atbash(ciphertext: str):
    return Utils.atbash(ciphertext)


def affine(ciphertext: str, a: int, b: int):
    mapped: list = []
    for i in range(0, 26):
        newVal: int = (Utils.modInverse(a) * (i - b)) % 26
        while newVal < 0:
            newVal += 26
        mapped[i] = chr(newVal + 65)
    return Utils.convert(ciphertext, mapped)


def hill(ciphertext: str, key: str):
    ciphertext = Utils.lettersOnly(ciphertext.upper())
    key = Utils.lettersOnly(key.upper())
    lenVal: int = math.ceil(math.sqrt(len(key)))
    squareVal: int = int(math.pow(lenVal, 2))
    while len(key) < squareVal:
        key += "Z"
    while len(ciphertext) % lenVal != 0:
        ciphertext += "Z"
    plainMatrix: numpy.array = numpy.array(list(ciphertext)).reshape((int(len(ciphertext) / lenVal), lenVal)).T
    keyMatrix: numpy.array = numpy.array(list(key)).reshape(lenVal, lenVal)
    invKey = sympy.Matrix(Utils.charToNumMatrix(keyMatrix)).inv_mod(26)
    productMatrix = numpy.matmul(invKey, Utils.charToNumMatrix(plainMatrix))
    return Utils.numToString(productMatrix)
