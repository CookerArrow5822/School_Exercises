#include <stdio.h>
#include <stdlib.h>

float find_second_largest(float *arr, int n) {
    float largest, second_largest;

    if (arr[0] > arr[1]) {
        largest = arr[0];
        second_largest = arr[1];
    } else {
        largest = arr[1];
        second_largest = arr[0];
    }

    for (int i = 2; i < n; i++) {
        if (arr[i] > largest) {
            second_largest = largest;
            largest = arr[i];
        } else if (arr[i] > second_largest && arr[i] < largest) {
            second_largest = arr[i];
        }
    }
    return second_largest;
}

int main(int argc, char *argv[]) {
    int n = argc - 1;
    
    float *numbers = (float *)malloc(n * sizeof(float));

    for (int i = 0; i < n; i++)  {
        numbers[i] = atof(argv[1 + i]);
    }

    float result = find_second_largest(numbers, n);

    printf("%.1f\n", result);

    free(numbers);
    return 0;
}