import string
import random
import numpy
from libcodebusters import Utils
import math


def aristocrat(plaintext: str) -> str:
    ciphertext: str = ""
    alphMap: list = Utils.alphMap()
    plaintext = plaintext.strip().upper()
    for i in plaintext:
        ascii_val: int = ord(i)
        if Utils.isLetter(ascii_val):
            ciphertext += chr(alphMap[ascii_val - 65] + 65)
        else:
            ciphertext += chr(ascii_val)
    return ciphertext


def rot(plaintext: str, val: int) -> str:
    plaintext = plaintext.strip().upper()
    return Utils.rot(plaintext, val)


def randomRot(plaintext: str) -> str:
    val: int = random.randint(0, 25)
    return rot(plaintext, val)


def railFence(plaintext: str, val: int) -> str:
    plaintext = plaintext.strip().upper()
    return Utils.rail(plaintext, val, "encrypt")


def vigenere(plaintext: str, key: str) -> str:
    ciphertext: str = ""
    plaintext = plaintext.strip().upper()
    key = key.upper()
    plainChar: list = [ord(letter) for letter in plaintext]
    keyChar: list = Utils.vigKeyArr(key, plainChar)
    for i in range(0, len(plainChar)):
        if Utils.isLetter(plainChar[i]):
            ciphertext += chr((plainChar[i] + keyChar[i] - 130) % 26 + 65)
        else:
            ciphertext += chr(plainChar[i])
    return ciphertext


def patristocrat(plaintext: str) -> str:
    ciphertext: str = ""
    newCipher: str = ""
    alphMap: list = Utils.alphMap()
    plaintext = plaintext.strip().upper()
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


def atbash(plaintext: str) -> str:
    return Utils.atbash(plaintext)


def hill(plaintext: str, key: str) -> str:
    plaintext = Utils.lettersOnly(plaintext.strip().upper())
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


def affine(plaintext: str, a: int, b: int) -> str:
    alphMap: list = [chr((a * i + b) % 26 + 65) for i in range(0, 26)]
    return Utils.convert(plaintext, alphMap)


def baconian(plaintext: str) -> str:
    plaintext = Utils.lettersOnly(plaintext.strip().upper())
    punctuation: list = [c for c in string.punctuation]
    numbers = [bin(c) for c in range(0, 26)]
    numbers[9] = numbers[8]
    numbers[21] = numbers[20]
    aSym, bSym = random.sample(punctuation, 2)
    ciphertext: str = ""
    for letter in plaintext:
        binary = numbers[ord(l) - 65][2:]
        while len(binary) < 5:
            binary = "0" + binary
        ciphertext += (binary.replace("0", aSym).replace("1", bSym) + " ")
    return ciphertext.strip()


def morbit(plaintext: str, friendly: bool) -> str:
    ciphertext: str = Utils.morse(plaintext)
    numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    chunks: tuple = ("..", ".-", ".x", "-.", "--", "-x", "x.", "x-", "xx")
    pairings = {chunk: num for chunk, num in zip(chunks, numbers)}
    out: str = ""
    for count in range(0, len(ciphertext), 2):
        phrase = ciphertext[count:count + 2]
        out += str(pairings[phrase])
    pair_list = list(pairings)
    random.shuffle(pair_list)
    clues: list = list((pairings[k], k) for k in pair_list[:-3])
    random.shuffle(clues)
    return Utils.morseOut(out, clues, friendly)


def pollux(plaintext: str, friendly: bool) -> str:
    ciphertext: str = Utils.morse(plaintext)
    numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    num_lists: tuple = (numbers[0:3], numbers[3:6], numbers[6:9])
    chunks: tuple = (".", "-", "x")
    pairings = {chunk: num for chunk, num in zip(chunks, num_lists)}
    out: str = ""
    for count in range(0, len(ciphertext)):
        phrase = ciphertext[count]
        out += str(random.choice(pairings[phrase]))
    clues: list = [(value, key) for key in pairings.keys() for value in pairings[key]]
    random.shuffle(clues)
    clues = clues[:-3]
    return Utils.morseOut(out, clues, friendly)


def xenocrypt(plaintext: str) -> str:
    ciphertext: str = ""
    used = []
    for i in range(0, 27):
        used.append(False)
    alphMap: list = []
    for i in range(0, 26):
        newval: int = random.randint(0, 26)
        while newval == i or used[newval]:
            newval: int = random.randint(0, 26)
        used[newval] = True
        alphMap.append(newval)
    plaintext = plaintext.strip().upper()
    letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
    for i in plaintext:
        ascii_val: int = ord(i)
        if Utils.isLetter(ascii_val):
            ciphertext += letters[alphMap[ascii_val - 65]]
        elif ascii_val == 165:
            ciphertext += letters[26]
        else:
            ciphertext += chr(ascii_val)
    return ciphertext


def tjsoAtbash(plaintext: str) -> str:
    ciphertext: str = ""
    plaintext = plaintext.upper()
    for i in plaintext:
        ascii_val: int = ord(i)
        if 65 <= ascii_val <= 77:
            ciphertext += chr(77 - ascii_val)
        elif 78 <= ascii_val <= 90:
            ciphertext += chr(103 - ascii_val)
        else:
            ciphertext += chr(ascii_val)
    return ciphertext
