#ifndef JUEGO_H
#define JUEGO_H

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

// ------------------ PROTOTIPOS ------------------
struct lista* crear_lista();
struct nave* crear_nave(int id);
void insertar_final(struct lista *l, struct nave *n);
void imprimir_lista(struct lista *l);
void eliminar_nave(struct lista *l, struct nave *n);
void disparar(struct lista *l, int id_nave);
int equipo_vivo(struct lista *l, int equipo);

#endif