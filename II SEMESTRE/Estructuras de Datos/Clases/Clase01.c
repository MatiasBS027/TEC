#include <stdio.h>
#include <stdlib.h> // Para calloc y free
#include <string.h> // Para strncmp

//Elaborado por: Matias Benavides
//Fecha: 21/08/2025

// Este struct representa un nodo de una lista enlazada
// Contiene un valor entero y un puntero al siguiente nodo
struct nodo {
    int valor;
    struct nodo *siguiente;
};

struct lista{
    struct nodo *inicio; // Puntero al primer nodo de la lista
};
struct nodo*crear_nodo(int valor) {
    struct nodo *nuevo_nodo = calloc(1,sizeof(struct nodo)); // Reservar memoria para el nuevo nodo
    if (nuevo_nodo == NULL) {
        fprintf(stderr, "Error al reservar memoria para el nodo.\n");
        exit(EXIT_FAILURE);
    }
    nuevo_nodo->valor = valor; // Asignar el valor al nodo
    //nuevo_nodo->siguiente = NULL; // Inicializar el puntero siguiente como NULL
    return nuevo_nodo;
}

struct lista*crear_lista() {
    struct lista *nueva_lista = calloc(1, sizeof(struct lista)); // Reservar memoria para la lista
    if (nueva_lista == NULL) {
        fprintf(stderr, "Error al reservar memoria para la lista.\n");
        exit(EXIT_FAILURE);
    }
    //nueva_lista->inicio = NULL; // Inicializar el inicio de la lista como NULL
    return nueva_lista;
}

int imprimir_lista(struct lista *lista) {
    if (lista == NULL || lista->inicio == NULL) {
        printf("La lista esta vacia.\n");
        return 0; // Retornar 0 si la lista esta vacia
    }
    
    struct nodo *actual = NULL;
    actual = lista->inicio; // Comenzar desde el inicio de la lista
    printf("Elementos de la lista: ");
    while (actual != NULL) { // Recorrer la lista hasta que no haya mas nodos
        printf("%d ", actual->valor);
        actual = actual->siguiente; // Avanzar al siguiente nodo
    }
    printf("\n");
    return 0; // Retornar 0 si se imprimieron elementos
}

int insertar_final(struct lista *lista, int valor) {
    if (lista == NULL) {
        fprintf(stderr, "La lista no ha sido creada.\n");
        return -1; // Retornar -1 si la lista no existe
    }
    
    struct nodo *nuevo_nodo = crear_nodo(valor); // Crear un nuevo nodo con el valor dado
    struct nodo *actual = NULL;
    if (lista->inicio == NULL) {
        lista->inicio = nuevo_nodo; // Si la lista esta vacia, el nuevo nodo es el inicio
        return 0; // Retornar 0 si se inserto correctamente
    }        
        actual = lista->inicio; // Comenzar desde el inicio de la lista
        while (actual->siguiente != NULL) { // Recorrer hasta el ultimo nodo
            actual = actual->siguiente;
        }
        actual->siguiente = nuevo_nodo; // Enlazar el ultimo nodo al nuevo nodo
    return 0; // Retornar 0 si se inserto correctamente
}


int main() {
    struct lista *mi_lista = crear_lista(); // Crear una nueva lista enlazada

    insertar_final(mi_lista, 10); // Insertar elementos en la lista
    insertar_final(mi_lista, 20);
    insertar_final(mi_lista, 30);

    imprimir_lista(mi_lista); // Imprimir los elementos de la lista

    // Liberar memoria (no implementado en este ejemplo)
    return 0;
}

