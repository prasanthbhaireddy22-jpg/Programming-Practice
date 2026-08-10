#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *head = NULL;

void insert(int val) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = val;
    newNode->next = NULL;
    if (head == NULL) { head = newNode; return; }
    struct Node *temp = head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}

void deleteBeginning() {
    if (head == NULL) { printf("List is empty.\n"); return; }
    struct Node *temp = head;
    head = head->next;
    printf("Deleted: %d\n", temp->data);
    free(temp);
}

void deleteEnd() {
    if (head == NULL) { printf("List is empty.\n"); return; }
    struct Node *temp = head;
    if (temp->next == NULL) {
        printf("Deleted: %d\n", temp->data);
        head = NULL; free(temp); return;
    }
    while (temp->next->next != NULL)
        temp = temp->next;
    printf("Deleted: %d\n", temp->next->data);
    free(temp->next);
    temp->next = NULL;
}

void deletePosition(int pos) {
    if (head == NULL) { printf("List is empty.\n"); return; }
    if (pos == 1) { deleteBeginning(); return; }
    struct Node *temp = head;
    int i;
    for (i = 1; i < pos - 1 && temp->next != NULL; i++)
        temp = temp->next;
    if (temp->next == NULL) { printf("Position out of range.\n"); return; }
    struct Node *delNode = temp->next;
    temp->next = delNode->next;
    printf("Deleted: %d\n", delNode->data);
    free(delNode);
}

void display() {
    struct Node *temp = head;
    if (temp == NULL) { printf("List is empty.\n"); return; }
    printf("List: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main() {
    int choice, pos;
    insert(10); insert(20); insert(30); insert(40); insert(50);
    printf("Initial "); display();
    do {
        printf("\n--- SLL Deletion Menu ---\n");
        printf("1.Delete Beginning  2.Delete End  3.Delete Position  4.Display  5.Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: deleteBeginning(); break;
            case 2: deleteEnd(); break;
            case 3:
                printf("Enter position: ");
                scanf("%d", &pos);
                deletePosition(pos);
                break;
            case 4: display(); break;
            case 5: printf("Exiting...\n"); break;
            default: printf("Invalid choice!\n");
        }
    } while (choice != 5);
    return 0;
}
