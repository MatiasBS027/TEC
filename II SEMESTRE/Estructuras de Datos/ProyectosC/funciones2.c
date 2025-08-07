#include <stdio.h>

int multiplicar(int primero, int segundo) {
    return primero * segundo;
}

int main() {
    int resultado1 = multiplicar(3, 5);
    printf("%d\n", resultado1);
    int resultado2 = multiplicar(10, 20);
    printf("%d\n", resultado2);
    return 0;
}