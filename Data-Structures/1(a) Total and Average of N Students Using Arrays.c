#include <stdio.h>
int main() {
    int n, i;
    float marks[50], total = 0, average;
    printf("Enter number of students: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        printf("Enter marks of student %d: ", i + 1);
        scanf("%f", &marks[i]);
        total += marks[i];
    }
    average = total / n;
    printf("\nTotal Marks   : %.2f", total);
    printf("\nAverage Marks : %.2f\n", average);
    return 0;
}
