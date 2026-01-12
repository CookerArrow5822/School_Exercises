#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

    int count = argc - 1;
    int numbers[10];
    int even_found = 0;

    for (int i = 0; i < count; i++) {
        numbers[i] = atoi(argv[i + 1]);

    }

    for (int i = 0; i < count; i++) {

        if (numbers[i] % 2 == 0) {
            printf("%d - %d\n", i, numbers[i]);
            even_found = 1;
        }
    }

    if (!even_found) {
        printf("Not found!\n");

    }

    return 0;
}
