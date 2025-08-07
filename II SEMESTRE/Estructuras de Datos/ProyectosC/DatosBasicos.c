#include <stdio.h>

int main() {
    // Ejemplo de uso de printf con diferentes tipos de datos
    char libro[] = "El Quijote";
    printf("%s\n", libro);
    char telf[] = "8968-3020";
    printf("%s\n", telf);
    int entero = 13213312;
    printf("%d\n", entero);
    float decimal = 3.14159;
    printf("%f\n", decimal);
    // Ejemplo de uso de printf con un array
    int numeros[] ={ 1, 2, 3, 4, 5 };
    printf("%d\n ", numeros[0]);
    // Ejemplo de uso de printf con un array de caracteres
    char *animales[4] = {"Perro", "Gato", "Pájaro", "Pececito"};
    printf("%s\n",animales[0]);
    
    const float pi= 3.14159;
    printf("%f\n", pi);
    return 0;
}  