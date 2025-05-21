#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 20/05/2025
#última modificación 20/05/2025 20:00
#python versión 3.13.2
import csv
import pandas as pd
import random
import string
import names
from Lab O_O import personalidad
# Lista para almacenar los miembros 
listaMiembros = []

def crearBaseDatos():
    """
    base de datos en csv con la información de los usuarios
    con las celdas con la siguiente información
    celda1=Nombre completo ("nombre","Apellido1","apellido2")
    celda2=cedula (9 dígitos, el primero no puede ser 0)
    celda3=Categoria y personalidad ([número, string])
    celda4=profesión (string)
    celda5=estado (activo=true, inactivo=false)
    """
    df = pd.DataFrame(columns=["Nombre", "Cedula", "CateYPerso", "Profesion", "Estado"])
    df.to_csv("BaseDatos.csv", index=False)
    print("Base de datos creada exitosamente.")

def insertarMiembro(listaMiembros):
    """
    Función que solicita al usuario el número de personas 
    que tiene el equipo de trabajo y con base a este valor crea los valores
    ficticios de cada uno cumpliendo con los requisitos de la clase.

    nombre: Tupla de 3 valores string (“nombre”, “ap1”, “Ap2”) para el registro del nombre completo ficticio
    cédula: 9 valores numéricos, el primero no puede ser 0
    cateYPerso: lista de 2 valores [número, string] según especificación
    profesión: número de la posición aleatoria de la lista de profesiones
    estado: booleano, True (Activo) o False (Inactivo)
    """
    try:
        cantidadPersonas = int(input("¿Cuántas personas tiene el equipo de trabajo? "))

        listaProfesiones = [
            "Software Developer", "Analyst", "Engineer", "Game designer", "Web designer", "Designer",
            "Game programmer", "Webmaster", "Web developer", "Network administrator", "Software Engineer",
            "Scientist", "Video game developer", "Data Engineer", "Strategist", "Web Application Developer",
            "Java Developer"
        ]
        categoriasPersonalidad = {
            1: "an",  # Analista
            2: "di",  # Diplomático
            3: "ce",  # Centinelas
            4: "ex"   # Exploradores
        }

        nuevosMiembros = []

        for _ in range(cantidadPersonas):
            miembro = personalidad()
            # Nombre ficticio como tupla (nombre, apellido1, apellido2)
            nombreTupla = (names.get_first_name(), names.get_last_name(), names.get_last_name())
            miembro.asignarNombre(nombreTupla)
            # Cédula de 9 dígitos, el primero no puede ser 0
            cedulaAleatoria = str(random.randint(1, 9)) + ''.join([str(random.randint(0, 9)) for _ in range(8)])
            miembro.asignarCedula(cedulaAleatoria)
            # Categoría y personalidad: [número, string]
            categoriaNum = random.randint(1, 4)
            inicialesPersonalidad = categoriasPersonalidad[categoriaNum]
            cateYPerso = [categoriaNum, inicialesPersonalidad]
            miembro.asignarCateYPerso(cateYPerso)
            # Profesión: guardar el número de la posición aleatoria
            profesionIndice = random.randint(0, len(listaProfesiones) - 1)
            miembro.asignarProfesion(profesionIndice)
            # Estado: True (Activo) o False (Inactivo)
            estadoBool = random.choice([True, False])
            miembro.asignarEstado(estadoBool)
            listaMiembros.append(miembro)
            # Para guardar en CSV:
            nombreCompleto = f"{nombreTupla[0]} {nombreTupla[1]} {nombreTupla[2]}"
            profesionNombre = listaProfesiones[profesionIndice]
            estadoStr = "Activo" if estadoBool else "Inactivo"
            cateYPersoStr = f"[{categoriaNum},\"{inicialesPersonalidad}\"]"
            nuevosMiembros.append([nombreCompleto, cedulaAleatoria, cateYPersoStr, profesionNombre, estadoStr])

        # Guardar en memoria secundaria (agregar al CSV)
        try:
            dataFrame = pd.read_csv("BaseDatos.csv")
        except FileNotFoundError:
            dataFrame = pd.DataFrame(columns=["Nombre", "Cedula", "CateYPerso", "Profesion", "Estado"])
        nuevosDataFrame = pd.DataFrame(nuevosMiembros, columns=["Nombre", "Cedula", "CateYPerso", "Profesion", "Estado"])
        dataFrame = pd.concat([dataFrame, nuevosDataFrame], ignore_index=True)
        dataFrame.to_csv("BaseDatos.csv", index=False)

        print("Procesamiento total terminado. Los miembros han sido guardados en BaseDatos.csv.")
    except Exception as error:
        print(f"Ocurrió un error: {error}")