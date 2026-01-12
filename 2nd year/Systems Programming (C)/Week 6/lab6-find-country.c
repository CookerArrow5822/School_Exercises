#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Country {
    char name[50];
    char capital[50];
    float population;
    int size;
};

void printHeader() {
    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");

}

void printSmallCountries(struct Country countries[], int count) {
    for (int i = 0; i < count; i++) {
        if (countries[i].size < 100000) {
            printf("%s\t\t\t%s\t\t\t%d\t\t\t%.2f\n",
                countries[i].name,
                countries[i].capital,
                countries[i].size,
                countries[i].population);
        }
    }
}

int main(int argc, char *argv[]) {
    struct Country countries[100];
    int count = 0;

    for (int i = 1; i + 3 < argc; i +=4) {
        strcpy(countries[count].name, argv[i]);
        strcpy(countries[count].capital, argv[i + 1]);
        countries[count].population = atof(argv[i + 2]);
        countries[count].size = atoi(argv[i + 3]);
        count++;
    }

    printHeader();
    printSmallCountries(countries, count);

    return 0;
}