# Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
# Fecha de creación 20/05/2025
# Última modificación 21/05/2025
# Python versión 3.13.2

#importacion 
from funciones import *
from clase import *
from archivos import *

#funciones
def pedirCantidadMiembros():
    """
    Funcionalidad:
    - Solicita al usuario la cantidad de miembros que desea ingresar al equipo.
    Entradas:
    - Ninguna (usa input internamente).
    Salidas:
    - int: cantidad válida mayor a cero.
    """
    while True:
        try:
            cantidad = int(input("¿Cuántas personas tiene el equipo de trabajo? "))
            if cantidad > 0:
                return cantidad
            else:
                print("Ingrese un número mayor que cero.")
        except ValueError:
            print("Debe ingresar un número válido.")

def pedirCedulaValida(equipo):
    """
    Funcionalidad:
    - Solicita la cédula y verifica que exista en el equipo.
    Entradas:
    - equipo (lista): lista de objetos persona.
    Salidas:
    - str: cédula válida si se encuentra en el equipo.
    - None: si la cédula no es válida o no se encuentra.
    """
    cedula = buscarCedula()
    if not cedula:
        return None
    persona = buscarPersona(equipo, cedula)
    if not persona:
        print(f"No se encontró persona con cédula {cedula}.")
        return None
    return cedula

def pedirNuevoNombre():
    """
    Funcionalidad:
    - Solicita al usuario ingresar un nuevo nombre completo (nombre y dos apellidos).
    Entradas:
    - Ninguna (usa input internamente).
    Salidas:
    - str: nuevo nombre completo ingresado.
    """
    nuevoNombre = input("Ingrese el nuevo nombre completo (nombre apellido1 apellido2): ").strip()
    return nuevoNombre

def manejarInsertarMiembro(equipo):
    """
    Funcionalidad:
    - Maneja el flujo para insertar miembros al equipo solicitando la cantidad y agregándolos.
    Entradas:
    - equipo (lista): lista de objetos persona.
    Salidas:
    - int: cantidad de miembros insertados, o 0 si no se insertó nada.
    """
    cantidad = pedirCantidadMiembros()
    if cantidad <= 0:
        return 0
    insertarMiembro(equipo, cantidad)
    return cantidad

def manejarCambiarNombre(equipo):
    """
    Funcionalidad:
    - Maneja el proceso para cambiar el nombre de un miembro existente solicitando cédula y nuevo nombre.
    Entradas:
    - equipo (lista): lista de objetos persona.
    Salidas:
    - bool: True si el nombre fue cambiado, False si no se cambió o hubo error.
    """
    cedula = pedirCedulaValida(equipo)
    if not cedula:
        return False
    personaEncontrada = buscarPersona(equipo, cedula)
    nombreActual = personaEncontrada.mostrarName()
    nombre = f"{nombreActual[0]} {nombreActual[1]} {nombreActual[2]}"
    print(f"Nombre actual: {nombre}")
    confirmar = input("¿Desea cambiar el nombre completo? (s/n): ").lower()
    if confirmar != 's':
        print("No se realizaron cambios.")
        return False
    nuevoNombre = pedirNuevoNombre()
    cambiarNombre(equipo, cedula, nuevoNombre)
    return True

def manejarEliminarMiembro(equipo):
    """
    Funcionalidad:
    - Maneja la eliminación ficticia de un miembro cambiando su estado a "Inactivo".
    Entradas:
    - equipo (lista): lista de objetos persona.
    Salidas:
    - bool: True si el miembro fue eliminado, False si no se eliminó o hubo error.
    """
    cedula = pedirCedulaValida(equipo)
    if not cedula:
        return False
    personaEncontrada = buscarPersona(equipo, cedula)
    estadoActual = personaEncontrada.mostrarEstado()
    if estadoActual == "Inactivo":
        print("La persona ya está eliminada (estado Inactivo). No es posible eliminarla nuevamente.")
        return False
    confirmar = input("La persona está activa. ¿Desea eliminarla? (s/n): ").lower()
    if confirmar != 's':
        print("No se realizaron cambios.")
        return False
    eliminarMiembro(equipo, cedula)
    return True

def menuReportes(equipo):
    """
    Funcionalidad:
    - Muestra un submenú para reportes con opciones para mostrar información completa, categorías o persona.
    Entradas:
    - equipo (lista): lista de objetos persona.
    Salidas:
    - Ninguna (realiza impresiones y llamadas a funciones auxiliares).
    """
    while True:
        print("""
        --------- MENÚ DE REPORTES---------
        1. Mostrar información completa
        2. Mostrar Categorías
        3. Mostrar persona
        4. Salir al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrarInfoCompleta(equipo)
        elif opcion == "2":
            mostrarCategorias(equipo)
        elif opcion == "3":
            mostrarPersonaPorCedula(equipo)
        elif opcion == "4":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def menuPrincipal():
    """
    Funcionalidad:
    - Muestra el menú principal del programa y permite gestionar el equipo de trabajo.
    Entradas:
    - Ninguna (maneja el flujo principal del programa).
    Salidas:
    - Ninguna (modifica la lista equipo y guarda en archivo).
    """
    equipo = cargarArchivos("equipo.pkl")
    while True:
        print("""
    --------- MENÚ PRINCIPAL ---------
    1. Insertar miembros del equipo
    2. Modificar miembro del equipo
    3. Eliminar miembro del equipo
    4. Reportes de la aplicación
    5. Salir
    """)
        opcion = input("Seleccione una opción: ")
        try:
            if opcion == "1":
                manejarInsertarMiembro(equipo)
            elif opcion == "2":
                manejarCambiarNombre(equipo)
            elif opcion == "3":
                manejarEliminarMiembro(equipo)
                print()
            elif opcion == "4":
                menuReportes(equipo)
            elif opcion == "5":
                print("Saliendo del programa. ¡Hasta luego!")
                guardarArchivo(equipo)
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")


menuPrincipal()
