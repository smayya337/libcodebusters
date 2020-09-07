import random
import numpy
import Utils
import math


def aristocrat(plaintext: str):
    ciphertext: str = ""
    map = Utils.alphMap()
    plaintext = plaintext.upper()
    for i in plaintext:
        ascii_val: int = ord(i)
        if Utils.isLetter(ascii_val):
            ciphertext += chr(map[ascii_val - 65] + 65)
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
    columns: int = int(len(plaintext) / val) + 1
    if len(plaintext) % val == 0:
        columns -= 1
    characters: numpy.array = numpy.empty((val, columns), dtype='object')
    return Utils.rail(characters, val, plaintext)


def vigenere(plaintext: str, key: str):
    ciphertext: str = ""
    plaintext = plaintext.upper()
    key = key.upper()
    plainChar: list = Utils.genArr(plaintext)
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
    map: list = Utils.alphMap()
    plaintext = plaintext.upper()
    for i in range(0, len(plaintext)):
        ascii_val: int = ord(plaintext[i])
        if Utils.isLetter(ascii_val):
            newCipher += chr(ascii_val)
    letters: int = 0
    for i in range(0, len(newCipher)):
        ascii_val: int = ord(newCipher[i])
        ciphertext += chr(map[ascii_val - 65] + 65)
        letters += 1
        if letters == 5 and i != len(newCipher) - 1:
            ciphertext += " "
            letters = 0
    return ciphertext


def atbash(plaintext: str):
    return Utils.atbash(plaintext)


def hill(plaintext: str, key: str):
    ciphertext: str = ""
    newPlain: str = ""
    newKey: str = ""
    plaintext = plaintext.upper()
    for i in range(0, len(plaintext)):
        if Utils.isLetter(ord(plaintext[i])):
            newPlain += plaintext[i]
    plaintext = newPlain
    key = key.upper()
    for i in range(0, len(key)):
        if Utils.isLetter(ord(key[i])):
            newKey += key[i]
    lenVal: int = math.ceil(math.sqrt(len(key)))
    squareVal: int = int(math.pow(lenVal, 2))
    while len(key) < squareVal:
        key += "Z"
    while len(plaintext) % lenVal != 0:
        plaintext += "Z"
    keyMatrix = numpy.empty((lenVal, lenVal), dtype=object)
    keyMatrix = Utils.matrix(keyMatrix, lenVal, "columns", key)
    for i in range(0, len(plaintext), lenVal):
        letters: list = [0 for i in range(0, lenVal)]
        for k in range(i, i + lenVal):
            letters[k % lenVal] = plaintext[k]
        for k in range(0, lenVal):
            newCharVal: int = 0
            for j in range(0, lenVal):
                keyCharVal: int = ord(keyMatrix[k][j]) - 65
                plainCharVal: int = ord(letters[j]) - 65
                newCharVal += keyCharVal * plainCharVal
            ciphertext += chr((newCharVal % 26) + 65)
    return ciphertext


def affine(plaintext: str, a: int, b: int):
    map: list = [chr((a * i + b) % 26 + 65) for i in range(0, 26)]
    return Utils.affineConv(plaintext, map)
