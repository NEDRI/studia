#include <stdio.h>

int main() {
    double dlugosc, szerokosc, wysokosc;
    double objetosc, pole_powierzchni;
    
    printf("Podaj wymiary (dlugosc, szerokosc, wysokosc) oddzielone spacja: ");
    
    if (scanf("%lf %lf %lf", &dlugosc, &szerokosc, &wysokosc) != 3) {
        printf("Zle dane\n");
    }

    objetosc = dlugosc * szerokosc * wysokosc;
    pole_powierzchni = 2 * (dlugosc * szerokosc + dlugosc * wysokosc + szerokosc * wysokosc);

    printf("Objetosc: %.2lf\n", objetosc);
    printf("Pole powierzchni: %.2lf\n", pole_powierzchni);

    return 0;
}