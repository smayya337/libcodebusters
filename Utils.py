import random
import numpy
import math


def isLetter(i: int):
    return 65 <= i <= 90


def alphMap():
    used = []
    for i in range(0, 26):
        used.append(False)
    mapped: list = []
    for i in range(0, 26):
        newval: int = random.randint(0, 25)
        while newval == i or used[newval]:
            newval: int = random.randint(0, 25)
        used[newval] = True
        mapped.append(newval)
    return mapped


def rail(text: str, divisor: int, mode: str):
    characters: numpy.array = []
    textLen: int = len(text)
    val: int = math.ceil(len(text) / divisor)
    while len(text) < (val * divisor):
        text += " "
    if mode == "encrypt":
        characters = numpy.array(list(text)).reshape(val, divisor).T
    elif mode == "decrypt":
        characters = numpy.array(list(text)).reshape(divisor, val).T
    out = [str(c) for character in characters for c in character]
    return "".join(out)[0:textLen]


def vigKeyArr(text: str, arr: list):
    keyIndex: int = 0
    keyChar: list = []
    for i in range(0, len(arr)):
        if isLetter(arr[i]):
            keyChar.append(ord(text[keyIndex]))
            keyIndex += 1
            if keyIndex == len(text):
                keyIndex = 0
        else:
            keyChar.append(0)
    return keyChar


def rot(text: str, val: int):
    out: str = ""
    for i in text:
        ascii_val: int = ord(i)
        if isLetter(ascii_val):
            out += chr((ascii_val - 65 + val) % 26 + 65)
        else:
            out += chr(ascii_val)
    return out


def atbash(text: str):
    out: str = ""
    text = text.upper()
    for i in text:
        ascii_val: int = ord(i)
        if isLetter(ascii_val):
            out += chr(155 - ascii_val)
        else:
            out += chr(ascii_val)
    return out


def modInverse(i: int):
    i = i % 26
    if i == 1:
        return 1
    elif i == 3:
        return 9
    elif i == 5:
        return 21
    elif i == 7:
        return 15
    elif i == 9:
        return 3
    elif i == 11:
        return 19
    elif i == 15:
        return 7
    elif i == 17:
        return 23
    elif i == 19:
        return 11
    elif i == 21:
        return 15
    elif i == 23:
        return 17
    else:
        return 25


def convert(text: str, mapped: list):
    out: str = ""
    text = text.upper()
    for i in range(0, len(text)):
        ascii_val: int = ord(text[i])
        if isLetter(ascii_val):
            out += mapped[ascii_val - 65]
        else:
            out += chr(ascii_val)
    return out


def lettersOnly(text: str):
    chars: list = [l for l in text if isLetter(ord(l))]
    return "".join(chars)


def charToNumMatrix(matrix: numpy.array):
    nums: numpy.array = numpy.empty((len(matrix), len(matrix[0])), dtype='int')
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            nums[i][j] = ord(matrix[i][j]) - 65
    return nums


def numToString(matrix: numpy.array):
    chars: str = ""
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix)):
            chars += chr(matrix[j][i] % 26 + 65)
    return chars
