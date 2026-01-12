
#include <stdio.h>

int main(void)
{
     for (int cm = 30; cm <= 49; cm++)
     {

        double inches = cm / 2.54;
        printf("%.2f", inches);

        if ((cm - 29) % 5 == 0)
        {
            printf("\n");

        }
     }

     return 0;
}
