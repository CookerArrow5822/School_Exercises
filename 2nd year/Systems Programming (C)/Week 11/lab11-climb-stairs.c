#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int n;
    int i;

    n = atoi(argv[1]);

    if (n == 0) {
        printf("1\n");
        return 0;
    }

    if (n == 1) {
        printf("1\n");
        return 0;
    }


    int ways[n + 1];

    ways[0] = 1;
    ways[1] = 1;

    for (i = 2; i <= n; i++) {
        ways[i] = ways[i - 1] + ways[i - 2];
    }

    printf("%d\n", ways[n]);

    return 0;
}