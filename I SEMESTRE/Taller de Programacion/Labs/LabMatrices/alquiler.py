#Elaborado por Luis Tinoco y Matias Benavides
#Fecha de creación 2/5/2025 07:30
#última modificación 2/5/2025 20:00
#python versión 3.13

#importar librerías
from funciones import *

#definición de funciones
def menuPrincipal(edificio):
    """
    Funcionamiento:
    - Muestra un menú principal con opciones para gestionar el alquiler de apartamentos en un edificio.
    - Permite al usuario seleccionar una opción y ejecuta la función correspondiente.
    Entradas:
    - edificio: dict o estructura que representa el estado del edificio (pisos, apartamentos, etc.).
    Salidas:
    - str: Mensaje de despedida si el usuario selecciona la opción de salir.
    - Imprime mensajes en consola indicando el resultado de las operaciones seleccionadas.
    """
    while True:        
        try:
            menu = "\n--- Menú Principal ---\n" + \
                    "1. Alquilar apartamento\n" + \
                    "2. Modificar Renta\n" + \
                    "3. Desalojar\n" + \
                    "4. Indicar ingreso por alquiler\n" + \
                    "5. Reporte total del edificio\n" + \
                    "6. Salir"
            print(menu)
            opcion = input("Seleccione una opción (1-6): ")
            if opcion == "1":
                resultado = alquilarApartamento(edificio)
            elif opcion == "2":
                resultado = modificarRenta(edificio)
            elif opcion == "3":
                resultado = desalojar(edificio)
            elif opcion == "4":
                resultado = ingresoAlquilerMenu(edificio)
            elif opcion == "5":
                resultado = reporteTotalEdificio(edificio)
            elif opcion == "6":
                return "Gracias por usar el sistema. ¡Hasta luego!"
            else:
                resultado = "Opción inválida. Intente nuevamente."
            print(resultado)
        except ValueError:
            print("Debe ingresar un número entero.")


def alquilerEs():
    """
    Funcionamiento:
    - Solicita al usuario el número de pisos y apartamentos por piso para inicializar un edificio.
    - Llama a la función `menuPrincipal` para gestionar las operaciones del edificio.
    Entradas:
    - Ninguna entrada directa, pero solicita al usuario ingresar el número de pisos y apartamentos por consola.
    Salidas:
    - str: Mensaje de error si la inicialización del edificio falla.
    - str: Mensaje de despedida al finalizar el programa.
    - Imprime mensajes en consola indicando errores o resultados de las operaciones.
    """
    while True:
        try:
            pisos = int(input("Ingrese el número de pisos del edificio: "))
            apartamentos = int(input("Ingrese el número de apartamentos por piso: "))
            edificio = alquilarAux(pisos, apartamentos)
            if isinstance(edificio, str):
                return edificio
            else:
                resultado = menuPrincipal(edificio)
                return resultado
        except ValueError:
            print("Debe ingresar un número entero.")
        
print (alquilerEs())
