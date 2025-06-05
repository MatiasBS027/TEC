#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creación 4/06/2025
#última actualización 4/06/2025
#python versión 3.13.2

#importación 
from funciones import *

#definición de la funciónes
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