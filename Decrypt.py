import numpy
import Utils


def rot(ciphertext: str, val: int):
    ciphertext = ciphertext.upper()
    return Utils.rot(ciphertext, 26 - val)


def vigenere(ciphertext: str, key: str):
    plaintext: str = ""
    ciphertext = ciphertext.upper()
    key = key.upper()
    cipherChar: list = Utils.genArr(ciphertext)
    keyChar: list = Utils.vigKeyArr(key, cipherChar)
    for i in range(0, len(cipherChar)):
        if Utils.isLetter(cipherChar[i]):
            plaintext += chr((cipherChar[i] - keyChar[i] + 26) % 26 + 65)
        else:
            plaintext += chr(cipherChar[i])
    return plaintext


def railFence(ciphertext: str, val: int):
    ciphertext = ciphertext.upper()
    rows: int = int(len(ciphertext) / val) + 1
    if len(ciphertext) % val == 0:
        rows -= 1
    characters: numpy.array = numpy.empty((rows, val), dtype='object')
    return Utils.rail(characters, rows, ciphertext)


def atbash(ciphertext: str):
    return Utils.atbash(ciphertext)


def affine(ciphertext: str, a: int, b: int):
    map: list = []
    for i in range(0, 26):
        newVal: int = (Utils.modInverse(a) * (i - b)) % 26
        while newVal < 0:
            newVal += 26
        map[i] = chr(newVal + 65)
    return Utils.affineConv(ciphertext, map)
