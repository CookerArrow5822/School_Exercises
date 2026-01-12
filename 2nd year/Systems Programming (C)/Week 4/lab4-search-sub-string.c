#include <stdio.h>
#include <string.h>

int find_substring(char *str, char *sub, int *start, int *end) {
    int len_str = strlen(str);
    int len_sub = strlen(sub);

    for (int i = 0; i <= len_str - len_sub; i++) {
        int j;
        for (j = 0; j < len_sub; j++) {
            if (str[i + j] != sub[j]) {
                break;
            }
        }

        if (j == len_sub) {
        *start = i;
        *end = i + len_sub - 1;
        return 1;
    }

    }

    return 0;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        return 1;
    }

    char *str = argv[1];
    char *sub = argv[2];
    int start, end;

    if (find_substring(str, sub, &start, &end)) {
        printf("%d %d\n", start, end);
    }

    return 0;
}