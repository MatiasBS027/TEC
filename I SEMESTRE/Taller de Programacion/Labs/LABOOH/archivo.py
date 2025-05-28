#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creación 24/05/2025
#última actualización 24/05/2025
#python versión 3.13.2

import csv

def crearBaseDeDatos(baseDatos):
    """
    Crea una base de datos en formato CSV con los datos de las herramientas.
    BaseDatos: str, nombre del archivo CSV.
    """
    with open(baseDatos, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Durabilidad", "Metal", "Color", "Dano", "Velocidad", "Defensa"])
    print(f"Base de datos '{baseDatos}' creada exitosamente.")
    return baseDatos

def mostrarHerramientas(baseDatos):
    """
    Muestra los datos de una herramienta específica almacenada en la base de datos CSV.
    Solicita el ID al usuario y muestra la información si existe.
    """
    idBuscar = input("Ingrese el ID de la herramienta a buscar: ")
    encontrada = False
    with open(baseDatos, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera
        for row in reader:
            if len(row) == 7 and row[0] == idBuscar:
                idHerramienta = row[0]
                durabilidad = row[1]
                metal = row[2]
                color = row[3]
                dano = row[4]
                velocidad = row[5]
                defensa = row[6]
                if velocidad != '' and defensa == '':
                    print(f"Tipo: Arma | ID: {idHerramienta}, Durabilidad: {durabilidad}, Metal: {metal}, Color: {color}, Daño: {dano}, Velocidad: {velocidad}")
                elif velocidad == '' and defensa != '':
                    print(f"Tipo: Armadura | ID: {idHerramienta}, Durabilidad: {durabilidad}, Metal: {metal}, Color: {color}, Daño: {dano}, Defensa: {defensa}")
                encontrada = True
                break
    if not encontrada:
        print("id no encontrada o incorrecta")