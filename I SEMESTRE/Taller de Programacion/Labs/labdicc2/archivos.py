# Elaborado por Luis Tinoco y Matias Benavides 
# Fecha de elaboración: 11/05/2025
# Última modificación: 14/05/2025 19:32
# Versión de Python: 3.13.2

import pickle

# Nombre del archivo donde se almacenan los deportes con pickle
DBFILE = "deportes.pkl"

def cargarDeportes() -> dict:
    """
    Carga los deportes almacenados en un archivo pickle y los retorna en un diccionario.
    Si el archivo no existe o está vacío, retorna un diccionario vacío.
    Returns:
        dict: Diccionario con los deportes cargados.
    """
    try:
        with open(DBFILE, "rb") as archivo:
            deportes = pickle.load(archivo)
    except (FileNotFoundError, EOFError):
        deportes = {}
    return deportes

def guardarDeportes(deportes: dict) -> None:
    """
    Guarda el diccionario de deportes en un archivo pickle.
    Args:
        deportes (dict): Diccionario de deportes a guardar.
    """
    with open(DBFILE, "wb") as archivo:
        pickle.dump(deportes, archivo)
