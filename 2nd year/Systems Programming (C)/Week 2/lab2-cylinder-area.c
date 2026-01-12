#include<stdio.h>
#include<stdlib.h>

int main(int argc, char*argv[])
{

    const double PI = 3.1415;

    if (argc == 1) {
        printf("No input given\n");
        return 1;
    }
    else if (argc == 2) {
        printf("Two arguments needed!\n");
        return 1;
    }


    double val1 = atof(argv[1]);
    double val2 = atof(argv[2]);

    if (val1 < 0 || val2 < 0) {
        printf("The radious or height cannot be negative!\n");
        return 1;
    }

    double area = 2 * PI * val1 * val1 + 2 * PI * val1 * val2;

    printf("%.2f\n", area);

    return 0;
}
