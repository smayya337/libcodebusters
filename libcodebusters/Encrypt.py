import string
import random
import numpy
from libcodebusters import Utils
import math


def aristocrat(plaintext: str):
    ciphertext: str = ""
    alphMap = Utils.alphMap()
    plaintext = plaintext.upper()
    for i in plaintext:
        ascii_val: int = ord(i)
        if Utils.isLetter(ascii_val):
            ciphertext += chr(alphMap[ascii_val - 65] + 65)
        else:
            ciphertext += chr(ascii_val)
    return ciphertext


def rot(plaintext: str, val: int):
    plaintext = plaintext.upper()
    return Utils.rot(plaintext, val)


def randomRot(plaintext: str):
    val: int = random.randint(0, 25)
    return rot(plaintext, val)


def railFence(plaintext: str, val: int):
    plaintext = plaintext.upper()
    return Utils.rail(plaintext, val, "encrypt")


def vigenere(plaintext: str, key: str):
    ciphertext: str = ""
    plaintext = plaintext.upper()
    key = key.upper()
    plainChar: list = [ord(l) for l in plaintext]
    keyChar: list = Utils.vigKeyArr(key, plainChar)
    for i in range(0, len(plainChar)):
        if Utils.isLetter(plainChar[i]):
            ciphertext += chr((plainChar[i] + keyChar[i] - 130) % 26 + 65)
        else:
            ciphertext += chr(plainChar[i])
    return ciphertext


def patristocrat(plaintext: str):
    ciphertext: str = ""
    newCipher: str = ""
    alphMap: list = Utils.alphMap()
    plaintext = plaintext.upper()
    for i in range(0, len(plaintext)):
        ascii_val: int = ord(plaintext[i])
        if Utils.isLetter(ascii_val):
            newCipher += chr(ascii_val)
    letters: int = 0
    for i in range(0, len(newCipher)):
        ascii_val: int = ord(newCipher[i])
        ciphertext += chr(alphMap[ascii_val - 65] + 65)
        letters += 1
        if letters == 5 and i != len(newCipher) - 1:
            ciphertext += " "
            letters = 0
    return ciphertext


def atbash(plaintext: str):
    return Utils.atbash(plaintext)


def hill(plaintext: str, key: str):
    plaintext = Utils.lettersOnly(plaintext.upper())
    key = Utils.lettersOnly(key.upper())
    lenVal: int = math.ceil(math.sqrt(len(key)))
    squareVal: int = int(math.pow(lenVal, 2))
    while len(key) < squareVal:
        key += "Z"
    while len(plaintext) % lenVal != 0:
        plaintext += "Z"
    plainMatrix: numpy.array = numpy.array(list(plaintext)).reshape((int(len(plaintext) / lenVal), lenVal)).T
    keyMatrix: numpy.array = numpy.array(list(key)).reshape(lenVal, lenVal)
    productMatrix = numpy.matmul(Utils.charToNumMatrix(keyMatrix), Utils.charToNumMatrix(plainMatrix))
    return Utils.numToString(productMatrix)


def affine(plaintext: str, a: int, b: int):
    alphMap: list = [chr((a * i + b) % 26 + 65) for i in range(0, 26)]
    return Utils.convert(plaintext, alphMap)


def baconian(plaintext: str):
    plaintext = Utils.lettersOnly(plaintext.upper())
    punctuation: list = [c for c in string.punctuation]
    numbers = [bin(c) for c in range(0, 26)]
    numbers[9] = numbers[8]
    numbers[21] = numbers[20]
    aSym, bSym = random.sample(punctuation, 2)
    ciphertext: str = ""
    for l in plaintext:
        binary = numbers[ord(l) - 65][2:]
        while len(binary) < 5:
            binary = "0" + binary
        ciphertext += (binary.replace("0", aSym).replace("1", bSym) + " ")
    return ciphertext.strip()
