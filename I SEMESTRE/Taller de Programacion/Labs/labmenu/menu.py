# elaborado por: Matias Benavides y Luis Tinoco

from funciones import *

def textoAux(texto, n, opcion):
    """
    Funcionamiento:
        Compara la ejecución de mostrar un texto n veces de forma iterativa y recursiva, mostrando los resultados y tiempos.
    Entradas:
        - texto: cadena de caracteres a mostrar.
        - n: número de repeticiones.
        - opcion: opción seleccionada del menú.
    Salidas:
        - None. Imprime los resultados y tiempos en pantalla.
    """
    if len(texto) < 3:
        print("El texto debe tener al menos 3 caracteres.")
        return
    elif n <= 0:
        print("El número de repeticiones debe ser mayor que 0.")
        return

    resultadoI, tiempoI, resultadoR, tiempoR = compararTiempos(
        textoIterativo, textoRecursivo, texto, n
    )

    print("algoritmo recursivo:")
    for linea in resultadoR:
        print(linea)
    print(f"Tiempo recursivo: {tiempoR:.6f} segundos\n")

    print("algoritmo iterativo:")
    for linea in resultadoI:
        print(linea)
    print(f"Tiempo iterativo: {tiempoI:.6f} segundos\n")

    diferencia = abs(tiempoI - tiempoR)
    print(f"Diferencia de tiempo: {diferencia:.6f} segundos")
    if tiempoI < tiempoR:
        print("La versión iterativa es más rápida.")
    elif tiempoR < tiempoI:
        print("La versión recursiva es más rápida.")
    else:
        print("Ambas versiones tienen el mismo tiempo.")

def textoES(opcion):
    """
    Funcionamiento:
        Solicita al usuario un texto y un número, y llama a textoAux para mostrar los resultados.
    Entradas:
        - opcion: opción seleccionada del menú.
    Salidas:
        - None. Imprime los resultados en pantalla.
    """
    while True:
        try:
            texto = str(input("Ingrese el texto a mostrar: "))
            n = int(input("Ingrese el número de veces que desea mostrar el texto: "))
            textoAux(texto, n, opcion)
            break
        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")
            continue

def numAux(n, opcion):
    """
    Funcionamiento:
        Ejecuta la función correspondiente (primo, factorial, fibonacci, MCD) según la opción y compara tiempos.
    Entradas:
        - n: número entero ingresado por el usuario.
        - opcion: opción seleccionada del menú.
    Salidas:
        - Tupla con resultados y tiempos de ejecución.
    """
    if n <= 0:
        print("El número debe ser mayor que 0.")
        return None
    if opcion == 2:
        return compararTiempos(esPrimoI, esPrimoR, n)
    elif opcion == 3:
        return compararTiempos(factorialI, factorialR, n)
    elif opcion == 4:
        return compararTiempos(fibonacciI, fibonacciR, n)
    elif opcion == 5:
        a = int(input("Ingrese el primer número para calcular el MCD: "))
        b = int(input("Ingrese el segundo número para calcular el MCD: "))
        return compararTiempos(maximoComunDivisorI, maximoComunDivisorR, a, b)
    return None

