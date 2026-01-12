#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char *argv[]) {
    char str[100];
    strcpy(str, argv[1]);

    char largestNumber[50] = "";
    char *token = strtok(str, " ");

    while (token != NULL) {
        if (strlen(token) > strlen(largestNumber)){
            strcpy(largestNumber, token);

        }
        token = strtok(NULL, " ");
        
    }

    printf("%s\n", largestNumber);
}