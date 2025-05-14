#Elaborado por Luis Tinoco y Matias Benavides
#Fecha de creación 12/5/2025 07:30
#última modificación 12/5/2025 20:00
#python versión 3.13

#importar librerías
from funciones import *
from archivo import * 

#definición de funciones

def ingresoAlquilerMenu(edificio):
    """
    Funcionamiento:
    - Muestra un menú para calcular ingresos por alquiler según diferentes criterios.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - str: Mensaje con el resultado del cálculo según la opción seleccionada.
    """
    menu = "\n--- Menú de Alquiler ---\n" + \
            "a. Por apartamento\n" + \
            "b. Por piso\n" + \
            "c. Por columna\n" + \
            "d. Por totalidad del edificio\n" + \
            "e. Salir"
    print(menu)
    opcion = input("Seleccione una opción (a-e): ").lower()
    if opcion == "a": 
        return alquilerPorApartamento(edificio)
    if opcion == "b":
        return alquilerPorPiso(edificio)
    if opcion == "c":
        return alquilerPorColumna(edificio)
    if opcion == "d":
        return totalidadEdificio(edificio)
    if opcion == "e":   
        return "Volviendo al menú principal."
    else:
        return "Opción inválida. Intente nuevamente."


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
                resultado = alquilarApartamento(edificio, solicitarValorAlquiler)
                guardarEdificio(edificio)
            elif opcion == "2":
                resultado = modificarRenta(edificio)
                guardarEdificio(edificio)
            elif opcion == "3":
                resultado = desalojar(edificio)
                guardarEdificio(edificio)
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
    archivo = "edificio.pkl"
    try:
        edificio = cargarEdificio(archivo)  # Cargar el edificio desde el archivo pickle
        print("Archivo existente encontrado. Cargando edificio...")
        return menuPrincipal(edificio)  # Si el archivo existe, carga y muestra el menú
    except FileNotFoundError:
        while True:  # Si no se encuentra el archivo, solicita los datos para crear el edificio
            try:
                pisos = int(input("Ingrese el número de pisos del edificio: "))
                apartamentos = int(input("Ingrese el número de apartamentos por piso: "))
                edificio = alquilarAux(pisos, apartamentos)
                if isinstance(edificio, str):
                    return edificio
                else:
                    guardarEdificio(edificio)  # Guardar el edificio recién creado
                    return menuPrincipal(edificio)
            except ValueError:
                print("Debe ingresar un número entero.")

print (alquilerEs())
