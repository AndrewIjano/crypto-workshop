import sys

def bucketize(text, n_buckets):
    text = text.upper()
    buckets = ['']*n_buckets
    count = 0
    for char in text:
        if char.isalpha():
            buckets[count] += char
            count = (count + 1) % n_buckets
    return buckets

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 bucketize.py ciphertext n_buckets')
    else:
        with open(sys.argv[1], 'r') as textfile:
            buckets = bucketize(textfile.read(), int(sys.argv[2]))
            for i in range(len(buckets)):
                with open(f'bucket_{i}.txt', 'w+') as bucket:
                    bucket.write(buckets[i])     