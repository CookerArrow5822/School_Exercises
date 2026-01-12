#include <stdio.h>
#include <stdlib.h>

int dot_product(int *v1, int *v2, int n) {
    int result = 0;
    for (int i = 0; i < n; i++) {
        result += v1[i] * v2[i];

    }
    return result;
}

int main(int argc, char *argv[]) {
    
    int n = atoi(argv[1]);
    int *vector1 = (int *)malloc(n* sizeof(int));
    int *vector2 = (int *)malloc(n* sizeof(int));

    for (int i = 0; i < n; i++) {
        vector1[i] = atoi(argv[2 + i]);
    
    }
    for (int i = 0; i < n; i++) {
        vector2[i] = atoi(argv[2 + n + i]);
    }

    int result = dot_product(vector1, vector2, n);

    printf("%d\n", result);

    free(vector1);
    free(vector2);

    return 0;
}
