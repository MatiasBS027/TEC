def obtenerMCM (a, b):
    # Determinamos el mayor entre a y b 
    if a > b:
        mayor = a
    else:
        mayor = b
    mcm = mayor # Empezamos desde el mayor

    while True:
        if mcm % a == 0 and mcm % b == 0:
            return mcm
        mcm += 1  # Probamos el siguiente número

def obtenerMCMAUX (a, b):
    # Asegurarse de que ambos números sean positivos
    if a <= 0 or b <= 0:
        print("Por favor, ingrese números enteros positivos.")
    return obtenerMCM(a, b)  # Llamar a la función para calcular el MCD


def obtenerMCMES ():
    try:
        # Solicitar al usuario que ingrese dos números enteros
        a = int(input("Ingrese el primer número entero: "))
        b = int(input("Ingrese el segundo número entero: "))
        resultado = obtenerMCMAUX(a, b)
        return "El MCM de " + str(a) + " y "+ str(b) + " es: " + str(resultado)
    except ValueError:
        print("Por favor, ingrese números enteros positivos.")

print(obtenerMCMES())