# Elaborado por Tinoco Vargas Luis Carlos
# Fecha de creación: 18/03/2025
# Última modificación: 18/03/2025 21:13
# Python version 3.13

def esBinario(numero):
    """
    Función para determinar si una cifra numérica es binaria.
    
    Parámetros:
    numero (int): La cifra numérica a evaluar.
    
    Retorna:
    bool: True si la cifra es binaria, False si no lo es.
    """
    while numero > 0:
        digito = numero % 10
        if digito != 0 and digito != 1:
            return False
        numero = numero // 10
    return True

# Solicitar número al usuario
while True:
    try:
        entrada = input("Digite un valor numérico: ")
        if not entrada.isdigit():
            print("El valor debe ser únicamente entero.")
            continue
        numero = int(entrada)
        break
    except ValueError:
        print("El valor debe ser únicamente entero.")

# Determinar si es binario y mostrar el resultado
if esBinario(numero):
    print("El valor es binario")
else:
    print("El valor NO es binario")