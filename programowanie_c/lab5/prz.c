#include <stdio.h>

void wypisz(int n) // n = 3 -> n = 2 -> n = 1 -> n = 0
{
    if(n <= 0) // n = 3 (Nie) -> n = 2 (Nie) -> n = 1 (Nie) -> n = 0 (Tak)
    {
        return; // powrót z n = 0 do n = 1
    }

    wypisz(n - 1); // wywołanie z n = 2 -> wywołanie z n = 1 -> wywołanie z n = 0
    printf("%d\n", n); // po powrocie: wypisze 1 -> wypisze 2 -> wypisze 3
}

int main()
{
    int n;

    printf("Podaj n: ");
    scanf("%d", &n);

    wypisz(n);

    return 0;
}

/*
wypisz(3)
  |
  |---> wypisz(2)
          |
          |---> wypisz(1)
                  |
                  |---> wypisz(0)  ==> STOP
                  |
                  |---> printf(1)  ==> WYPISUJE: 1
          |
          |---> printf(2)  ==> WYPISUJE: 2
  |
  |---> printf(3)  ==> WYPISUJE: 3
*/