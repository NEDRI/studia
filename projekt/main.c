#include <stdio.h>
#include <stdlib.h>

float obliczSrednia(float pomiary[], int liczba) {
    float suma = 0;
    for (int i = 0; i < liczba; i++) {
        suma += pomiary[i];
    }
    return suma / liczba;
}

float wartoscBezwzgledna(float wartosc) {
    if (wartosc < 0) {
        return -wartosc;
    }
    return wartosc;
}

void ocenaPartii(int poprawne, int wszystkie) {
    float procent = ((float)poprawne / wszystkie) * 100.0;
    if (procent == 100.0) {
        printf("Ocena partii: Partia prawidlowa\n");
    } else if (procent >= 80.0) {
        printf("Ocena partii: Partia warunkowo prawidlowa\n");
    } else {
        printf("Ocena partii: Partia nieprawidlowa\n");
    }
}

void generujRaport(float pomiary[], int liczba, float nominalna, float tolerancja) {
    int poprawne = 0;
    int niepoprawne = 0;
    float min = pomiary[0];
    float max = pomiary[0];
    float maxOdchylka = 0;

    printf("\nRaport kontroli jakosci:\n");
    printf("Wartosc nominalna: %.2f mm\n", nominalna);
    printf("Tolerancja: +/-%.2f mm\n", tolerancja);
    printf("Zakres poprawny: %.2f - %.2f mm\n\n", nominalna - tolerancja, nominalna + tolerancja);

    for (int i = 0; i < liczba; i++) {
        float odchylka = pomiary[i] - nominalna;
        float absOdchylka = wartoscBezwzgledna(odchylka);

        if (pomiary[i] < min) {
            min = pomiary[i];
        }
        if (pomiary[i] > max) {
            max = pomiary[i];
        }
        if (absOdchylka > maxOdchylka) {
            maxOdchylka = absOdchylka;
        }

        printf("Pomiar %d: %.2f mm\n", i + 1, pomiary[i]);
        printf("Odchylka: %.2f mm\n", odchylka);

        if (pomiary[i] >= nominalna - tolerancja && pomiary[i] <= nominalna + tolerancja) {
            printf("PRAWIDLOWY\n");
            poprawne++;
        } else {
            printf("NIEZGODNY\n");
            niepoprawne++;
        }
    }

    printf("\nLiczba detali poprawnych: %d\n", poprawne);
    printf("Liczba detali niepoprawnych: %d\n", niepoprawne);
    printf("Srednia wartosc pomiarow: %.2f mm\n", obliczSrednia(pomiary, liczba));
    printf("Najmniejszy pomiar: %.2f mm\n", min);
    printf("Najwiekszy pomiar: %.2f mm\n", max);
    printf("Najwieksza odchylka bezwzgledna: %.2f mm\n", maxOdchylka);
    
    ocenaPartii(poprawne, liczba);
}

int main() {
    int opcja;
    float nominalna = 0;
    float tolerancja = 0;
    int liczbaPomiarow = 0;
    float *pomiary = NULL;

    do {
        printf("\n--- SYSTEM KONTROLI JAKOSCI ---\n");
        printf("1. Wprowadz dane nominalne i pomiary\n");
        printf("2. Generuj raport kontroli jakosci\n");
        printf("3. Zakoncz program\n");
        printf("Wybierz operacje: ");
        scanf("%d", &opcja);

        if (opcja == 1) {
            printf("Podaj wartosc nominalna [mm]: ");
            scanf("%f", &nominalna);
            printf("Podaj tolerancje [mm]: ");
            scanf("%f", &tolerancja);
            printf("Podaj liczbe pomiarow: ");
            scanf("%d", &liczbaPomiarow);

            if (pomiary != NULL) {
                free(pomiary);
            }

            pomiary = (float*)malloc(liczbaPomiarow * sizeof(float));
            
            for (int i = 0; i < liczbaPomiarow; i++) {
                printf("Podaj wynik pomiaru %d: ", i + 1);
                scanf("%f", &pomiary[i]);
            }
            printf("Dane zostaly poprawnie wczytane.\n");
            
        } else if (opcja == 2) {
            if (pomiary == NULL) {
                printf("Brak wprowadzonych danych! Wybierz najpierw opcje 1.\n");
            } else {
                generujRaport(pomiary, liczbaPomiarow, nominalna, tolerancja);
            }
        }
    } while (opcja != 3);

    if (pomiary != NULL) {
        free(pomiary);
    }

    return 0;
}