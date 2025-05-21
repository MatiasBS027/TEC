#
#
#
#

def calcularAreaT(pbase,paltura):
    '''
    Funionamiento: Calcula el area del triangulo
    Entradas:
    -pbase(float):Medida de la base del Triangulo
    -paltura(float):Medida de la altura del Triangulo
    Salidas:
    -area(float);Tamaño del area del Triangulo
    '''
    
    return((pbase*paltura)/2)

base=float(input("El valor de la base es: "))
altura=float(input("El valor de la altura es: "))

print("El area del tringulo es :", calcularAreaT(base,altura))