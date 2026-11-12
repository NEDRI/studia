#include <stdio.h>
#include <stdlib.h>

void analizuj(double tab[], int n, double *min, double *max, double *srednia, double *rozrzut)
{
    double suma = 0.0;

    *min = tab[0];
    *max = tab[0];

    for (int i = 0; i < n; i++)
    {
        if (tab[i] < *min)
        {
            *min = tab[i];
        }
        if (tab[i] > *max)
        {
            *max = tab[i];
        }
        suma = suma + tab[i];
    }

    *srednia = suma / n;
    *rozrzut = *max - *min;
}

int licz_powyzej(double tab[], int n, double graniczna)
{
    int licznik = 0;

    for (int i = 0; i < n; i++)
    {
        if (tab[i] > graniczna)
        {
            licznik = licznik + 1;
        }
    }

    return licznik;
}

int rekurencja_suma(double tab[], int n){
    float sum;
    for (int i = 0; i < tab[i]; i++)
    {
        sum = sum + tab[i];
    }
    return sum;
}

int main()
{
    int n;
    double *pomiary;
    double min, max, srednia, rozrzut;
    double graniczna;
    int powyzej;

    printf("Podaj liczbe pomiarow: ");
    scanf("%d", &n);

    pomiary = (double *)malloc(n * sizeof(double));
    if (pomiary == NULL)
    {
        printf("Cos blad z alokacja\n");
        return 1;
    }

    printf("Podaj %d wartosci napiecia (w woltach):\n", n);
    for (int i = 0; i < n; i++)
    {
        printf("Pomiar %d: ", i + 1);
        scanf("%lf", &pomiary[i]);
    }

    analizuj(pomiary, n, &min, &max, &srednia, &rozrzut);

    printf("\nWyniki analizy:\n");
    printf("Wartosc minimalna: %.2f V\n", min);
    printf("Wartosc maksymalna: %.2f V\n", max);
    printf("Wartosc srednia: %.2f V\n", srednia);
    printf("Rozrzut: %.2f V\n", rozrzut);

    printf("\nPodaj wartosc graniczna napiecia: ");
    scanf("%lf", &graniczna);

    powyzej = licz_powyzej(pomiary, n, graniczna);
    printf("Liczba pomiarow powyzej %.2f V: %d\n", graniczna, powyzej);

    float suma = rekurencja_suma(pomiary,n);
    printf("Suma: %.2f \n",suma);

    printf("\nOcena napiecia: ");
    if (srednia < 11.8)
    {
        printf("Zbyt niskie napiecie\n");
    }
    else if (srednia <= 12.2)
    {
        printf("Napiecie w zakresie roboczym\n");
    }
    else if (srednia <= 12.5)
    {
        printf("Podwyzszone napiecie\n");
    }
    else
    {
        printf("Zbyt wysokie napiecie\n");
    }

    free(pomiary);
    return 0;
}
