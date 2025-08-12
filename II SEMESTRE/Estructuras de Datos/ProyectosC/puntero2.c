// Elaborado por: Matias Benavides 
#include <stdio.h>
#include<stdlib.h>

void change_value(char* pointer){
    *pointer = 'B'; // Cambia el valor apuntado por el puntero a 'B'
}

int main(){
    char *l = malloc(sizeof(char)); // Reserva memoria para un carácter
    if (l == NULL) {
        fprintf(stderr, "Error al reservar memoria\n");
        return 1; // Manejo de error si malloc falla
    }
    *l = 'A'; // Asigna un valor al carácter apuntado por l
    change_value(l); // Llama a la función change_value con el puntero
    printf("Valor apuntado por l: %c\n", *l); // Imprime el valor apuntado por l
    free(l); // Libera la memoria reservada
    return 0; // Fin
}

