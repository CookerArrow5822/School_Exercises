#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp;
    fp = fopen("studentBinary.bin", "rb");

    if (fp == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    int name_len;
    int college_len;
    int age;
    float grade;

    char *name;
    char *college;

    fread(&name_len, sizeof(int), 1, fp);
    name = (char*)malloc(name_len + 1);
    fread(name, sizeof(char), name_len, fp);
    name[name_len] = '\0';

    fread(&college_len, sizeof(int), 1, fp);
    college = (char*)malloc(college_len + 1);
    fread(college, sizeof(char), college_len, fp);
    college[college_len] = '\0';

    fread(&age, sizeof(int), 1, fp);
    fread(&grade, sizeof(float), 1, fp);

    printf("Name: %s\n", name);
    printf("College: %s\n", college);
    printf("Age: %d\n", age);
    printf("Grade: %.2f\n", grade);

    free(name);
    free(college);
    fclose(fp);

    return 0;
}