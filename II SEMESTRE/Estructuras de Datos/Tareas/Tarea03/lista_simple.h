#ifndef LISTA_SIMPLE_H
#define LISTA_SIMPLE_H

#include <stdio.h>

// Estructura: Nodo
struct nodo {
    int valor;
    struct nodo *siguiente;
};

// Estructura: Lista
struct lista {
    struct nodo *inicio;
};

// Prototipos de funciones
struct lista* crear_lista();
struct nodo* crear_nodo(int valor);

int imprimir_lista(struct lista *lista);
int insertar_final(struct lista *lista, int valor);
int insertar_inicio(struct lista *lista, int valor);
int insertar_ordenado(struct lista *lista, int valor);
int eliminar_elemento(struct lista *lista, int valor);
void liberar_lista(struct lista *lista); // Para evitar fugas de memoria

#endif
