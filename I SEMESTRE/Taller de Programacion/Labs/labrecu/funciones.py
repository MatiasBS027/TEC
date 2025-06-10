#Elaborado por Luis Carlos Tinoco Vargas y Matias Benavides 
#fecha de creación 10/06/2025
#ultima modificación 10/06/2025 10:03
#python 3.13.2

#====================Reto 2. Suma de Cuadrados.====================
"""
instrucciones:Desarrolle la función obtenerSumCuadrados para implementar esta sumatoria de 
cuadrados en un intervalo desde m hasta n. Estos dos valores son la entrada a la 
función y n >= m. Validar entradas y en caso de error retorne -1.
ejemplos de uso
>>>obtenerSumCuadrados(4, 7) 
126     #   4**2 + 5**2 + 6**2 + 7**2 = 126
>>>obtenerSumCuadrados(7, 4) 
-1 
>>>obtenerSumCuadrados(4.5, 7) 
-1 
>>>obtenerSumCuadrados(1, 5) 
55
"""

def obtenerSumCuadrados(m, n, acc):
    if m > n:
        return acc
    return obtenerSumCuadrados(m + 1, n, acc + m ** 2)


#========================Reto 3. Obtener cantidad de pares e impares. ========================
"""
Desarrolle la función obtenerParesImpares que reciba un entero y retorne dos 
resultados: la cantidad de dígitos pares y la cantidad de impares que contiene. 
Validar restricciones y retornar () en caso de error.
ejemplos de uso:
>>>obtenerParesImpares(3214) 
(2, 2) 
>>>obtenerParesImpares(-18006) 
(4, 1) 
>>>obtenerParesImpares(0) 
(1, 0) 
>>>obtenerParesImpares(1) 
(0, 1) 
>>>obtenerParesImpares(“abc”) 
()
"""

def obtenerParesImpares(n, pares, impares):
    if n == 0:
        if pares == 0 and impares == 0:
            return (1, 0)
        return (pares, impares)
    else:
        digito = n % 10
        if digito % 2 == 0:
            return obtenerParesImpares(n // 10, pares + 1, impares)
        else:
            return obtenerParesImpares(n // 10, pares, impares + 1)


#========================Reto 4. Validar binario.  . ========================
"""
Implementar una función recursiva en Python que reciba un número y valide que 
sea binario, devuelve true si toda la cifra es binaria o devuelve false en caso 
contrario.  
Algunas corridas ejemplo son las siguientes: 
>>>esBinario(1001019)  
False 
>>>esBinario (5679)   
False 
Reto 5. Contar Bisiestos.  
>>>esBinario (0)   
True 
>>>esBinario (10101)  
True
"""

def esBinario(n):
    if n == 0:
        return True
    digito = abs(n) % 10
    if digito != 0 and digito != 1:
        return False
    return esBinario(abs(n) // 10)


#========================Reto 5. Contar Bisiestos. ========================
"""
Implementar una función recursiva por cola en Python que reciba un intervalo de 
años y determine cuantos años bisiestos existen en ese periodo de tiempo. Los 
años son números enteros positivos mayores que 0 y además el año inicial debe 
ser debe ser menor que el año final. 
Algunas corridas ejemplo son las siguientes: 
>>>>contarBisiestos(1500, 1836) Devuelve: 82 
>>>>contarBisiestos (2000, 2025) Devuelve: 7 
>>>>contarBisiestos (2022, 2023) Devuelve: 0 
>>>>contarBisiestos (2023, 2020) Devuelve: El año inicial debe ser debe ser menor que el año final. 
"""

def contarBisiestos(a, b, acc):
    if a > b:
        return acc
    if (a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)):
        return contarBisiestos(a + 1, b, acc + 1)
    else:
        return contarBisiestos(a + 1, b, acc)

