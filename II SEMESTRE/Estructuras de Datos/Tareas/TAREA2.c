#include <stdio.h>
#include <stdlib.h> // Para calloc y free
#include <string.h> // Para strncmp

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

void eliminar_prefijo(char *texto, const char *prefijo) {
    int prefijo_len = 0;
    while (prefijo[prefijo_len] != '\0') {
        prefijo_len++;
    } // Calcular la longitud del prefijo

    int texto_len = 0;
    while (texto[texto_len] != '\0') {
        texto_len++;
    } // Calcular la longitud del texto

    if (texto_len >= prefijo_len && strncmp(texto, prefijo, prefijo_len) == 0) {
        // Si el texto comienza con el prefijo, desplazar el texto hacia la izquierda
        for (int i = 0; i <= texto_len - prefijo_len; i++) {
            texto[i] = texto[i + prefijo_len];
        }
    }
}

void encontrar_num_arreglo(int *arreglo,int tam,int numero) {

    printf("Buscando el numero %d en el arreglo:\n", numero);
    for (int i = 0; i < tam; i++) {
        printf("%d",arreglo[i]); // Imprimir el elemento actual del arreglo
        if (arreglo[i] == numero) {
            printf("El numero %d se encuentra en la posicion %d del arreglo.\n", numero, i);
            return;
        }
    }
    printf("El numero %d no se encuentra en el arreglo.\n", numero);
}

int main(){
    char *texto = calloc(100, sizeof(char)); // Reservar memoria
    if (texto == NULL) {
        printf("No se pudo asignar memoria.\n");
        return 1;
    }

    printf("Ingrese el texto a invertir: ");
    scanf("%s", texto); // Leer el texto ingresado por el usuario

    //invertir_Texto(texto); // Llamar a la funcion para invertir el texto

    printf("Texto invertido: %s\n", texto); // Imprimir el texto invertido

    free(texto); // Liberar la memoria

    int numero;
    printf("Ingrese un numero entero a invertir: ");
    scanf("%d", &numero); // Leer el numero ingresado por el usuario
    //invertir_Entero(&numero); // Llamar a la funcion para invertir el numero
    printf("Numero invertido: %d\n", numero); // Imprimir el numero invertido
    
    char *texto_prefijo = calloc(100, sizeof(char)); // Reservar memoria para el texto con prefijo
    if (texto_prefijo == NULL) {
        printf("No se pudo asignar memoria.\n");
        return 1;
    }
    char *prefijo = calloc(100, sizeof(char)); // Reservar memoria para el prefijo
    if (prefijo == NULL) {
        printf("No se pudo asignar memoria.\n");
        free(texto_prefijo); // Liberar la memoria previamente asignada
        return 1;
    }
    printf("Ingrese el texto con prefijo: ");
    scanf("%s", texto_prefijo); // Leer el texto con prefijo ingresado por
    printf("Ingrese el prefijo a eliminar: ");
    scanf("%s", prefijo); // Leer el prefijo ingresado por el usuario   
    //eliminar_prefijo(texto_prefijo, prefijo); // Llamar a la funcion para eliminar el prefijo
    printf("Texto sin prefijo: %s\n", texto_prefijo); // Imprimir el texto sin prefijo
    free(texto_prefijo); // Liberar la memoria
    free(prefijo); // Liberar la memoria

    int arreglo[] = {1, 2, 3, 4, 5}; // Definir un arreglo de enteros
    int tam = sizeof(arreglo) / sizeof(arreglo[0]); // Calcular el tamaño del arreglo
    int numero_buscar;
    printf("Ingrese un numero a buscar en el arreglo: ");
    scanf("%d", &numero_buscar); // Leer el numero ingresado por el usuario
    encontrar_num_arreglo(arreglo, tam ,numero_buscar); // Llamar a la funcion
    
    return 0; // Terminar el programa

}