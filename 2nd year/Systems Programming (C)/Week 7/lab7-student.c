#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a structure for student data
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
        students = (Student *)realloc(students, num_students * sizeof(Student));
        capacity = num_students;
    }

    int arg_index = 1;
    for (int i = 0; i < num_students; i++) {
        strncpy(students[i].name, argv[arg_index++], 19);
        students[i].name[19] = '\0';

        strncpy(students[i].programme, argv[arg_index++], 19);
        students[i].programme[19] = '\0';

        students[i].grade = atof(argv[arg_index++]);
    }

    for (int i = 0; i < num_students; i++) {
        printf("%s, %s, %.2f\n", students[i].name, students[i].programme, students[i].grade);
    }

    free(students);
    return 0;
}