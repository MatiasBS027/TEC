#include <stdio.h>
#include <stdlib.h> // Para calloc y free
#include <string.h> // Para strncmp

//Elaborado por: Matias Benavides
//Fecha: 14/08/2025

/**
 * FUNCION: invertir_Texto
 * DESCRIPCION: Invierte el orden de los caracteres en una cadena de texto
 * COMO SE MUEVEN LOS DATOS:
 * - Recibe un puntero char* que apunta al inicio del texto
 * - Calcula la longitud recorriendo hasta encontrar '\0'
 * - Intercambia caracteres simétricamente: el primero con el último, el segundo con el penúltimo, etc.
 * - Los cambios se hacen directamente en la memoria original (modifica el arreglo original)
 * EJEMPLO: "hola" → "aloh"
 */
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

/**
 * FUNCION: invertir_Entero
 * DESCRIPCION: Invierte los dígitos de un número entero
 * COMO SE MUEVEN LOS DATOS:
 * - Recibe un puntero int* que apunta a la variable del número
 * - Extrae dígitos de derecha a izquierda usando módulo 10
 * - Construye el número invertido multiplicando por 10 y sumando el dígito
 * - Almacena el resultado en la misma dirección de memoria (modifica el valor original)
 * EJEMPLO: 1234 → 4321
 */
void invertir_Entero(int *numero) {
    int invertido = 0;
    while (*numero > 0) { // Mientras el numero sea mayor que 0
        invertido = invertido * 10 + (*numero % 10); // Agregar el ultimo digito al numero invertido
        *numero /= 10; // Eliminar el ultimo digito
    }
    *numero = invertido; // Asignar el numero invertido al puntero
}

/**
 * FUNCION: eliminar_prefijo
 * DESCRIPCION: Elimina un prefijo específico del inicio de un texto si existe
 * COMO SE MUEVEN LOS DATOS:
 * - Recibe dos punteros: texto (se modifica) y prefijo (solo lectura)
 * - Compara los primeros caracteres del texto con el prefijo usando strncmp
 * - Si coincide, desplaza todos los caracteres hacia la izquierda
 * - El texto original se sobrescribe con el texto sin prefijo
 * EJEMPLO: texto="universidad", prefijo="uni" → "versidad"
 */
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

/**
 * FUNCION: encontrar_num_arreglo
 * DESCRIPCION: Busca un número específico en un arreglo de enteros
 * COMO SE MUEVEN LOS DATOS:
 * - Recibe: puntero al arreglo (solo lectura), tamaño del arreglo, número a buscar
 * - Recorre secuencialmente cada posición del arreglo
 * - Compara cada elemento con el número buscado
 * - Imprime el resultado por pantalla (no modifica el arreglo)
 * EJEMPLO: arreglo=[1,2,3,4,5], numero=3 → imprime "posicion 2"
 */
void encontrar_num_arreglo(int *arreglo,int tam,int numero) {
    printf("Buscando el numero %d en el arreglo:\n", numero);
    for (int i = 0; i < tam; i++) {
        if (arreglo[i] == numero) {
            printf("El numero %d se encuentra en la posicion %d del arreglo.\n", numero, i);
            return;
        }
    }
    printf("El numero %d no se encuentra en el arreglo.\n", numero);
}

/**
 * FUNCION: main
 * DESCRIPCION: Función principal que coordina la ejecución del programa
 * COMO SE MUEVEN LOS DATOS:
 * - Solicita entrada del usuario para diferentes operaciones
 * - Crea variables dinámicas usando calloc (memoria heap)
 * - Llama a las funciones auxiliares pasando punteros
 * - Libera memoria al final usando free
 * FLUJO: Entrada → Procesamiento → Salida → Liberación de memoria
 */
int main(){
    char *texto = calloc(100, sizeof(char)); // Reservar memoria dinámica para texto (heap)
    if (texto == NULL) {
        printf("No se pudo asignar memoria.\n");
        return 1;
    }

    printf("Ingrese el texto a invertir: ");
    scanf("%s", texto); // Leer el texto ingresado por el usuario

    invertir_Texto(texto); // Llamar a la funcion para invertir el texto (modifica texto in-place)

    printf("Texto invertido: %s\n", texto); // Imprimir el texto invertido

    free(texto); // Liberar la memoria dinámica del heap

    int numero;
    printf("Ingrese un numero entero a invertir: ");
    scanf("%d", &numero); // Leer el numero ingresado por el usuario (stack)
    invertir_Entero(&numero); // Pasar la dirección de memoria de la variable
    printf("Numero invertido: %d\n", numero); // Imprimir el numero invertido
    
    char *texto_prefijo = calloc(100, sizeof(char)); // Reservar memoria para el texto con prefijo
    if (texto_prefijo == NULL) {
        printf("No se pudo asignar memoria.\n");
        return 1;
    }
    char *prefijo = calloc(100, sizeof(char)); // Reservar memoria para el prefijo
    if (prefijo == NULL) {
        printf("No se pudo asignar memoria.\n");
        free(texto_prefijo);
        return 1;
    }
    printf("Ingrese el texto con prefijo: ");
    scanf("%s", texto_prefijo);
    printf("Ingrese el prefijo a eliminar: ");
    scanf("%s", prefijo);
    eliminar_prefijo(texto_prefijo, prefijo); // Modifica texto_prefijo in-place
    printf("Texto sin prefijo: %s\n", texto_prefijo);
    free(texto_prefijo);
    free(prefijo);
  
    int arreglo[] = {1, 2, 3, 4, 5}; // Arreglo estático en stack
    int tam = sizeof(arreglo) / sizeof(arreglo[0]); // Cálculo del tamaño
    int numero_buscar;
    printf("Ingrese un numero a buscar en el arreglo: ");
    scanf("%d", &numero_buscar);
    encontrar_num_arreglo(arreglo, tam ,numero_buscar); // Solo lectura del arreglo
    
    return 0;
}
