import sys
import random
BASE = ord('A')

def rotate(char, shift):
    if not char.isalpha():
        return char
    return chr((ord(char) + shift - BASE) % 26 + BASE)

def encoder(plaintext):
    plaintext = plaintext.upper()
    ciphertext = ''
    random.seed(BASE - 66)
    for char in plaintext:
        if char.isalpha():
            ciphertext += rotate(char, (random.randint(0, 25) + BASE))
        else:
            ciphertext += char
    return ciphertext

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 one_time_pad.py plaintext')
        print('Example:\n python3 one_time_pad.py plaintext.txt')
    else:
        with open(sys.argv[1], 'r') as textfile:
            print(encoder(textfile.read()))
