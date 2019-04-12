import sys
import random
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 one_time_pad2.py plaintext')
        print('Example:\n python3 one_time_pad2.py plaintext.txt')
    else:
        with open(sys.argv[1], 'r') as textfile:
            print((lambda x: (lambda f: ["".join(chr((ord(c) + i - f) % (ord('Z') - f + 1) + f) if c.isalpha() else c for c in x) for i in range(ord('Y') - f + 2)][random.randint(0, 25)])(ord('A')))(textfile.read()))
