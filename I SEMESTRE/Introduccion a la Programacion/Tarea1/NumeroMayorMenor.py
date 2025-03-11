# Elaborado por: Matias Benavides
# Fecha de creacion: 10/3/2025 8:00pm
# Fecha de ultima modificacion: 10/3/2025 8:24pm
# Version de Python: 3.13.2

# Se inicializan las variables
mayor = -100000
menor = 100000
i = 1

while i <= 12:
    numero = int(input("Digite un numero entero: "))   # Se pide al usuario que digite un numero entero
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    i = i + 1

print("El numero mayor es: " + str(mayor) + "\nEl numero menor es: " + str(menor))  # Se imprime el numero mayor y el numero menor
