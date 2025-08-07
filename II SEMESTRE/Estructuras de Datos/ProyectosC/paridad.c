#include <stdio.h>

int main (){
    int numero;
    printf("Digite um numero: ");
    scanf("%d", &numero);
    if (numero % 2 == 0) {
        printf("El numero %d es par.\n", numero);
    } else {
        printf("El numero %d es impar.\n", numero);
    }
    return 0;
}