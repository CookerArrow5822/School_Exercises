#include <stdio.h>
#include <stdlib.h>

char find_most_frequent_char( char *str) {

    int char_counts[256] = {0};

    const char *p = str;

    while (*p != '\0') {
        if (*p != ' ') {
            char_counts[*p]++;
        }
        p++;
    }


    int max_count = 0;
    char most_frequent_char = '\0';

    for (int i = 0; i < 256; i++) {
        if (char_counts[i] > max_count) {
            max_count = char_counts[i];
            most_frequent_char = (char)i;
        }
    }
    return most_frequent_char;
}
int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s \"input string\"\n", argv[0]);
        return 1;
    }
    char *input_string = argv[1];

    char result_char = find_most_frequent_char(input_string);

    printf("%c\n", result_char);

    return 0;


}