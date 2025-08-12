// Elaborado por: Matias Benavides 
#include <stdio.h>
#include<stdlib.h>

int main(){
    char str[] = "Hello, World!"; // Cadena de caracteres
    char *ptr = str; // Puntero a la cadena, esto apuntaria al primer caracter de la cadena
    printf("caracteres de la cadena: ");
    while (*ptr != '\0') { // Recorre la cadena hasta el caracter nulo
        printf("%c", * ptr); // Imprime el caracter apuntado por ptr
        ptr++; // Avanza al siguiente caracter
    }
    return 0; // Fin
}
