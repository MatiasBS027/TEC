#include <stdio.h>
#include <stdlib.h> // Para calloc y free

//Elaborado por: Matias Benavides
//Fecha: 21/08/2025

/*
 * ESTRUCTURA: struct nodo
 * DESCRIPCION: Representa un nodo individual en una lista enlazada
 * - Contiene un campo 'valor' para almacenar datos enteros
 * - Contiene un puntero 'siguiente' que apunta al siguiente nodo en la lista
 * - El puntero puede ser NULL si es el último nodo
 * EJEMPLO: [valor:10, siguiente]->[valor:20, siguiente]->NULL
 */
struct nodo {
    int valor;
    struct nodo *siguiente;
};

/*
 * ESTRUCTURA: struct lista
 * DESCRIPCION: Representa una lista enlazada completa
 * - Contiene un puntero 'inicio' que apunta al primer nodo de la lista
 * - Si la lista está vacía, 'inicio' es NULL
 * - Todos los nodos se acceden siguiendo los punteros desde 'inicio'
 */
struct lista{
    struct nodo *inicio; // Puntero al primer nodo de la lista
};

/*
 * FUNCION: crear_nodo
 * DESCRIPCION: Crea un nuevo nodo con un valor específico
 * - Reserva memoria dinámica en el heap para un struct nodo usando calloc
 * - Inicializa el campo 'valor' con el parámetro recibido
 * - Inicializa 'siguiente' como NULL (calloc lo pone en 0 automáticamente)
 * - Retorna un puntero al nuevo nodo creado
 * EJEMPLO: crear_nodo(42) → retorna puntero a [valor:42, siguiente:NULL]
 */
struct nodo*crear_nodo(int valor) {
    struct nodo *nuevo_nodo = calloc(1,sizeof(struct nodo)); // Reservar memoria para el nuevo nodo
    if (nuevo_nodo == NULL) {
        fprintf(stderr, "Error al reservar memoria para el nodo.\n");
        exit(EXIT_FAILURE);
    }
    nuevo_nodo->valor = valor; // Asignar el valor al nodo
    return nuevo_nodo;
}

/*
 * FUNCION: crear_lista
 * DESCRIPCION: Crea una nueva lista enlazada vacía
 * - Reserva memoria dinámica en el heap para un struct lista usando calloc
 * - Inicializa el puntero 'inicio' como NULL (lista vacía)
 * - Retorna un puntero a la nueva lista creada
 * EJEMPLO: crear_lista() → retorna puntero a [inicio:NULL]
 */
struct lista*crear_lista() {
    struct lista *nueva_lista = calloc(1, sizeof(struct lista)); // Reservar memoria para la lista
    if (nueva_lista == NULL) {
        fprintf(stderr, "Error al reservar memoria para la lista.\n");
        exit(EXIT_FAILURE);
    }
    return nueva_lista;
}

/*
 * FUNCION: imprimir_lista
 * DESCRIPCION: Imprime todos los elementos de la lista en orden
 * - Recibe un puntero a la lista (solo lectura)
 * - Comienza desde el nodo 'inicio' y sigue los punteros 'siguiente'
 * - Recorre secuencialmente cada nodo hasta encontrar NULL
 * - Imprime cada valor por pantalla sin modificar la lista
 * FLUJO: inicio → siguiente → siguiente → ... → NULL
 */
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

/*
 * FUNCION: insertar_final
 * DESCRIPCION: Inserta un nuevo nodo al final de la lista 
 * - Recibe la lista y el valor a insertar
 * - Crea un nuevo nodo usando crear_nodo()
 * - Si la lista está vacía (inicio == NULL), el nuevo nodo se convierte en el primero
 * - Si no está vacía, recorre todos los nodos hasta encontrar el último (donde siguiente == NULL)
 * - Enlaza el último nodo con el nuevo nodo
 * - La lista crece dinámicamente en el heap
 * FLUJO: Buscar último nodo → enlazar → nuevo nodo se convierte en último
 */
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

/*
 * FUNCION: insertar_inicio
 * DESCRIPCION: Inserta un nuevo nodo al inicio de la lista 
 * - Recibe la lista y el valor a insertar
 * - Crea un nuevo nodo usando crear_nodo()
 * - Si la lista está vacía (inicio == NULL), el nuevo nodo se convierte en el primero
 * - Si no está vacía, el nuevo nodo apunta al nodo actual de inicio
 * - El nuevo nodo se convierte en el nuevo inicio de la lista
 * FLUJO: Nuevo nodo → apunta al inicio actual → nuevo nodo se convierte en inicio
 */
