#include <stdio.h>

int main() {
    int a = 4;
    printf("podaj liczbe\n");
    
    if (a % 2 == 0) {
        printf("jest parzyste");
    }
    else
    {
        printf("nie jest parzyste");
    }
    
    return 0;
}