#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_COUNTRIES 100
#define NAME_LEN 50
#define NUM_CITIES 3

struct City {
    char name[NAME_LEN];
    float size;
};

struct Country {
    char name[NAME_LEN];
    struct City cities[NUM_CITIES];
};

void printLargestCities(struct Country countries[], int count) {
    for (int i = 0; i < count; i++) {
        int maxId = 0;
        for (int c = 1; c < NUM_CITIES; c++) {
            if (countries[i].cities[c].size > countries[i].cities[maxId].size) {
                maxId = c;
            }
        }

        printf("%s: %s\n", countries[i].name, countries[i].cities[maxId].name);
    }
}

int readCountries(int argc, char *argv[], struct Country countries[]) {
    int count = 0;
    for (int i = 1; i + 6 < argc; i += (1 + 2 * NUM_CITIES)) {
        strcpy(countries[count].name, argv[i]);
        
        int arg = i + 1;
        for (int c = 0; c < NUM_CITIES; c++) {
            strcpy(countries[count].cities[c].name, argv[arg]);
            countries[count].cities[c].size = (float)atof(argv[arg + 1]);
            arg += 2;
        }

        count++;
        if (count >= MAX_COUNTRIES) break;
    }
    return count;

}

int main(int argc, char *argv[]) {
    struct Country countries[MAX_COUNTRIES];
    int count = readCountries(argc, argv, countries);
    printLargestCities(countries, count);
    return 0;

}