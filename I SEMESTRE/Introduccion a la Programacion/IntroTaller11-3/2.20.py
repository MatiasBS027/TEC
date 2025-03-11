#
#
#
#

def determinarSigno(pnum):
    '''
    Funionamiento: Calcula si un numero es positivo, negativo o nulo
    Entradas:
    -pnum(float):Numero al que vamos a evaluar
    Salidas:
    -positivo(str): Si el numero es positivo osea mayor a cero
    -negativo(str): Si el numero es negativo osea menor a cero
    -nulo(str): Si el numero es nulo osea es cero
    '''
    
    if pnum>0:
        return "positivo"
    if pnum<0:
        return "negativo"
    else:
        return "nulo"
    

numeroEntero=float(input("Ingrese un numero: "))
print("El numero es ", determinarSigno(numeroEntero))
