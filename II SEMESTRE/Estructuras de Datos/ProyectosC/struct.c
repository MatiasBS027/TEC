// Elaborado por: Matias Benavides 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { // El typedef nos ayuda a crear un alias para la estructura y asi no tener que usar 'struct' cada vez que la queramos usar
    char name[50];
    int age;
    float height;
}Persona; // Como hemos definido la estructura, ahora podemos usar 'Persona' como un tipo de dato e incluso podrias tener un struct vacio ya que llama al "apodo" 'Persona'

void print_persona(Persona *p) {
    printf("Nombre: %s\n", p->name); // El operador '->' se usa para acceder a los miembros de la estructura a través de un puntero
    printf("Edad: %d\n", p->age); // Que lo mismo es igual a (*p).age
    printf("Altura: %.2f\n", p->height);    
}

int main(){
    Persona p1;
    
    strcpy(p1.name, "Matias"); // Aqui ponemos el p1.name para que sea igual a "Matias"
    p1.age = 20; // En vez de usar un puntero, asignamos directamente el valor a la estructura
    p1.height = 1.75;// Y no usamos el p-> para acceder a los miembros de la estructura, sino que usamos el punto (.)

    print_persona(&p1); // Llama a la función para imprimir los datos de la persona

    return 0; // Fin
}