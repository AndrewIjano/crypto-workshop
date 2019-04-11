import sys
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
    if len(sys.argv) < 3:
        print('Usage: python3 vigenere_cipher.py plaintext key')
        print('Example:\n python3 vigenere_cipher.py plaintext.txt "SENHA"')
    else:
        with open(sys.argv[1], 'r') as textfile:
            print(vigenere_encoder(textfile.read(), sys.argv[2]))
