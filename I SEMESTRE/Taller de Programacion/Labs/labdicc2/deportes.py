# Elaborado por Luis Tinoco y Matias Benavides 
# Fecha de elaboración: 11/05/2025
# Última modificación: 14/05/2025 19:32
# Versión de Python: 3.13.2

print ("""\n
=========================
Módulo de gestión de deportes
=========================
""")

from archivos import *
from funciones import *

# Carga los deportes almacenados desde un archivo externo.
deportes = cargarDeportes()

def submenuBusquedas() -> None:
    """
    Muestra un submenú para realizar búsquedas y consultas sobre los deportes registrados.
    Permite:
    1. Ver todos los deportes activos.
    2. Buscar un deporte por su código.
    3. Buscar deportes por lugar.
    4. Listar deportes eliminados.
    5. Regresar al menú principal.
    """
    while True:
        print("\nSubmenú de Búsquedas")
        print("1. Información completa de todos los deportes")
        print("2. Información de un deporte por código")
        print("3. Deportes según lugar")
        print("4. Lista de deportes eliminados")
        print("5. Regresar al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            # Muestra todos los deportes activos
            activos = {c: d for c, d in deportes.items() if d['estado']}
            if not activos:
                print("Aún no se han agregados nuevos deportes.")
            else:
                for codigo, datos in activos.items():
                    print(f"{codigo} - {datos['nombre']} (Activo)")
        elif opcion == "2":
            # Busca un deporte por su código si está activo
            if not deportes:
                print("Aún no se han agregados nuevos deportes.")
            else:
                codigo = input("Ingrese el código del deporte: ").strip()
                if codigo in deportes and deportes[codigo]['estado']:
                    datos = deportes[codigo]
                    print(f"Código: {codigo}\nNombre: {datos['nombre']}\nExplicación: {datos['explicacion']}\nLugar: {datos['lugar']}\nEstado: Activo")
                else:
                    print("Deporte no encontrado o está inactivo.")
        elif opcion == "3":
            # Busca deportes activos por lugar
            lugar = input("Ingrese el lugar a buscar: ").strip()
            encontrados = {c: d for c, d in deportes.items() if lugar.lower() in d['lugar'].lower() and d['estado']}
            if encontrados:
                for codigo, datos in encontrados.items():
                    print(f"{codigo} - {datos['nombre']} (Activo)")
            else:
                print(f"No existe deportes registrados por el TEC en el lugar {lugar} que usted especifica.")
        elif opcion == "4":
            # Lista los deportes eliminados (inactivos)
            eliminados = [d for d in deportes.values() if not d['estado']]
            if eliminados:
                for codigo, datos in deportes.items():
                    if not datos['estado']:
                        print(f"{codigo} - {datos['nombre']} (Eliminado)")
            else:
                print("Todavía no existe deportes eliminados.")
        elif opcion == "5":
            # Regresa al menú principal
            break
        else:
            print("Opción no válida.")

def menuPrincipal():
    """
    Muestra el menú principal del sistema de gestión de deportes.
    Permite:
    1. Registrar un nuevo deporte.
    2. Modificar el nombre de un deporte existente.
    3. Eliminar (desactivar) un deporte.
    4. Acceder al submenú de búsquedas.
    5. Salir del programa.
    """
    while True:
        print("\nMenú Principal")
        print("1. Registrar deporte")
        print("2. Modificar nombre de un deporte")
        print("3. Eliminar un deporte")
        print("4. Submenú de búsquedas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrarDeporte(deportes)
        elif opcion == "2":
            modificarDeporte(deportes)
        elif opcion == "3":
            eliminarDeporte(deportes)
        elif opcion == "4":
            submenuBusquedas()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

menuPrincipal()