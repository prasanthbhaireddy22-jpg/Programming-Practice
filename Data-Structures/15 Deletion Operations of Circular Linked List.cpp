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
    if (head == NULL) { head = newNode; head->next = head; return; }
    struct Node *temp = head;
    while (temp->next != head) temp = temp->next;
    temp->next = newNode;
    newNode->next = head;
}

void deleteBeginning() {
    if (head == NULL) { printf("List is empty.\n"); return; }
    struct Node *temp = head, *last = head;
    if (head->next == head) {
        printf("Deleted: %d\n", head->data);
        free(head); head = NULL; return;
    }
    while (last->next != head) last = last->next;
    head = head->next;
    last->next = head;
    printf("Deleted: %d\n", temp->data);
    free(temp);
}

void deleteEnd() {
    if (head == NULL) { printf("List is empty.\n"); return; }
    struct Node *temp = head;
    if (head->next == head) {
        printf("Deleted: %d\n", head->data);
        free(head); head = NULL; return;
    }
    while (temp->next->next != head) temp = temp->next;
    printf("Deleted: %d\n", temp->next->data);
    free(temp->next);
    temp->next = head;
}

void deletePosition(int pos) {
    if (head == NULL) { printf("List is empty.\n"); return; }
    if (pos == 1) { deleteBeginning(); return; }
    struct Node *temp = head;
    int i;
    for (i = 1; i < pos - 1; i++) {
        temp = temp->next;
        if (temp == head) { printf("Position out of range.\n"); return; }
    }
    struct Node *delNode = temp->next;
    if (delNode == head) { printf("Position out of range.\n"); return; }
    temp->next = delNode->next;
    printf("Deleted: %d\n", delNode->data);
    free(delNode);
}

void display() {
    if (head == NULL) { printf("List is empty.\n"); return; }
    struct Node *temp = head;
    printf("List: ");
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("(back to %d)\n", head->data);
}

int main() {
    int choice, pos;
    insert(10); insert(20); insert(30); insert(40); insert(50);
    printf("Initial "); display();
    do {
        printf("\n--- CLL Deletion Menu ---\n");
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
