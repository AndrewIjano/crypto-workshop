#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define BASE (int)'A'

char rotate(int shift, char chr)
{
    if (!isalpha(chr))
        return chr;

    return ((int)toupper(chr) + shift - BASE) % 26 + BASE;
}

char *encode(int shift, char *msg)
{
    char *cipher_msg = strdup(msg);

    // encrypts the msg

    return cipher_msg;
}

char *decode(int shift, char *msg)
{
    // decrypts the msg
}

int main()
{
    char *msg;
    int shift;
    scanf("%s", msg);
    scanf("%d", &shift);

    printf("%s", encode(msg, shift));
    return 0;
}
