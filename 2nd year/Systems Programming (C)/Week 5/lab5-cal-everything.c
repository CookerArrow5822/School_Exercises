#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// defining functions

double add (double a, double b) { return a + b; }
double subtract (double a, double b) { return a - b; }
double multiply (double a, double b) { return a * b; }
double division (double a, double b) { return a / b; }
double power (double a, double b) { return pow(a, b); }
double logsum(double a, double b) { return log(a) + log(b); }

typedef double (*calcfunction)(double, double);

int main(int argc, char *argv[]) {
    double a = atof(argv[1]);
    double b = atof(argv[2]);

    calcfunction functions[] = {add, subtract, multiply, division, power, logsum };

    for (int i = 0; i < 6; i++)
        printf("%.2f\n", functions[i](a,b));

    return 0;
}
