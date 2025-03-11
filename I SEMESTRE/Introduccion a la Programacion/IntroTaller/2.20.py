#
#
#
#

def determinarSigno(pnum):
    if pnum>0:
        return "positivo"
    if pnum<0:
        return "negativo"
    else:
        return "nulo"
    

numeroEntero=float(input("Ingrese un numero: "))
print("El numero es", determinarSigno(numeroEntero))
