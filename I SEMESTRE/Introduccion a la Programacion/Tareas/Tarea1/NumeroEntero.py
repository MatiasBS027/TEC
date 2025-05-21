# Elaborado por: Matias Benavides
# Fecha de creacion: 10/3/2025 7:00pm
# Fecha de ultima modificacion: 10/3/2025 7:15pm
# Version de Python: 3.13.2

numeroEntero= int(input("Digite un numero entero: "))   #Se pide al usuario que digite un numero entero
if numeroEntero>0:  
    print("El numero "+ str(numeroEntero) +" es positivo" )   #Se imprime el numero entero y se dice que es positivo
else:
    if numeroEntero==0:
        print("El numero "+ str(numeroEntero) +" es nulo" )   #Se imprime el numero entero y se dice que es nulo
    else:
        print("El numero "+ str(numeroEntero) +" es negativo" )   #Se imprime el numero entero y se dice que es negativo
