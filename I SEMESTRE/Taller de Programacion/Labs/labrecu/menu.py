#Elaborado por Luis Carlos Tinoco Vargas y Matias Benavides 
#fecha de creación 10/06/2025
#ultima modificación 10/06/2025 10:03
#python 3.13.2

from funciones import *


#====================Reto 2. Suma de Cuadrados.====================
print("\n=========================recursividad por cola==============================")
print("Reto 2. Suma de Cuadrados.")
def obtenerSumCuadradosAUX(m,n):
    if m > n or type(m) != int or type(n) != int:
        return -1
    elif m == n:
        return m**2
    else:
        return obtenerSumCuadrados(m+1,n) + m**2


print(obtenerSumCuadradosAUX(4,7))
print(obtenerSumCuadradosAUX(7,4))
print(obtenerSumCuadradosAUX(4.5,7))
print(obtenerSumCuadradosAUX(1,5))

#========================Reto 3. Obtener cantidad de pares e impares. ========================
print("\n=========================Reto 3. Obtener cantidad de pares e impares. =========================")
def obtenerParesImparesAUX(n):
    if type(n) != int:
        return ()
    return obtenerParesImpares(abs(n), 0, 0)

# Pruebas
print(obtenerParesImparesAUX(3214))     # (2, 2)
print(obtenerParesImparesAUX(-18006))   # (4, 1)
print(obtenerParesImparesAUX(0))        # (1, 0)
print(obtenerParesImparesAUX(1))        # (0, 1)
print(obtenerParesImparesAUX("abc"))    # ()

#========================Reto 4. Validar binario.  . ========================
print("\n=========================Reto 4. Validar binario. =========================")
def esBinarioAUX(n):
    if type(n) != int or n < 0:
        return False
    return esBinario(n)

print(esBinarioAUX(1001019))
print(esBinarioAUX(5679))
print(esBinarioAUX(0))
print(esBinarioAUX(10101))

#========================Reto 5. Contar Bisiestos. ========================
print("\n=========================Reto 5. Contar Bisiestos.     =========================")
def contarBisiestosAUX(a,b):
    if a > b or a <= 0 or b <= 0:
        return "El año inicial debe ser debe ser menor que el año final."
    else:
        return contarBisiestos(a,b)


print(contarBisiestosAUX(1500,1836))
print(contarBisiestosAUX(2000,2025))
print(contarBisiestosAUX(2022,2023))
print(contarBisiestosAUX(2023,2020))
