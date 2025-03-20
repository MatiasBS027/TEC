# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 18/03/2025
# Última modificación: 18/03/2025 19:48
# Python version 3.13

#Reto#6
def determinarDigitoMayor(pNumero):
    """
    Determina el dígito más grande en un número entero.
    Entrada:
        pNumero (int): Número entero positivo a evaluar
    Salida:
        int: El dígito más grande encontrado
        str: Mensaje de error si la entrada no es válida
    """
    if not isinstance(pNumero, int):
        return "El valor debe ser únicamente entero"
    digitoMaximo = 0
    while pNumero != 0:
        digito = pNumero % 10
        if digito > digitoMaximo:
            digitoMaximo = digito
        pNumero = pNumero // 10
    return digitoMaximo

def validarEntrada(pNumero):
    """
    Valida que la entrada sea un número entero positivo.
    Entrada:
        pNumero (int): Número a validar
    Salida:
        str/int: Mensaje de error o resultado de determinarDigitoMayor
    """
    if not isinstance(pNumero, int):
        return "Debe ingresar un número entero"
    elif pNumero <= 0:
        return "Debe ingresar un número mayor a 0"
    else:
        return determinarDigitoMayor(pNumero)

#Reto#7
def calcularPotencia(pBase, pExponente):
    """
    Calcula la potencia de un número.
    Entrada:
        pBase (int): Base de la potencia
        pExponente (int): Exponente al cual elevar la base
    Salida:
        int: Resultado de la operación
    """
    if pBase < 0 or pExponente < 0:
        return "La base y el exponente deben ser mayor o igual a cero"
    return pBase ** pExponente

#Reto#8
def esNumeroPrimo(pNumero):
    """
    Determina si un número es primo.
    Entrada:
        pNumero (int): Número a evaluar
    Salida:
        str: Mensaje indicando si el número es primo o no
    """
    if pNumero <= 1:
        return "El número debe ser mayor a 1"
    elif pNumero == 2:
        return "El número es primo"
    else:
        for i in range(2, int(pNumero**0.5) + 1):
            if pNumero % i == 0:
                return "El número no es primo"
        return "El número es primo"

#Reto#9
def sumarDigitosMultiplos(pNumero, pDigito):
    """
    Suma los dígitos de un número que son múltiplos de otro dígito.
    Entrada:
        pNumero (int): Número a evaluar sus dígitos
        pDigito (int): Dígito para verificar múltiplos
    Salida:
        int/str: Suma de los dígitos múltiplos o mensaje de error
    """
    if pNumero <= 0:
        return "El número debe ser mayor a 0"
    
    sumaTotal = 0
    while pNumero > 0:
        digito = pNumero % 10
        if digito % pDigito == 0:
            sumaTotal += digito
        pNumero = pNumero // 10
    return sumaTotal

#Reto#10
def esNumeroBinario(pNumero):
    """
    Verifica si un número está compuesto solo por 0s y 1s.
    Entrada:
        pNumero (int): Número a verificar
    Salida:
        bool: True si es binario, False si no lo es
    """
    while pNumero > 0:
        digito = pNumero % 10
        if digito != 0 and digito != 1:
            return False
        pNumero = pNumero // 10
    return True

#Reto#11
def convertirBinarioADecimal(pNumeroBinario):
    """
    Convierte un número binario a decimal.
    Entrada:
        pNumeroBinario (str): Número binario en formato string
    Salida:
        int: Número decimal equivalente
    """
    valorDecimal = 0
    potencia = len(pNumeroBinario) - 1
    
    for digito in pNumeroBinario:
        if digito == '1':
            valorDecimal += (2 ** potencia)
        potencia -= 1
    return valorDecimal

def determinarDigitoMayorAUX(pNumero):
    """
    Función auxiliar para validar entrada del Reto 6
    """
    try:
        if not pNumero.isdigit():
            return "El valor debe ser únicamente entero"
        numero = int(pNumero)
        if numero <= 0:
            return "El número debe ser mayor a 0"
        return determinarDigitoMayor(numero)
    except ValueError:
        return "Error en la entrada"

def calcularPotenciaAUX(pBase, pExponente):
    """
    Función auxiliar para validar entrada del Reto 7
    """
    try:
        base = int(pBase)
        exponente = int(pExponente)
        if base < 0 or exponente < 0:
            return "Los valores deben ser positivos"
        return calcularPotencia(base, exponente)
    except ValueError:
        return "Error: Ingrese solo números"

def esNumeroPrimoAUX(pNumero):
    """
    Función auxiliar para validar entrada del Reto 8
    """
    try:
        numero = int(pNumero)
        if numero <= 1:
            return "El número debe ser mayor a 1"
        return esNumeroPrimo(numero)
    except ValueError:
        return "Error: Ingrese un número válido"

def sumarDigitosMultiplosAUX(pNumero, pDigito):
    """
    Función auxiliar para validar entrada del Reto 9
    """
    try:
        numero = int(pNumero)
        digito = int(pDigito)
        if numero <= 0:
            return "El número debe ser mayor a 0"
        if digito <= 0:
            return "El dígito debe ser mayor a 0"
        return sumarDigitosMultiplos(numero, digito)
    except ValueError:
        return "Error: Ingrese solo números"

def esNumeroBinarioAUX(pNumero):
    """
    Función auxiliar para validar entrada del Reto 10
    """
    try:
        numero = int(pNumero)
        if numero < 0:
            return "El número debe ser positivo"
        return "El número ES binario" if esNumeroBinario(numero) else "El número NO es binario"
    except ValueError:
        return "Error: Ingrese un número válido"

def convertirBinarioADecimalAUX(pBinario):
    """
    Función auxiliar para validar entrada del Reto 11
    """
    if not pBinario:
        return "Error: Ingrese un número"
    if not all(digito in '01' for digito in pBinario):
        return "Error: Ingrese solo números binarios (0 y 1)"
    return convertirBinarioADecimal(pBinario)

# Modificar el código principal para usar las nuevas funciones AUX
print("\n=== Reto 6: Dígito Mayor ===")
numeroReto6 = input("Digite un número sin letras: ")
print(determinarDigitoMayorAUX(numeroReto6))

print("\n=== Reto 7: Potencia ===")
baseReto7 = input("Digite la base: ")
exponenteReto7 = input("Digite el exponente: ")
print(calcularPotenciaAUX(baseReto7, exponenteReto7))

print("\n=== Reto 8: Número Primo ===")
numeroReto8 = input("Digite un número: ")
print(esNumeroPrimoAUX(numeroReto8))

print("\n=== Reto 9: Suma de Múltiplos ===")
numeroReto9 = input("Digite un número entero positivo: ")
digitoReto9 = input("Digite el dígito para verificar múltiplos: ")
print(sumarDigitosMultiplosAUX(numeroReto9, digitoReto9))

print("\n=== Reto 10: Verificar Binario ===")
numeroReto10 = input("Digite un número para verificar si es binario: ")
print(esNumeroBinarioAUX(numeroReto10))

print("\n=== Reto 11: Convertir Binario a Decimal ===")
numeroBinarioReto11 = input("Digite un número binario: ")
resultado = convertirBinarioADecimalAUX(numeroBinarioReto11)
if isinstance(resultado, int):
    print(f"El número binario {numeroBinarioReto11} en decimal es: {resultado}")
else:
    print(resultado)