#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creación 24/05/2025
#última actualización 24/05/2025
#python versión 3.13.2

from funciones import *
import csv
from archivo import crearBaseDeDatos, mostrarHerramientas

# ==========================
# ES
# ==========================
def herramientaEs():
    idHerramienta = input("Ingrese el ID de la herramienta: ")
    
    while True:
        metal = input("Ingrese el tipo de metal (oro, diamante, hierro): ")
        if validarMetal(metal):
            break
        print("Metal inválido. Intente de nuevo.")
    
    while True:
        color = input("Ingrese el color (azul, amarillo, gris): ")
        if validarColor(color):
            break
        print("Color inválido. Intente de nuevo.")
    
    return idHerramienta, metal, color

# ==========================
# Crear arma
# ==========================

def crearArmaMenu():
    while True:
        try:
            idHerramienta, metal, color = herramientaEs()
            
            while True:
                try:
                    dano = int(input("Ingrese el daño (7, 8, 9): "))
                    if validarDano(dano):
                        break
                    else:
                        print("Daño inválido. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un número entero válido.")
            
            while True:
                try:
                    velocidad = float(input("Ingrese la velocidad de ataque (0.1 a 0.3): "))
                    if validarVelocidad(velocidad):
                        break
                    else:
                        print("Velocidad inválida. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un número decimal válido.")
            
            arma = crearArma(idHerramienta, metal, color, dano, velocidad)
            mostrarObjeto(arma)
            guardarEnBaseDatos("BaseDatos.csv", arma)  # Guardar en base de datos
            break  # salir del ciclo si se creó exitosamente
        except ValueError as error:
            print(f"Error: {error}. Intente de nuevo.\n")

# ==========================
# Crear armadura
# ==========================

def crearArmaduraMenu():
    while True:
        try:
            idHerramienta, metal, color = herramientaEs()
            
            while True:
                try:
                    defensa = int(input("Ingrese la defensa (4, 5, 6): "))
                    if validarDefensa(defensa):
                        break
                    else:
                        print("Defensa inválida. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un número entero válido.")
            
            armadura = crearArmadura(idHerramienta, metal, color, defensa)
            mostrarObjeto(armadura)
            guardarEnBaseDatos("BaseDatos.csv", armadura)  # Guardar en base de datos
            break  # salir del ciclo si se creó exitosamente
        except ValueError as error:
            print(f"Error: {error}. Intente de nuevo.\n")

# ==========================
# Submenú de búsqueda
# ==========================
"""
se agregó este submenú de busqueda por decisión de los estudiantes ya que las instrucciones no solicitaban
que se mostrara de esta forma la información sin embargo se consideró que es más practico y mejor
"""
def subMenuBusqueda(baseDatos):
    while True:
        print("\n=== SUBMENÚ DE BÚSQUEDA ===")
        print("1. Búsqueda por tipo (arma/armadura)")
        print("2. Búsqueda por ID")
        print("3. Mostrar todas")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("1. Mostrar armas")
            print("2. Mostrar armaduras")
            tipo = input("Seleccione el tipo: ")
            with open(baseDatos, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                encontrado = False
                if tipo == "1":
                    print("\n--- ARMAS ---")
                    for row in reader:
                        if len(row) == 7 and row[5] != '' and row[6] == '':
                            print(f"Tipo: Arma | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Daño: {row[4]}, Velocidad: {row[5]}")
                            encontrado = True
                    if not encontrado:
                        print("No hay armas registradas.")
                elif tipo == "2":
                    print("\n--- ARMADURAS ---")
                    for row in reader:
                        if len(row) == 7 and row[5] == '' and row[6] != '':
                            print(f"Tipo: Armadura | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Daño: {row[4]}, Defensa: {row[6]}")
                            encontrado = True
                    if not encontrado:
                        print("No hay armaduras registradas.")
                else:
                    print("Opción inválida.")
        
        elif opcion == "2":
            idBuscar = input("Ingrese el ID de la herramienta a buscar: ")
            encontrada = False
            with open(baseDatos, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) == 7 and row[0] == idBuscar:
                        if row[5] != '' and row[6] == '':
                            print(f"Tipo: Arma | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Daño: {row[4]}, Velocidad: {row[5]}")
                        elif row[5] == '' and row[6] != '':
                            print(f"Tipo: Armadura | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Daño: {row[4]}, Defensa: {row[6]}")
                        encontrada = True
                        break
            if not encontrada:
                print("id no encontrada o incorrecta")
        
        elif opcion == "3":
            armas = []
            armaduras = []
            with open(baseDatos, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) == 7 and row[5] != '' and row[6] == '':
                        armas.append(row)
                    elif len(row) == 7 and row[5] == '' and row[6] != '':
                        armaduras.append(row)
            print("\n--- ARMAS ---")
            if armas:
                for row in armas:
                    print(f"Tipo: Arma | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Daño: {row[4]}, Velocidad: {row[5]}")
            else:
                print("No hay armas registradas.")
            print("\n--- ARMADURAS ---")
            if armaduras:
                for row in armaduras:
                    print(f"Tipo: Armadura | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Daño: {row[4]}, Defensa: {row[6]}")
            else:
                print("No hay armaduras registradas.")
        
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# ==========================
# Función principal
# ==========================

def main():
    # Crear la base de datos solo si no existe
    baseDatos = "BaseDatos.csv"
    try:
        with open(baseDatos, 'r'):
            pass
    except FileNotFoundError:
        crearBaseDeDatos(baseDatos)

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Crear arma")
        print("2. Crear armadura")
        print("3. Buscar herramientas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crearArmaMenu()
        elif opcion == "2":
            crearArmaduraMenu()
        elif opcion == "3":
            subMenuBusqueda(baseDatos)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

main()

