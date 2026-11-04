#include <stdio.h>

void kaczka(int b){
    for (int i = 0; i <= b; i++)
    {
        printf("%d\n", i);
    }

}
int main(){
    int a;
    printf("Podaj do ilu liczb czy cos: ");
    scanf("%d",&a);
    kaczka(a);
    printf("przerwa\n");
    for (int i = 0; i <= a; i++)
    {
        printf("%d\n", i);
    }
}