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

    for (int i = 0; i < strlen(msg); i++)
        cipher_msg[i] = rotate(shift, cipher_msg[i]);

    return cipher_msg;
}

char *decode(int shift, char *msg)
{
    return encode(26 - shift, msg);
}

void brute_force(char *msg)
{
    // brute-force attack
}

int main()
{
    char msg[10000];
    int shift;
    scanf("%s", msg);
    brute_force(msg);
    return 0;
}
