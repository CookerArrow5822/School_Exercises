#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int max = atoi(argv[1]);
    int current_num;

    for (int i = 2; i < argc; i++) {
        current_num = atoi(argv[i]);

        if (current_num > max) {
            max = current_num;
        }

    }

    printf("%d\n", max);

    return 0;
}
