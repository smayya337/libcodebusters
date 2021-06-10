import random
from numpy import array, empty
import math
from typing import Union, List, Tuple, Dict


def is_letter(i: int) -> bool:
    return 65 <= i <= 90


def alph_map() -> List[int]:
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


def rail(text: str, divisor: int, mode: str) -> str:
    characters: array = []
    text_len: int = len(text)
    val: int = math.ceil(len(text) / divisor)
    while len(text) < (val * divisor):
        text += " "
    if mode == "encrypt":
        characters = array(list(text)).reshape(val, divisor).T
    elif mode == "decrypt":
        characters = array(list(text)).reshape(divisor, val).T
    out = [str(c) for character in characters for c in character]
    return "".join(out)[0:text_len]


def vig_key_array(text: str, arr: list) -> List[str]:
    key_index: int = 0
    key_char: list = []
    for i in range(0, len(arr)):
        if is_letter(arr[i]):
            key_char.append(ord(text[key_index]))
            key_index += 1
            if key_index == len(text):
                key_index = 0
        else:
            key_char.append(0)
    return key_char


def rot(text: str, val: int) -> str:
    out: str = ""
    for i in text:
        ascii_val: int = ord(i)
        if is_letter(ascii_val):
            out += chr((ascii_val - 65 + val) % 26 + 65)
        else:
            out += chr(ascii_val)
    return out


def atbash(text: str) -> str:
    out: str = ""
    text = text.upper()
    for i in text:
        ascii_val: int = ord(i)
        if is_letter(ascii_val):
            out += chr(155 - ascii_val)
        else:
            out += chr(ascii_val)
    return out


def convert(text: str, mapped: list) -> str:
    out: str = ""
    text = text.upper()
    for i in range(0, len(text)):
        ascii_val: int = ord(text[i])
        if is_letter(ascii_val):
            out += mapped[ascii_val - 65]
        else:
            out += chr(ascii_val)
    return out


def letters_only(text: str) -> str:
    chars: list = [l for l in text if is_letter(ord(l))]
    return "".join(chars)


def char_to_num_matrix(matrix: array) -> array:
    nums: array = empty((len(matrix), len(matrix[0])), dtype='int')
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            nums[i][j] = ord(matrix[i][j]) - 65
    return nums


def num_to_string(matrix: array) -> str:
    chars: str = ""
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix)):
            chars += chr(matrix[j][i] % 26 + 65)
    return chars


def morse(text: str) -> str:
    text = text.strip().upper()
    ciphertext: str = ""
    morse_code_dict = {"A": ".-", "B": "-...",
                       "C": "-.-.", "D": "-..", "E": ".",
                       "F": "..-.", "G": "--.", "H": "....",
                       "I": "..", "J": ".---", "K": "-.-",
                       "L": ".-..", "M": "--", "N": "-.",
                       "O": "---", "P": ".--.", "Q": "--.-",
                       "R": ".-.", "S": "...", "T": "-",
                       "U": "..-", "V": "...-", "W": ".--",
                       "X": "-..-", "Y": "-.--", "Z": "--.."}
    for c in text:
        if is_letter(ord(c)):
            ciphertext += morse_code_dict[c]
            ciphertext += "x"
        elif c == " ":
            ciphertext += "x"
    if len(ciphertext) % 2 == 0 and ciphertext[-2:] == "xx":
        ciphertext = ciphertext[:-2]
    elif len(ciphertext) % 2 == 1 and ciphertext[-1:] == "x":
        ciphertext = ciphertext[:-1]
    return ciphertext


def morse_out(out: str, clues: list, friendly: bool) -> Union[str, Tuple[str, Dict[Union[str, int], Union[str, int]]]]:
    if friendly:
        formatted: str = f"""{out} given that:
    {clues[0][0]} = {clues[0][1]}
    {clues[1][0]} = {clues[1][1]}
    {clues[2][0]} = {clues[2][1]}
    {clues[3][0]} = {clues[3][1]}
    {clues[4][0]} = {clues[4][1]}
    {clues[5][0]} = {clues[5][1]}
    """
        return formatted
    else:
        return out, {c[0]: c[1] for c in clues}


def tjso_atbash(text: str) -> str:
    out: str = ""
    text = text.upper()
    for i in text:
        ascii_val: int = ord(i)
        if 65 <= ascii_val <= 77:
            out += chr(142 - ascii_val)
        elif 78 <= ascii_val <= 90:
            out += chr(168 - ascii_val)
        else:
            out += chr(ascii_val)
    return out
