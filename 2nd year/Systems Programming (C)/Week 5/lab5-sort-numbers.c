#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ascending(int a, int b) { return a > b; }
int descending(int a, int b) { return a < b; }

typedef int (*choice) (int, int);

void bubblesort(int arr[], int n, choice cmp) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (cmp(arr[j], arr[j + 1])) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main(int argc, char *argv[]) {

    int n = atoi(argv[1]);
    int arr[n];


    for (int i = 0; i < n; i++) {
        arr[i] = atoi(argv[i + 2]);
    }

    char *order = argv[n + 2];

    choice cmp;
    if (strcmp(order, "asc") == 0)
        cmp = ascending;
    else
        cmp = descending;

    bubblesort(arr, n, cmp);

    printf("Sorted numbers:");
    for (int i = 0; i < n; i++) {
        printf(" %d", arr[i]);
    }
    printf("\n");

    return 0;
}
