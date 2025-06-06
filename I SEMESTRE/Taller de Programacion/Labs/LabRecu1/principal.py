#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creación 4/06/2025
#última actualización 4/06/2025
#python versión 3.13.2

#importación 
from funciones import *

#definición de la funciónes

#============= reto1 ================

def esParAux(n, x):
    """
    Función recursiva que determina si el dígito en la posición 'x' (desde la derecha) del número 'n' es par.
    - Si la posición no existe, retorna un mensaje de error.
    - Si existe, retorna True si el dígito es par, False si es impar.
    """
    if contarDigitos(n) < x:
        return "El número no posee en índice solicitado"
    if x == 1:
        return (n % 10) % 2 == 0
    return esParAux(n // 10, x - 1)

def esParES(n, x):
    """
    Función de entrada/salida para verificar si el dígito en la posición 'x' del número 'n' es par.
    Devuelve una cadena con el resultado o un mensaje de error si los datos no son válidos.
    """
    try:
        resultado = esParAux(n, x)
        if resultado == True:
            return f"El dígito en la posición {x} de {n} es par: True"
        elif resultado == False:
            return f"El dígito en la posición {x} de {n} es par: False"
        else:
            return resultado
    except Exception:
        return "Los valores ingresados no son válidos. Deben ser números enteros."

# Pruebas
print("======RETO 1======")
print(esParES(6700, 3))   # False
print(esParES(92553, 4))  # True
print(esParES(80, 3))     # "El número no posee en índice solicitado"
print(esParES(94, 1))     # True


#==========Reto 3==========
def decodeBinaryAUX(binario):
    # Verifica que todos los dígitos sean 0 o 1
    temp = binario
    while temp > 0:
        digito = temp % 10
        if digito not in [0, 1]:
            return "El número ingresado no es un binario válido."
        temp //= 10
    return decodeBinary(binario)

def decodeBinaryES(binario):
    try:
        #binario = int(input("Ingrese el número binario: "))
        resultado = decodeBinaryAUX(binario)
        return (f"El número decimal es: {resultado}")
    except ValueError:
        return "El número ingresado no es un binario válido."

print("======RETO 3======")
binario = 1010
print(f"Para la entrada {binario}")
print(decodeBinaryES(binario))
binario = 101
print(f"Para la entrada {binario}")
print(decodeBinaryES(binario))
binario = 10000000
print(f"Para la entrada {binario}")
print(decodeBinaryES(binario))
binario = 110010
print(f"Para la entrada {binario}")
print(decodeBinaryES(binario))
#==========Reto 5==========

def cantPrimosRangoAUX(inicio, fin):
    if inicio > fin:
        return "El inicio del rango debe ser menor o igual al fin del rango."
    else:
        return cantPrimosRango(inicio, fin)


def cantPrimosRangoES(inicio, fin):
    try:
        #inicio = int(input("Ingrese el inicio del rango: "))
        #fin = int(input("Ingrese el fin del rango: "))
        resultado = cantPrimosRangoAUX(inicio, fin)
        return f"Cantidad de números primos entre {inicio} y {fin}: {resultado}"
    except ValueError:
        return "Los valores ingresados no son válidos. Deben ser números enteros."

print("\n======RETO 5======")
print(cantPrimosRangoES(1, 3))  #Aunque el numero 1 no es primo viene que tiene "contar" por que en las instrucciones del reto lo cuentan
print(cantPrimosRangoES(1, 7))   
print(cantPrimosRangoES(1, 15)) 

#==========Reto 7===============
def primosCercanosAUX(a, b):
    """
    Función recursiva que determina si dos números enteros positivos 'a' y 'b' son cercanos.
    Dos números son cercanos si la suma de sus divisores propios es igual.
    """
    sumaA = sumaDivisores(a)
    sumaB = sumaDivisores(b)
    return sumaA == sumaB

def primosCercanosES(a, b):
    """
    Función de entrada/salida que evalúa si dos números son cercanos.
    Devolverá 'True' o 'False' directamente. (así se pidió en las instrucciones)
    """
    try:
        if a <= 0 or b <= 0:
            return "Los números deben ser enteros positivos."
        return primosCercanosAUX(a, b)
    except Exception:
        return "Los valores ingresados no son válidos. Deben ser números enteros."

# Pruebas
print("======RETO 7======")
print(primosCercanosES(13, 7))     # True
print(primosCercanosES(18, 51))    # True
print(primosCercanosES(98, 175))   # True
print(primosCercanosES(220, 562))  # True 
