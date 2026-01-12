#include <stdio.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node *next;
};

int main(int argc, char *argv[]) {

    int findNum = atoi(argv[1]);
    int newNum = atoi(argv[2]);

    int data[10] = {8, 7, 3, 4, 5, 6, 9, 2, 14, 12};

    struct Node *head = NULL;
    struct Node *tail = NULL;

    for (int i = 0; i < 10; i++) {
        struct Node *newNode = (struct Node*) malloc(sizeof(struct Node));
        newNode->value = data[i];
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    struct Node *cur = head;
    while (cur != NULL) {
        if (cur->value == findNum) {

            struct Node *newNode = (struct Node*) malloc(sizeof(struct Node));
            newNode->value = newNum;
            newNode->next = cur->next;
            cur->next = newNode;

            break;
        }
        cur = cur->next;
    }

    cur = head;
    while (cur != NULL) {
        printf("%d\n", cur->value);
        cur = cur->next;
    }

    return 0;
}