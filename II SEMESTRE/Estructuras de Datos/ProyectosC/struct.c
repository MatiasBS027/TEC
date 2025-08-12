// Elaborado por: Matias Benavides 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Persona {
    char name[50];
    int age;
    float height;
};

int main(){
    struct Persona p1;
    strcpy(p1.name, "Matias");
    p1.age = 20;
    p1.height = 1.75;

    printf("Nombre: %s\n", p1.name);
    printf("Edad: %d\n", p1.age);
    printf("Altura: %.2f\n", p1.height);





    return 0; // Fin
}