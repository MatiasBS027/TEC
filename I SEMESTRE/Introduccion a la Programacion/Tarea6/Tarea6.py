# Elaboraddo por: Matias Benavides Sandoval, Genesis Fajardo y Dorian Vargas
# Fecha de creación: 25/03/2025
# Última modificación: 25/03/2025
# Python version 3.13

def contarDigitos(pn): #Función para determinar la cantidad de digitos
    """
    Funcionamiento: Cuenta los dígitos de una cifra.
    Entradas:
    - pn(int): La cifra numérica.
    Salidas:
    - contador(int): La cantidad de dígitos de la cifra.
    """
    if pn==0:
        return 1
    contador=0
    while pn!=0:
        contador+=1
        pn//=10
    return contador #Retorna la cantidad de digitos

def compararNumeros(pn1,pn2): #Función para comparar dos números
    if pn1==pn2:
        return  "Los números son iguales"
    else:
        return "Los números nos son iguales"

def compararNumerosAux(pn1,pn2): #Función para comparar dos números
    if contarDigitos(pn1)!=contarDigitos(pn2): #Se compara la cantidad de digitos de ambos números
        return"La cantidad dígitos debe ser igual"
    else:
        return compararNumeros(pn1,pn2)

def compararNumerosES():
    try:
        numero1=int(input("Ingrese el primer número: "))
        numero2=int(input("Ingrese el segundo número: "))
        return compararNumerosAux(numero1,numero2)
    except ValueError:
        return "Debe ingresar un número entero"

print(compararNumerosES()) #Se imprime el resultado de la función compararNumerosES

