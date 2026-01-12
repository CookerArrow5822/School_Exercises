#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[20];
    char programme[20];
    float grade;
} Student;

int main(int argc, char *argv[]) {

    int num_students = (argc - 1) / 3;

    int capacity = 2;
    Student *students = (Student *)malloc(capacity * sizeof(Student));

    if (num_students > capacity) {
        Student *tmp = (Student *)realloc(students, num_students * sizeof(Student));
        students = tmp;
        capacity = num_students;
    }

    int argi = 1;
    float sum = 0.0f;
    for (int i = 0; i < num_students; i++) {
        strncpy(students[i].name, argv[argi++], 19);
        students[i].name[19] = '\0';
        strncpy(students[i].programme, argv[argi++], 19);
        students[i].programme[19] = '\0';
        students[i].grade = (float)atof(argv[argi++]);
        sum += students[i].grade;
    }

    float avg = sum / num_students;

    for (int i = 0; i < num_students; i++) {
        if (strcmp(students[i].programme, "CSCE") == 0 && students[i].grade > avg) {
            printf("%s, %.2f\n", students[i].name, students[i].grade);
        }
    }
    printf("Average grade: %.2f\n", avg);

    free(students);
    return 0;
}