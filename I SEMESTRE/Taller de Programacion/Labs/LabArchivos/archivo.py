import csv

def guardarEdificioCSV(edificio, nombre_archivo="edificio.csv"):
    """
    Guarda la matriz del edificio en un archivo CSV.
    
    Parámetros:
    - edificio: list[list[int]], matriz de alquileres del edificio
    - nombre_archivo: str, nombre del archivo a guardar
    """
    with open(nombre_archivo, mode="w", newline="") as archivo:
        writer = csv.writer(archivo)
        for fila in edificio:
            writer.writerow(fila)


def cargarEdificioCSV(nombre_archivo="edificio.csv"):
    """
    Carga la matriz del edificio desde un archivo CSV.

    Parámetros:
    - nombre_archivo: str, nombre del archivo a leer

    Retorna:
    - list[list[int]], matriz del edificio
    """
    edificio = []
    with open(nombre_archivo, mode="r") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            edificio.append([int(valor) for valor in fila])
    return edificio
