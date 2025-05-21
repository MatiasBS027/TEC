# Elaborado por Luis Tinoco y Matias Benavides
# Fecha de creación: 16/05/2025
# Última modificación: 18/05/2025 20:02
# Python version: 3.13.2

# ==========================
# MÓDULOS PRINCIPALES
# ==========================
import tkinter as tk  # Biblioteca base para la interfaz gráfica
from tkinter import ttk  # Widgets temáticos (mejor apariencia)
from tkinter import messagebox  # Ventanas emergentes para mensajes
import random

# ==========================
# MÓDULOS PARA IMÁGENES (esto se usó principalmente para la estética usando imagenes)
# ==========================
from PIL import ImageTk, Image  # Procesamiento de imágenes (requiere pip install pillow en caso de no tenerlo)
import requests  # Para descargar imágenes desde URLs (requiere pip install requests en caso de no tenerlo)
from io import BytesIO  # Conversión de bytes a imagen 
import urllib.request  # Alternativa para descarga de imágenes
import os  # Manejo de rutas y archivos


def obtenerInfoPokemon(idPoke):
    """
    Obtiene la información del Pokémon de la API.
    Args:
        idPoke: ID del Pokémon
    Returns:
        Diccionario con la información del Pokémon o None si hubo error
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        idApi = datos['id']
        nombre = datos['name']
        esShiny = False
        peso = datos['weight']
        altura = datos['height']
        estadisticas = datos['stats']
        stats = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
        statsValores = []
        for statNombre in stats:
            for stat in estadisticas:
                if stat['stat']['name'] == statNombre:
                    statsValores.append(stat['base_stat'])
                    break
        totalEstats = sum(statsValores)
        statsTupla = tuple(statsValores)  # (PS, A, D, AE, DE, V)
        tipos = []
        for tipo in datos['types']:
            nombreTipo = tipo['type']['name']
            tipos.append(nombreTipo)
        if esShiny:
            urlImagen = datos['sprites']['front_shiny']
        else:
            urlImagen = datos['sprites']['front_default']
        infoPokemon = {
            idApi: [
                nombre,
                (esShiny, peso, altura),
                [totalEstats, statsTupla],
                tipos,
                urlImagen]}
        return infoPokemon
    except Exception as e:
        print(f"Error al obtener info de Pokémon {idPoke}: {e}")
        return None

def construirXML(diccPoke):
    xml = "<Pokemons>\n"
    for idPoke, datos in diccPoke.items():
        nombre = datos[0]
        totalEstad, stats = datos[2]
        xml += f"""  <Pokemon id="{idPoke}">
    <nombre>{nombre}</nombre>
    <totalEstad>{totalEstad}</totalEstad>
    </Pokemon>\n"""
    xml += "</Pokemons>"
    return xml

def escribirXml(archivoXml, contenido):
    """
    Función:
    - Escribe el contenido XML en un archivo.
    Entradas:
    - archivoXml: str, ruta del archivo XML a crear.
    - contenido: str, contenido XML a escribir.
    Salidas:
    - Crea/sobrescribe el archivo XML especificado.
    """
    with open(archivoXml, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

def buscarTxt():
    """
    Lee el archivo MisPokemon.txt y retorna una lista de tuplas (id, nombre)
    solo para los Pokémon que huyeron.
    """
    pokemonesHuidos = []
    try:
        rutaBase = os.path.dirname(os.path.abspath(__file__))
        rutaArchivo = os.path.join(rutaBase, "MisPokemon.txt")
        with open(rutaArchivo, "r", encoding="utf-8") as file:
            for line in file:
                linea = line.strip()
                if linea:
                    partes = linea.split("^")
                    if len(partes) == 3:
                        idPokedex = partes[0].strip()
                        nombre = partes[1].strip()
                        estado = partes[2].strip().lower()
                        if estado == "h":
                            pokemonesHuidos.append((idPokedex, nombre))
                    else:
                        print(f"Línea mal formada: {linea}")
    except FileNotFoundError:
        print("El archivo 'MisPokemon.txt' no existe.")
    return pokemonesHuidos



def crearXML():
    huidos = buscarTxt()
    # Obtener información desde la API
    if huidos:
        diccPokemones = {}
        for idPoke, _ in huidos:
            info = obtenerInfoPokemon(idPoke)
            if info:
                diccPokemones.update(info)
        if diccPokemones:
            xml = construirXML(diccPokemones)
            escribirXml("pokemonesHuidos.xml", xml)
            print("Archivo XML generado correctamente.")
        else:
            print("No se pudo obtener información de los Pokémon.")
    else:
        print("No hay Pokémon que hayan huido.")

crearXML()