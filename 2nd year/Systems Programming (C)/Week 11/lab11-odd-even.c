#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int number;

    number = atoi(argv[1]);

    if (number & 1) {
        printf("Odd\n");
    } else {
        printf("Even\n");
    }

    return 0;
}