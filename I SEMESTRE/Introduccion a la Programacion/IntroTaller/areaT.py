#
#
#
#

def calcularAreaT(pbase,paltura):
    return((pbase*paltura)/2)

base=float(input("El valor de la base es: "))
altura=float(input("El valor de la altura es: "))

print("El area del tringulo es :", calcularAreaT(base,altura))