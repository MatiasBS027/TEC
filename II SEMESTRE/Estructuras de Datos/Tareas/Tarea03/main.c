#include "lista_simple.h"

/*
 * FUNCIÓN: main
 * DESCRIPCIÓN: Demuestra uso de la lista enlazada
 */
int main() {
    struct lista *mi_lista = crear_lista(); // Crear una nueva lista enlazada

    insertar_final(mi_lista, 10); // Insertar elementos en la lista
    insertar_final(mi_lista, 20);
    insertar_final(mi_lista, 30);

    imprimir_lista(mi_lista); // Imprimir los elementos de la lista

    insertar_inicio(mi_lista, 5); // Insertar elemento al inicio
    insertar_inicio(mi_lista, 1); // Insertar otro elemento al inicio
    imprimir_lista(mi_lista); // Imprimir los elementos de la lista nuevamente

    insertar_ordenado(mi_lista, 15); // Insertar elemento en orden
    insertar_ordenado(mi_lista, 25); // Insertar otro elemento en orden
    imprimir_lista(mi_lista); // Imprimir los elementos de la lista nuevamente

    eliminar_elemento(mi_lista, 20);
    imprimir_lista(mi_lista);

    return 0;
}
