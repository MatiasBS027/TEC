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
    cedula = buscarCedula()
    if not cedula:
        return None
    persona = buscarPersona(equipo, cedula)
    if not persona:
        print(f"No se encontró persona con cédula {cedula}.")
        return None
    return cedula

def pedirNuevoNombre():
    nuevoNombre = input("Ingrese el nuevo nombre completo (nombre apellido1 apellido2): ").strip()
    return nuevoNombre

def manejarInsertarMiembro(equipo):
    cantidad = pedirCantidadMiembros()
    insertarMiembro(equipo, cantidad)

def manejarCambiarNombre(equipo):
    cedula = pedirCedulaValida(equipo)
    if not cedula:
        return
    personaEncontrada = buscarPersona(equipo, cedula)
    nombreActual = personaEncontrada.mostrarName()
    nombre = f"{nombreActual[0]} {nombreActual[1]} {nombreActual[2]}"
    print(f"Nombre actual: {nombre}")
    confirmar = input("¿Desea cambiar el nombre completo? (s/n): ").lower()
    if confirmar != 's':
        print("No se realizaron cambios.")
        return
    nuevoNombre = pedirNuevoNombre()
    cambiarNombre(equipo, cedula, nuevoNombre)

def manejarEliminarMiembro(equipo):
    cedula = pedirCedulaValida(equipo)
    if not cedula:
        return
    personaEncontrada = buscarPersona(equipo, cedula)
    estadoActual = personaEncontrada.mostrarEstado()
    if estadoActual == "Inactivo":
        print("La persona ya está eliminada (estado Inactivo). No es posible eliminarla nuevamente.")
        return
    confirmar = input("La persona está activa. ¿Desea eliminarla ficticiamente? (s/n): ").lower()
    if confirmar != 's':
        print("No se realizaron cambios.")
        return
    eliminarMiembro(equipo, cedula)


def menuReportes(equipo):
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
