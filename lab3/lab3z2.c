#include <stdio.h>

int main() {

    float C;

    printf("Podaj temp C \n");
    scanf("%f",&C);
    float F=(9/5)*C+32;
    printf("%f",F);

    return 0;
}