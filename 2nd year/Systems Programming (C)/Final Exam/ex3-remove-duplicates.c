// Author Nicholas Meehan
// 10/Dec/2025
/*
Write a program that accepts a sequence of integers
from the command line and remove all duplicate values, keeping the first occurance
we must also display the output one element per line
*/

/* if i had more time i would reverse the print order as the removal of duplication works fine, it just prints in reverse*/
// adding includes
#include <stdio.h>
#include <stdlib.h>
// defining node struct
typedef struct Node {
    int value;
    struct Node* next;
} Node;
// initialising main
int main(int argc, char* argv[]) {

	    Node* head = NULL; //makes sure the first value (head) is empty

    //remove duplicates
    for (int i = 1; i < argc; i++) {
        int val = atoi(argv[i]); // reads all values
        Node* curr = head;
        int found = 0; // initialising the found variable
        
        // Check if value already exists
        while (curr) {
            if (curr->value == val) {
                found = 1; //increment the found value if a duplicate is found
                break;
            }
            curr = curr->next;
        }
        
        if (!found) {
            Node* new = malloc(sizeof(Node)); // updating the allocated memory
            new->value = val; // makes the value the current val[i] we are on
            new->next = head; // makes the next value the value of head
            head = new;
        }
    }
    
    // Print result on seperate lines
	Node* curr = head;
    while (curr) {
        printf("%d\n", curr->value); //prints the value
        curr = curr->next; // points curr to the next value
    }
    printf("\n");
    
    // Free all allocated memory
    while (head) {
        Node* temp = head;
        head = head->next;
        free(temp);
    }
    return 0; // return the program has completed correctly
}