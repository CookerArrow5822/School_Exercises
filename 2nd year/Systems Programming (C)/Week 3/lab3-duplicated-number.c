#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int duplicated_number = -1;
    int found = 0;

    for (int i = 1; i < argc; i++) {
        int num1 = atoi(argv[i]);

        for (int j = i + 1; j < argc; j++) {

            int num2 = atoi(argv[j]);

            if (num1 == num2) {
                duplicated_number = num1;
                found = 1;
                break;
            }

        }
        if (found) {
            break;
        }
    }

    if (found) {
        printf("%d\n", duplicated_number);

    } else {
        printf("no duplicated number\n");

    }

    return 0;
}
