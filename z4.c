#include <stdio.h>

int main() {
    int a=3;
    int b=4;
    int c=5;
    //scanf("%d %d %d", &a, &b, &c);

    int max = a;

    if (b > max) {
        max = b;
    }

    if (c > max) {
        max = c;
    }

    printf("Najwieksza liczba: %d\n", max);

    return 0;
}
