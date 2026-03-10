#include <stdio.h>

int main() {
    float liczba1, liczba2, liczba3, srednia;
    printf("Podaj trzy liczby oddzielone spacja: ");
    scanf("%f %f %f", &liczba1, &liczba2, &liczba3);
    srednia = (liczba1 + liczba2 + liczba3) / 3.0;
    printf("Srednia arytmetyczna wynosi: %f\n", srednia);
    return 0;
}