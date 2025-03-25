# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 25/03/2025
# Última modificación: 25/03/2025 12:00
# Python version 3.13

def diferenciaDigitos(num1, num2):
    """
    Determina los dígitos que están en num1 pero no en num2 sin usar listas ni len().
    
    :param num1: int, primer número.
    :param num2: int, segundo número.
    :return: int o bool, número con los dígitos únicos de num1 o False si no hay diferencia.
    """
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return "Debe indicar números enteros."

    if num1 <= 0 or num2 <= 0:
        return "Ambos valores deben ser enteros positivos."

    num1_str = str(num1)
    num2_str = str(num2)
    
    resultado = ""
    indice = 0
    largoNum1 = 0

    for _ in num1_str:  # Contar la cantidad de dígitos de num1
        largoNum1 += 1

    while indice < largoNum1:
        digito = num1_str[indice]
        encontrado = False
        for d in num2_str:
            if digito == d:
                encontrado = True
                break
        if not encontrado:
            repetido = False
            for r in resultado:
                if digito == r:
                    repetido = True
                    break
            if not repetido:
                resultado += digito
        indice += 1

    if resultado == "":
        return False
    else:
        return int(resultado)

def solicitarNumero(mensaje):
    """
    Solicita un número entero positivo al usuario, asegurando que no sea una cadena con comillas.
    
    :param mensaje: str, mensaje para la solicitud.
    :return: int, número ingresado por el usuario.
    """
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():  # Verifica que la entrada sea solo números y no tenga comillas
            valor = int(entrada)
            if valor > 0:
                return valor
            else:
                print("El número debe ser positivo. Inténtelo de nuevo.")
        else:
            print("Debe indicar números enteros.")

# Programa principal
num1 = solicitarNumero("Ingrese el primer número: ")
num2 = solicitarNumero("Ingrese el segundo número: ")

resultado = diferenciaDigitos(num1, num2)
if resultado:
    print("Dígitos en", num1, "pero no en", num2, ":", resultado)
else:
    print("No hay diferencia de dígitos entre los dos números.")
