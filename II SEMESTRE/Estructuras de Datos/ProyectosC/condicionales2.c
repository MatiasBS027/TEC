#include <stdio.h>

int main () {
    char color = 'A';

    //Switch solo acepta enteros o caracteres
    switch (color) {
        case 'R':
            printf("Rojo\n");
            break;
        case 'G':
            printf("Verde\n");
            break;
        case 'B':
            printf("Azul\n");
            break;
        default:
            printf("Color desconocido\n");
            break;
    }
    return 0;
}