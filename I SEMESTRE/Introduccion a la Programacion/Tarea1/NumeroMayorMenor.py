# Elaborado por: Matias Benavides
# Fecha de creacion: 10/3/2025 8:00pm
# Fecha de ultima modificacion: 10/3/2025 8:24pm
# Version de Python: 3.13.2

# Se inicializan las variables
mayor = -100000
menor = 100000
i = 1
n = int(input("Digite la cantidad de números que quiere ingresar: "))
# Se pide al usuario que digite n numeros enteros
while i <= n:
    numero = int(input("Digite un numero entero: "))   
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    i = i + 1

print("El numero mayor es: " + str(mayor) + "\nEl numero menor es: " + str(menor))  # Se imprime el numero mayor y el numero menor
