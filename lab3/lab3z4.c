#include <stdio.h>

int main() {
    char znak;
    printf("Podaj Znak:");
    scanf("%c", &znak);

    printf("%c\n", znak);
    printf("%d\n", znak);
    printf("%c\n", znak + 1);
    printf("%c\n", znak + 32);

    return 0;
}