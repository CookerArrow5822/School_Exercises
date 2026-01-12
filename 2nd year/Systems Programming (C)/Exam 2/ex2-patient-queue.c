//Author: Nicholas Meehan
//Date 27/11/2025
/* Take a patent queue system, order the patients in terms of id
and then rint their name and priority while keeping track of the number of
high priority clients (those 4 and above)
*/

// adding all includes
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// making struct type
typedef struct Queue Queue;
// defining struct
struct Queue
{
	int ID;
	char name[20];
	int priority;
};
// declaring functions
void AddPerson(Queue q[], int argc, char*argv[]);
void PrintQueue(Queue q[], int NumOfPeople);
// main
int main(int argc, char* argv[]) {
	Queue person[50]; //defined queue to have max of 50 people
	int NumOfPeople = atoi(argv[1]);
	// calling functions
	AddPerson(person, argc, argv);
	PrintQueue(person, NumOfPeople);
}

void AddPerson(Queue q[], int argc, char*argv[]) {
	int NumOfPeople = atoi(argv[1]); // gets num of people
	int index = 2; // skips file name and num of people
	for(int i = 1; i < NumOfPeople + 1; i++) { // starting on one o avoid id 0 so i must also add that to num of people
		q[i].ID = i; // giving each person an id using the increment
		strcpy(q[i].name, argv[index]); // name being added to struct
		q[i].priority = atoi(argv[index + 1]); // priority added to struct
		index = index + 2;
	} 
}


void PrintQueue(Queue q[], int NumOfPeople) {
	int HighPriority = 0; // defining highpriority
	for(int i = 1; i < NumOfPeople + 1; ++i){ // same as addperson
		if (q[i].priority >= 4){ // any person with a priority <= 4 is added to an incrementing variable
			HighPriority += 1;
		}
		printf("ID: %d, Name: %s, Priority: %d\n", q[i].ID, q[i].name, q[i].priority); // prints out the patients id in order of id number
	}
	printf("High priority count: %d\n", HighPriority);// highpriority printed out of for loop for 1 clean print
}