#include <stdio.h>

int main () {
    int resultado;
    int nota1;
    int nota2;
    int nota3;

    printf("Ingrese la primera nota: ");
    scanf("%d", &nota1);
    printf("Ingrese la segunda nota: ");
    scanf("%d", &nota2);
    printf("Ingrese la tercera nota: ");
    scanf("%d", &nota3);

    resultado = (nota1 + nota2 + nota3) / 3;
    if (resultado >= 70) {
        printf("Aprobado\n");
    } else {
        printf("Desaprobado\n");
    }
    return 0;
}