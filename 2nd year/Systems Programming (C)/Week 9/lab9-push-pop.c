#include <stdio.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node *next;
};

int main(int argc, char *argv[]) {

    int n = atoi(argv[1]);

    struct Node *head = NULL;
    struct Node *tail = NULL;

    for (int i = 0; i < n; i++) {

        int num = atoi(argv[i + 2]);

        struct Node *newNode = (struct Node*) malloc(sizeof(struct Node));
        newNode->value = num;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    struct Node *temp = head;
    struct Node *prev = NULL;

    while (temp->next != NULL) {
        prev = temp;
        temp = temp->next;
    }
    prev->next = NULL;
    tail = prev;

    temp = head;
    prev = NULL;
    while (temp->next != NULL) {
        prev = temp;
        temp = temp->next;
    }
    prev->next = NULL;
    tail = prev;

    int push1 = atoi(argv[n + 2]);
    int push2 = atoi(argv[n + 3]);

    struct Node *node1 = (struct Node*) malloc(sizeof(struct Node));
    node1->value = push1;
    node1->next = NULL;
    tail->next = node1;
    tail = node1;

    struct Node *node2 = (struct Node*) malloc(sizeof(struct Node));
    node2->value = push2;
    node2->next = NULL;
    tail->next = node2;
    tail = node2;

    struct Node *cur = head;
    while (cur != NULL) {
        printf("%d\n", cur->value);
        cur = cur->next;
    }

    return 0;
}