#include <stdio.h>
#define MAX 5

int stack[MAX], top = -1;

void push(int val) {
    if (top == MAX - 1)
        printf("Stack Overflow!\n");
    else {
        stack[++top] = val;
        printf("%d pushed to stack.\n", val);
    }
}

void pop() {
    if (top == -1)
        printf("Stack Underflow! Stack is empty.\n");
    else
        printf("%d popped from stack.\n", stack[top--]);
}

void peek() {
    if (top == -1)
        printf("Stack is empty.\n");
    else
        printf("Top element: %d\n", stack[top]);
}

void display() {
    int i;
    if (top == -1) { printf("Stack is empty.\n"); return; }
    printf("Stack (top to bottom): ");
    for (i = top; i >= 0; i--)
        printf("%d ", stack[i]);
    printf("\n");
}

int main() {
    int choice, val;
    do {
        printf("\n--- Stack Menu ---\n");
        printf("1.Push  2.Pop  3.Peek  4.Display  5.Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &val);
                push(val);
                break;
            case 2: pop(); break;
            case 3: peek(); break;
            case 4: display(); break;
            case 5: printf("Exiting...\n"); break;
            default: printf("Invalid choice!\n");
        }
    } while (choice != 5);
    return 0;
}
