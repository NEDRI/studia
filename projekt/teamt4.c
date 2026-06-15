#include <stdio.h>

int main() {

    float nominalna = 50.00;
    float tolerancja = 0.10;
    float pomiar[6] = {50.02, 49.95, 50.13, 49.88, 50.00, 50.08};
    int licznikP = 0;
    int licznikN = 0;
    float max = pomiar[0];
    float min = pomiar[0];
    float suma = 0.0;
    float maxOdch = 0.0;

    printf("Raport kontroli jakosci:\n");
    printf("Wartosc nominalna: %.2f mm\n", nominalna);
    printf("Tolerancja: +/- %.2f mm\n", tolerancja);
    printf("Zakres poprawny: %.2f - %.2f mm\n\n", nominalna - tolerancja, nominalna + tolerancja);

    for (int i = 0; i < 6; i++) {
        float odchylenie = pomiar[i] - nominalna;
        printf("Pomiar %d: %.2f mm  Odchylka: %.2f mm  ", i + 1, pomiar[i], odchylenie);

        if (pomiar[i] >= nominalna - tolerancja && pomiar[i] <= nominalna + tolerancja) {
            printf("PRAWIDLOWY\n");
            licznikP++;
        } else {
            printf("NIEZGODNY\n");
            licznikN++;
        }

        suma = suma + pomiar[i];

        if (pomiar[i] > max) {
            max = pomiar[i];
        }

        if (pomiar[i] < min) {
            min = pomiar[i];
        }

        float absOdch = odchylenie;
        if (absOdch < 0) {
            absOdch = -absOdch;
        }
        if (absOdch > maxOdch) {
            maxOdch = absOdch;
        }
    }

    float srednia = suma / 6;
    float procent = (float)licznikP / 6 * 100.0;

    printf("\nLiczba detali poprawnych: %d\n", licznikP);
    printf("Liczba detali niepoprawnych: %d\n", licznikN);
    printf("Srednia wartosc pomiarow: %.2f mm\n", srednia);
    printf("Najmniejszy pomiar: %.2f mm\n", min);
    printf("Najwiekszy pomiar: %.2f mm\n", max);
    printf("Najwieksza odchylka bezwzgledna: %.2f mm\n", maxOdch);

    if (procent == 100.0) {
        printf("Ocena partii: Partia prawidlowa\n");
    } else if (procent >= 80.0) {
        printf("Ocena partii: Partia warunkowo prawidlowa\n");
    } else {
        printf("Ocena partii: Partia nieprawidlowa\n");
    }

    return 0;
}
