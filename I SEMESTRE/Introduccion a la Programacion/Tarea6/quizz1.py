# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 27/03/2025 9:30
# Última modificación: 27/03/2025 10:23
# Python version 3.13

def contarDigitos(pn): #Función para determinar la cantidad de digitos
    if pn==0:
        return 1
    contador=0
    while pn!=0:
        contador+=1
        pn//=10
    return contador #Retorna la cantidad de digitos

def contarApariciones(pnum, pnum2):
    digitosPnum = contarDigitos(pnum)  # Cantidad de dígitos del número a buscar
    divisor = 10 ** digitosPnum  # Potencia de 10 para dividir
    contador = 0

    while pnum2 > 0:
        if pnum2 % divisor == pnum:  # Verifica si los últimos dígitos coinciden
            contador += 1
        pnum2 //= divisor  

    return contador 
def contarAparicionesAUX(pnum,pnum2):
    if pnum < 0 and pnum2 < 0:
        return "Ambos números deben ser mayores a 0"
    else:
        return contarApariciones(pnum,pnum2)

def contarAparicionesES(pn1,pn2):
    try:
        #pnum=int(input("Ingrese el número a buscar: "))
        #pnum2=int(input("Ingrese el numero donde buscar: "))
        return contarAparicionesAUX(pn1,pn2)
    except ValueError:
        return "Debe ingresar un número entero"

print("\n=== Encontrar Digitos ===")
pn1= 22
pn2= 2228
print("Para la entrada:",pn1,pn2)
print(contarAparicionesES(pn1,pn2))
pn1= 808
pn2= 80808808
print("Para la entrada:",pn1,pn2)
print(contarAparicionesES(pn1,pn2))
pn1= 12345
pn2= 1234
print("Para la entrada:",pn1,pn2)
print(contarAparicionesES(pn1,pn2))
pn1= 1
pn2= 10111010 
print("Para la entrada:",pn1,pn2)
print(contarAparicionesES(pn1,pn2))

#==============================reto2=============================

def invertirNumero(pnum):
    # Invertir el número de forma iterativa
    numeroInvertido = 0
    while pnum > 0:
        digito = pnum % 10  # Obtener el último dígito
        numeroInvertido = numeroInvertido * 10 + digito  # Construir el número invertido
        pnum = pnum // 10  # Eliminar el último dígito del número original
    return numeroInvertido

def remplazarNumero(pnume, pnume2, pnume3):
    digitosPnum = contarDigitos(pnume)  # Cantidad de dígitos del número a buscar
    divisor = 10 ** digitosPnum  # Potencia de 10 para dividir
    resultado = 0
    multiplicador = 1
    invertido1 = invertirNumero(pnume)  # Invertir el número a buscar
    invertido2 = invertirNumero(pnume2)  # Invertir el número a reemplazar
    invertido3 = invertirNumero(pnume3)  # Invertir el número a reemplazar

    while invertido2 > 0:
        # Extraer los últimos dígitos de invertido para comparar con pnume
        if invertido2 % divisor == invertido1:
            # Si coinciden, agregar pnume3 al resultado
            resultado += invertido3 * multiplicador
            invertido2 //= divisor  # Eliminar los dígitos ya procesados
            multiplicador *= 10 ** contarDigitos(invertido3)  # Ajustar el multiplicador
        else:
            # Si no coinciden, agregar el último dígito de invertido al resultado
            resultado += (invertido2 % 10) * multiplicador
            invertido2 //= 10  # Eliminar el último dígito
            multiplicador *= 10  # Incrementar el multiplicador

    return invertirNumero(resultado)
def remplazarNumeroAUX(pnume,pnume2,pnume3):
    if not isinstance(pnume, int) or not isinstance(pnume2, int) or not isinstance(pnume3, int):
        return "Todos los números deben ser naturales."
    elif pnume < 0 or pnume2 < 0 or pnume3 < 0:
        return "Todos los números deben ser mayores o iguales a 0."
    else:
        return remplazarNumero(pnume,pnume2,pnume3)

def remplazarNumeroES(pnume,pnume2,pnume3):
    try:
        #pnum=int(input("Ingrese el número a buscar: "))
        #pnum2=int(input("Ingrese el numero donde buscar: "))
        #pnum3=int(input("Ingrese el número a reemplazar: "))
        return remplazarNumeroAUX(pnume, pnume2, pnume3)
    except ValueError:
        return "Debe ingresar un número entero"

print("\n=== Remplazar Digitos ===")
pnume= 22
pnume2= 2228
pnume3=4
print("Para la entrada:",pnume,pnume2,pnume3)
print(remplazarNumeroES(pnume,pnume2,pnume3))
pnume= 808
pnume2=980808808
pnume3=25
print("Para la entrada:",pnume,pnume2,pnume3)
print(remplazarNumeroES(pnume,pnume2,pnume3))
pnume= 457
pnume2= 4528457
pnume3=12345
print("Para la entrada:",pnume,pnume2,pnume3)
print(remplazarNumeroES(pnume,pnume2,pnume3))
pnume=123450
pnume2=1234
pnume3=30
print("Para la entrada:",pnume,pnume2,pnume3)
print(remplazarNumeroES(pnume,pnume2,pnume3))
pnume=22
pnume2=2228
pnume3=4.5
print("Para la entrada:",pnume,pnume2,pnume3)
print(remplazarNumeroES(pnume,pnume2,pnume3))
pnume=22
pnume2="0"
pnume3=4
print("Para la entrada:",pnume,pnume2,pnume3)
print(remplazarNumeroES(pnume,pnume2,pnume3))