#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Amigo_Enemigo.h"

int main() {
    srand(time(NULL));

    struct lista *juego = crear_lista();

    int min_naves = 5;  
    int max_naves = 10; 
    int n = min_naves + rand() % (max_naves - min_naves + 1); // Número aleatorio de naves entre 5 y 10
    printf("Se han creado %d naves en total.\n", n);

    for (int i = 1; i <= n; i++) {
        insertar_final(juego, crear_nave(i)); // Crea e inserta naves con IDs del 1 al n
    }
    imprimir_lista(juego);

    int turno = 1; 
    while (equipo_vivo(juego, 0) && equipo_vivo(juego, 1)) {
        printf("\n===== TURNO DEL EQUIPO %s =====\n", turno ? "Amigo" : "Enemigo");
        imprimir_lista(juego);
        int id;
        printf("Seleccione ID de la nave para disparar: ");
        scanf("%d", &id);

        struct nave *act = juego->inicio; // Verifica que la nave seleccionada sea válida
        int valido = 0;
        while (act) {
            if (act->id == id && act->equipo == turno) {  // Verifica que la nave pertenezca al equipo del turno
                valido = 1;
                break;
            }
            act = act->siguiente; // Avanza al siguiente
        }
        if (!valido) {
            printf("Selección inválida, intenta de nuevo.\n");
            continue;
        }
        disparar(juego, id);
        turno = !turno;
    }

    if (equipo_vivo(juego, 1)) {
        printf("\nEl equipo Amigo ganó!\n");
    } else {
        printf("\nEl equipo Enemigo ganó!\n");
    }
    return 0;
}
