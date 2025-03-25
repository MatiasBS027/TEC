# Elaborado por Tinoco Vargas Luis Carlos y Matias Benavides Sandoval
# Fecha de creación: 20/03/2025
# Última modificación: 20/03/2025 9:44
# Python version 3.13

def obtenerSumatoria(n):
    if n <= 0:
        return "El número debe ser mayor a 0"
    
    sumatoria = 0
    for i in range(1, n + 1):
        sumatoria += i**2  # Suma el cuadrado de cada número desde 1 hasta n
    
    return sumatoria

# Manejo de entrada con validación
while True:
    try:
        n = int(input("Digite un número entero mayor a 0: "))
        if n <= 0:
            print("El número debe ser mayor a 0.")
        else:
            print("La sumatoria de los cuadrados es:", obtenerSumatoria(n))
    except ValueError:
        print("Debe ingresar únicamente un número entero válido.")
    