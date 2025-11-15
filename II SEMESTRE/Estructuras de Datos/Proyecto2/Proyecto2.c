/*  
Proyecto2.c
Sistema de ordenamiento de artículos científicos
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

struct MonitculoArticulos {
    struct Articulo** elementos;  // Array de punteros a artículos
    int tamanio;
    int capacidad;
    int tipo_ordenamiento;  // 1 = por año, 2 = por tamaño título
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

/* 
Contar cantidad de palabras en una cadena
E: cadena de texto
S: cantidad de palabras
*/
int contar_palabras(const char* texto) {
    if (!texto) return 0;
    
    int palabras = 0;
    bool en_palabra = false;
    
    const char* ptr = texto;
    while (*ptr != '\0') {
        if (*ptr == ' ' || *ptr == '\t' || *ptr == '\n') {
            en_palabra = false;
        } else if (!en_palabra) {
            en_palabra = true;
            palabras++;
        }
        ptr++;
    }
    
    return palabras;
}

/* 
Comparar dos artículos según el tipo de ordenamiento
E: artículo1, artículo2, tipo (1=año, 2=tamaño título)
S: true si art1 < art2 (para min-heap)
*/
bool comparar_articulos(struct Articulo* art1, struct Articulo* art2, int tipo) {
    if (!art1 || !art2) return false;
    
    if (tipo == 1) {
        // Ordenar por año (convertir string a int)
        int anio1 = atoi(art1->anio);
        int anio2 = atoi(art2->anio);
        return anio1 < anio2;
    } else if (tipo == 2) {
        // Ordenar por tamaño del título
        int palabras1 = contar_palabras(art1->titulo);
        int palabras2 = contar_palabras(art2->titulo);
        return palabras1 < palabras2;
    }
    
    return false;
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
//          FUNCIONES DE HEAP - NAVEGACIÓN
//######################################################

// Obtener índice del padre: (indice - 1) / 2
int obtener_padre(int indice) {
    return (indice - 1) / 2;
}

// Obtener índice del hijo izquierdo: 2 * indice + 1
int obtener_hijo_izquierdo(int indice) {
    return 2 * indice + 1;
}

// Obtener índice del hijo derecho: 2 * indice + 2
int obtener_hijo_derecho(int indice) {
    return 2 * indice + 2;
}

//######################################################
//          HEAP PARA ARTÍCULOS
//######################################################

/* 
Crear un nuevo montículo para artículos
E: capacidad inicial, tipo de ordenamiento (1=año, 2=tamaño título)
S: puntero al montículo creado
*/
struct MonitculoArticulos* crear_monticulo_articulos(int capacidad, int tipo_ordenamiento) {
    struct MonitculoArticulos* nuevo = calloc(1, sizeof(struct MonitculoArticulos));
    if (!nuevo) return NULL;
    
    nuevo->elementos = calloc(capacidad, sizeof(struct Articulo*));
    if (!nuevo->elementos) {
        free(nuevo);
        return NULL;
    }
    
    nuevo->tamanio = 0;
    nuevo->capacidad = capacidad;
    nuevo->tipo_ordenamiento = tipo_ordenamiento;
    
    return nuevo;
}

/* 
Insertar un artículo en el montículo
E: puntero al montículo, puntero al artículo
S: true si se insertó correctamente, false si está lleno
*/
bool insertar_articulo(struct MonitculoArticulos* monticulo, struct Articulo* articulo) {
    if (!monticulo || !articulo) return false;
    
    // Verificar si hay espacio
    if (monticulo->tamanio >= monticulo->capacidad) {
        printf("Monticulo lleno\n");
        return false;
    }
    
    // Insertar al final del array
    int indice = monticulo->tamanio;
    struct Articulo** ptr_nuevo = monticulo->elementos;
    for (int i = 0; i < indice; i++) {
        ptr_nuevo++;
    }
    *ptr_nuevo = articulo;
    monticulo->tamanio++;
    
    // Bubble up: subir el elemento hasta su posición correcta
    while (indice > 0) {
        int indice_padre = obtener_padre(indice);
        
        // Obtener punteros a artículos
        struct Articulo** ptr_actual = monticulo->elementos;
        for (int i = 0; i < indice; i++) {
            ptr_actual++;
        }
        
        struct Articulo** ptr_padre = monticulo->elementos;
        for (int i = 0; i < indice_padre; i++) {
            ptr_padre++;
        }
        
        // Comparar según el tipo de ordenamiento
        if (!comparar_articulos(*ptr_actual, *ptr_padre, monticulo->tipo_ordenamiento)) {
            break; // Ya está en posición correcta
        }
        
        // Intercambiar
        struct Articulo* temp = *ptr_actual;
        *ptr_actual = *ptr_padre;
        *ptr_padre = temp;
        
        indice = indice_padre;
    }
    
    return true;
}

/* 
Extraer el mínimo del heap (artículo con menor valor según criterio)
E: puntero al montículo
S: puntero al artículo extraído
*/
struct Articulo* extraer_minimo(struct MonitculoArticulos* monticulo) {
    if (!monticulo || monticulo->tamanio == 0) return NULL;
    
    // Guardar el mínimo (raíz)
    struct Articulo* minimo = *monticulo->elementos;
    
    // Mover el último elemento a la raíz
    monticulo->tamanio--;
    
    if (monticulo->tamanio > 0) {
        struct Articulo** ptr_ultimo = monticulo->elementos;
        for (int i = 0; i < monticulo->tamanio; i++) {
            ptr_ultimo++;
        }
        *monticulo->elementos = *ptr_ultimo;
        
        // Bubble down: bajar el elemento desde la raíz
        int indice = 0;
        while (true) {
            int hijo_izq = obtener_hijo_izquierdo(indice);
            int hijo_der = obtener_hijo_derecho(indice);
            int menor = indice;
            
            // Encontrar el menor entre padre e hijos
            if (hijo_izq < monticulo->tamanio) {
                struct Articulo** ptr_menor = monticulo->elementos;
                for (int i = 0; i < menor; i++) ptr_menor++;
                
                struct Articulo** ptr_izq = monticulo->elementos;
                for (int i = 0; i < hijo_izq; i++) ptr_izq++;
                
                if (comparar_articulos(*ptr_izq, *ptr_menor, monticulo->tipo_ordenamiento)) {
                    menor = hijo_izq;
                }
            }
            
            if (hijo_der < monticulo->tamanio) {
                struct Articulo** ptr_menor = monticulo->elementos;
                for (int i = 0; i < menor; i++) ptr_menor++;
                
                struct Articulo** ptr_der = monticulo->elementos;
                for (int i = 0; i < hijo_der; i++) ptr_der++;
                
                if (comparar_articulos(*ptr_der, *ptr_menor, monticulo->tipo_ordenamiento)) {
                    menor = hijo_der;
                }
            }
            
            if (menor == indice) break; // Ya está en posición correcta
            
            // Intercambiar
            struct Articulo** ptr_indice = monticulo->elementos;
            for (int i = 0; i < indice; i++) ptr_indice++;
            
            struct Articulo** ptr_menor_final = monticulo->elementos;
            for (int i = 0; i < menor; i++) ptr_menor_final++;
            
            struct Articulo* temp = *ptr_indice;
            *ptr_indice = *ptr_menor_final;
            *ptr_menor_final = temp;
            
            indice = menor;
        }
    }
    
    return minimo;
}

/* 
Liberar memoria del montículo de artículos
E: puntero al montículo
S: void (libera la memoria, NO libera los artículos)
*/
void liberar_monticulo_articulos(struct MonitculoArticulos* monticulo) {
    if (!monticulo) return;
    
    if (monticulo->elementos) {
        free(monticulo->elementos);
    }
    
    free(monticulo);
}

//######################################################
//          SISTEMA DE MENÚS
//######################################################

/* 
Mostrar menú principal
E: void
S: void
*/
void mostrar_menu_principal() {
    printf("\n");
    printf("========================================\n");
    printf("  SISTEMA DE ORDENAMIENTO DE ARTICULOS\n");
    printf("========================================\n");
    printf("1. Ordenar por año de publicacion\n");
    printf("2. Ordenar por tamaño del titulo\n");
    printf("3. Salir\n");
    printf("========================================\n");
    printf("Seleccione una opcion: ");
}

/* 
Mostrar artículos ordenados
E: array de artículos ordenados, cantidad total, cantidad a mostrar
S: void
*/
void mostrar_articulos_ordenados(struct Articulo** articulos, int total, int cantidad_mostrar) {
    if (!articulos) return;
    
    if (cantidad_mostrar > total) {
        cantidad_mostrar = total;
    }
    
    printf("\n========================================\n");
    printf("  RESULTADOS (mostrando %d de %d)\n", cantidad_mostrar, total);
    printf("========================================\n\n");
    
    struct Articulo** ptr = articulos;
    for (int i = 0; i < cantidad_mostrar; i++) {
        printf("--- Articulo %d ---\n", i + 1);
        printf("Titulo: %s\n", (*ptr)->titulo);
        printf("Autor: %s %s\n", (*ptr)->nombre_autor, (*ptr)->apellido_autor);
        printf("Año: %s\n", (*ptr)->anio);
        printf("Abstract: %s\n", (*ptr)->abstract);
        printf("Ruta: %s\n", (*ptr)->ruta);
        printf("\n");
        ptr++;
    }
}

/* 
Ordenar artículos usando heap
E: array de artículos, cantidad, tipo de ordenamiento
S: void (modifica el array original con el orden)
*/
void ordenar_articulos_heap(struct Articulo** articulos, int cantidad, int tipo_ordenamiento) {
    if (!articulos || cantidad <= 0) return;
    
    // Crear heap
    struct MonitculoArticulos* heap = crear_monticulo_articulos(cantidad, tipo_ordenamiento);
    if (!heap) {
        printf("Error al crear heap\n");
        return;
    }
    
    // Insertar todos los artículos en el heap
    struct Articulo** ptr = articulos;
    for (int i = 0; i < cantidad; i++) {
        insertar_articulo(heap, *ptr);
        ptr++;
    }
    
    // Extraer todos en orden y guardarlos de vuelta en el array
    for (int i = 0; i < cantidad; i++) {
        struct Articulo** ptr_destino = articulos;
        for (int j = 0; j < i; j++) {
            ptr_destino++;
        }
        *ptr_destino = extraer_minimo(heap);
    }
    
    // Liberar heap
    liberar_monticulo_articulos(heap);
}

//######################################################
//          MAIN CON MENÚ
//######################################################

int main() {
    printf("=== SISTEMA DE GESTION DE ARTICULOS ===\n\n");
    
    // Leer artículos del archivo
    int cantidad = 0;
    struct Articulo** articulos = leer_articulos_desde_archivo("repo/Articulos.txt", &cantidad);
    
    if (!articulos) {
        printf("Error al leer el archivo\n");
        return 1;
    }
    
    printf("Articulos cargados: %d\n", cantidad);
    
    int opcion = 0;
    while (opcion != 3) {
        mostrar_menu_principal();
        scanf("%d", &opcion);
        
        if (opcion == 1 || opcion == 2) {
            printf("\nCuantos articulos desea mostrar? (1-%d): ", cantidad);
            int cantidad_mostrar;
            scanf("%d", &cantidad_mostrar);
            
            if (cantidad_mostrar < 1 || cantidad_mostrar > cantidad) {
                printf("Cantidad invalida\n");
                continue;
            }
            
            // Ordenar
            const char* tipo_texto = (opcion == 1) ? "año" : "tamaño del titulo";
            printf("\nOrdenando por %s...\n", tipo_texto);
            ordenar_articulos_heap(articulos, cantidad, opcion);
            
            // Mostrar resultados
            mostrar_articulos_ordenados(articulos, cantidad, cantidad_mostrar);
            
        } else if (opcion == 3) {
            printf("\nSaliendo del programa...\n");
        } else {
            printf("\nOpcion invalida\n");
        }
    }
    
    // Liberar memoria
    liberar_articulos(articulos, cantidad);
    printf("Memoria liberada. Programa terminado.\n");
    
    return 0;
}