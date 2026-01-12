#include <stdio.h>

int main(int argc, char *argv[]) {
    
    char *name = argv[1];
    char *capital = argv[2];
    char *pop_mil = argv[3];
    char *size_km2 = argv[4];

    printf("%s\n", name);
    printf("%s\n", capital);
    printf("%s million people\n", pop_mil);
    printf("%s km2\n", size_km2);

    return 0;

}