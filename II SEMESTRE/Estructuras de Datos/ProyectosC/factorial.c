#include <stdio.h>

int main (){
    int total = 1;
    int numero;

    printf("Digite um numero: ");
    scanf("%d", &numero);
    
    for (total; numero > 1; numero--) {
        total *= numero;
    }
    printf("Fatorial: %d\n", total);
    return 0;
}