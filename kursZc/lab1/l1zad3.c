#include <stdio.h>

int main() {
    int wejscie_sekundy, godziny, minuty, sekundy;
    printf("Podaj liczbe sekund: ");
    scanf("%d", &wejscie_sekundy);
    godziny = wejscie_sekundy / 3600;
    minuty = (wejscie_sekundy % 3600) / 60;
    sekundy = wejscie_sekundy % 60;
    printf("%d godzina %d minuty %d sekund\n", godziny, minuty, sekundy);
    return 0;
}