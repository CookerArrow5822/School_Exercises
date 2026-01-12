#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_COUNTRIES 50

struct Country {
    char name[100];
    char capital[100];
    double population_million;
    int size_km2;
};

int main(int argc, char *argv[]) {

    int numofcountries = (argc - 1) / 4;
    if (numofcountries > MAX_COUNTRIES) {
        numofcountries = MAX_COUNTRIES;
    }

    struct Country countries[MAX_COUNTRIES];

    int index = 1;
    for (int i = 0; i < numofcountries; i++) {
        strcpy(countries[i].name, argv[index]);
        strcpy(countries[i].capital, argv[index + 1]);

        countries[i].population_million = atof(argv[index + 2]);
        countries[i].size_km2 = atoi(argv[index + 3]);

        index += 4;

    }

    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");

    for (int i = 0; i < numofcountries; i++) {
        printf("%s\t\t\t%s\t\t\t%d\t\t\t%.2f\n",
            countries[i].name,
            countries[i].capital,
            countries[i].size_km2,
            countries[i].population_million);
    }

    return 0;
}