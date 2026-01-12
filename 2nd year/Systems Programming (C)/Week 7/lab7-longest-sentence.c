#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int find_longest_length(char **arr, int n) {
    int max_len = strlen(arr[0]);
    for (int i = 1; i < n; i++) {
        int len = strlen(arr[i]);
        if (len > max_len) {
            max_len = len;
        }
    }
    return max_len;
}

void print_longest_strings(char **arr, int n, int max_len) {
    for (int i = 0; i < n; i++) {
        if ((int)strlen(arr[i]) == max_len) {
            printf("%s\n", arr[i]);
        }
    }
}

int main(int argc, char *argv[]) {


    int n = argc - 1;

    char **strings = (char **)malloc(n * sizeof(char *));

    for (int i = 0; i < n; i++) {
        strings[i] = (char *)malloc((strlen(argv[i + 1]) + 1) * sizeof(char));
        strcpy(strings[i], argv[i + 1]);
    }

    int max_len = find_longest_length(strings, n);
    print_longest_strings(strings, n, max_len);

    for (int i = 0; i < n; i++) {
        free(strings[i]);
    }
    free(strings);

    return 0;
}