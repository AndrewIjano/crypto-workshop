import sys
from argparse import ArgumentParser, FileType

BASE = ord('A')

def rotate(char, shift):
    if not char.isalpha():
        return char
    return chr((ord(char) + shift - BASE) % 26 + BASE)

def vigenere_encoder(plaintext, key):
    plaintext = plaintext.upper()
    count = 0
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            ciphertext += rotate(char, ord(key[count].upper()) - BASE)
            count = (count + 1) % (len(key))
        else:
            ciphertext += char
    return ciphertext

def vigenere_decoder(ciphertext, key):
    reverse_key = ''.join(chr(26 - ord(k) + 2*BASE) for k in key.upper())
    return vigenere_encoder(ciphertext, reverse_key)

if __name__ == '__main__':
    parser = ArgumentParser(
        prog='vigenere_cipher.py',
        epilog='''
            Example:\n
            python3 vigenere_cipher.py plaintext.txt "SENHA"
            ''')
    parser.add_argument(
        'textfile', metavar='textfile', nargs=1, help='the input textfile', type=FileType('r'))
    parser.add_argument(
        'key', metavar='key', nargs=1, help='the key used to encrypt the plaintext', type=str)
    parser.add_argument(
        '-d', nargs='?', dest='decode', help='flag to decode the textfile',
        const=True, default=False)
    args = parser.parse_args()

    if args.decode:
        print(vigenere_decoder(args.textfile[0].read(), args.key[0]))
    else:
        print(vigenere_encoder(args.textfile[0].read(), args.key[0]))
