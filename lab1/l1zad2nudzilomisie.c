#include <stdio.h>

int main() {
    float liczba, suma = 0;
    int licznik = 0;

    printf("Podawaj liczby\n");
    printf("Wpisz dowolna litere aby zakonczyc:\n");

    while (scanf("%f", &liczba) == 1) {
        suma += liczba;
        licznik++;
    }

    if (licznik > 0) {
        float srednia = suma / licznik;
        printf("Srednia arytmetyczna z %d liczb wynosi: %f\n", licznik, srednia);
    } else {
        printf("Nie wprowadzono poprawnych danych\n");
    }

    return 0;
}