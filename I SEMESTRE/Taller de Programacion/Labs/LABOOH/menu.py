#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creación 24/05/2025
#última actualización 27/05/2025
#python versión 3.13.2

from funciones import *
import csv
from archivo import crearBaseDeDatos, mostrarHerramientas


def obtenerActivas(nombreArchivo):
    idsActivas = set()
    try:
        with open(nombreArchivo, 'r', newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) > 0 and fila[-1].strip().lower() == "activo":
                    idsActivas.add(fila[0].strip())
    except FileNotFoundError:
        pass  # Si no existe el archivo, no hay IDs
    return idsActivas

# ==========================
# ES
# ==========================
def herramientaEs():
    idHerramienta = input("Ingrese el ID de la herramienta: ")
    
    while True:
        metal = input("Ingrese el tipo de metal (oro, diamante, hierro): ").lower()
        if validarMetal(metal):
            break
        print("Metal inválido. Intente de nuevo.")
    
    while True:
        color = input("Ingrese el color (azul, amarillo, gris): ").lower()
        if validarColor(color):
            break
        print("Color inválido. Intente de nuevo.")
    
    return idHerramienta, metal, color

# ==========================
# Crear arma
# ==========================

def crearArmaMenu(baseDatos):
    idsActivas = obtenerActivas(baseDatos)
    
    while True:
        idHerramienta = input("Ingrese el ID de la herramienta: ").strip()
        if idHerramienta in idsActivas:
            print(f"Error: El ID '{idHerramienta}' ya está registrado. Intente otro.")
        else:
            break
    while True:
        metal = input("Ingrese el tipo de metal (oro, diamante, hierro): ").lower()
        if validarMetal(metal):
            break
        print("Metal inválido. Intente de nuevo.")
    while True:
        color = input("Ingrese el color (azul, amarillo, gris): ").lower()
        if validarColor(color):
            break
        print("Color inválido. Intente de nuevo.")
    while True:
        try:
            dano = int(input("Ingrese el daño (7, 8, 9): "))
            if validarDano(dano):
                break
            print("Daño inválido.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    while True:
        try:
            velocidad = float(input("Ingrese la velocidad de ataque (0.1 a 0.3): "))
            if validarVelocidad(velocidad):
                break
            print("Velocidad inválida.")
        except ValueError:
            print("Debe ingresar un número decimal válido.")
    arma = crearArma(idHerramienta, metal, color, dano, velocidad)
    mostrarObjeto(arma)
    guardarEnBaseDatos(baseDatos, arma)

# ==========================
# Crear armadura
# ==========================

def crearArmaduraMenu(baseDatos):
    idsActivas = obtenerActivas(baseDatos)
    while True:
        idHerramienta = input("Ingrese el ID de la herramienta: ").strip()
        if idHerramienta in idsActivas:
            print(f"Error: El ID '{idHerramienta}' ya está registrado. Intente otro.")
        else:
            break
    while True:
        metal = input("Ingrese el tipo de metal (oro, diamante, hierro): ").lower()
        if validarMetal(metal):
            break
        print("Metal inválido. Intente de nuevo.")
    while True:
        color = input("Ingrese el color (azul, amarillo, gris): ").lower()
        if validarColor(color):
            break
        print("Color inválido. Intente de nuevo.")
    while True:
        try:
            defensa = int(input("Ingrese la defensa (4, 5, 6): "))
            if validarDefensa(defensa):
                break
            print("Defensa inválida.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    armadura = crearArmadura(idHerramienta, metal, color, defensa)
    mostrarObjeto(armadura)
    guardarEnBaseDatos(baseDatos, armadura)


# ==========================
# Desgastar arma por ID
# ==========================

def desgastarArma():
    idBuscar = input("Ingrese el ID del arma a desgastar: ")
    if desgastarArmaPorID("BaseDatos.csv", idBuscar):
        print("Desgaste realizado correctamente.")
    else:
        print("No se encontró el arma o ya está eliminada.")

# ==========================
# Eliminar herramienta por ID con confirmación
# ==========================

def eliminarEquipo():
    idBuscar = input("Ingrese el ID del equipo a eliminar: ")
    confirmar = input(f"¿Está seguro que desea eliminar la herramienta con ID {idBuscar}? (s/n): ")
    if confirmar.lower() == 's':
        if eliminarPorID("BaseDatos.csv", idBuscar):
            print("Herramienta eliminada exitosamente.")
        else:
            print("ID no encontrado o ya eliminado.")
    else:
        print("Cancelado por el usuario.")

# ==========================
# Mostrar herramientas por metal
# ==========================

def mostrarPorMetal():
    print("Metales disponibles: oro, diamante, hierro")
    metal = input("Ingrese el metal: ").lower()
    if validarMetal(metal):
        mostrarArmasPorMetal("BaseDatos.csv", metal)
    else:
        print("Metal no válido.")

# ==========================
# Menú principal
# ==========================

def main():
    baseDatos = "BaseDatos.csv"
    try:
        with open(baseDatos, 'r'):
            pass
    except FileNotFoundError:
        crearBaseDeDatos(baseDatos)

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Registrar un arma")
        print("2. Registrar una armadura")
        print("3. Desgastar un arma por ID")
        print("4. Eliminar equipo por ID")
        print("5. Mostrar todas las herramientas")
        print("6. Mostrar armas por metal")
        print("7. Mostrar herramientas eliminadas")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crearArmaMenu(baseDatos)
        elif opcion == "2":
            crearArmaduraMenu(baseDatos)
        elif opcion == "3":
            desgastarArma()
        elif opcion == "4":
            eliminarEquipo()
        elif opcion == "5":
            mostrarTodo(baseDatos)
        elif opcion == "6":
            mostrarPorMetal()
        elif opcion == "7":
            mostrarEliminados("BaseDatos.csv")
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

main()