// Elaborado por: Matias Benavides 
#include <stdio.h>

void desreferencia(int* puntero){
    printf("En la variable apuntada hay un valor de: %d\n", *puntero); // Imprime el valor al que apunta el puntero
    *puntero *=2; // Multiplica el valor apuntado por 2 
}

int main(){
    int total = 30; // Variable total inicializada a 10
    int* mi_puntero = &total; // Puntero que apunta a la variable total

    desreferencia(mi_puntero); // Llama a la función desreferencia con el puntero

    printf("Valor de total: %d\n", total); // Imprime el valor de total

    //printf("Lo que vale mi puntero: 0x%p\n", puntero); Imprime la dirección de memoria del puntero
    return 0; // Fin
}

