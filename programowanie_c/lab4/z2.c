#include <stdio.h>

int main() {
  int a=0;
  //printf("podaj liczbe \n");
  //scanf("%d",&a);
  if (a > 0)
  {
  printf("liczba jest dodatnia: %d", a);
  }
  else if (a < 0)
  {
  printf("jest ujemna: %d",a);
  }
  else if (a == 0)
  {
  printf("liczba jest zero");
  }
  
  return 0;
}