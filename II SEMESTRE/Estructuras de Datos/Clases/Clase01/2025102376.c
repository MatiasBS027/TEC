#include <stdio.h>
#include <stdlib.h> // Para calloc y free

// Elaborado por: Matias Benavides
// Fecha: 21/08/2025
/*
 * ESTRUCTURA: struct nodo
 * DESCRIPCIÓN: Nodo de lista enlazada (valor + puntero al siguiente)
 */
struct nodo {
    int valor;
    struct nodo *siguiente;
};
/*
 * ESTRUCTURA: struct lista
 * DESCRIPCIÓN: Lista enlazada (puntero al primer nodo)
 */
struct lista {
    struct nodo *inicio;// Puntero al primer nodo de la lista
};
/*
 * FUNCIÓN: crear_nodo
 * DESCRIPCIÓN: Crea un nodo con valor y puntero NULL
 * FLUJO: Reserva memoria → asigna valor → retorna puntero
 */
struct nodo* crear_nodo(int valor) {
    struct nodo *nuevo_nodo = calloc(1, sizeof(struct nodo));// Reservar memoria para el nuevo nodo
    if (!nuevo_nodo) {
        fprintf(stderr, "Error al reservar memoria.\n");
        exit(EXIT_FAILURE);
    }
    nuevo_nodo->valor = valor; // Asignar el valor al nuevo nodo
    return nuevo_nodo;
}
/*
 * FUNCIÓN: crear_lista
 * DESCRIPCIÓN: Crea una lista vacía (inicio = NULL)
 * FLUJO: Reserva memoria → retorna puntero
 */
struct lista* crear_lista() {
    struct lista *nueva_lista = calloc(1, sizeof(struct lista));// Reservar memoria para la nueva lista
    if (!nueva_lista) {
        fprintf(stderr, "Error al reservar memoria.\n");
        exit(EXIT_FAILURE);
    }
    return nueva_lista;
}
/*
 * FUNCIÓN: imprimir_lista
 * DESCRIPCIÓN: Imprime todos los valores de la lista
 * FLUJO: Recorre desde inicio hasta NULL → imprime valores
 */
int imprimir_lista(struct lista *lista) {// Imprimir los elementos de la lista
    if (!lista || !lista->inicio) {
        printf("La lista está vacía.\n");
        return 0;
    }

    struct nodo *actual = lista->inicio;// Comenzar desde el inicio de la lista
    printf("Elementos: ");
    while (actual) {
        printf("%d ", actual->valor);
        actual = actual->siguiente;// Avanzar al siguiente nodo
    }
    printf("\n");
    return 0;
}
/*
 * FUNCIÓN: insertar_final
 * DESCRIPCIÓN: Inserta un nodo al final de la lista
 * FLUJO: Si vacía → nuevo inicio | si no → recorre hasta el último → enlaza
 */
int insertar_final(struct lista *lista, int valor) {
    if (!lista) return -1;

    struct nodo *nuevo_nodo = crear_nodo(valor);// Crear un nuevo nodo con el valor proporcionado
    if (!lista->inicio) {
        lista->inicio = nuevo_nodo;
        return 0;
    }

    struct nodo *actual = lista->inicio;// Comenzar desde el inicio de la lista
    while (actual->siguiente) actual = actual->siguiente;// Recorrer hasta el último nodo
    actual->siguiente = nuevo_nodo;// Enlazar el nuevo nodo al final de la lista
    return 0;
}
/*
 * FUNCIÓN: insertar_inicio
 * DESCRIPCIÓN: Inserta un nodo al inicio
 * FLUJO: Nuevo nodo → apunta a inicio → se vuelve inicio
 */
int insertar_inicio(struct lista *lista, int valor) {
    if (!lista) return -1;

    struct nodo *nuevo_nodo = crear_nodo(valor);// Crear un nuevo nodo con el valor proporcionado
    nuevo_nodo->siguiente = lista->inicio;// Apuntar el nuevo nodo al inicio actual
    lista->inicio = nuevo_nodo;// Actualizar el inicio de la lista al nuevo nodo
    return 0;
}
/*
 * FUNCIÓN: insertar_ordenado
 * DESCRIPCIÓN: Inserta un nodo manteniendo orden ascendente
 * FLUJO: Si vacío o menor que inicio → inserta inicio | si no → busca posición → inserta
 */
int insertar_ordenado(struct lista *lista, int valor) {
    if (!lista) return -1;

    struct nodo *nuevo_nodo = crear_nodo(valor);
    struct nodo *actual = lista->inicio;
    struct nodo *anterior = NULL;

    if (!actual || actual->valor >= valor) {
        nuevo_nodo->siguiente = actual;// Si la lista está vacía o el nuevo valor es menor que el inicio
        lista->inicio = nuevo_nodo;// Actualizar el inicio de la lista
        return 0;
    }

    while (actual && actual->valor < valor) {
        anterior = actual;
        actual = actual->siguiente;// Avanzar al siguiente nodo
    }
    nuevo_nodo->siguiente = actual;// Insertar el nuevo nodo en la posición correcta
    anterior->siguiente = nuevo_nodo;// Enlazar el nodo anterior al nuevo nodo
    return 0;
}
/*
 * FUNCIÓN: main
 * DESCRIPCIÓN: Demuestra uso de la lista enlazada
 */
int main() {
    struct lista *mi_lista = crear_lista(); // Crear una nueva lista enlazada

    // insertar_final(mi_lista, 10); // Insertar elementos en la lista
    // insertar_final(mi_lista, 20);
    // insertar_final(mi_lista, 30);

    // imprimir_lista(mi_lista); // Imprimir los elementos de la lista

    //  insertar_inicio(mi_lista, 5); // Insertar elemento al inicio
    //  insertar_inicio(mi_lista, 1); // Insertar otro elemento al inicio
    //  imprimir_lista(mi_lista); // Imprimir los elementos de la lista nuevamente

    //  insertar_ordenado(mi_lista, 15); // Insertar elemento en orden
    //  insertar_ordenado(mi_lista, 25); // Insertar otro elemento en orden
    //  imprimir_lista(mi_lista); // Imprimir los elementos de la lista nuevamente

    return 0;
}
