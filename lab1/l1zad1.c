#include <stdio.h>

int main() {
    float a, b, pole, obwod;
    printf("Podaj dlugosc boku a: ");
    scanf("%f", &a);
    printf("Podaj dlugosc boku b: ");
    scanf("%f", &b);
    pole = a * b;
    obwod = 2 * a + 2 * b;
    printf("Pole prostokata: %f\n", pole);
    printf("Obwod prostokata: %f\n", obwod);
    return 0;
}