def numES(opcion):
    """
    Funcionamiento:
        Solicita al usuario los datos necesarios según la opción y muestra los resultados y tiempos.
    Entradas:
        - opcion: opción seleccionada del menú.
    Salidas:
        - None. Imprime los resultados en pantalla.
    """
    if opcion == 2:
        while True:
            try:
                n = int(input("Ingrese un número para verificar si es primo: "))
                resultadoI, tiempoI, resultadoR, tiempoR = numAux(n, opcion)
                if resultadoI:
                    print(f"Iterativo: {n} es primo.")
                else:
                    print(f"Iterativo: {n} no es primo.")

                if resultadoR:
                    print(f"Recursivo: {n} es primo.")
                else:
                    print(f"Recursivo: {n} no es primo.")
                print(f"Tiempo iterativo: {tiempoI:.6f} segundos")
                print(f"Tiempo recursivo: {tiempoR:.6f} segundos")
                diferencia = abs(tiempoI - tiempoR)
                print(f"Diferencia de tiempo: {diferencia:.6f} segundos")
                if tiempoI < tiempoR:
                    print("La versión iterativa es más rápida.")
                elif tiempoR < tiempoI:
                    print("La versión recursiva es más rápida.")
                else:
                    print("Ambas versiones tienen el mismo tiempo.")
                break
            except ValueError:
                print("Entrada no válida. Por favor, intente de nuevo.")
    elif opcion == 3:
        while True:
            try:
                n = int(input("Ingrese un número para calcular su factorial: "))
                resultadoI, tiempoI, resultadoR, tiempoR = numAux(n, opcion)
                print(f"Iterativo: El factorial de {n} es {resultadoI}.")
                print(f"Recursivo: El factorial de {n} es {resultadoR}.")
                print(f"Tiempo iterativo: {tiempoI:.6f} segundos")
                print(f"Tiempo recursivo: {tiempoR:.6f} segundos")
                diferencia = abs(tiempoI - tiempoR)
                print(f"Diferencia de tiempo: {diferencia:.6f} segundos")
                if tiempoI < tiempoR:
                    print("La versión iterativa es más rápida.")
                elif tiempoR < tiempoI:
                    print("La versión recursiva es más rápida.")
                else:
                    print("Ambas versiones tienen el mismo tiempo.")
                break
            except ValueError:
                print("Entrada no válida. Por favor, intente de nuevo.")
    elif opcion == 4:
        while True:
            try:
                n = int(input("Ingrese un número para calcular su fibonacci: "))
                resultadoI, tiempoI, resultadoR, tiempoR = numAux(n, opcion)
                print(f"Iterativo: El fibonacci de {n} es {resultadoI}.")
                print(f"Recursivo: El fibonacci de {n} es {resultadoR}.")
                print(f"Tiempo iterativo: {tiempoI:.6f} segundos")
                print(f"Tiempo recursivo: {tiempoR:.6f} segundos")
                diferencia = abs(tiempoI - tiempoR)
                print(f"Diferencia de tiempo: {diferencia:.6f} segundos")
                if tiempoI < tiempoR:
                    print("La versión iterativa es más rápida.")
                elif tiempoR < tiempoI:
                    print("La versión recursiva es más rápida.")
                else:
                    print("Ambas versiones tienen el mismo tiempo.")
                break
            except ValueError:
                print("Entrada no válida. Por favor, intente de nuevo.")
    elif opcion == 5:
        while True:
            try:
                resultadoI, tiempoI, resultadoR, tiempoR = numAux(1, opcion)
                print(f"Iterativo: El MCD es {resultadoI}.")
                print(f"Recursivo: El MCD es {resultadoR}.")
                print(f"Tiempo iterativo: {tiempoI:.6f} segundos")
                print(f"Tiempo recursivo: {tiempoR:.6f} segundos")
                diferencia = abs(tiempoI - tiempoR)
                print(f"Diferencia de tiempo: {diferencia:.6f} segundos")
                if tiempoI < tiempoR:
                    print("La versión iterativa es más rápida.")
                elif tiempoR < tiempoI:
                    print("La versión recursiva es más rápida.")
                else:
                    print("Ambas versiones tienen el mismo tiempo.")
                break
            except ValueError:
                print("Entrada no válida. Por favor, intente de nuevo.")

def menu():
    """
    Funcionamiento:
        Muestra el menú principal, recibe la opción del usuario y llama a la función correspondiente.
    Entradas:
        - Ninguna.
    Salidas:
        - None. Controla el flujo principal del programa.
    """
    while True:
        menuTexto = """
        Menú de opciones:
        1. Mostrar texto iterativo
        2. Es primo iterativo.
        3. Factorial i/r
        4. Fibonacci i/r
        5. Máximo común divisor (MCD) i/r
        6.Salir
        """
        print(menuTexto)
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == "1":
            textoES(int(opcion))
        elif opcion in ["2", "3", "4", "5"]:
            numES(int(opcion))
        elif opcion == "6":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida.")

menu()