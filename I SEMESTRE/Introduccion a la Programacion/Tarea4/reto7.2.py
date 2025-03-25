# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 20/03/2025
# Última modificación: 22/03/2025 22:59
# Python version 3.13
'''
    Invierte un número entero positivo.

    Esta función toma un número entero positivo como entrada y devuelve
    el número invertido. El proceso se realiza de forma iterativa, 
    extrayendo los dígitos del número original y construyendo el número invertido.

    Parámetros:
    pnum (int): Número entero positivo a invertir.

    Retorna:
    int: El número invertido.
    '''
def invertirNumero(pnum):
    # Invertir el número de forma iterativa
    numeroInvertido = 0
    while pnum > 0:
        digito = pnum % 10  # Obtener el último dígito
        numeroInvertido = numeroInvertido * 10 + digito  # Construir el número invertido
        pnum = pnum // 10  # Eliminar el último dígito del número original
    return numeroInvertido


try:
    num=int(input("Digite un número: ")) 
    if num <= 0:
        print("El número debe ser mayor a 0.")
    elif num <=9:
        print("El número debe poseer al menos dos dígitos.")
    else:
        print("El número invertido es:", invertirNumero(num))
except ValueError:
    print("Debe ingresar únicamente un número entero válido.")