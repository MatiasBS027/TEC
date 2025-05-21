# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 23/03/2025
# Última modificación: 25/03/2025 12:00
# Python version 3.13

#==========================================================================
# Primera Función: Encontrar dígitos mayor y menor
#==========================================================================
def diferenciarvalores(pnum):
    '''
    Funcionamiento: Encuentra el dígito mayor y menor de un número y calcula la diferencia
    Entradas: pnum(int): Número a evaluar
    Salidas: tuple(int,int,int): Dígito mayor, menor y su diferencia
    '''
    numMenor = pnum % 10 
    numMayor = pnum % 10  
    while pnum > 0:
        if pnum % 10 > numMayor:
            numMayor = pnum % 10
        if pnum % 10 < numMenor:
            numMenor = pnum % 10
        pnum = pnum // 10
    diferencia = numMayor - numMenor
    return numMayor, numMenor, diferencia

def diferenciarvaloresAux(pnum):
    '''
    Funcionamiento: Valida los datos de entrada antes de procesarlos
    Entradas: pnum(int): Número a evaluar
    Salidas: tuple/str: Resultado del proceso o mensaje de error
    '''
    if not isinstance(pnum, int):
        return "Debe ingresar un número entero."
    if pnum <= 0:
        return "El número debe ser mayor a 0."
    elif pnum <= 9:  
        return "El número debe poseer al menos dos dígitos."
    return diferenciarvalores(pnum)

def diferenciarvaloresES():
    '''
    Funcionamiento: Maneja las entradas y salidas
    Entradas: None
    Salidas: str: Resultado del proceso o mensaje de error
    '''
    try:
        num = int(input("Digite el número: "))
        resultado = diferenciarvaloresAux(num)
        if isinstance(resultado, str):
            return resultado
        else:
            numMayor, numMenor, diferencia = resultado
            return f"El dígito mayor es: {numMayor}. El dígito menor es: {numMenor}. La diferencia es: {diferencia}."
    except ValueError:
        return "Entrada inválida. Por favor, ingresa un número entero."

#==========================================================================
# Segunda Función: Convertir decimal a octal
#==========================================================================
def convertirOctal(pnum2):
    '''
    Funcionamiento: Convierte un número decimal a octal
    Entradas: pnum2(int): Número decimal a convertir
    Salidas: str: Número en octal
    '''
    octal = ""
    while pnum2 > 0:
        octal = str(pnum2 % 8) + octal
        pnum2 = pnum2 // 8
    return octal

def convertirOctalAux(pnum2):
    '''
    Funcionamiento: Valida los datos de entrada
    Entradas: pnum2(int): Número decimal a convertir
    Salidas: str: Resultado u mensaje de error
    '''
    if not isinstance(pnum2, int):
        return "Debe ingresar un número entero."
    if pnum2 <= 0:
        return "El número debe ser mayor a 0."
    return f"El número en octal es: {convertirOctal(pnum2)}"

def convertirOctalES():
    '''
    Funcionamiento: Maneja las entradas y salidas
    Entradas: None
    Salidas: str: Resultado del proceso o mensaje de error
    '''
    try:
        num2 = int(input("Digite el número decimal: "))
        return convertirOctalAux(num2)
    except ValueError:
        return "Entrada inválida. Por favor, ingresa un número entero."

#==========================================================================
# Tercera Función: Verificar palíndromo
#==========================================================================
def esPalindromo(numero):
    '''
    Funcionamiento: Verifica si un número es palíndromo
    Entradas: numero(int): Número a verificar
    Salidas: str: Mensaje indicando si es palíndromo o no
    '''
    numStr = str(numero)
    inicio = 0
    fin = 0
    for _ in numStr:
        fin += 1
    fin -= 1
    while inicio < fin:
        if numStr[inicio] != numStr[fin]:
            return "El número no es palíndromo."
        inicio += 1
        fin -= 1
    return "El número es palíndromo."

def esPalindromoAux(numero):
    '''
    Funcionamiento: Valida los datos de entrada
    Entradas: numero(int): Número a verificar
    Salidas: str: Mensaje de verificación o error
    '''
    if not isinstance(numero, int):
        return "Debe ingresar un número entero."
    if numero <= 9:
        return "El número debe ser mayor que 9."
    return esPalindromo(numero)

def esPalindromoES():
    '''
    Funcionamiento: Maneja las entradas y salidas
    Entradas: None
    Salidas: str: Resultado del proceso o mensaje de error
    '''
    try:
        numero = int(input("Digite un número: "))
        return esPalindromoAux(numero)
    except ValueError:
        return "Entrada inválida. Por favor, ingresa un número entero."

#==========================================================================
# Cuarta Función: Diferencia de dígitos entre números
#==========================================================================
def diferenciaDigitos(num1, num2):
    '''
    Funcionamiento: Encuentra dígitos presentes en num1 pero no en num2
    Entradas: num1, num2(int): Números a comparar
    Salidas: int/bool: Dígitos únicos o False si no hay
    '''
    num1_str = str(num1)
    num2_str = str(num2)
    resultado = ""
    
    for digito in num1_str:
        if digito not in num2_str and digito not in resultado:
            resultado += digito
            
    return int(resultado) if resultado else False

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

def diferenciaDigitosES():
    '''
    Funcionamiento: Maneja las entradas y salidas
    Entradas: None
    Salidas: str: Resultado del proceso o mensaje de error
    '''
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = diferenciaDigitosAux(num1, num2)
        
        if isinstance(resultado, str):
            return resultado
        elif resultado:
            return f"Dígitos en {num1} pero no en {num2}: {resultado}"
        else:
            return "No hay diferencia de dígitos entre los números."
    except ValueError:
        return "Entrada inválida. Por favor, ingresa números enteros."

#==========================================================================
# Programa Principal
#==========================================================================
if __name__ == "__main__":
    print("\n=== Encontrar dígitos mayor y menor ===")
    print(diferenciarvaloresES())
    
    print("\n=== Convertir a octal ===")
    print(convertirOctalES())
    
    print("\n=== Verificar palíndromo ===")
    print(esPalindromoES())
    
    print("\n=== Diferencia de dígitos ===")
    print(diferenciaDigitosES())