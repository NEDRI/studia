#include <stdio.h>

float tolerancja = 0.10;
float nominalna = 50.00;
int licznikP = 0;
int licznikN = 0; 

int main() {
    float pomiar[6] = {50.02, 49.95, 50.13, 49.88, 50.00, 50.08};
    
    printf("pierwszy pomiar to: %f\n", pomiar[0]);
    printf("drugi pomiar to: %f\n", pomiar[1]);
    printf("trzeci pomiar to: %f\n", pomiar[2]);
    printf("czwarty pomiar to: %f\n", pomiar[3]);
    printf("piaty pomiar to: %f\n", pomiar[4]);
    printf("szosty pomiar to: %f\n", pomiar[5]); 

    int wielkoscTablicy = sizeof(pomiar) / sizeof(pomiar[0]);
    
    float max = pomiar[0];
    float min = pomiar[0];
 
    
    for (int i = 0; i < wielkoscTablicy; i++) {
        printf("pomiar: %f ", pomiar[i]);
        float dzialanie = pomiar[i] - nominalna;
        printf("odchylenie: %f ", dzialanie);
        float odch = dzialanie;
        if ( dzialanie >= tolerancja || dzialanie <= -tolerancja) {
            licznikN++;
            odchyl=
            printf("Niepoprawna \n");
        } else {
            licznikP++;
            printf("Poprawna \n");
        }   
        
        if (pomiar[i] > max) {
            max = pomiar[i];
        }
         if (dzialanie[i] > max) {
            odch = dzialanie[i];
        }
        
        if (pomiar[i] < min) {
            min = pomiar[i];
        }
        
    }
    
    printf("Liczba poprawnych: %d\n", licznikP);
    printf("Liczba niepoprawnych: %d\n", licznikN);
    printf("Najwiekszy pomiar: %f\n", max);
    printf("Najmniejszy pomiar: %f\n", min);

    return 0;
}