#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_COUNTRIES 50

typedef struct {
    char name[100];
    char capital[100];
    int size_km2;
    double population_million;

} Country;

int main(int argc, char *argv[]) {


    int count = (argc - 1) / 4;
    if (count > MAX_COUNTRIES) {
        count = MAX_COUNTRIES;
    }
    Country countries[MAX_COUNTRIES];

    int index = 1;
    for (int i = 0; i < count; i++) {

        strcpy(countries[i].name, argv[index]);
        strcpy(countries[i].capital, argv[index + 1]);

        countries[i].population_million = atof(argv[index + 2]);
        countries[i].size_km2 = atoi(argv[index + 3]);

        index += 4;
    }

    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");

    for (int i = 0; i < count; i++) {
        printf("%s\t\t\t%s\t\t\t%d\t\t\t%.2f\n",
            countries[i].name,
            countries[i].capital,
            countries[i].size_km2,
            countries[i].population_million);
        }
    
        double sum = 0.0;
        for (int i = 0; i < count; i++) {
            sum += countries[i].population_million;
        }
        double average;
        if (count > 0) {
            average = sum / count;
        } else {
            average = 0.0;
        }
    printf("Population average: %.2f\n", average);

    return 0;
}