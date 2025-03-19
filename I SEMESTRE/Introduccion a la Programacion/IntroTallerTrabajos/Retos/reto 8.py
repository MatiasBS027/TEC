# Elaborado por Tinoco Vargas Luis Carlos
# Fecha de creación: 18/03/2025
# Última modificación: 18/03/2025 20:26
# Python version 3.13

""" En esta función se determina si un número es primo o no, si el número es menor a 1 o no es un número entero
se le pide al usuario que ingrese un número mayor a 1 y que sea entero"""
def esNumeroPrimo (pnum):
    if pnum<=1:
        return "El número debe ser mayor a 1"
    elif pnum==2:
        return "El número es primo"
    else :
        for i in range (2,int(pnum**0.5)+1):
            if pnum%i==0:
                return "El número no es primo"
        return "El número es primo"
# Función auxiliar para validar la entrada
while True:
    try:
        num= int(input("Digite un número: "))
        break
    except ValueError:
        print ("Debe ingresar un número")
print(esNumeroPrimo(num))