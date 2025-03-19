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

# Código principal para probar las funciones
try:
# Prueba Reto 6
    print("\n=== Reto 6: Dígito Mayor ===")
    numeroReto6 = input("Digite un número sin letras: ")
    if numeroReto6.isdigit():
        print(validarEntrada(int(numeroReto6)))
    else:
        print("El valor debe ser únicamente entero")

    # Prueba Reto 7
    print("\n=== Reto 7: Potencia ===")
    baseReto7 = int(input("Digite la base: "))
    exponenteReto7 = int(input("Digite el exponente: "))
    print(calcularPotencia(baseReto7, exponenteReto7))

    # Prueba Reto 8
    print("\n=== Reto 8: Número Primo ===")
    numeroReto8 = int(input("Digite un número: "))
    print(esNumeroPrimo(numeroReto8))

    # Prueba Reto 9
    print("\n=== Reto 9: Suma de Múltiplos ===")
    numeroReto9 = int(input("Digite un número entero positivo: "))
    digitoReto9 = int(input("Digite el dígito para verificar múltiplos: "))
    print(f"La suma de los dígitos múltiplos de {digitoReto9} es: {sumarDigitosMultiplos(numeroReto9, digitoReto9)}")

    # Prueba Reto 10
    print("\n=== Reto 10: Verificar Binario ===")
    numeroReto10 = int(input("Digite un número para verificar si es binario: "))
    if esNumeroBinario(numeroReto10):
        print("El número ES binario")
    else:
        print("El número NO es binario")

    # Prueba Reto 11
    print("\n=== Reto 11: Convertir Binario a Decimal ===")
    numeroBinarioReto11 = input("Digite un número binario: ")
    if all(digito in '01' for digito in numeroBinarioReto11):
        resultado = convertirBinarioADecimal(numeroBinarioReto11)
        print(f"El número binario {numeroBinarioReto11} en decimal es: {resultado}")
    else:
        print("Por favor ingrese un número binario válido (solo 0s y 1s)")

except ValueError as e:
    print("Por favor ingrese valores numéricos válidos")