int insertar_inicio(struct lista *lista, int valor) {
    if (lista == NULL) {
        fprintf(stderr, "La lista no ha sido creada.\n");
        return -1; // Retornar -1 si la lista no existe
    }
    
    struct nodo *nuevo_nodo = crear_nodo(valor); // Crear un nuevo nodo con el valor dado
    if (lista->inicio == NULL) {
        lista->inicio = nuevo_nodo; // Si la lista esta vacia, el nuevo nodo es el inicio
        return 0; // Retornar 0 si se inserto correctamente
    }        
        nuevo_nodo->siguiente = lista->inicio; // El nuevo nodo apunta al inicio actual
        lista->inicio = nuevo_nodo; // El nuevo nodo se convierte en el nuevo inicio
    return 0; // Retornar 0 si se inserto correctamente
}

/*
 * FUNCION: insertar_ordenado
 * DESCRIPCION: Inserta un nuevo nodo de manera ordenada en la lista
 * - Recibe la lista y el valor a insertar
 * - Crea un nuevo nodo usando crear_nodo()
 * - Si la lista está vacía (inicio == NULL) o el valor es menor que el primer nodo, inserta al inicio
 * - Si no, recorre la lista buscando la posición correcta para mantener el orden
 * - Enlaza el nuevo nodo entre el nodo anterior y el actual
 * FLUJO: Buscar posición → enlazar → nuevo nodo se inserta en orden
 */
int insertar_ordenado(struct lista *lista, int valor) {
    if (lista == NULL) {
        fprintf(stderr, "La lista no ha sido creada.\n");
        return -1; // Retornar -1 si la lista no existe
    }
    
    struct nodo *nuevo_nodo = crear_nodo(valor); // Crear un nuevo nodo con el valor dado
    struct nodo *actual = NULL; // Puntero para recorrer la lista
    struct nodo *anterior = NULL; // Puntero para mantener el nodo anterior

    if (lista->inicio == NULL || lista->inicio->valor >= valor) {// Insertar al inicio si la lista esta vacia o el valor es menor o igual al primer nodo
        nuevo_nodo->siguiente = lista->inicio; // El nuevo nodo apunta al inicio actual
        lista->inicio = nuevo_nodo; // El nuevo nodo se convierte en el nuevo inicio
        return 0; // Retornar 0 si se inserto correctamente
    }

    actual = lista->inicio; // Comenzar desde el inicio de la lista
    while (actual != NULL && actual->valor < valor) { // Recorrer hasta encontrar la posicion correcta
        anterior = actual;
        actual = actual->siguiente; // Avanzar al siguiente nodo
    }
    // Insertar el nuevo nodo entre 'anterior' y 'actual'
    nuevo_nodo->siguiente = actual;
    anterior->siguiente = nuevo_nodo;
    return 0; // Retornar 0 si se inserto correctamente
}

/*
 * FUNCION: main
 * DESCRIPCION: Función principal que demuestra el uso de la lista enlazada
 * - Crea una lista vacía usando crear_lista()
 * - Inserta elementos al final usando insertar_final()
 * - Cada inserción crea nuevo nodo en memoria heap
 * - Imprime la lista completa usando imprimir_lista()
 * - Permite insertar al inicio y en orden usando insertar_inicio() e insertar_ordenado()
 */
int main() {
    struct lista *mi_lista = crear_lista(); // Crear una nueva lista enlazada

    //insertar_final(mi_lista, 10); // Insertar elementos en la lista
    //insertar_final(mi_lista, 20);
    //insertar_final(mi_lista, 30);

    //imprimir_lista(mi_lista); // Imprimir los elementos de la lista

    // insertar_inicio(mi_lista, 5); // Insertar elemento al inicio
    // insertar_inicio(mi_lista, 1); // Insertar otro elemento al inicio
    // imprimir_lista(mi_lista); // Imprimir los elementos de la lista nuevamente

    // insertar_ordenado(mi_lista, 15); // Insertar elemento en orden
    // insertar_ordenado(mi_lista, 25); // Insertar otro elemento en orden
    // imprimir_lista(mi_lista); // Imprimir los elementos de la lista nuevamente

    return 0;
}
