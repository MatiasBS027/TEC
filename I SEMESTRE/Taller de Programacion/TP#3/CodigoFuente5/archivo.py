#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 11/06/2025
#última modificación 21/06/2025 20:00
#python versión 3.13.2


import os
import ast

def leerNombresAnimales():
    """
    Funcionalidad:
    - Lee y retorna una lista con los nombres de animales almacenados en el archivo 'nombresAnimales.txt'.

    Entradas:
    - Ninguna.

    Salidas:
    - Retorna una lista de cadenas con los nombres de animales.
    """
    nombres = []
    if not os.path.exists("nombresAnimales.txt"):
        return nombres
    with open("nombresAnimales.txt", "r", encoding="utf-8") as f:
        for linea in f:
            nombre = linea.strip()
            if nombre != "":
                nombres.append(nombre)
    return nombres

def cargarInventario(archivo="inventario.txt"):
    """
    Funcionalidad:
    - Carga el inventario de animales desde un archivo de texto y lo convierte en una lista de objetos Animal.

    Entradas:
    - archivo: str, nombre del archivo desde donde se cargará el inventario (por defecto 'inventario.txt').

    Salidas:
    - Retorna una lista de objetos Animal con la información cargada del archivo.
    """
    if not os.path.exists(archivo):
        return []
    inventario = []
    with open(archivo, "r", encoding="utf-8") as file:
        for linea in file:
            linea = linea.strip()
            if not linea:
                continue
            try:
                iniNombres = linea.find('(')
                finNombres = linea.find(')')
                nombresStr = linea[iniNombres + 1:finNombres]
                nombresSplit = nombresStr.split(',')
                nombreComun = nombresSplit[0].strip().strip("'")
                nombreCientifico = nombresSplit[1].strip().strip("'")

                iniInfo = linea.find('[', finNombres)
                finInfo = linea.find(']', iniInfo)
                infoStr = linea[iniInfo + 1:finInfo]
                infoSplit = infoStr.split(',')
                estado = int(infoSplit[0].strip().strip("'"))
                calificacion = int(infoSplit[1].strip().strip("'"))
                orden = infoSplit[2].strip().strip("'")
                peso = float(infoSplit[3].strip().strip("'"))

                urlIni = linea.find("'", finInfo)
                urlFin = linea.rfind("'")
                if urlIni != -1 and urlFin != -1 and urlFin > urlIni:
                    url = linea[urlIni + 1:urlFin]
                else:
                    url = ""
                from funciones import Animal  # Importación local para evitar dependencias circulares
                animal = Animal(nombreComun, nombreCientifico, url, orden)
                animal.asignarEstado(estado)
                animal.asignarCalificacion(calificacion)
                animal.asignarOrdenYPeso(orden)
                animal.asignarPeso(peso)
                inventario.append(animal)
            except Exception as error:
                print(f"Error cargando línea: {error}")
                continue
    return inventario

def cargarMostrarInventario():
    """
    Funcionalidad:
    - Carga el inventario desde el archivo 'inventario.txt' y lo retorna como una lista de elementos evaluados.

    Entradas:
    - Ninguna.

    Salidas:
    - Retorna una lista de elementos (listas o diccionarios) obtenidos del archivo.
    """
    inventario = []
    with open("inventario.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                try:
                    elemento = ast.literal_eval(linea)
                    inventario.append(elemento)
                except:
                    print(" Error al leer una línea, se omitió:", linea)
    return inventario