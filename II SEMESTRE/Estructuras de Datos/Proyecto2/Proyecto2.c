/*  
Proyecto2.c
Prueba de arbol de monticulo
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//######################################################
//          ESTRUCTURA
//######################################################
struct Monticulo {
    int* elementos;      // array dinámico
    int tamanio;        // elementos actuales
    int capacidad;      // capacidad máxima
};

//######################################################
//          FUNCIONES DE MONTÍCULO
//######################################################

/* 
Crear un nuevo montículo vacío
E: capacidad inicial
S: puntero al montículo creado
*/ 
struct Monticulo* crear_monticulo(int capacidad) {
    struct Monticulo* nuevo = calloc(1, sizeof(struct Monticulo));
    if (!nuevo) {
        return NULL;
    }
    
    nuevo->elementos = calloc(capacidad, sizeof(int));
    if (!nuevo->elementos) {
        free(nuevo);
        return NULL;
    }
    
    nuevo->tamanio = 0;
    nuevo->capacidad = capacidad;
    
    return nuevo;
}

//----------------------------------------------------------------
// FUNCIONES AUXILIARES PARA NAVEGAR
//----------------------------------------------------------------

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


/* 
Intercambiar dos elementos en el array
Entradas: array de elementos, índice1, índice2
Salidas: void (modifica el array directamente)
*/
void intercambiar(int* elementos, int indice1, int indice2) {
    // Mover puntero a la posición del primer elemento
    int* ptr1 = elementos;
    for (int i = 0; i < indice1; i++) {
        ptr1++;
    }
    
    // Mover puntero a la posición del segundo elemento
    int* ptr2 = elementos;
    for (int i = 0; i < indice2; i++) {
        ptr2++;
    }
    
    // Intercambiar valores
    int temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
}

//----------------------------------------------------------------
// INSERTAR ELEMENTO
//----------------------------------------------------------------

/* 
Insertar un nuevo elemento en el montículo
E: puntero al montículo, valor a insertar
S: true si se insertó correctamente, false si está lleno
*/
bool insertar(struct Monticulo* monticulo, int valor) {
    if (!monticulo) return false;
    
    // Verificar si hay espacio
    if (monticulo->tamanio >= monticulo->capacidad) {
        printf("Montículo lleno\n");
        return false;
    }
    
    // Insertar al final del array
    int indice = monticulo->tamanio;
    int* ptr_nuevo = monticulo->elementos;
    for (int i = 0; i < indice; i++) {
        ptr_nuevo++;
    }
    *ptr_nuevo = valor;
    monticulo->tamanio++;
    
    // Bubble up: subir el elemento hasta su posición correcta
    while (indice > 0) {
        int indice_padre = obtener_padre(indice);
        
        // Obtener valores del elemento actual y su padre
        int* ptr_actual = monticulo->elementos;
        for (int i = 0; i < indice; i++) {
            ptr_actual++;
        }
        
        int* ptr_padre = monticulo->elementos;
        for (int i = 0; i < indice_padre; i++) {
            ptr_padre++;
        }
        
        // Si el padre es menor o igual, ya está en posición correcta
        if (*ptr_padre <= *ptr_actual) {
            break;
        }
        
        // Si el padre es mayor, intercambiar
        intercambiar(monticulo->elementos, indice, indice_padre);
        indice = indice_padre;
    }
    
    return true;
}

//----------------------------------------------------------------
// IMPRIMIR MONTÍCULO
//----------------------------------------------------------------

/* 
Imprimir el montículo por niveles
E: puntero al montículo
S: void (imprime en consola)
*/
void imprimir_por_niveles(struct Monticulo* monticulo) {
    if (!monticulo || monticulo->tamanio == 0) {
        printf("Montículo vacío\n");
        return;
    }
    
    printf("\n=== Montículo (Min-Heap) ===\n");
    printf("Tamaño: %d / %d\n\n", monticulo->tamanio, monticulo->capacidad);
    
    int nivel = 0;
    int elementos_en_nivel = 1; // Primer nivel tiene 1 elemento
    int indice = 0;
    
    while (indice < monticulo->tamanio) {
        printf("Nivel %d: ", nivel);
        
        // Imprimir elementos de este nivel
        int elementos_a_imprimir = elementos_en_nivel;
        for (int i = 0; i < elementos_a_imprimir && indice < monticulo->tamanio; i++) {
            // Mover puntero a la posición actual
            int* ptr_actual = monticulo->elementos;
            for (int j = 0; j < indice; j++) {
                ptr_actual++;
            }
            
            printf("%d ", *ptr_actual);
            indice++;
        }
        
        printf("\n");
        nivel++;
        elementos_en_nivel = elementos_en_nivel * 2; // Cada nivel tiene el doble de elementos
    }
    
    printf("\n");
}

/* 
Liberar memoria del montículo
E: puntero al montículo
S: void (libera la memoria)
*/
void liberar_monticulo(struct Monticulo* monticulo) {
    if (!monticulo) {
        return;
    }
    
    if (monticulo->elementos) {
        free(monticulo->elementos);
    }
    
    free(monticulo);
}

//######################################################
//          MAIN DE PRUEBA
//######################################################

int main() {
    
    printf("=== PRUEBA DE MONTÍCULO MIN-HEAP ===\n\n");
    
    // Crear montículo con capacidad de 20
    struct Monticulo* heap = crear_monticulo(20);
    if (!heap) {
        printf("Error al crear montículo\n");
        return 1;
    }
    
    printf("Montículo creado con capacidad de 20 elementos\n\n");
    
    // Insertar algunos valores de prueba
    printf("Insertando valores: 15, 10, 20, 8, 25, 5, 30, 12, 18, 7\n");
    insertar(heap, 15);
    insertar(heap, 10);
    insertar(heap, 20);
    insertar(heap, 8);
    insertar(heap, 25);
    insertar(heap, 5);
    insertar(heap, 30);
    insertar(heap, 12);
    insertar(heap, 18);
    insertar(heap, 7);
    
    // Mostrar el heap por niveles
    imprimir_por_niveles(heap);
    
    printf("Insertando más valores: 3, 50, 1, 40\n");
    insertar(heap, 3);
    insertar(heap, 50);
    insertar(heap, 1);
    insertar(heap, 40);
    
    // Mostrar el heap actualizado
    imprimir_por_niveles(heap);
    
    // Liberar memoria
    liberar_monticulo(heap);
    printf("Memoria liberada. Programa terminado.\n");
    
    return 0;
}