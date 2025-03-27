# Elaborado por: Matias Benavides Sandoval, Genesis Fajardo y Dorian Vargas
# Fecha de creación: 25/03/2025 9:15am
# Última modificación: 25/03/2025 11:00am
# Python version 3.13

def contarDigitos(pn):
    """
    Funcionamiento: Cuenta los dígitos de una cifra numérica
    Entradas:
    - pn(int): Número entero a contar sus dígitos
    Salidas:
    - contador(int): Cantidad de dígitos que tiene el número
    """
    if pn==0:
        return 1
    contador=0
    while pn!=0:
        contador+=1
        pn//=10
    return contador

def compararNumeros(pn1,pn2):
    """
    Funcionamiento: Compara si dos números son iguales
    Entradas:
    - pn1(int): Primer número a comparar
    - pn2(int): Segundo número a comparar
    Salidas:
    - str: Mensaje indicando si los números son iguales o no
    """
    if pn1==pn2:
        return "Los números son iguales"
    else:
        return "Los números nos son iguales"

def compararNumerosAux(pn1,pn2):
    """
    Funcionamiento: Verifica que los números tengan la misma cantidad de dígitos antes de comparar
    Entradas:
    - pn1(int): Primer número a comparar
    - pn2(int): Segundo número a comparar
    Salidas:
    - str: Mensaje de error o resultado de la comparación
    """
    if contarDigitos(pn1)!=contarDigitos(pn2):
        return "La cantidad dígitos debe ser igual"
    else:
        return compararNumeros(pn1,pn2)

def compararNumerosES(pn1, pn2):
    """
    Funcionamiento: Maneja las entradas y salidas de la comparación de números
    Entradas:
    - pn1(int): Primer número a comparar
    - pn2(int): Segundo número a comparar
    Salidas:
    - str: Mensaje de error o resultado de la comparación
    """
    try:
        return compararNumerosAux(pn1,pn2)
    except ValueError:
        return "Debe ingresar un número entero"

def diferenciaDigitos(num1, num2):
    """
    Funcionamiento: Encuentra los dígitos que están en el primer número pero no en el segundo
    Entradas:
    - num1(int): Primer número para comparar sus dígitos
    - num2(int): Segundo número para comparar sus dígitos
    Salidas:
    - int/str: Número formado por los dígitos diferentes o mensaje si no hay diferencias
    """
    diferencia = 0
    while num1 > 0:
        digito1 = num1 % 10
        existe = 0
        temp = num2
        while temp > 0:
            if temp % 10 == digito1:
                existe = 1
            temp //= 10
        if existe == 0:
            diferencia = diferencia * 10 + digito1
        num1 //= 10
    if diferencia > 0:
        resultado = 0
        while diferencia > 0:
            resultado = resultado * 10 + diferencia % 10
            diferencia //= 10
        return resultado
    else:
        return "Todos los valores fueron eliminados."

def diferenciaDigitosAux(num1, num2):
    """
    Funcionamiento: Valida los datos de entrada para la diferencia de dígitos
    Entradas:
    - num1(int): Primer número a validar
    - num2(int): Segundo número a validar
    Salidas:
    - str/int: Mensaje de error o resultado de la diferencia de dígitos
    """
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return "Debe indicar números enteros."
    if num1 <= 0 or num2 <= 0:
        return "Ambos valores deben ser enteros positivos."
    return diferenciaDigitos(num1, num2)

def diferenciaDigitosES(num1, num2):
    """
    Funcionamiento: Maneja las entradas y salidas de la diferencia de dígitos
    Entradas:
    - num1(int): Primer número a procesar
    - num2(int): Segundo número a procesar
    Salidas:
    - str: Resultado del proceso o mensaje de error
    """
    try:
        resultado = diferenciaDigitosAux(num1, num2)
        if isinstance(resultado, str):
            return resultado
    except ValueError:
        return "Entrada inválida. Por favor, ingresa números enteros."

def rotarIzq(pn):
    """
    Funcionamiento: Rota un número a la izquierda
    Entradas:
    - pn(int): Número a rotar
    Salidas:
    - int: Número rotado a la izquierda
    """
    ultimo=pn%10
    ultimo*=10**(contarDigitos(pn)-1)
    pn//=10
    return ultimo+pn

def rotarIzqAux(pn):
    """
    Funcionamiento: Valida que el número tenga más de 3 dígitos antes de rotar
    Entradas:
    - pn(int): Número a validar y rotar
    Salidas:
    - int/str: Número rotado o mensaje de error
    """
    if contarDigitos(pn)>3:
        return rotarIzq(pn)
    else:
        return "El número debe tener más de tres dígitos"

def rotarIzqES(x):
    """
    Funcionamiento: Maneja las entradas y salidas de la rotación de números
    Entradas:
    - x(str/int): Número a rotar (puede ser string o entero)
    Salidas:
    - int/str: Número rotado o mensaje de error
    """
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