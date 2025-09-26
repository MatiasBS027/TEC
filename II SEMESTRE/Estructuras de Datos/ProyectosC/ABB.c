#include <stdio.h>

struct nodo_arbol{
    int dato;
    struct nodo_arbol *izquierda;
    struct nodo_arbol *derecha;
};

void insertar_elemento(struct nodo_arbol **nodo, int valor){
    if (*nodo == NULL){
        struct nodo_arbol *nuevo_nodo = (struct nodo_arbol *)calloc(sizeof(struct nodo_arbol));
        nuevo_nodo->dato = valor;
        nuevo_nodo->izquierda = NULL;
        nuevo_nodo->derecha = NULL;
        *nodo = nuevo_nodo;
    } else if (valor < (*nodo)->dato){
        insertar_elemento(&(*nodo)->izquierda, valor);
    } else {
        insertar_elemento(&(*nodo)->derecha, valor);
    }
}

void print_preorden(struct nodo_arbol *nodo){
    if (nodo == NULL)
        return;
    printf("%d ", nodo->dato);
    print_preorden(nodo->izquierda);
    print_preorden(nodo->derecha);
}

void print_inorden(struct nodo_arbol *nodo){
    if (nodo == NULL)
        return;
    print_inorden(nodo->izquierda);
    printf("%d ", nodo->dato);
    print_inorden(nodo->derecha);
}

void print_postorden(struct nodo_arbol *nodo){
    if (nodo == NULL)
        return;
    print_postorden(nodo->izquierda);
    print_postorden(nodo->derecha);
    printf("%d ", nodo->dato);
}

int main() {
    struct nodo_arbol *raiz = NULL;
    int valores[] = {50, 30, 20, 40, 70, 60, 80};
    int n = sizeof(valores)/sizeof(valores[0]);

    for (int i = 0; i < n; i++) {
        insertar_elemento(&raiz, valores[i]);
    }

    printf("Recorrido en preorden: ");
    print_preorden(raiz);
    printf("\n");

    printf("Recorrido en inorden: ");
    print_inorden(raiz);
    printf("\n");

    printf("Recorrido en postorden: ");
    print_postorden(raiz);
    printf("\n");

    return 0;
}