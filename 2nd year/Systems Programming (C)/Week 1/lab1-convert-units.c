
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    double cm = atof(argv[1]);

    double inches = cm / 2.54;

    printf("%.2f\n", inches);

    return 0;

}
