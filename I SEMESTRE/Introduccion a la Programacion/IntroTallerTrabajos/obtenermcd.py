def obtenerMCD(num1, num2):
    # Calcular el MCD utilizando el algoritmo de Euclides
    while num2 != 0:
        temp = num2  # Guardar el valor de num2 en una variable temporal
        num2 = num1 % num2  # Calcular el nuevo valor de num2 como el residuo de num1 dividido por num2
        num1 = temp  # Asignar el valor de num2 a num1
    # Mostrar el resultado
    return num1


def obtenerMCDAUX(num1,num2):    # Asegurarse de que ambos números sean positivos
    if num1 <= 0 or num2 <= 0:
        print("Por favor, ingrese números enteros positivos.")
    return obtenerMCD(num1, num2)  # Llamar a la función para calcular el MCD
def obtenerMCDES():
    try:# Solicitar al usuario que ingrese dos números enteros
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        resutado =  obtenerMCDAUX(num1, num2)
        return "El MCD de " + str(num1) + " y "+ str(num2) + " es: " + str(resutado)
    except ValueError:
        print("Por favor, ingrese números enteros positivos.")
print(obtenerMCDES())
