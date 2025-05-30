def fibonacciR(n):
    """
    Funcionamiento:
        Calcula el n-ésimo número de la sucesión de Fibonacci de forma recursiva.
    Entradas:
        - n: número entero mayor o igual a 0.
    Salidas:
        - Número entero correspondiente al valor de Fibonacci en la posición n.
    """
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacciR(n - 1) + fibonacciR(n - 2)

def fibonacciI(n):
    """
    Funcionamiento:
        Calcula el n-ésimo número de la sucesión de Fibonacci de forma iterativa.
    Entradas:
        - n: número entero mayor o igual a 0.
    Salidas:
        - Número entero correspondiente al valor de Fibonacci en la posición n.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def factorialR(n):
    """
    Funcionamiento:
        Calcula el factorial de un número de forma recursiva.
    Entradas:
        - n: número entero mayor o igual a 0.
    Salidas:
        - Número entero correspondiente al factorial de n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorialR(n - 1)

def factorialI(n):
    """
    Funcionamiento:
        Calcula el factorial de un número de forma iterativa.
    Entradas:
        - n: número entero mayor o igual a 0.
    Salidas:
        - Número entero correspondiente al factorial de n.
    """
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def esPrimoR(n, divisor=2):
    """
    Funcionamiento:
        Determina si un número es primo de forma recursiva.
    Entradas:
        - n: número entero mayor o igual a 2.
        - divisor: entero (por defecto 2), usado para la recursión.
    Salidas:
        - True si n es primo, False en caso contrario.
    """
    if n < 2:
        return False
    elif divisor > n // 2:
        return True
    elif n % divisor == 0:
        return False
    return esPrimoR(n, divisor + 1)

def esPrimoI(n):
    """
    Funcionamiento:
        Determina si un número es primo de forma iterativa.
    Entradas:
        - n: número entero mayor o igual a 2.
    Salidas:
        - True si n es primo, False en caso contrario.
    """
    if n < 2:
        return False
    for divisor in range(2, (n // 2) + 1):
        if n % divisor == 0:
            return False
    return True

def textoRecursivo(texto, n):
    """
    Funcionamiento:
        Genera una lista con el texto repetido n veces de forma recursiva.
    Entradas:
        - texto: cadena de caracteres.
        - n: número entero mayor o igual a 0.
    Salidas:
        - Lista de cadenas con el texto repetido n veces.
    """
    if n == 0:
        return []
    else:
        resultado = [texto]
        resultado += textoRecursivo(texto, n - 1)
        return resultado

def textoIterativo(texto, n):
    """
    Funcionamiento:
        Genera una lista con el texto repetido n veces de forma iterativa.
    Entradas:
        - texto: cadena de caracteres.
        - n: número entero mayor o igual a 0.
    Salidas:
        - Lista de cadenas con el texto repetido n veces.
    """
    resultado = []
    for _ in range(n):
        resultado.append(texto)
    return resultado

def maximoComunDivisorR(a, b):
    """
    Funcionamiento:
        Calcula el máximo común divisor (MCD) de dos números de forma recursiva.
    Entradas:
        - a: número entero.
        - b: número entero.
    Salidas:
        - Número entero correspondiente al MCD de a y b.
    """
    if b == 0:
        return a
    else:
        return maximoComunDivisorR(b, a % b)

def maximoComunDivisorI(a, b):
    """
    Funcionamiento:
        Calcula el máximo común divisor (MCD) de dos números de forma iterativa.
    Entradas:
        - a: número entero.
        - b: número entero.
    Salidas:
        - Número entero correspondiente al MCD de a y b.
    """
    while b != 0:
        a, b = b, a % b
    return a

import time
def compararTiempos(funcI, funcR, *args, **kwargs):
    """
    Funcionamiento:
        Compara el tiempo de ejecución de dos funciones (iterativa y recursiva) con los mismos argumentos.
    Entradas:
        - funcI: función iterativa.
        - funcR: función recursiva.
        - *args, **kwargs: argumentos para las funciones.
    Salidas:
        - resultadoI: resultado de la función iterativa.
        - tiempoI: tiempo de ejecución de la función iterativa.
        - resultadoR: resultado de la función recursiva.
        - tiempoR: tiempo de ejecución de la función recursiva.
    """
    inicioI = time.time()
    resultadoI = funcI(*args, **kwargs)
    tiempoI = time.time() - inicioI

    inicioR = time.time()
    resultadoR = funcR(*args, **kwargs)
    tiempoR = time.time() - inicioR

    return resultadoI, tiempoI, resultadoR, tiempoR