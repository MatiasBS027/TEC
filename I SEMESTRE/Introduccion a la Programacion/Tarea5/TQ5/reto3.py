# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 24/03/2025
# Última modificación: 24/03/2025 11:30
# Python version 3.13

def esPalindromo(numero):
    """
    Verifica si un número es palíndromo sin usar listas, slicing ni len().
    
    :param numero: int, número entero positivo mayor que 9.
    :return: str, mensaje indicando si es palíndromo o no.
    """
    if not isinstance(numero, int) or numero <= 9:
        return "El número debe ser un entero positivo mayor que 9."

    numStr = str(numero)
    inicio = 0
    fin = 0

    for digito in numStr:
        fin += 1  # Contar la cantidad de caracteres
    
    fin -= 1  # Última posición válida

    while inicio < fin:
        if numStr[inicio] != numStr[fin]:
            return "El número no es palíndromo."
        inicio += 1
        fin -= 1

    return "El número es palíndromo."

def solicitarNumero():
    """
    Solicita un número entero positivo mayor que 9 al usuario.
    
    :return: int, número ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input("Ingrese un número entero positivo mayor que 9: "))
            if valor > 9:
                return valor
            else:
                print("El número debe ser mayor que 9. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

# Programa principal
num = solicitarNumero()
print(esPalindromo(num))
