#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        return 1;
    }

    int n = atoi(argv[1]);

    int *matrix = malloc(n * n * sizeof(int));

    for (int i = 0; i < n * n; i++) {
        matrix[i] = atoi(argv[i + 2]);
    }

    int sum = 0;

    for (int i = 0; i < n; i++) {
        sum += matrix[i * n + i];
    }

    printf("%d\n", sum);

    free(matrix);
    return 0;
}