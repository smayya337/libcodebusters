import random
import numpy


def isLetter(i: int):
    return 65 <= i <= 90


def alphMap():
    used = []
    for i in range(0, 26):
        used.append(False)
    map = []
    for i in range(0, 26):
        newval: int = random.randint(0, 25)
        while newval == i or used[newval]:
            newval: int = random.randint(0, 25)
        used[newval] = True
        map.append(newval)
    return map


def rail(characters, divisor: int, text: str):
    matrix(characters, divisor, "rows", text)
    out = [str(c) for character in characters for c in character if str(c) != "None"]
    return "".join(out)


def genArr(text: str):
    arr: list = [ord(l) for l in text]
    return arr


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


def matrix(characters, divisor, mode, text):
    rowToUse: int = 0
    columnToUse: int = 0
    for i in range(0, len(text)):
        characters[rowToUse][columnToUse] = text[i]
        if mode == "columns":
            columnToUse += 1
            if columnToUse % divisor == 0:
                rowToUse += 1
                columnToUse = 0
        else:
            rowToUse += 1
            if rowToUse % divisor == 0:
                columnToUse += 1
                rowToUse = 0
    return characters


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


def affineConv(text: str, map: list):
    out: str = ""
    text = text.upper()
    for i in range(0, len(text)):
        ascii_val: int = ord(text[i])
        if isLetter(ascii_val):
            out += map[ascii_val - 65]
        else:
            out += chr(ascii_val)
    return out
