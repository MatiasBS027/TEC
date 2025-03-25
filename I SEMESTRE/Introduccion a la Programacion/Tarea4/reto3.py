# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 20/03/2025
# Última modificación: 20/03/2025 9:44
# Python version 3.13

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

while True:
    try:
        n = int(input("Digite un número entero: "))
        if n < 0:
            print("Por favor, ingrese un número no negativo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. ingrese un número entero.")

print("El factorial de", n, "es", factorial(n))