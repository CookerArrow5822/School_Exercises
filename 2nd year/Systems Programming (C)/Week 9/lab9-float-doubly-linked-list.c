#include <stdio.h>
#include <stdlib.h>

struct DNode {
    double value;
    struct DNode *prev;
    struct DNode *next;
};

int main(int argc, char *argv[]) {

    int n = atoi(argv[1]);
    struct DNode *head = NULL;
    struct DNode *tail = NULL;

    for (int i = 0; i < n; i++) {

        double num = atof(argv[i + 2]); 

        struct DNode *newNode = (struct DNode*) malloc(sizeof(struct DNode));
        newNode->value = num;
        newNode->prev = NULL;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }

    struct DNode *temp = tail;
    while (temp != NULL) {
        printf("%.2f\n", temp->value);
        temp = temp->prev;
    }

    return 0;
}