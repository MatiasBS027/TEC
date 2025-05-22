#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 20/05/2025
#última modificación 20/05/2025 20:00
#python versión 3.13.2

import pickle

def guardarArchivo(equipo):
    """
    Guarda la matriz del edificio en un archivo binario usando pickle.
    Parámetros:
    - edificio: list[list[int]], matriz de alquileres del edificio
    - nombre_archivo: str, nombre del archivo a guardar
    """
    nombreArchivo="equipo.pkl"
    try:
        with open(nombreArchivo, "wb") as archivo:
            pickle.dump(equipo, archivo)
        return f"El equipo de trabajo se creó y guardó en {nombreArchivo}."
    except Exception as e:
        return f"Error al guardar el archivo: {e}"

def cargarArchivos(nombreArchivo):
    """
    Carga la matriz del edificio desde un archivo binario usando pickle.
    Parámetros:
    - nombre_archivo: str, nombre del archivo a leer
    Retorna:
    - list[list[int]] si tiene éxito
    - Excepción si no se encuentra el archivo
    """
    try:
        with open(nombreArchivo, "rb") as archivo:
            equipo = pickle.load(archivo)
        return equipo
    except FileNotFoundError:
        return []  # Retorna una lista vacía si no existe el archivo
    except Exception as e:
        print(f"Error al cargar archivo: {e}")
        return []
    
