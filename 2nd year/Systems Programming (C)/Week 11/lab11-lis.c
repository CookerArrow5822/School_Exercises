#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int n;
    int i, j;


    n = argc - 1;

    int arr[n];
    int lis[n];

    for (i = 0; i < n; i++) {
        arr[i] = atoi(argv[i + 1]);
    }

    for (i = 0; i < n; i++) {
        lis[i] = 1;
    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < i; j++) {
            if (arr[j] < arr[i] && lis[j] + 1 > lis[i]) {
                lis[i] = lis[j] + 1;
            }
        }
    }

    int max = lis[0];
    for (i = 1; i < n; i++) {
        if (lis[i] > max) {
            max = lis[i];
        }
    }
    printf("%d\n", max);

    return 0;
}