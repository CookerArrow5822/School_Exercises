#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int target = atoi(argv[1]);
    int array_length = argc - 2;
    int found_index = -1;

    for (int i = 2; i < argc; i++) {
        int current_element = atoi(argv[i]);

        if (current_element == target) {
            found_index = i - 2;
            break;

        }
    }

    if (found_index != -1) {
        printf("Found %d at %d\n", target, found_index);
        } else {
            printf("%d not found\n", target);

        }

        return 0;
}
