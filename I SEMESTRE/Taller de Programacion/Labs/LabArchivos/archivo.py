import pickle

def guardarEdificio(edificio, nombre_archivo="edificio.pkl"):
    """
    Guarda la matriz del edificio en un archivo binario usando pickle.
    Parámetros:
    - edificio: list[list[int]], matriz de alquileres del edificio
    - nombre_archivo: str, nombre del archivo a guardar
    """
    try:
        with open(nombre_archivo, "wb") as archivo:
            pickle.dump(edificio, archivo)
        return f"El edificio se ha guardado correctamente en {nombre_archivo}."
    except Exception as e:
        return f"Error al guardar el archivo: {e}"

def cargarEdificio(nombre_archivo="edificio.pkl"):
    """
    Carga la matriz del edificio desde un archivo binario usando pickle.
    Parámetros:
    - nombre_archivo: str, nombre del archivo a leer
    Retorna:
    - list[list[int]] si tiene éxito
    - Excepción si no se encuentra el archivo
    """
    with open(nombre_archivo, "rb") as archivo:
        edificio = pickle.load(archivo)
    return edificio