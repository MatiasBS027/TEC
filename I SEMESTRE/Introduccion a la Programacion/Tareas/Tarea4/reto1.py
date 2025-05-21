# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 20/03/2025
# Última modificación: 20/03/2025 9:44
# Python version 3.13

a = 0
b = 0
c = 0

def formarNumeroInverso(pa, pb, pc):
    if not (isinstance(pa, int) and isinstance(pb, int) and isinstance(pc, int)):
        return "Todos los valores deben ser números enteros."
    if pa > 9 or pb > 9 or pc > 9:
        return "Los números deben ser menores o iguales a 9."
    elif pa < 0 or pb < 0 or pc < 0:
        return "Los números deben ser mayores o iguales a 0."
    else:
        return str(pc) + str(pb) + str(pa)

def solicitarNumero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0 or valor > 9:
                print("El número debe estar entre 0 y 9. Inténtalo de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

a = solicitarNumero("Digite el valor de a: ")
b = solicitarNumero("Digite el valor de b: ")
c = solicitarNumero("Digite el valor de c: ")

print(formarNumeroInverso(a, b, c))