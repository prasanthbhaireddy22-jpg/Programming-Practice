#include <stdio.h>
#define MAX 5

int queue[MAX], front = -1, rear = -1;

void enqueue(int val) {
    if (rear == MAX - 1)
        printf("Queue is Full!\n");
    else {
        if (front == -1) front = 0;
        queue[++rear] = val;
        printf("%d enqueued.\n", val);
    }
}

void dequeue() {
    if (front == -1 || front > rear)
        printf("Queue is Empty!\n");
    else {
        printf("%d dequeued.\n", queue[front++]);
        if (front > rear)
            front = rear = -1;
    }
}

void display() {
    int i;
    if (front == -1) { printf("Queue is Empty!\n"); return; }
    printf("Queue elements: ");
    for (i = front; i <= rear; i++)
        printf("%d ", queue[i]);
    printf("\n");
}

int main() {
    int choice, val;
    do {
        printf("\n--- Queue Menu ---\n");
        printf("1.Enqueue  2.Dequeue  3.Display  4.Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &val);
                enqueue(val);
                break;
            case 2: dequeue(); break;
            case 3: display(); break;
            case 4: printf("Exiting...\n"); break;
            default: printf("Invalid choice!\n");
        }
    } while (choice != 4);
    return 0;
}
