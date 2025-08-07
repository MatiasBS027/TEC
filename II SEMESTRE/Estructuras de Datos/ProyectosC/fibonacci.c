#include <stdio.h>

int main (){
    int a = 1;
    int b = 0;
    int numero;

    printf("Digite um numero: ");
    scanf("%d", &numero);
    
    for (int i = 0; i < numero; i++) {
        printf("%d ", a);
        int temp = a;
        a += b;
        b = temp;
    }

    return 0;
}