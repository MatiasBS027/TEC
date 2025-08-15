#include <stdio.h>
#include <stdlib.h> // Para calloc y free

//Elaborado por: Matias Benavides
//Fecha: 14/08/2025

//Esta funcion invertira un texto
void invertir_Texto(char *texto) {
    int longitud = 0;
    while (texto[longitud] != '\0') {
        longitud++;
    }   // Calcular la longitud del texto

    for (int i = 0; i < longitud / 2; i++) { // Intercambiar los caracteres
        char temp = texto[i];                // Almacenar el caracter temporalmente
        texto[i] = texto[longitud - i - 1]; // Intercambiar el caracter actual con su par en el otro extremo
        texto[longitud - i - 1] = temp;     // Asignar el caracter temporal al otro extremo
    }
}

void invertir_Entero(int *numero) {
    int invertido = 0;
    while (*numero > 0) { // Mientras el numero sea mayor que 0
        invertido = invertido * 10 + (*numero % 10); // Agregar el ultimo digito al numero invertido
        *numero /= 10; // Eliminar el ultimo digito
    }
    *numero = invertido; // Asignar el numero invertido al puntero
}

int main(){
    char *texto = calloc(100, sizeof(char)); // Reservar memoria
    if (texto == NULL) {
        printf("No se pudo asignar memoria.\n");
        return 1;
    }

    printf("Ingrese el texto a invertir: ");
    scanf("%s", texto); // Leer el texto ingresado por el usuario

    invertir_Texto(texto); // Llamar a la funcion para invertir el texto

    printf("Texto invertido: %s\n", texto); // Imprimir el texto invertido

    free(texto); // Liberar la memoria

    int numero;
    printf("Ingrese un numero entero a invertir: ");
    scanf("%d", &numero); // Leer el numero ingresado por el usuario
    invertir_Entero(&numero); // Llamar a la funcion para invertir el numero
    printf("Numero invertido: %d\n", numero); // Imprimir el numero invertido
    

    return 0; // Terminar el programa

}