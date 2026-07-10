#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

void drukujRaport(FILE *f, float nominalna, float tolerancja, float pomiar[], int n,
                  int licznikP, int licznikN, float srednia, float min, float max, float maxOdch) {
    fprintf(f, "\nRaport kontroli jakosci:\n");
    fprintf(f, "Wartosc nominalna: %.2f mm\n", nominalna);
    fprintf(f, "Tolerancja: +/- %.2f mm\n", tolerancja);
    fprintf(f, "Zakres poprawny: %.2f - %.2f mm\n\n", nominalna - tolerancja, nominalna + tolerancja);

    for (int i = 0; i < n; i++) {
        float odchylka = pomiar[i] - nominalna;
        fprintf(f, "Pomiar %d: %.2f mm  Odchylka: %.2f mm  ", i + 1, pomiar[i], odchylka);
        if (pomiar[i] >= nominalna - tolerancja && pomiar[i] <= nominalna + tolerancja) {
            fprintf(f, "PRAWIDLOWY\n");
        } else {
            fprintf(f, "NIEZGODNY\n");
        }
    }

    fprintf(f, "\nLiczba detali poprawnych: %d\n", licznikP);
    fprintf(f, "Liczba detali niepoprawnych: %d\n", licznikN);
    fprintf(f, "Srednia wartosc pomiarow: %.2f mm\n", srednia);
    fprintf(f, "Najmniejszy pomiar: %.2f mm\n", min);
    fprintf(f, "Najwiekszy pomiar: %.2f mm\n", max);
    fprintf(f, "Najwieksza odchylka bezwzgledna: %.2f mm\n", maxOdch);

    float procent = (float)licznikP / n * 100.0f;
    if (procent == 100.0f) {
        fprintf(f, "Ocena partii: Partia prawidlowa\n");
    } else if (procent >= 80.0) {
        fprintf(f, "Ocena partii: Partia warunkowo prawidlowa\n");
    } else {
        fprintf(f, "Ocena partii: Partia nieprawidlowa\n");
    }
}

void sortuj(float pomiar[], int n, int kierunek) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            int zamien;
            if (kierunek == 1) {
                zamien = pomiar[j] > pomiar[j + 1];
            } else {
                zamien = pomiar[j] < pomiar[j + 1];
            }
            if (zamien) {
                float tmp = pomiar[j];
                pomiar[j] = pomiar[j + 1];
                pomiar[j + 1] = tmp;
            }
        }
    }
}

