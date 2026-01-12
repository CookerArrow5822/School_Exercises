#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {

    int count = argc - 1;
    int odd_count = 0;
    int numbers[10];

    for (int i = 0; i < count; i++) {
        numbers[i] = atoi(argv[i + 1]);

        if (numbers[i] % 2 != 0) {
            odd_count++;
        }

    }

    printf("%d\n", odd_count);

    return 0;
}
