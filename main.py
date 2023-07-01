import numpy as np
import sys

EncoderOutput = np.array([])

def init_dict():
    dictionary = {}
    for i in range(0, 256):
        dictionary[chr(i)] = i
    return dictionary

def init_dict_encoder():
    dictionary = {}
    for i in range(0, 256):
        dictionary[i] = chr(i)
    return dictionary

def encode():
    dictionary = init_dict()
    file = open("test", 'rb')

    foundChars = ""
    result = []
    while 1:
        byte = file.read(1)
        if not byte:
            result.append(dictionary.get(foundChars))
            break
        character = byte.decode("utf-8")
        charsToAdd = foundChars + character

        if charsToAdd in dictionary:
            foundChars = charsToAdd
        else:
            result.append(dictionary.get(foundChars))
            dictionary[charsToAdd] = len(dictionary)
            foundChars = character

    return result


def decode(encoded: list):
    dictionary = init_dict_encoder()
    characters = chr(encoded.pop(0))
    result = list(characters)

    for code in encoded:

        if code in dictionary:
            entry = dictionary[code]
        else:
            entry = characters + characters[0]
        result.append(entry)
        dictionary[len(dictionary)] = characters + entry[0]
        characters = entry
    return result


def convert(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

    # return string
    return new

code = encode()
print(code)
result = decode(code)
print(result)
print(convert(result))