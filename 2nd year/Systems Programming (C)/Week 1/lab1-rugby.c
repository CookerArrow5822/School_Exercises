#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    
    int tries = atoi(argv[1]);
    int conversion = atoi(argv[2]);
    int penalty = atoi(argv[3]);
    int drop = atoi(argv[4]);
    int total = 0;

    total = total + (tries * 5) + (conversion * 2) + (penalty * 3) + (drop * 3);

    printf("%d\n", total);
}