#include <stdio.h>
#include <stdlib.h>

int largest_twice(const int *arr, int n) {
    if (n < 2) return 0;

    int largest = arr[0];
    int smallest = arr[0];

    for (int i = 1; i < n; i++) {
        if (arr[i] > largest)  largest  = arr[i];
        if (arr[i] < smallest) smallest = arr[i];
    }

    if (largest >= 2 * smallest) return largest;
    return 0;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <list of at least two integers>\n", argv[0]);
        return 1;
    }

    int n = argc - 1;

    int *nums = (int *)malloc(n * sizeof(int));
    if (!nums) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        nums[i] = atoi(argv[i + 1]);
    }

    int ans = largest_twice(nums, n);
    printf("%d\n", ans);

    free(nums);
    return 0;
}