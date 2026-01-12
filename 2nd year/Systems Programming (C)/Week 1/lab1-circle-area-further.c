
#include <stdio.h>
#include <stdlib.h>

#define PI 3.14

int main(int argc, char *argv[])
{

    int radius = 0;
    float area = 0.0;

    if (radius < 0);
    {
       radius = radius * -1;
       printf ("the radius of a circle cannot be negative\n");
    }
    radius = radius*radius;

    area = radius*PI;

    printf ("%.2f\n", area);

    return 0;
}
