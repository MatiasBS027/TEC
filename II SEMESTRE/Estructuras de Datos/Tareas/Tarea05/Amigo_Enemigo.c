#include <stdio.h>
#include <stdlib.h>
#include "Amigo_Enemigo.h"

// ------------------ CREAR LISTA ------------------
// Crea una lista vacía y retorna el puntero a la estructura lista
struct lista* crear_lista() {
    struct lista *nueva = calloc(1, sizeof(struct lista)); // Reserva memoria inicializada en cero
    return nueva;
}

// ------------------ CREAR NAVE ------------------
// Crea una nave con valores aleatorios para equipo, vida y ataque
struct nave* crear_nave(int id) {  
    struct nave *n = calloc(1, sizeof(struct nave)); // Reserva memoria para la nave
    n->id = id; // Asigna el identificador
    n->equipo = rand() % 2; // 0 = enemigo, 1 = amigo (aleatorio)
    n->vida = 5 + rand() % 16; // Vida entre 5 y 20
    n->ataque = 5 + rand() % 11; // Ataque entre 5 y 15
    n->siguiente = n->anterior = NULL; // Inicializa punteros
    return n;
}

// ------------------ INSERTAR AL FINAL ------------------
// Inserta una nave al final de la lista doblemente enlazada
void insertar_final(struct lista *l, struct nave *n) {
    if (!l->inicio) { // Si la lista está vacía
        l->inicio = l->fin = n;
    } else {
        l->fin->siguiente = n; // Enlaza la nueva nave al final
        n->anterior = l->fin;  // Enlaza la nueva nave con la anterior última
        l->fin = n;            // Actualiza el puntero al final de la lista
    }
}

// ------------------ IMPRIMIR LISTA ------------------
// Muestra todas las naves y sus datos en la lista
void imprimir_lista(struct lista *l) {
    if (!l->inicio) {
        printf("La lista está vacía.\n");
        return;
    }
    struct nave *act = l->inicio;
    printf("\nNaves en la fila:\n");
    while (act) {
        // Imprime si la nave es amiga o enemiga y sus atributos
        if (act->equipo == 1) { 
            printf("[ID:%d|Amigo|Vida:%d|Atq:%d] ",
                act->id, act->vida, act->ataque);
        } else {
            printf("[ID:%d|Enemigo|Vida:%d|Atq:%d] ",
                act->id, act->vida, act->ataque);
        }
        act = act->siguiente;
    }
    printf("\n");
}

// ------------------ ELIMINAR NAVE ------------------
// Elimina una nave de la lista y libera su memoria
void eliminar_nave(struct lista *l, struct nave *n) {
    if (!n) return;
    // Actualiza los punteros de la lista para saltar la nave eliminada
    if (n->anterior) {
        n->anterior->siguiente = n->siguiente;
    } else {
        l->inicio = n->siguiente; // Si es la primera nave
    }
    if (n->siguiente) {
        n->siguiente->anterior = n->anterior;
    } else {
        l->fin = n->anterior; // Si es la última nave
    }
    free(n); // Libera la memoria de la nave eliminada
}

// ------------------ DISPARAR ------------------
// La nave con id_nave ataca a sus vecinas (izquierda y derecha)
void disparar(struct lista *l, int id_nave) {
    struct nave *act = l->inicio;
    // Busca la nave con el id dado
    while (act && act->id != id_nave) {
        act = act->siguiente;
    }
    if (!act) {
        printf("Nave no encontrada.\n");
        return;
    }
    printf("\nLa nave ID:%d (%s) dispara con ataque de %d\n", 
        act->id, act->equipo ? "Amigo" : "Enemigo", act->ataque);

    // Ataca a la nave de la izquierda (si existe)
    if (act->anterior) {
        act->anterior->vida -= act->ataque; // Resta vida
        printf("El ataque afecta a nave ID:%d (Vida:%d)\n", 
            act->anterior->id, act->anterior->vida);
        // Si la nave queda sin vida, se elimina
        if (act->anterior->vida <= 0) {
            printf("La nave ID:%d fue destruida!\n", act->anterior->id);
            eliminar_nave(l, act->anterior);
        }
    }
    // Ataca a la nave de la derecha (si existe)
    if (act->siguiente) {
        act->siguiente->vida -= act->ataque; // Resta vida
        printf("El disparo afecta a nave ID:%d (Vida:%d)\n", 
            act->siguiente->id, act->siguiente->vida);
        // Si la nave queda sin vida, se elimina
        if (act->siguiente->vida <= 0) {
            printf("La nave ID:%d fue destruida!\n", act->siguiente->id);
            eliminar_nave(l, act->siguiente);
        }
    }
}

// ------------------ VERIFICAR FIN DE JUEGO ------------------
// Retorna 1 si queda alguna nave del equipo dado, 0 si no
int equipo_vivo(struct lista *l, int equipo) {
    struct nave *act = l->inicio;
    while (act) {
        if (act->equipo == equipo) return 1; // Si encuentra una nave del equipo, retorna 1
        act = act->siguiente;
    }
    return 0; // No queda ninguna nave del equipo
}
