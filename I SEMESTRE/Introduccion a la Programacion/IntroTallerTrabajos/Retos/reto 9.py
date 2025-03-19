# Elaborado por Tinoco Vargas Luis Carlos
# Fecha de creación: 18/03/2025
# Última modificación: 18/03/2025 20:59
# Python version 3.13

def SumarDigitosMultiplos(num, dig):
    """
    Función para sumar los dígitos de un número que son múltiplos de un dígito dado.
    
    Parámetros:
    num (int): El número entero positivo mayor que cero.
    dig (int): El dígito del cual deben ser múltiplos los dígitos a sumar.
    
    Retorna:
    int: La suma de los dígitos que son múltiplos del dígito especificado.
    """
    if num <= 0:
        return "El número debe ser mayor a 0"
    
    suma = 0
    while num > 0:
        digito = num % 10
        if digito % dig == 0:
            suma += digito
        num = num // 10
    return suma

# Solicitar número y dígito al usuario
while True:
    try:
        numero = int(input("Digite un número entero positivo mayor que cero: "))
        if numero <= 0:
            print("El número debe ser mayor que cero.")
            continue
        digito = int(input("Digite el dígito para verificar los múltiplos: "))
        if digito < 0:
            print("El dígito debe ser un número positivo.")
            continue
        break
    except ValueError:
        print("Debe ingresar un número entero válido.")

# Llamar a la función y mostrar el resultado
resultado = SumarDigitosMultiplos(numero, digito)
print("La suma de los dígitos múltiplos de", digito, "es:", resultado)