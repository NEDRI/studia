#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void wypiszMenu();
void przeliczCzas(int sekundyCalkowite);
void operacjeNaZnakach(char znak);
int czyTrojkat(float a, float b, float c);
void graZgadywanka();
void operacjeMacierzowe();
void dynamicznaTablicaOdwrocona(int n);
int fibonacciRekurencja(int n);
int sumaCyfrRekurencja(int n);

int main() {
    srand(time(NULL));
    int wybor = 0;

    while (wybor != 6) {
        wypiszMenu();
        scanf("%d", &wybor);

        if (wybor == 1) {
            int podaneSekundy;
            scanf("%d", &podaneSekundy);
            przeliczCzas(podaneSekundy);
        } else if (wybor == 2) {
            char z = 'A';
            operacjeNaZnakach(z);
        } else if (wybor == 3) {
            float bokA = 3.0, bokB = 4.0, bokC = 5.0;
            if (czyTrojkat(bokA, bokB, bokC)) {
                printf("Trojkat jest mozliwy\n");
            } else {
                printf("Trojkat nie jest mozliwy\n");
            }
        } else if (wybor == 4) {
            graZgadywanka();
        } else if (wybor == 5) {
            operacjeMacierzowe();
            dynamicznaTablicaOdwrocona(5);
            
            int nFib = 6;
            printf("%d\n", fibonacciRekurencja(nFib));
            
            int liczbaDoSumy = 1234;
            printf("%d\n", sumaCyfrRekurencja(liczbaDoSumy));
        }
    }
    
    return 0;
}

void wypiszMenu() {
    printf("1 - Operacje na czasie (Lab01)\n");
    printf("2 - Tablica ASCII (Lab03)\n");
    printf("3 - Warunek trojkata (Lab04)\n");
    printf("4 - Zgadywanka (Lab05)\n");
    printf("5 - Macierze, Wskazniki i Rekurencja (Lab08, 10, 13)\n");
    printf("6 - Wyjscie\n");
}

void przeliczCzas(int sekundyCalkowite) {
    int godziny = sekundyCalkowite / 3600;
    int reszta = sekundyCalkowite % 3600;
    int minuty = reszta / 60;
    int sekundy = reszta % 60;
    printf("%d %d %d\n", godziny, minuty, sekundy);
}

void operacjeNaZnakach(char znak) {
    printf("%c %d\n", znak, znak);
    char nowyZnak = znak + 32;
    printf("%c %d\n", nowyZnak, nowyZnak);
}

int czyTrojkat(float a, float b, float c) {
    if (a + b > c && a + c > b && b + c > a) {
        return 1;
    }
    return 0;
}

void graZgadywanka() {
    int wylosowana = rand() % 100 + 1;
    int strzal = 0;
    int proby = 0;

    while (strzal != wylosowana) {
        scanf("%d", &strzal);
        proby++;
        if (strzal < wylosowana) {
            printf("Za nisko\n");
        } else if (strzal > wylosowana) {
            printf("Za wysoko\n");
        }
    }
    printf("%d\n", proby);
}

void operacjeMacierzowe() {
    int macierz[3][3] = {
        {1, 2, 3},
        {2, 5, 6},
        {3, 6, 9}
    };
    int symetryczna = 1;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (macierz[i][j] != macierz[j][i]) {
                symetryczna = 0;
            }
        }
    }
    printf("%d\n", symetryczna);
}

void dynamicznaTablicaOdwrocona(int n) {
    int *tab = malloc(n * sizeof(int));
    if (tab != NULL) {
        for (int i = 0; i < n; i++) {
            tab[i] = i * 10;
        }
        for (int i = n - 1; i >= 0; i--) {
            printf("%d ", tab[i]);
        }
        printf("\n");
        free(tab);
    }
}

int fibonacciRekurencja(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacciRekurencja(n - 1) + fibonacciRekurencja(n - 2);
}

int sumaCyfrRekurencja(int n) {
    if (n == 0) return 0;
    return (n % 10) + sumaCyfrRekurencja(n / 10);
}