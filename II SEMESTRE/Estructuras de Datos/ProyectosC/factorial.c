// Elaborado por: Matias Benavides 
#include <stdio.h>
/*
 * Funcionamiento: Calcula el factorial de un número entero ingresado por el usuario.
 * Entrada: Un número entero (digitado por el usuario).
 * Salida: El factorial del número ingresado.
 */
int main (){
    int total = 1; // Variable para almacenar el resultado del factorial
    int numero;    // Variable para almacenar el número ingresado por el usuario

    printf("Digite um numero: "); // Solicita al usuario que ingrese un número
    scanf("%d", &numero);         // Lee el número ingresado

    // Calcula el factorial multiplicando desde 'numero' hasta 1
    for (total; numero > 1; numero--) {
        total *= numero;
    }
    printf("Fatorial: %d\n", total); // Muestra el resultado del factorial
    return 0; // Fin
}