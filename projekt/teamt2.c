#include <stdio.h>
#include <stdlib.h>

#define MAX_STUDENTOW 50

char imiona[MAX_STUDENTOW][30];
double *oceny[MAX_STUDENTOW];
int liczba_ocen[MAX_STUDENTOW];
int liczba_studentow = 0;

void dodaj_studenta() {
    if (liczba_studentow >= MAX_STUDENTOW) {
        printf("Brak miejsca na kolejnego studenta.\n");
        return;
    }
    printf("Podaj imie studenta: ");
    scanf("%29s", imiona[liczba_studentow]);
    oceny[liczba_studentow] = NULL;
    liczba_ocen[liczba_studentow] = 0;
    liczba_studentow++;
    printf("Student dodany.\n");
}

void dodaj_oceny(int i) {
    int n;
    printf("Ile ocen dodac? ");
    scanf("%d", &n);
    if (n <= 0) {
        printf("Nieprawidlowa liczba.\n");
        return;
    }

    oceny[i] = malloc(n * sizeof(double));
    if (oceny[i] == NULL) {
        printf("Blad alokacji pamieci.\n");
        return;
    }

    for (int j = 0; j < n; j++) {
        printf("Ocena %d: ", j + 1);
        scanf("%lf", &oceny[i][j]);
    }
    liczba_ocen[i] = n;
    printf("Oceny zapisane.\n");
}

void wyswietl_oceny(int i) {
    printf("Oceny studenta %s:\n", imiona[i]);
    for (int j = 0; j < liczba_ocen[i]; j++) {
        printf("  Ocena %d: %.1f\n", j + 1, oceny[i][j]);
    }
}

double oblicz_srednia(int i) {
    double suma = 0;
    for (int j = 0; j < liczba_ocen[i]; j++) {
        suma += oceny[i][j];
    }
    return suma / liczba_ocen[i];
}

void statystyki(int i) {
    if (liczba_ocen[i] == 0) {
        printf("Brak ocen.\n");
        return;
    }

    double min = oceny[i][0];
    double max = oceny[i][0];
    int niedostateczne = 0;

    for (int j = 0; j < liczba_ocen[i]; j++) {
        if (oceny[i][j] < min) min = oceny[i][j];
        if (oceny[i][j] > max) max = oceny[i][j];
        if (oceny[i][j] < 3.0) niedostateczne++;
    }

    double srednia = oblicz_srednia(i);

    printf("Student: %s\n", imiona[i]);
    wyswietl_oceny(i);
    printf("Srednia: %.2f\n", srednia);
    printf("Najlepsza ocena: %.1f\n", max);
    printf("Najgorsza ocena: %.1f\n", min);
    printf("Ocen niedostatecznych: %d\n", niedostateczne);

    if (srednia >= 3.0 && niedostateczne == 0) {
        printf("Zaliczenie: TAK\n");
    } else {
        printf("Zaliczenie: NIE\n");
    }
}

void raport_grupy() {
    if (liczba_studentow == 0) {
        printf("Brak studentow.\n");
        return;
    }
    printf("\n--- Raport grupy ---\n");
    for (int i = 0; i < liczba_studentow; i++) {
        if (liczba_ocen[i] == 0) {
            printf("%s - brak ocen\n", imiona[i]);
        } else {
            double sr = oblicz_srednia(i);
            int niedost = 0;
            for (int j = 0; j < liczba_ocen[i]; j++) {
                if (oceny[i][j] < 3.0) niedost++;
            }
            if (sr >= 3.0 && niedost == 0) {
                printf("%s - srednia %.2f - ZALICZYL\n", imiona[i], sr);
            } else {
                printf("%s - srednia %.2f - NIEZALICZYL\n", imiona[i], sr);
            }
        }
    }
}

int wybierz_studenta() {
    if (liczba_studentow == 0) {
        printf("Najpierw dodaj studenta.\n");
        return -1;
    }
    printf("Studenci:\n");
    for (int i = 0; i < liczba_studentow; i++) {
        printf("  %d. %s\n", i + 1, imiona[i]);
    }
    int wybor;
    printf("Wybierz numer: ");
    scanf("%d", &wybor);
    if (wybor < 1 || wybor > liczba_studentow) {
        printf("Zly numer.\n");
        return -1;
    }
    return wybor - 1;
}

int main() {
    int opcja;

    do {
        printf("\n=== SYSTEM OCEN STUDENTOW ===\n");
        printf("1. Dodaj studenta\n");
        printf("2. Dodaj oceny studentowi\n");
        printf("3. Wyswietl oceny studenta\n");
        printf("4. Oblicz srednia studenta\n");
        printf("5. Sprawdz zaliczenie\n");
        printf("6. Wyswietl pelny raport studenta\n");
        printf("7. Raport calej grupy\n");
        printf("0. Zakoncz\n");
        printf("Wybor: ");
        scanf("%d", &opcja);

        int idx;

        if (opcja == 1) {
            dodaj_studenta();
        } else if (opcja == 2) {
            idx = wybierz_studenta();
            if (idx >= 0) dodaj_oceny(idx);
        } else if (opcja == 3) {
            idx = wybierz_studenta();
            if (idx >= 0) wyswietl_oceny(idx);
        } else if (opcja == 4) {
            idx = wybierz_studenta();
            if (idx >= 0) {
                if (liczba_ocen[idx] == 0) {
                    printf("Brak ocen.\n");
                } else {
                    printf("Srednia: %.2f\n", oblicz_srednia(idx));
                }
            }
        } else if (opcja == 5) {
            idx = wybierz_studenta();
            if (idx >= 0) {
                if (liczba_ocen[idx] == 0) {
                    printf("Brak ocen.\n");
                } else {
                    double sr = oblicz_srednia(idx);
                    int niedost = 0;
                    for (int j = 0; j < liczba_ocen[idx]; j++) {
                        if (oceny[idx][j] < 3.0) niedost++;
                    }
                    if (sr >= 3.0 && niedost == 0) {
                        printf("%s ZALICZYL przedmiot.\n", imiona[idx]);
                    } else {
                        printf("%s NIE ZALICZYL przedmiotu.\n", imiona[idx]);
                    }
                }
            }
        } else if (opcja == 6) {
            idx = wybierz_studenta();
            if (idx >= 0) statystyki(idx);
        } else if (opcja == 7) {
            raport_grupy();
        } else if (opcja == 0) {
            printf("Do widzenia!\n");
        } else {
            printf("Nieprawidlowa opcja.\n");
        }

    } while (opcja != 0);

    for (int i = 0; i < liczba_studentow; i++) {
        free(oceny[i]);
    }

    return 0;
}
