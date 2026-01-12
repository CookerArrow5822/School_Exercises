#include <stdio.h>
#include <stdlib.h>

int count_char_occurences(char *str, char target_char) {
    int count = 0;


    while (*str != '\0') {
        if (*str == target_char) {
            count++;
        }
        str++;
    }
    return count;
}

int main(int argc, char *argv[]) {
    char *input_string = argv[2];
    char target_char = argv[1][0];

    int occurrences = count_char_occurences(input_string, target_char);

    printf("%d\n", occurrences);

    return 0;
   
}