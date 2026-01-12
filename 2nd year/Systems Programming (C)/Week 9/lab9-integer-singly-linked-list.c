#include <stdio.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node *next;
};

int main(int argc, char *argv[]) {

    int n = atoi(argv[1]);

    struct Node *head = NULL;
    struct Node *current = NULL;

    for (int i = 0; i < n; i++) {
        int num = atoi(argv[i + 2]);

        struct Node *newNode = (struct Node*) malloc(sizeof(struct Node));
        newNode->value = num;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
        } else {
            current->next = newNode;
        }

        current = newNode;
    }

    struct Node *temp = head;
    while (temp != NULL) {
        printf("%d\n", temp->value);
        temp = temp->next;
    }

    return 0;
}
