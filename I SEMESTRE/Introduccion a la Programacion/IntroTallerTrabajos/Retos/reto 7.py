# Elaborado por Tinoco Vargas Luis Carlos
# Fecha de creación: 18/03/2025
# Última modificación: 18/03/2025 20:08
# Python version 3.13

base=0
exponente=0
""" En esta función se eleva un número a una potencia, si la base y el exponente son menores a cero"""
def elevarNumero (base,exponente):
    if base and exponente < 0:
        print ("la bsese y el exponente deben de ser mayor o igual a cero")
    else:
        base and exponente >=0
        print ("El resultado de la operación es: ")
    return base ** exponente
"""while si los números cumplen con la función calcula y printea los resultados de la potencia"""
while True:
    try:
        base = int(input("Digite la base: "))
        exponente = int(input("Digite el exponente: "))
        break
    except ValueError:
        print ("Debe ingresar un número entero")
        
print(elevarNumero(base,exponente))