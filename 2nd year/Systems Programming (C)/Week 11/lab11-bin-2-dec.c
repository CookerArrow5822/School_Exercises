#include <stdio.h>
#include <stdlib.h>

void convert(char *bits[], int count, int *answer)
{
    int i;
    int value = 0;

    for (i = 0; i < count; i++) {
        value = value * 2;
        value = value + (bits[i][0] - '0');
    }

    *answer = value;
}

int main(int argc, char *argv[])
{
    int numBits = argc - 1;
    int i;
    int result;

    if (numBits > 8) {
        printf("Too many binary digits entered.\n");
        return 0;
    }

    for (i = 1; i < argc; i++) {
        if (argv[i][1] != '\0' || (argv[i][0] != '0' && argv[i][0] != '1')) {
            printf("Only digits 1 and 0 are permitted.\n");
            return 0;
        }
    }

    convert(&argv[1], numBits, &result);
    printf("%d\n", result);

    return 0;
}