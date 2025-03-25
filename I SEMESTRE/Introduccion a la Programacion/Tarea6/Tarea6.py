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


def compararNumerosES(pn1, pn2):
    try:
        #pn1=int(input("Ingrese el primer número: "))
        #pn2=int(input("Ingrese el segundo número: "))
        return compararNumerosAux(pn1,pn2)
    except ValueError:
        return "Debe ingresar un número entero"\



def diferenciaDigitos(num1, num2):
    """
    Retorna los dígitos que están en el primer número pero no en el segundo.
    Si no existe diferencia, retorna False.
    """
    diferencia = 0
    while num1 > 0:
        digito1 = num1 % 10  # Obtiene el último dígito de numero1
        existe = 0
        temp = num2
        # Comprobamos si el dígito de numero1 está en numero2
        while temp > 0:
            if temp % 10 == digito1:
                existe = 1  # Si se encuentra el dígito, cambia a 1
            temp //= 10
        # Si no se encuentra, se agrega el dígito a la diferencia
        if existe == 0:
            diferencia = diferencia * 10 + digito1
        
        num1 //= 10  # Elimina el último dígito de numero1
    # Si hay una diferencia, la retornamos; si no, retornamos False
    if diferencia > 0:
        resultado = 0
        while diferencia > 0:
            resultado = resultado * 10 + diferencia % 10
            diferencia //= 10
        return resultado
    else:
        return "Todos los valores fueron eliminados."

def diferenciaDigitosAux(num1, num2):
    '''
    Funcionamiento: Valida los datos de entrada
    Entradas: num1, num2(int): Números a comparar
    Salidas: str/int: Mensaje de error o resultado
    '''
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return "Debe indicar números enteros."
    if num1 <= 0 or num2 <= 0:
        return "Ambos valores deben ser enteros positivos."
    return diferenciaDigitos(num1, num2)

def diferenciaDigitosES(num1, num2):
    '''
    Funcionamiento: Maneja las entradas y salidas
    Entradas: None
    Salidas: str: Resultado del proceso o mensaje de error
    '''
    try:
        #num1 = int(input("Ingrese el primer número: "))
        #num2 = int(input("Ingrese el segundo número: "))
        resultado = diferenciaDigitosAux(num1, num2)
        
        if isinstance(resultado, str):
            return resultado
    except ValueError:
        return "Entrada inválida. Por favor, ingresa números enteros."

def rotarIzq(pn):
    ultimo=pn%10
    ultimo*=10**(contarDigitos(pn)-1)
    pn//=10
    return ultimo+pn

def rotarIzqAux(pn):
    if contarDigitos(pn)>3:
        return rotarIzq(pn)
    else:
        return "El número debe tener más de tres dígitos"

def rotarIzqES(x):
    try:
        if isinstance(x, str):
            x = int(x)
        return rotarIzqAux(x)
    except ValueError:
        return "Debe ingresar un número entero"

print("\n=== Comparar numeros ===")
pn1= 123
pn2= 34456 
print("Para la entrada:",pn1,pn2)
print(compararNumerosES(pn1,pn2))
pn1= 4356
pn2= 4356
print("Para la entrada:",pn1,pn2)
print(compararNumerosES(pn1,pn2))
pn1= 6987
pn2= 5987
print("Para la entrada:",pn1,pn2)
print(compararNumerosES(pn1,pn2))
pn1= 0
pn2= 0 
print("Para la entrada:",pn1,pn2)
print(compararNumerosES(pn1,pn2))

print("\n=== Diferencia de digitos ===")
num1 = 24375
num2 = 345
print("Para la entrada:",num1,num2)
print(diferenciaDigitosAux(num1, num2))
num1 = 12
num2 = 21
print("Para la entrada:",num1,num2)
print(diferenciaDigitosAux(num1, num2))
num1 = 234
num2 = 987
print("Para la entrada:",num1,num2)
print(diferenciaDigitosAux(num1, num2))



print("\n=== Rotar numero a la izquierda ===")
x="432"
print("Para la entrada:",x)
print(rotarIzqES(x))
x=432
print("Para la entrada:",x)
print(rotarIzqES(x))
x=4321
print("Para la entrada:",x)
print(rotarIzqES(x))
x=10000
print("Para la entrada:",x)
print(rotarIzqES(x))
x=100001
print("Para la entrada:",x)
print(rotarIzqES(x))