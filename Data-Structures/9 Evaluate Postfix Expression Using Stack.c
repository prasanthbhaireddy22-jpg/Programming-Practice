#include <stdio.h>
#include <ctype.h>
#include <string.h>

int stack[50];
int top = -1;

void push(int val) {
    stack[++top] = val;
}

int pop() {
    return stack[top--];
}

int evaluatePostfix(char *expr) {
    int i, a, b;
    for (i = 0; i < strlen(expr); i++) {
        if (isdigit(expr[i])) {
            push(expr[i] - '0');
        } else {
            b = pop();
            a = pop();
            switch (expr[i]) {
                case '+': push(a + b); break;
                case '-': push(a - b); break;
                case '*': push(a * b); break;
                case '/': push(a / b); break;
            }
        }
    }
    return pop();
}

int main() {
    char expr[50];
    printf("Enter postfix expression (no spaces): ");
    scanf("%s", expr);
    printf("Result = %d\n", evaluatePostfix(expr));
    return 0;
}
