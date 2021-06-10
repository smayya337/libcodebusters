import string
import random
from numpy import array, matmul
from libcodebusters import utils
import math


def aristocrat(plaintext: str) -> str:
    ciphertext: str = ""
    alph_map: list = utils.alph_map()
    plaintext = plaintext.strip().upper()
    for i in plaintext:
        ascii_val: int = ord(i)
        if utils.is_letter(ascii_val):
            ciphertext += chr(alph_map[ascii_val - 65] + 65)
        else:
            ciphertext += chr(ascii_val)
    return ciphertext


def rot(plaintext: str, val: int) -> str:
    plaintext = plaintext.strip().upper()
    return utils.rot(plaintext, val)


def random_rot(plaintext: str) -> str:
    val: int = random.randint(0, 25)
    return rot(plaintext, val)


def rail_fence(plaintext: str, val: int) -> str:
    plaintext = plaintext.strip().upper()
    return utils.rail(plaintext, val, "encrypt")


def vigenere(plaintext: str, key: str) -> str:
    ciphertext: str = ""
    plaintext = plaintext.strip().upper()
    key = key.upper()
    plain_char: list = [ord(letter) for letter in plaintext]
    key_char: list = utils.vig_key_array(key, plain_char)
    for i in range(0, len(plain_char)):
        if utils.is_letter(plain_char[i]):
            ciphertext += chr((plain_char[i] + key_char[i] - 130) % 26 + 65)
        else:
            ciphertext += chr(plain_char[i])
    return ciphertext


def patristocrat(plaintext: str) -> str:
    ciphertext: str = ""
    new_cipher: str = ""
    alph_map: list = utils.alph_map()
    plaintext = plaintext.strip().upper()
    for i in range(0, len(plaintext)):
        ascii_val: int = ord(plaintext[i])
        if utils.is_letter(ascii_val):
            new_cipher += chr(ascii_val)
    letters: int = 0
    for i in range(0, len(new_cipher)):
        ascii_val: int = ord(new_cipher[i])
        ciphertext += chr(alph_map[ascii_val - 65] + 65)
        letters += 1
        if letters == 5 and i != len(new_cipher) - 1:
            ciphertext += " "
            letters = 0
    return ciphertext


def atbash(plaintext: str) -> str:
    return utils.atbash(plaintext)


def hill(plaintext: str, key: str) -> str:
    plaintext = utils.letters_only(plaintext.strip().upper())
    key = utils.letters_only(key.upper())
    len_val: int = math.ceil(math.sqrt(len(key)))
    square_val: int = int(math.pow(len_val, 2))
    while len(key) < square_val:
        key += "Z"
    while len(plaintext) % len_val != 0:
        plaintext += "Z"
    plain_matrix: array = array(list(plaintext)).reshape((int(len(plaintext) / len_val), len_val)).T
    key_matrix: array = array(list(key)).reshape(len_val, len_val)
    product_matrix = matmul(utils.char_to_num_matrix(key_matrix), utils.char_to_num_matrix(plain_matrix))
    return utils.num_to_string(product_matrix)


def affine(plaintext: str, a: int, b: int) -> str:
    alph_map: list = [chr((a * i + b) % 26 + 65) for i in range(0, 26)]
    return utils.convert(plaintext, alph_map)


def baconian(plaintext: str) -> str:
    plaintext = utils.letters_only(plaintext.strip().upper())
    punctuation: list = [c for c in string.punctuation]
    numbers = [bin(c) for c in range(0, 26)]
    numbers[9] = numbers[8]
    numbers[21] = numbers[20]
    a_sym, b_sym = random.sample(punctuation, 2)
    ciphertext: str = ""
    for letter in plaintext:
        binary = numbers[ord(letter) - 65][2:]
        while len(binary) < 5:
            binary = "0" + binary
        ciphertext += (binary.replace("0", a_sym).replace("1", b_sym) + " ")
    return ciphertext.strip()


def morbit(plaintext: str, friendly: bool) -> str:
    ciphertext: str = utils.morse(plaintext)
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
    return utils.morse_out(out, clues, friendly)


def pollux(plaintext: str, friendly: bool) -> str:
    ciphertext: str = utils.morse(plaintext)
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
    return utils.morse_out(out, clues, friendly)


def xenocrypt(plaintext: str) -> str:
    ciphertext: str = ""
    used = []
    for i in range(0, 27):
        used.append(False)
    alph_map: list = []
    for i in range(0, 26):
        newval: int = random.randint(0, 26)
        while newval == i or used[newval]:
            newval: int = random.randint(0, 26)
        used[newval] = True
        alph_map.append(newval)
    plaintext = plaintext.strip().upper()
    letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
    for i in plaintext:
        ascii_val: int = ord(i)
        if utils.is_letter(ascii_val):
            ciphertext += letters[alph_map[ascii_val - 65]]
        elif ascii_val == 165:
            ciphertext += letters[26]
        else:
            ciphertext += chr(ascii_val)
    return ciphertext


def tjso_atbash(plaintext: str) -> str:
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
