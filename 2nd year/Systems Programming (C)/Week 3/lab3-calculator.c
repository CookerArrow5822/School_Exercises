
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float multiply(float a, float b) {
    return a * b;
}

float divide(float a, float b) {
    return a / b;
}

int main(int argc, char *argv[]) {
    char *operation = argv[1];
    float num1 = atof(argv[2]);
    float num2 = atof(argv[3]);
    float result;

    if (strcmp(operation, "multiply") == 0) {
        result = multiply(num1, num2);
            printf("%f\n", result);

        }

    else if (strcmp(operation, "divide") == 0) {
        if(num2 == 0) {
            printf("invalid\n");
        } else {
            result = divide(num1, num2);
            printf("%f\n", result);
        }
    }

    return 0;
}
