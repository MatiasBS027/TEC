/*  
Proyecto2.c
Prueba de lectura de artículos
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

//######################################################
//          ESTRUCTURAS
//######################################################

struct Articulo {
    char nombre_autor[21];     // 20 + 1 para '\0'
    char apellido_autor[21];   // 20 + 1 para '\0'
    char titulo[51];           // 50 + 1 para '\0'
    char ruta[61];             // 60 + 1 para '\0'
    char anio[11];             // 10 + 1 para '\0'
    char abstract[101];        // 100 + 1 para '\0'
};

//######################################################
//          FUNCIONES AUXILIARES
//######################################################

/* 
Eliminar espacios en blanco al final de una cadena
E: cadena de texto
S: void (modifica la cadena directamente)
*/
void limpiar_espacios_final(char* cadena) {
    int longitud = strlen(cadena);
    
    // Retroceder desde el final eliminando espacios
    char* ptr = cadena;
    for (int i = 0; i < longitud; i++) {
        ptr++;
    }
    ptr--; // Volver al último carácter
    
    while (ptr >= cadena && (*ptr == ' ' || *ptr == '\n' || *ptr == '\r')) {
        *ptr = '\0';
        ptr--;
    }
}

//######################################################
//          FUNCIONES PARA LEER ARTÍCULOS
//######################################################

/* 
Leer una línea y crear un struct Articulo
E: línea de texto del archivo
S: puntero a struct Articulo con los datos
*/
struct Articulo* leer_articulo_desde_linea(char* linea) {
    if (!linea) return NULL;
    
    // Crear el artículo
    struct Articulo* nuevo = calloc(1, sizeof(struct Articulo));
    if (!nuevo) return NULL;
    
    // Extraer los 6 campos con strtok
    char* nombre = strtok(linea, "|");
    char* apellido = strtok(NULL, "|");
    char* titulo = strtok(NULL, "|");
    char* ruta = strtok(NULL, "|");
    char* anio = strtok(NULL, "|");
    char* abstract = strtok(NULL, "|");
    
    // Verificar que todos los campos existan
    if (!nombre || !apellido || !titulo || !ruta || !anio || !abstract) {
        free(nuevo);
        return NULL;
    }
    
    // Copiar a la estructura (strncpy para seguridad)
    strncpy(nuevo->nombre_autor, nombre, 20);
    nuevo->nombre_autor[20] = '\0';
    
    strncpy(nuevo->apellido_autor, apellido, 20);
    nuevo->apellido_autor[20] = '\0';
    
    strncpy(nuevo->titulo, titulo, 50);
    nuevo->titulo[50] = '\0';
    
    strncpy(nuevo->ruta, ruta, 60);
    nuevo->ruta[60] = '\0';
    
    strncpy(nuevo->anio, anio, 10);
    nuevo->anio[10] = '\0';
    
    strncpy(nuevo->abstract, abstract, 100);
    nuevo->abstract[100] = '\0';
    
    // Limpiar espacios al final de cada campo
    limpiar_espacios_final(nuevo->nombre_autor);
    limpiar_espacios_final(nuevo->apellido_autor);
    limpiar_espacios_final(nuevo->titulo);
    limpiar_espacios_final(nuevo->ruta);
    limpiar_espacios_final(nuevo->anio);
    limpiar_espacios_final(nuevo->abstract);
    
    return nuevo;
}

/* 
Leer todos los artículos del archivo
E: nombre del archivo (ruta), puntero para guardar cantidad
S: array de punteros a struct Articulo
*/
struct Articulo** leer_articulos_desde_archivo(const char* nombre_archivo, int* cantidad) {
    FILE* archivo = fopen(nombre_archivo, "r");
    if (!archivo) {
        printf("Error al abrir el archivo: %s\n", nombre_archivo);
        return NULL;
    }
    
    // Contar cuántas líneas tiene el archivo (cuántos artículos)
    int total_articulos = 0;
    char linea_temp[500];
    while (fgets(linea_temp, sizeof(linea_temp), archivo)) {
        total_articulos++;
    }
    
    // Volver al inicio del archivo
    rewind(archivo);
    
    // Crear array de punteros (uno extra para NULL al final)
    struct Articulo** articulos = calloc(total_articulos + 1, sizeof(struct Articulo*));
    if (!articulos) {
        fclose(archivo);
        return NULL;
    }
    
    // Leer cada línea y crear artículos
    int indice = 0;
    char linea[500];
    while (fgets(linea, sizeof(linea), archivo) && indice < total_articulos) {
        struct Articulo* art = leer_articulo_desde_linea(linea);
        if (art) {
            struct Articulo** ptr = articulos;
            for (int i = 0; i < indice; i++) {
                ptr++;
            }
            *ptr = art;
            indice++;
        }
    }
    
    // Guardar la cantidad de artículos leídos
    *cantidad = indice;
    
    fclose(archivo);
    return articulos;
}

/* 
Liberar memoria de array de artículos
E: array de artículos, cantidad
S: void
*/
void liberar_articulos(struct Articulo** articulos, int cantidad) {
    if (!articulos) return;
    
    struct Articulo** ptr = articulos;
    for (int i = 0; i < cantidad; i++) {
        if (*ptr) {
            free(*ptr);
        }
        ptr++;
    }
    
    free(articulos);
}

//######################################################
//          MAIN DE PRUEBA - LECTURA DE ARTÍCULOS
//######################################################

int main() {
    printf("=== PRUEBA DE LECTURA DE ARTICULOS ===\n\n");
    
    int cantidad = 0;
    struct Articulo** articulos = leer_articulos_desde_archivo("repo/Articulos.txt", &cantidad);
    
    if (!articulos) {
        printf("Error al leer el archivo\n");
        return 1;
    }
    
    printf("Articulos leidos: %d\n\n", cantidad);
    
    // Mostrar cada artículo
    struct Articulo** ptr = articulos;
    for (int i = 0; i < cantidad; i++) {
        printf("=== Articulo %d ===\n", i + 1);
        printf("Autor: %s %s\n", (*ptr)->nombre_autor, (*ptr)->apellido_autor);
        printf("Titulo: %s\n", (*ptr)->titulo);
        printf("Ruta: %s\n", (*ptr)->ruta);
        printf("Anio: %s\n", (*ptr)->anio);
        printf("Abstract: %s\n", (*ptr)->abstract);
        printf("\n");
        ptr++;
    }
    
    // Liberar memoria
    liberar_articulos(articulos, cantidad);
    printf("Memoria liberada. Programa terminado.\n");
    
    return 0;
}