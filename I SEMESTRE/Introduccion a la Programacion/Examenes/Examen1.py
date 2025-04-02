#Elaborado por:: Matias Benavides
def esPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def contarDigitos(num):
    contador = 0
    while num > 0:
        num //= 10
        contador += 1
    return contador

#----------------------Reto 1----------------------
def obtenerValores(pnum1, pnum2, pnum3):
    nCifra = 0  # Lo tuve que inicializar fuera del ciclo
    cifra = pnum1//(10**(pnum2-1))
    muliplicador = 0
    if pnum3 == 0:
        while cifra > 0: 
            if esPar(cifra%10) == True:
                nCifra += (cifra%10)*10**muliplicador
                muliplicador += 1
            cifra //= 10
    else:
        while cifra > 0: 
            if esPar(cifra%10) == False:
                nCifra += (cifra%10)*10**muliplicador
                muliplicador += 1
            cifra //= 10
    return nCifra
def obtenerDigitosAUX(pnum1, pnum2, pnum3):
    if type(pnum1) != int or type(pnum2) != int or type(pnum3) != int: 
        return "Todos los valores deben ser enteros positivos."
    #Tuve que agregar estas lineas de cogido ya que en el examen no senecesitaba por que la validacion se hacia con el try except de las entradas y salidas
    elif contarDigitos(pnum1) < 3:
        return "La cifra de analisis debe ser un entero mayor o igual a 3 dígitos."
    elif pnum2 <=0: #Agregue el igual a 0
        return "Debe ingresar una posicion superior o igual a 1."
    elif pnum3 != 0 and pnum3 != 1: #Lo tuve que cambiar de or a and
        return "Solo es posible extraer pares e impares: 0 o 1."
    elif  pnum2 > contarDigitos(pnum1):
        return "La cifra numerica no posee esa cantidad de digitos."
    else:
        return obtenerValores(pnum1, pnum2, pnum3)

def obtenerDigitosES(pnum1, pnum2, pnum3):
    try:
        #pnum1 = int(input("Ingrese una cifra a analizar: "))
        #pnum2 = int(input("Ingrese la posicion del digito a extraer: "))
        #pnum3 = int(input("Ingrese 0 para extraer pares o 1 para extraer impares: "))
        return obtenerDigitosAUX(pnum1, pnum2, pnum3)
    except ValueError: 
        return "Todos los valores deben ser enteros positivos."
    
print("\n=== Obtener Valores ===")
pnum1= "78"
pnum2= 5
pnum3= 1
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 78
pnum2= "5"
pnum3= 1
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 78
pnum2= 5
pnum3= "1"
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 78
pnum2= 5
pnum3= 1
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 12345678
pnum2= 0
pnum3= 1
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 12345678
pnum2= 4
pnum3= 2
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 678
pnum2= 5
pnum3= 1
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 12345678
pnum2= 4
pnum3= 1
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 12345678
pnum2= 4
pnum3= 0
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 2345678
pnum2= 2
pnum3= 1
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))
pnum1= 345678
pnum2= 1
pnum3= 0
print("Para la entrada:",(pnum1,pnum2,pnum3))
print(obtenerDigitosES(pnum1,pnum2,pnum3))

#----------------------Reto 2----------------------
def esSubConjunto(pnum1, pnum2):
    while pnum1 > 0:
        valor = False
        temp = pnum1 % 10
        pnum2Temp = pnum2 #Lo tuve que agregar para guardar el valor original de pnum2

        while pnum2Temp > 0:
            if temp == pnum2Temp % 10:
                valor = True
            pnum2Temp //= 10 #Lo tuve que sacar del else ya que no seguia el flujo del ciclo

        if valor == False:
            return valor 
        else:
            pnum1 //= 10
        
    return valor

def esSubConjuntoAUX(pnum1, pnum2):
    if pnum1 < 0 or pnum2 < 0:
        return "Ambos valores deben ser mayores a 0."
    else:
        return esSubConjunto(pnum1, pnum2)

print("\n=== Es Sub-Conjunto ===")
pnum1= 915
pnum2= 241593
print("Para la entrada:",(pnum1,pnum2))
print(esSubConjuntoAUX(pnum1,pnum2))
pnum1= 89
pnum2= 12345678
print("Para la entrada:",(pnum1,pnum2))
print(esSubConjuntoAUX(pnum1,pnum2))
pnum1= 6421
pnum2= 12345678
print("Para la entrada:",(pnum1,pnum2))
print(esSubConjuntoAUX(pnum1,pnum2))
pnum1= 1
pnum2= 2345678
print("Para la entrada:",(pnum1,pnum2))
print(esSubConjuntoAUX(pnum1,pnum2))
pnum1= 1
pnum2= -10
print("Para la entrada:",(pnum1,pnum2))
print(esSubConjuntoAUX(pnum1,pnum2))

#----------------------Reto 3----------------------
def obtenerSecuencias(num):
    i = 1
    resultado = 0 #Tuve que inicializar resultado
    while i <= num:
        resultado+= (i+1)/num**2
        i += 1
    return resultado

def obtenerSecuenciasAUX(num):
    if num <= 0:
        return "El valor del numero debe ser mayor a 0."
    else:
        return obtenerSecuencias(num)

def obtenerSecuenciasES(num):
    try:
        #num = int(input("Ingrese un numero entero positivo: "))
        return obtenerSecuenciasAUX(num)
    except ValueError:
        return "El valor del numero."

print("\n=== Obtener Secuencia ===")
num= 0
print("Para la entrada:",(num))
print(obtenerSecuenciasES(num))
num= 2
print("Para la entrada:",(num))
print(obtenerSecuenciasES(num))
num= 6
print("Para la entrada:",(num))
print(obtenerSecuenciasES(num))
num= 8
print("Para la entrada:",(num))
print(obtenerSecuenciasES(num))