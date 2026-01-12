#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[]) {

    int start = atoi(argv[1]);
    int end = atoi(argv[2]);
    int i = start;

    while (i < end + 1) {
        if ((i % 400 == 0) || i % 4 == 0 && i % 100 != 0) {
            printf("%d\n", i);
        }
        i++;
    }
}