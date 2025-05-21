# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 20/03/2025
# Última modificación: 20/03/2025 9:44
# Python version 3.13

num=0
def invertirNumero(pnum):
    pnum=str(pnum)
    return pnum[::-1]


try:
    num=int(input("Digite un número: ")) 
    if num <= 0:
        print("El número debe ser mayor a 0.")
    elif num <=9:
        print("El número debe poseer al menos dos dígitos.")
    else:
        print("El número invertido es:", invertirNumero(num))
except ValueError:
    print("Debe ingresar únicamente un número entero válido.")