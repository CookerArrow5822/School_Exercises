#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char str[51];
    char reversed[51];
    int length, i;

    strcpy(str, argv[1]);

    length = strlen(str);

    for (i = 0; i < length; i++) {
        reversed[i] = str[length - 1 - i];
    }

    reversed[length] = '\0';

    printf("%s\n", reversed);

    return 0;

}
