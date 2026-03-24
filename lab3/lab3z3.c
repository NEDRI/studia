#include <stdio.h>

int main() {

    float R1,R2;
    printf("Podaj R1 i R2\n");
    scanf("%f %f",&R1,&R2);
    float R=(R1*R2)/(R1+R2);
    printf("Wynik: %f",R);

    return 0;
}