import numpy as np
import sys

EncoderOutput = np.array([])

def bits(f):
    bytes = (ord(b) for b in f.read())
    for b in bytes:
        for i in range(8):
            yield (b >> i) & 1

def init_dict():
    dictionary = {}
    for i in range(0, 2):
        dictionary[(i,)] = i
    return dictionary

def init_dict_encoder():
    dictionary = {}
    for i in range(0, 2):
        dictionary[i] = (i,)
    return dictionary

def encode():
    dictionary = init_dict()
    file = open("sine.wav", 'rb')

    foundChars = ()
    result = []
    while 1:
        byte = file.read(1)

        if not byte:
            result.append(dictionary.get(foundChars))
            break
        b = int.from_bytes(byte, 'big')
        for i in reversed(range(8)):

            character = (b >> i) & 1
            charsToAdd = foundChars + (character, )

            if charsToAdd in dictionary:
                foundChars = charsToAdd
            else:
                result.append(dictionary.get(foundChars))
                dictionary[charsToAdd] = len(dictionary)
                foundChars = (character,)

    return result


def decode(encoded: list):
    dictionary = init_dict_encoder()
    characters = (encoded.pop(0),)
    result = list(characters)

    for code in encoded:

        if code in dictionary:
            entry = dictionary[code]
        else:
            entry = characters + (characters[0],)
        for number in entry:
            result.append(number)
        dictionary[len(dictionary)] = characters + (entry[0],)
        characters = entry
    return result


code = encode()
print(code)
print(len(code))
print(max(code))
import pickle

with open('plik.bin', 'wb') as file:
    pickle.dump(code, file)

result = decode(code)
with open("decom.wav", 'wb') as f:
    for r in result:
        f.write(r.to_bytes(1, 'big'))