#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creación 4/06/2025
#última actualización 4/06/2025
#python versión 3.13.2


def decodeBinary(binario):
    if binario == 0:
        return 0
    else:
        return (binario % 10) + 2 * decodeBinary(binario // 10)

def esPrimo(n): 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def cantPrimosRango(inicio, fin):
    if inicio > fin:
        return 0
    else:
        if esPrimo(inicio):
            return 1 + cantPrimosRango(inicio + 1, fin)
        else:
            return cantPrimosRango(inicio + 1, fin)
    
def contarDigitos(n):
    """
    Cuenta la cantidad de dígitos de un número entero positivo n.
    """
    if n < 10:
        return 1
    else:
        return 1 + contarDigitos(n // 10)

def sumaDivisores(n, divisor=1):
    if divisor >= n:
        return 0
    if n % divisor == 0:
        return divisor + sumaDivisores(n, divisor + 1)
    else:
        return sumaDivisores(n, divisor + 1)