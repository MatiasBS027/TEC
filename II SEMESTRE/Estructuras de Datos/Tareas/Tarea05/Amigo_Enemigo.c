#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// ------------------ ESTRUCTURA NAVE ------------------
struct nave {
    int id;
    int equipo; // 0 = enemigo, 1 = amigo
    int vida;
    int ataque;
    struct nave *siguiente;
    struct nave *anterior;
};
// ------------------ LISTA ------------------
struct lista {
    struct nave *inicio;
    struct nave *fin;
};
// ------------------ CREAR LISTA ------------------
struct lista* crear_lista() {
    struct lista *nueva = calloc(1, sizeof(struct lista));
    return nueva;
}
// ------------------ CREAR NAVE ------------------
struct nave* crear_nave(int id) {  
    struct nave *n = calloc(1, sizeof(struct nave));// inicializa en 0
    n->id = id; // id único
    n->equipo = rand() % 2; // aleatorio 0 o 1
    n->vida = 5 + rand() % 16;    // entre 5 y 20
    n->ataque = 5 + rand() % 11;  // entre 5 y 15
    n->siguiente = n->anterior = NULL; // inicializa en NULL
    return n;
}
// ------------------ INSERTAR AL FINAL ------------------
void insertar_final(struct lista *l, struct nave *n) {
    if (!l->inicio) { // lista vacía
        l->inicio = l->fin = n; // inicio y fin apuntan a la nueva nave
    } else { 
        l->fin->siguiente = n; // el siguiente del fin actual es la nueva nave
        n->anterior = l->fin; // el anterior de la nueva nave es el fin actual
        l->fin = n;  // actualizar el fin de la lista
    }
}
// ------------------ IMPRIMIR LISTA ------------------
void imprimir_lista(struct lista *l) {
    if (!l->inicio) {
        printf("La lista está vacía.\n");
        return;
    }
    struct nave *act = l->inicio; // nave actual
    printf("\nNaves en la fila:\n");
    while (act) { // mientras haya nave actual
        // Mostrar si es amigo o enemigo 
        if (act->equipo == 1) { 
            printf("[ID:%d|Amigo|Vida:%d|Atq:%d] ",
                act->id, act->vida, act->ataque);  //act->id es el id de la nave, act->vida es la vida de la nave, act->ataque es el ataque de la nave
        } else {
            printf("[ID:%d|Enemigo|Vida:%d|Atq:%d] ",
                act->id, act->vida, act->ataque); 
        }
        act = act->siguiente; // avanzar al siguiente
    }
    printf("\n");
}
// ------------------ ELIMINAR NAVE ------------------
void eliminar_nave(struct lista *l, struct nave *n) {
    if (!n) {
        return; // si la nave es NULL, salir
    }
    if (n->anterior) { // si no es la primera nave
        n->anterior->siguiente = n->siguiente; // el siguiente del anterior es el siguiente de la nave a eliminar
    } else {  // si es la primera nave
        l->inicio = n->siguiente; // actualizar el inicio de la lista
    }
    if (n->siguiente) { // si no es la última nave
        n->siguiente->anterior = n->anterior;  // el anterior del siguiente es el anterior de la nave a eliminar
    } else { // si es la última nave 
        l->fin = n->anterior; // actualizar el fin de la lista
    }
free(n);
}

// ------------------ DISPARAR ------------------
void disparar(struct lista *l, int id_nave) {
    struct nave *act = l->inicio;  // nave actual
    while (act && act->id != id_nave) {  // buscar nave por id
        act = act->siguiente; // avanzar al siguiente
    }
    if (!act) { // si no se encontró la nave
        printf("Nave no encontrada.\n");
        return;
    }
    printf("\nLa nave ID:%d (", act->id);

    if (act->equipo == 1) {
        printf("Amigo");
    } else {
        printf("Enemigo");
    }
    printf("dispara con ataque de %d\n", act->ataque); // mostrar info de la nave que dispara


    // Disparo a la izquierda
    if (act->anterior) {  // si hay nave a la izquierda
        act->anterior->vida -= act->ataque; // restar vida al enemigo
        printf("El ataque afecta a nave ID:%d (Vida:%d)\n", act->anterior->id, act->anterior->vida); // mostrar vida restante
        if (act->anterior->vida <= 0) { // si la vida es 0 o menos
            printf("La nave ID:%d fue destruida!\n", act->anterior->id); // mostrar mensaje de destrucción
            struct nave *tmp = act->anterior;  // guardar nave a eliminar
            eliminar_nave(l, tmp); 
        }
    }
    // Disparo a la derecha
    if (act->siguiente) {  // si hay nave a la derecha
        act->siguiente->vida -= act->ataque;  // restar vida al enemigo
        printf("El disparo afecta a nave ID:%d (Vida:%d)\n", act->siguiente->id, act->siguiente->vida);  // mostrar vida restante
        if (act->siguiente->vida <= 0) {  // si la vida es 0 o menos
            printf("La nave ID:%d fue destruida!\n", act->siguiente->id);  // mostrar mensaje de destrucción
            struct nave *tmp = act->siguiente;
            eliminar_nave(l, tmp);
        }
    }
}
// ------------------ VERIFICAR FIN DE JUEGO ------------------
int equipo_vivo(struct lista *l, int equipo) {
    struct nave *act = l->inicio;  // nave actual
    while (act) {  // recorrer lista
        if (act->equipo == equipo) return 1;  // si encuentra nave del equipo, retorna 1
        act = act->siguiente;  // avanzar al siguiente
    }
    return 0;
}
// ------------------ MAIN ------------------
int main() {
    srand(time(NULL));

    struct lista *juego = crear_lista();  // crear lista de naves

    // Aquí se decide cuantas naves crear 
    int min_naves = 5;  
    int max_naves = 10; 
    int n = min_naves + rand() % (max_naves - min_naves + 1); // entre 5 y 10 naves
    printf("Se han creado %d naves en total.\n", n);

    // Crear naves
    for (int i = 1; i <= n; i++) {
        insertar_final(juego, crear_nave(i));  // insertar nave al final de la lista
    }

    imprimir_lista(juego);

    int turno = 1; // empieza equipo amigo
    while (equipo_vivo(juego, 0) && equipo_vivo(juego, 1)) { // mientras ambos equipos tengan naves
        if (turno == 1) {
            printf("\n===== TURNO DEL EQUIPO Amigo =====\n");
        } else {
            printf("\n===== TURNO DEL EQUIPO Enemigo =====\n");
        }
        imprimir_lista(juego);
        int id;
        printf("Seleccione ID de la nave para disparar: ");
        scanf("%d", &id);
        struct nave *act = juego->inicio; // nave actual
        int valido = 0;
        while (act) {
            if (act->id == id && act->equipo == turno) { // si la nave existe y es del equipo correcto
                valido = 1;
                break;
            }
            act = act->siguiente; // avanzar al siguiente
        }
        if (!valido) {
            printf("Selección inválida, intenta de nuevo.\n");
            continue;
        }
        disparar(juego, id);
        turno = !turno; // cambiar turno
    }
    if (equipo_vivo(juego, 1)) {
        printf("\nEl equipo Amigo ganó!\n");
    } else {
        printf("\nEl equipo Enemigo ganó!\n");
    }
    return 0;
}