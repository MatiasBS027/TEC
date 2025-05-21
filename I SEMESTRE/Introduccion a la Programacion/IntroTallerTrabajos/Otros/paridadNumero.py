def esPar(pnum):
    if pnum %2 ==0:
        return True
    else:
        return False

def contarDigitos(pn): #Función para determinar la cantidad de digitos
    if pn==0:
        return 1
    contador=0
    while pn!=0:
        contador+=1
        pn//=10
    return contador #Retorna la cantidad de digitos

def determinarParidad(pn1,pn2):
    contador=1
    while contador!=pn1:
        pn2//=10
        contador+=1
    if esPar(pn2) == True:
        return True
    else: 
        return False

def determinarParidadAUX(pn1,pn2):
    if pn1 > contarDigitos(pn2):
        return "La posicion indicada no es valida"
    if pn1 < 0:
        return "El numero debe ser mayor o igual a 0"
    if pn2 < 1:
        return "La posición debe ser mayor a 1"
    return determinarParidad(pn1,pn2)

def determinarParidadES():
    try:
        pn1 = int(input("Digite la posicion del numero: "))
        pn2 = int(input("Digite el numero: ")) 
        resultado = determinarParidadAUX(pn1, pn2)
        if resultado == True:
            return "El dígito en la posición indicada es PAR"
        elif resultado == False:
            return "El dígito en la posición indicada es IMPAR"
        else:
            return resultado  # Esto maneja los mensajes de error como "La posicion indicada no es valida"
    
    except ValueError:
        return "Los numeros deben ser enteros positivos"

print(determinarParidadES())
