#include <stdio.h>

int main (){
    int total = 0;
    int numero;
    printf("Digite um numero: ");
    scanf("%d", &numero);

    for (; numero > 0; total++) {
        numero = numero /10;
    }
    printf("%d\n", total);

    return 0;
}