int main() {

    char dalej;

    do {
        float nominalna, tolerancja;
        int n = 0;
        float *pomiar = NULL;

        printf("\n=== Analiza wymiaru detalu ===\n");
        printf("Podaj wartosc nominalna [mm]: ");
        scanf("%f", &nominalna);
        printf("Podaj tolerancje [mm]: ");
        scanf("%f", &tolerancja);

        int zrodlo;
        printf("Skad wczytac pomiary? (1 - klawiatura, 2 - plik): ");
        scanf("%d", &zrodlo);

        if (zrodlo == 2) {
            char nazwa[100];
            printf("Podaj nazwe pliku (np. pomiary.txt): ");
            scanf("%99s", nazwa);

            FILE *plik = fopen(nazwa, "r");
            if (plik == NULL) {
                printf("Nie mozna otworzyc pliku %s!\n", nazwa);
                printf("Czy przeanalizowac kolejny wymiar? (t/n): ");
                scanf(" %c", &dalej);
                continue;
            }

            float tmp;
            while (fscanf(plik, "%f", &tmp) == 1) {
                n++;
            }

            if (n == 0) {
                printf("Plik nie zawiera pomiarow!\n");
                fclose(plik);
                printf("Czy przeanalizowac kolejny wymiar? (t/n): ");
                scanf(" %c", &dalej);
                continue;
            }

            pomiar = (float *)malloc(n * sizeof(float));
            if (pomiar == NULL) {
                printf("Blad alokacji pamieci!\n");
                fclose(plik);
                return 1;
            }

            rewind(plik);
            for (int i = 0; i < n; i++) {
                fscanf(plik, "%f", &pomiar[i]);
            }
            fclose(plik);
            printf("Wczytano %d pomiarow z pliku %s.\n", n, nazwa);
        } else {
            printf("Podaj liczbe pomiarow: ");
            scanf("%d", &n);

            if (n <= 0) {
                printf("Liczba pomiarow musi byc wieksza od zera!\n");
                printf("Czy przeanalizowac kolejny wymiar? (t/n): ");
                scanf(" %c", &dalej);
                continue;
            }

            pomiar = (float *)malloc(n * sizeof(float));
            if (pomiar == NULL) {
                printf("Blad alokacji pamieci!\n");
                return 1;
            }

            for (int i = 0; i < n; i++) {
                printf("Pomiar %d: ", i + 1);
                scanf("%f", &pomiar[i]);
            }
        }

        int licznikP = 0;
        int licznikN = 0;
        float suma = 0.0;
        float maxOdch = 0.0;
        float max = pomiar[0];
        float min = pomiar[0];

        for (int i = 0; i < n; i++) {
            if (pomiar[i] >= nominalna - tolerancja && pomiar[i] <= nominalna + tolerancja) {
                licznikP++;
            } else {
                licznikN++;
            }

            suma = suma + pomiar[i];

            if (pomiar[i] > max) {
                max = pomiar[i];
            }
            if (pomiar[i] < min) {
                min = pomiar[i];
            }

            float absOdch = pomiar[i] - nominalna;
            if (absOdch < 0) {
                absOdch = -absOdch;
            }
            if (absOdch > maxOdch) {
                maxOdch = absOdch;
            }
        }

        float srednia = suma / n;


        drukujRaport(stdout, nominalna, tolerancja, pomiar, n, licznikP, licznikN, srednia, min, max, maxOdch);

        char odp;
        printf("\nZapisac raport do pliku raport.txt? (t/n): ");
        scanf(" %c", &odp);
        if (odp == 't' || odp == 'T') {
            FILE *raport = fopen("raport.txt", "a");
            if (raport == NULL) {
                printf("Nie mozna otworzyc pliku raport.txt!\n");
            } else {
                drukujRaport(raport, nominalna, tolerancja, pomiar, n, licznikP, licznikN, srednia, min, max, maxOdch);
                fclose(raport);
                printf("Raport zapisano do pliku raport.txt.\n");
            }
        }

        printf("\nWyswietlic wylacznie detale niezgodne? (t/n): ");
        scanf(" %c", &odp);
        if (odp == 't' || odp == 'T') {
            if (licznikN == 0) {
                printf("Brak detali niezgodnych.\n");
            } else {
                printf("Detale niezgodne:\n");
                for (int i = 0; i < n; i++) {
                    if (pomiar[i] < nominalna - tolerancja || pomiar[i] > nominalna + tolerancja) {
                        printf("Pomiar %d: %.2f mm  Odchylka: %.2f mm  NIEZGODNY\n", i + 1, pomiar[i], pomiar[i] - nominalna);
                    }
                }
            }
        }

        int kierunek;
        printf("\nPosortowac pomiary? (1 - rosnaco, 2 - malejaco, 0 - nie): ");
        scanf("%d", &kierunek);
        if (kierunek == 1 || kierunek == 2) {
            sortuj(pomiar, n, kierunek);
            printf("Pomiary posortowane:\n");
            for (int i = 0; i < n; i++) {
                printf("%.2f mm\n", pomiar[i]);
            }
        }

        free(pomiar);

        printf("\nCzy przeanalizowac kolejny wymiar? (t/n): ");
        scanf(" %c", &dalej);

    } while (dalej == 't' || dalej == 'T');

    printf("Koniec programu.\n");
    return 0;
}
