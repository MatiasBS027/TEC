#include <stdio.h>

int main () {
    char *animales[] = {"Perro", "Gato", "Pájaro", "Pez"};
    //Iniciamos un bucle for para recorrer el array
    //Mientras i sea menor que 4, incrementamos i en 1
    //Aumentamos i en 1 en cada iteración
    //Imprimimos cada elemento del array
    for (int i = 0; i < 4; i++) {
        printf("%s\n", animales[i]);
    }
    return 0;
}