#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 4) {
        printf("Usage: ./program <name> <marks1> <marks2>\n");
        return 1;
    }
    char *name = argv[1];
    int m1 = atoi(argv[2]);
    int m2 = atoi(argv[3]);
    int total = m1 + m2;

    printf("\n--- Student Details ---\n");
    printf("Name    : %s\n", name);
    printf("Marks 1 : %d\n", m1);
    printf("Marks 2 : %d\n", m2);
    printf("Total   : %d\n", total);
    return 0;
}
