# Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
# Fecha de creación: 11/06/2025
# Última modificación: 21/06/2025 21:15
# Python versión 3.11.2

from clase import Animal  # Importar la clase Animal desde el archivo clase.py
from archivo import *   
import tkinter as tk            # Se usa para la interfaz gráfica
from tkinter import messagebox  # Se usa para mostrar mensajes emergentes al usuario
import os                       # Se usa para verificar si existe un archivo y manejar rutas del sistema
import random                      # Se usa para generar valores aleatorios (estado, peso, ID)
import google.generativeai as genai  # Se usa para configurar la API de Gemini
from google.generativeai import GenerativeModel  # Se usa para crear un modelo generativo como 'gemini-pro'
from PIL import Image, ImageTk  # Se usa para manejar imágenes
# puede ser necesario usar 'pip install -U google-generativeai' para actualizar la biblioteca gemini v1
import json
import ast
import io
import urllib.request
import time
import csv
import ast

#=======================1. obtener lista =========================
"""
    instrucciones:Programe lo necesario para que Gemini pida a Wikipedia n nombres comunes de animales y 
se guarden en un archivo .txt 
Por ejemplo, puedo pedir traiga 475 nombres comunes. Desde interfaz gráfica, solicite al 
usuario cuántos desea, cree una ventana funcional según su iniciativa.  

Si analiza los botones habilitados e inhabilitados, notará que sólo 1 vez se van a pedir la 
información de los animales a Gemini.  
    """

def validarCantidadAux(cantidadTexto):
    """
    Funcionalidad:
    - Valida que la cantidad ingresada sea un número entero positivo.

    Entradas:
    - cantidadTexto: str, texto ingresado por el usuario.

    Salidas:
    - Retorna una tupla (bool, int/str). Si es válido, True y el número; si no, False y mensaje de error.
    """
    try:
        cantidad = int(cantidadTexto)
        if cantidad <= 0:
            return False, "Debe ingresar un número mayor a 0."
        return True, cantidad
    except ValueError:
        return False, "Por favor, ingrese un número válido."
"""
        #====== Función central: pedir nombres a Gemini=======================
import google.generativeai as genai
from google.generativeai import GenerativeModel"""

def obtenernombresAnimales(cantidad):
    """
    Funcionalidad:
    - Solicita a Gemini una lista de nombres comunes de animales y la retorna.

    Entradas:
    - cantidad: int, cantidad de nombres a solicitar.

    Salidas:
    - Retorna una lista de nombres de animales (str).
    """
    try:
        genai.configure(api_key="AIzaSyDVce9ynQYkU--tTfEiIwP9_BqjDAr9-tI")
        modelo = GenerativeModel('gemini-2.0-flash')  # ← cambio aqui el modelo usado (depende el que se use puede dar error)

        prompt = (f"Proporcióname una lista exactamente de {cantidad} nombres comunes de animales en español, uno por línea, sin numeración ni explicaciones."
                "(no me des nombres muy generales como 'mono', 'Gamba', 'ballena', 'gato', 'lagartija' o cosas que no espeficiquen a un animal en particular).\n\n")
        respuesta = modelo.generate_content(prompt)
        
        texto = respuesta.text.strip()
        nombres = []
        for linea in texto.split("\n"):
            nombre = linea.strip("•-•1234567890. ").strip()
            if nombre:
                nombres.append(nombre)
                
        if len(nombres) < cantidad:
            raise Exception(f"Solo se obtuvieron {len(nombres)} nombres de los {cantidad} solicitados")
            
        return nombres[:cantidad]

    except Exception as e:
        raise Exception(f"Error al obtener lista de animales: {str(e)}")

def obtenerListaES(cantidadTexto, ventana):
    """
    Funcionalidad:
    - Obtiene la cantidad de nombres de animales desde la interfaz, los guarda en un archivo y cierra la ventana.

    Entradas:
    - cantidadTexto: str, cantidad de nombres a obtener.
    - ventana: objeto Tkinter, ventana a cerrar al finalizar.

    Salidas:
    - No retorna valor. Guarda los nombres en archivo y muestra mensajes en la interfaz.
    """
    # Verificar si el archivo ya existe
    if os.path.exists("nombresAnimales.txt"):
        messagebox.showinfo("Información", "El archivo de lista de animales ya existe y no se puede sobrescribir.") #esto al final no es tan necesario porque el botón se desactiva si existe
        return

    # Validar la cantidad
    try:
        cantidad = int(cantidadTexto)
        if cantidad <= 0:
            messagebox.showerror("Error", "La cantidad debe ser un número positivo.")
            return
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido.")
        return

    # Obtener los nombres
    try:
        nombres = obtenernombresAnimales(cantidad)
        
        # Guardar en archivo
        with open("nombresAnimales.txt", "w", encoding="utf-8") as archivo:
            for nombre in nombres:
                archivo.write(nombre + "\n")
                
        messagebox.showinfo("Éxito", f"Se han guardado {len(nombres)} nombres de animales en 'nombresAnimales.txt'")
        
        # Mostrar en consola (opcional)
        print("Nombres obtenidos:")
        for i, nombre in enumerate(nombres, 1):
            print(f"{i}. {nombre}")
        
        ventana.destroy()  

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener la lista de animales: {str(e)}")

#=======================2. Crear Inventario =========================

def seleccionarNombresAleatorios(nombres, cantidad):
    """
    Funcionalidad:
    - Selecciona una cantidad de nombres aleatorios de una lista.

    Entradas:
    - nombres: lista de str, nombres disponibles.
    - cantidad: int, cantidad a seleccionar.

    Salidas:
    - Retorna una lista de nombres seleccionados.
    """
    if len(nombres) < cantidad:
        return []
    seleccionados = random.sample(nombres, cantidad)
    return seleccionados

def pedirDatosAnimalAGemini(nombreComun):
    """
    Funcionalidad:
    - Solicita a Gemini los datos de un animal específico en formato JSON.

    Entradas:
    - nombreComun: str, nombre común del animal.

    Salidas:
    - Retorna un diccionario con los datos del animal.
    """
    reintentos=3
    espera=10
    prompt = (
        f"Dame la siguiente información del animal '{nombreComun}' en español, "
        "en formato JSON con las claves: nombre_cientifico, url_imagen(formato de png), orden. "
        "El orden debe ser 'c' para carnívoro, 'h' para herbívoro, 'o' para omnívoro. "
        "Ejemplo: {\"nombre_cientifico\": \"Panthera leo\", \"url_imagen\": \"https://...\", \"orden\": \"c\"}")
    genai.configure(api_key="AIzaSyDVce9ynQYkU--tTfEiIwP9_BqjDAr9-tI")
    modelo = GenerativeModel('gemini-2.0-flash')
    for intento in range(reintentos):
        try:
            respuesta = modelo.generate_content(prompt)
            texto = respuesta.text.strip()
            # Extraer JSON 
            inicio = texto.find('{')
            fin = texto.rfind('}')
            if inicio != -1 and fin != -1 and fin > inicio:
                jsonTexto = texto[inicio:fin+1]
                if texto.strip().startswith('['):
                    try:
                        lista = json.loads(texto)
                        if isinstance(lista, list) and len(lista) > 0:
                            return lista[0]
                    except Exception:
                        pass  
                    primerObjeto = texto[texto.find('{'):texto.find('}')+1]
                    return json.loads(primerObjeto)
                else:
                    return json.loads(jsonTexto)
            else:
                print(f"Respuesta inesperada de Gemini para '{nombreComun}': {texto}")
                raise ValueError("No se encontró JSON válido en la respuesta de Gemini.")
        except Exception as e:
            if "429" in str(e) or "límite" in str(e).lower():
                print(f"Límite alcanzado, esperando {espera} segundos antes de reintentar...")
                time.sleep(espera)
            else:
                raise e
    raise RuntimeError("Has superado el límite de peticiones de Gemini. Intenta más tarde.")

def crearAnimal(nombreComun, datos):
    """
    Funcionalidad:
    - Crea un objeto Animal usando los datos proporcionados.

    Entradas:
    - nombreComun: str, nombre común del animal.
    - datos: dict, datos del animal (nombre científico, url, orden).

    Salidas:
    - Retorna un objeto Animal.
    """
    nombreCientifico = datos.get("nombre_cientifico", "Desconocido")
    urlImagen = datos.get("url_imagen", "")
    orden = datos.get("orden", "o")
    animal = Animal(nombreComun, nombreCientifico, urlImagen, orden)
    return animal

def crearInventarioDesdeInterfaz(ventana):
    """
    Funcionalidad:
    - Crea un inventario de 20 animales seleccionados aleatoriamente y lo guarda en archivo.

    Entradas:
    - ventana: objeto Tkinter, ventana principal para mostrar mensajes.

    Salidas:
    - Retorna la lista de objetos Animal creados.
    """
    nombres = leerNombresAnimales()
    if len(nombres) < 20:
        messagebox.showerror("Error", "No hay suficientes nombres en el archivo.")
        return

    seleccionados = seleccionarNombresAleatorios(nombres, 20)
    print("Nombres seleccionados para el inventario:")
    for nombre in seleccionados:
        print(nombre)

    inventario = []
    for nombre in seleccionados:
        try:
            datos = pedirDatosAnimalAGemini(nombre)
            animal = crearAnimal(nombre, datos)
            inventario.append(animal)
            time.sleep(2)  # Espera para evitar sobrecargar la API
        except Exception as e:
            print(f"Error obteniendo datos de '{nombre}': {e}")
            animal = Animal(nombre, "Desconocido", "", "o")
            inventario.append(animal)

    guardarInventario(inventario)  # Guardar en archivo
    messagebox.showinfo("Éxito", "Inventario de 20 animales creado correctamente.")
    return inventario

def guardarInventario(inventario, archivo="inventario.txt"):
    """
    Funcionalidad:
    - Guarda el inventario de animales en un archivo de texto.

    Entradas:
    - inventario: lista de objetos Animal.
    - archivo: str, nombre del archivo destino.

    Salidas:
    - No retorna valor. Escribe los datos en el archivo.
    """
    with open(archivo, "w", encoding="utf-8") as f:
        for animal in inventario:
            nombres = animal.obtenerNombres()
            info = [
                animal.obtenerEstado(),
                animal.obtenerCalificacion(),
                animal.obtenerOrdenYPeso()[0],
                animal.obtenerOrdenYPeso()[1]]
            url = animal.obtenerUrl()
            f.write(f"{[nombres, info, url]}\n")

#=======================3. Mostrar inventario =========================


# Diccionario que asocia estados específicos con imágenes locales
# Sirve para mostrar una imagen apropiada cuando el animal no tiene una URL válida
imagenesPorEstado = {
    2: "ambulancia.jpg",     # Enfermo
    3: "ambulancia.jpg",     # Trasladado
    4: "museo.jpg",          # Muerto en museo
    5: "calavera.jpg"        # Muerto
}


def cargarImagen(desdeUrlOArchivo):
    """
    Esta función intenta cargar una imagen desde una URL o desde un archivo local.
    Si es desde una URL, hace una petición HTTP y lee la imagen desde los datos binarios (lo investigué pero entendí poco sobre el funcionamiento).
    En ambos casos, la imagen se redimensiona a 120x120 y se convierte en un objeto
    que Tkinter puede mostrar (ImageTk.PhotoImage).
    Si ocurre un error (como una URL inválida o archivo no encontrado), se muestra el error
    en la consola y se retorna None.
    """
    try:
        if desdeUrlOArchivo.startswith("http"):
            # Si la imagen viene de internet, se hace una solicitud HTTP con headers
            req = urllib.request.Request(
                desdeUrlOArchivo,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req) as respuesta:
                datosImagen = respuesta.read()
            imagen = Image.open(io.BytesIO(datosImagen))  # Convertimos los datos en imagen
        else:
            # Si la imagen está en el equipo local
            imagen = Image.open(desdeUrlOArchivo)

        imagenRedimensionada = imagen.resize((120, 120))
        imagenConvertida = ImageTk.PhotoImage(imagenRedimensionada)
        return imagenConvertida

    except Exception as e:
        print(f"Error cargando imagen desde {desdeUrlOArchivo}: {e}")
        return None


def cargarMostrarInventario():
    """
    Lee el archivo 'inventario.txt' y convierte cada línea en una estructura de datos válida usando ast.literal_eval.
    Retorna una lista con todos los animales registrados.
    """
    lista = []
    try:
        with open("inventario.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                try:
                    animal = ast.literal_eval(linea.strip())  # Convierte el texto a lista/tupla
                    lista.append(animal)
                except Exception as e:
                    print(f"[ERROR] Línea inválida en inventario.txt:\n{linea.strip()}\n{e}")
    except FileNotFoundError:
        print("[ERROR] El archivo 'inventario.txt' no fue encontrado.")
    return lista

def mostrarInventarioES():
    """
    Esta función abre una ventana para mostrar el inventario de animales.
    Cada animal se muestra en una tarjeta con su imagen, nombre, familia, estado y emojis para calificar.
    Se permite navegar entre páginas (de 4 animales por página) con botones.
    La imagen se elige según el estado o la URL, y los emojis permiten calificar al animal.
    """

    # Diccionario para convertir valores numéricos de estado en palabras comprensibles
    estadoTexto = {
        1: "Vivo",
        2: "Enfermo",
        3: "Trasladado",
        4: "Muerto en museo",
        5: "Muerto"
    }

    listaAnimales = cargarMostrarInventario()  # Carga todos los animales del inventario
    paginaMostrada = [0]  # Usamos una lista para que el valor pueda cambiar dentro de funciones anidadas

    # Creamos la ventana emergente
    ventana = tk.Toplevel()
    ventana.title("Mostrar inventario")
    ventana.geometry("600x500")

    # Marco principal donde se colocarán los animales
    marcoPrincipal = tk.Frame(ventana)
    marcoPrincipal.pack(pady=10)

    def mostrarPagina():
        """
        Esta función muestra los animales correspondientes a la página actual.
        Cada animal se representa visualmente con su imagen, nombre, familia y estado.
        También se incluyen botones de emoji para calificar al animal.
        """
        # Limpiamos la vista anterior antes de mostrar la nueva página
        for widget in marcoPrincipal.winfo_children():
            widget.destroy()

        inicio = paginaMostrada[0] * 4
        final = inicio + 4
        animalesEnPagina = []

        # Se seleccionan hasta 4 animales para esta página
        for i in range(inicio, final):
            if i < len(listaAnimales):
                animalesEnPagina.append(listaAnimales[i])

        # Para cada animal, creamos un marco visual con su información
        for posicion, animal in enumerate(animalesEnPagina):
            nombres = animal[0]      # ['Nombre común', 'Familia']
            datos = animal[1]        # [estado, calificación, orden, peso]
            enlaceImagen = animal[2] # URL o ruta de imagen

            estado = int(datos[0])
            calificacion = datos[1]
            orden = datos[2]
            peso = datos[3]

            # Se crea un "cuadro" para cada animal
            cuadroAnimal = tk.Frame(marcoPrincipal, bd=2, relief="groove")
            fila = posicion // 2
            columna = posicion % 2
            cuadroAnimal.grid(row=fila, column=columna, padx=10, pady=10)

            # --- CARGA DE IMAGEN ---
            imagen = None
            # Si está vivo y tiene imagen en URL válida, se intenta cargar desde internet
            if estado == 1 and enlaceImagen.strip() != "" and enlaceImagen.strip().lower() != "none":
                imagen = cargarImagen(enlaceImagen)
                if imagen is None:
                    print(f"[INFO] Imagen desde URL falló para '{nombres[0]}'")
                    imagen = cargarImagen("imagen-no-disponible.png")
            else:
                # Si no tiene URL válida, se carga según el estado del animal
                imagenLocal = imagenesPorEstado.get(estado, "calavera.jpg")
                if os.path.exists(imagenLocal):
                    imagen = cargarImagen(imagenLocal)
                else:
                    print(f"[ADVERTENCIA] Imagen local no encontrada: {imagenLocal}")
                    imagen = cargarImagen("imagen-no-disponible.png")

            # Se muestra la imagen si se cargó correctamente
            if imagen:
                etiquetaImagen = tk.Label(cuadroAnimal, image=imagen)
                etiquetaImagen.image = imagen  # Esto es necesario para que la imagen no se borre
                etiquetaImagen.pack()

            # Mostramos texto con la información del animal
            tk.Label(cuadroAnimal, text=nombres[0], font=("Arial", 10, "bold")).pack()  # Nombre común
            tk.Label(cuadroAnimal, text=nombres[1], font=("Arial", 9)).pack()           # Familia
            tk.Label(cuadroAnimal, text=f"Estado: {estadoTexto.get(estado, 'Desconocido')}", font=("Arial", 8, "italic")).pack()

            # --- SECCIÓN DE EMOJIS ---
            marcoEmojis = tk.Frame(cuadroAnimal)
            marcoEmojis.pack()

            def aplicarCalificacion(valorEmoji, posicionAnimal):
                """
                Cambia la calificación del animal (según emoji) y actualiza el archivo.
                Luego, refresca la página para mostrar los cambios.
                """
                listaAnimales[inicio + posicionAnimal][1][1] = valorEmoji
                with open("inventario.txt", "w", encoding="utf-8") as archivo:
                    for animal in listaAnimales:
                        archivo.write(f"{animal}\n")
                mostrarPagina()

            for valorEmoji in range(1, 6):
                # Definimos qué emoji corresponde a cada valor
                if valorEmoji == 1:
                    emoji = "❤️"
                elif valorEmoji == 2:
                    emoji = "👍"
                elif valorEmoji == 3:
                    emoji = "⭐"
                elif valorEmoji == 4:
                    emoji = "😢"
                elif valorEmoji == 5:
                    emoji = "😡"

                # Se permite usar solo algunos emojis según el estado del animal
                if estado == 1:  # Si está vivo
                    esPermitido = valorEmoji in (1, 2, 3)
                else:            # Si está muerto o en otro estado
                    esPermitido = valorEmoji in (4, 5)

                # Se crea el botón del emoji
                botonEmoji = tk.Button(
                    marcoEmojis,
                    text=emoji,
                    width=3,
                    font=("Segoe UI Emoji", 12), # si se usa uno diferente a segoe... los emojis se pueden mostrar en menos definición
                    command=lambda ve=valorEmoji, pa=posicion: aplicarCalificacion(ve, pa)
                )

                # Si el emoji ya está seleccionado, se marca hundido
                if calificacion == valorEmoji:
                    botonEmoji.config(relief="sunken")
                # Si el emoji no es permitido según el estado, se desactiva
                if not esPermitido:
                    botonEmoji.config(state="disabled")

                botonEmoji.pack(side="left", padx=2)

    def avanzarPagina():
        """Permite avanzar a la siguiente página si hay más animales por mostrar."""
        totalPaginas = (len(listaAnimales) - 1) // 4
        if paginaMostrada[0] < totalPaginas:
            paginaMostrada[0] += 1
            mostrarPagina()

    def retrocederPagina():
        """Permite volver a la página anterior si no estamos en la primera."""
        if paginaMostrada[0] > 0:
            paginaMostrada[0] -= 1
            mostrarPagina()

    # Marco con los botones de navegación (izquierda/derecha)
    marcoNavegacion = tk.Frame(ventana)
    marcoNavegacion.pack(pady=5)

    tk.Button(marcoNavegacion, text="⬅️", command=retrocederPagina).pack(side="left", padx=10)
    tk.Button(marcoNavegacion, text="➡️", command=avanzarPagina).pack(side="left", padx=10)

    mostrarPagina()  # Se muestra la primera página al abrir la ventana




#=======================4. Estadistica por Estado =========================
def mostrarEstadisticaPorEstado():
    """
    Funcionalidad:
    - Muestra una ventana con la estadística de animales por estado.

    Entradas:
    - Ninguna.

    Salidas:
    - No retorna valor. Muestra la ventana con los datos.
    """
    inventario = cargarInventario()
    if not inventario:
        messagebox.showerror("Error", "No hay inventario cargado.")
        return
    estados = {
        1: "Vivo",
        2: "Enfermo",
        3: "Traslado",
        4: "Muerto en museo",
        5: "Muerto"}
    conteo = {}
    for k in estados:
        conteo[k] = 0
    for animal in inventario:
        estado = animal.obtenerEstado()
        if estado in conteo:
            conteo[estado] += 1
    total = 0
    for valor in conteo.values():
        total += valor
    porcentajes = {}
    for k in conteo:
        if total > 0:
            porcentaje = conteo[k] * 100 // total
        else:
            porcentaje = 0
        porcentajes[k] = porcentaje

    # Crear ventana
    ventanaEst = tk.Toplevel()
    ventanaEst.title("Estadística por estado")
    ventanaEst.resizable(False, False)

    tk.Label(ventanaEst, text="Estadística por estado", font=("Arial", 12)).grid(row=0, column=0, columnspan=3, pady=8)
    tk.Label(ventanaEst, text="").grid(row=1, column=0)  # Espacio
    tk.Label(ventanaEst, text="", width=10).grid(row=2, column=0)
    tk.Label(ventanaEst, text="Cant", width=6).grid(row=2, column=1)
    tk.Label(ventanaEst, text="Porc", width=6).grid(row=2, column=2)
    fila = 3
    for k in estados:
        tk.Label(ventanaEst, text=estados[k], anchor="w", width=16).grid(row=fila, column=0, sticky="w")
        tk.Entry(ventanaEst, width=5, justify="center", state="readonly", 
                readonlybackground="white", fg="black", 
                font=("Arial", 10), 
                textvariable=tk.StringVar(value=str(conteo[k]))).grid(row=fila, column=1)
        tk.Entry(ventanaEst, width=5, justify="center", state="readonly", 
                readonlybackground="white", fg="black", 
                font=("Arial", 10), 
                textvariable=tk.StringVar(value=str(porcentajes[k]))).grid(row=fila, column=2)
        fila += 1

#=======================5. HTML =========================
def clasificarAnimalesPorOrden(inventario):
    """
    Funcionalidad:
    - Clasifica los animales del inventario por su orden (omnívoro, carnívoro, herbívoro).

    Entradas:
    - inventario: lista de objetos Animal.

    Salidas:
    - Retorna un diccionario con listas de animales por orden.
    """
    ordenes = {'o': [], 'c': [], 'h': []}
    for animal in inventario:
        orden = animal.obtenerOrdenYPeso()[0]
        if orden in ordenes:
            ordenes[orden].append(animal)
    return ordenes

def contarAnimalesPorOrden(ordenes):
    """
    Funcionalidad:
    - Cuenta la cantidad de animales por cada orden.

    Entradas:
    - ordenes: dict, animales clasificados por orden.

    Salidas:
    - Retorna un diccionario con los conteos.
    """
    conteo = {'o': 0, 'c': 0, 'h': 0}
    for clave in ordenes:
        conteo[clave] = len(ordenes[clave])
    return conteo

def generarFilasTablaHtml(ordenes, ordenNombre):
    """
    Funcionalidad:
    - Genera las filas HTML para la tabla de animales por orden.

    Entradas:
    - ordenes: dict, animales clasificados por orden.
    - ordenNombre: dict, nombres de los órdenes.

    Salidas:
    - Retorna un string con las filas HTML.
    """
    filas = ""
    for clave in ['o', 'c', 'h']:
        animales = ordenes[clave]
        cantidad = len(animales)
        indice = 0
        for animal in animales:
            peso = animal.obtenerOrdenYPeso()[1]
            nombre = animal.obtenerNombres()[0]
            if indice == 0:
                filas += (
                    f"        <tr>\n"
                    f"            <td rowspan='{cantidad}'>{ordenNombre[clave]}</td>\n"
                    f"            <td>{peso:.2f}</td>\n"
                    f"            <td>{nombre}</td>\n"
                    f"        </tr>\n"
                )
            else:
                filas += (
                    f"        <tr>\n"
                    f"            <td>{peso:.2f}</td>\n"
                    f"            <td>{nombre}</td>\n"
                    f"        </tr>\n"
                )
            indice += 1
    return filas

def generarTotalesHtml(conteo):
    """
    Funcionalidad:
    - Genera el HTML para mostrar los totales por orden.

    Entradas:
    - conteo: dict, conteo de animales por orden.

    Salidas:
    - Retorna un string con el HTML de los totales.
    """
    htmlTotales = (
        f'    <div class="totales">\n'
        f'        <p>Total de omnívoros: {conteo["o"]}</p>\n'
        f'        <p>Total de carnívoros: {conteo["c"]}</p>\n'
        f'        <p>Total de herbívoros: {conteo["h"]}</p>\n'
        f'    </div>\n'
    )
    return htmlTotales

def crearHtmlInventario():
    """
    Funcionalidad:
    - Crea un archivo HTML con la estadística de animales por orden.

    Entradas:
    - Ninguna.

    Salidas:
    - No retorna valor. Genera el archivo HTML y muestra mensaje.
    """
    inventario = cargarInventario()
    if not inventario:
        messagebox.showerror("Error", "No hay inventario para exportar a HTML.")
        return

    ordenes = clasificarAnimalesPorOrden(inventario)
    conteo = contarAnimalesPorOrden(ordenes)
    ordenNombre = {'o': 'Omnívoro', 'c': 'Carnívoro', 'h': 'Herbívoro'}

    htmlInicio = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Estadistica por Orden</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { border-collapse: collapse; width: 60%; margin: 30px auto; }
        th, td { border: 1px solid #888; padding: 8px 12px; text-align: center; }
        th { background-color: #4CAF50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        tr:nth-child(odd) { background-color: #ffffff; }
        caption { font-size: 1.5em; margin-bottom: 10px; }
        .totales { width: 60%; margin: 20px auto; font-size: 1.1em; }
    </style>
</head>
<body>
    <table>
        <caption>Estadisticas Por Orden</caption>
        <tr>
            <th>Orden</th>
            <th>Peso (kg)</th>
            <th>Nombre común</th>
        </tr>
"""

    filasTabla = generarFilasTablaHtml(ordenes, ordenNombre)
    htmlFin = "    </table>\n"
    htmlTotales = generarTotalesHtml(conteo)
    htmlCierre = "</body>\n</html>\n"

    htmlCompleto = htmlInicio + filasTabla + htmlFin + htmlTotales + htmlCierre

    with open("estadisticasPorOrden.html", "w", encoding="utf-8") as f:
        f.write(htmlCompleto)

    messagebox.showinfo("Éxito", "Archivo 'inventario.html' creado correctamente.")

#=======================6. Generar PDF =========================
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def seccionCalificacionPDF(pdf, animales, titulo, y, mostrarEstado=False):
    """
    Funcionalidad:
    - Agrega una sección al PDF con los animales de una calificación específica.

    Entradas:
    - pdf: objeto canvas de ReportLab.
    - animales: lista de objetos Animal.
    - titulo: str, título de la sección.
    - y: int, posición vertical inicial.
    - mostrarEstado: bool, si se debe mostrar el estado.

    Salidas:
    - Retorna la nueva posición vertical (int) para continuar escribiendo.
    """
    pdf.setFont("Helvetica-BoldOblique", 11)
    pdf.drawString(40, y, titulo)
    y -= 15
    pdf.setFont("Helvetica-Oblique", 9)
    pdf.drawString(60, y, "Código")
    pdf.drawString(120, y, "Nombre común")
    if mostrarEstado:
        pdf.drawString(220, y, "Estado")
    y -= 12
    pdf.setFont("Helvetica", 10)
    for i, animal in enumerate(animales, 1):
        pdf.drawString(60, y, f"{i}.")
        pdf.drawString(80, y, animal.obtenerId())
        pdf.drawString(120, y, animal.obtenerNombres()[0])
        if mostrarEstado:
            estado = animal.obtenerEstado()
            if estado == 2:
                estadoStr = "Enfermo"
            elif estado == 3:
                estadoStr = "Traslado"
            elif estado == 4:
                estadoStr = "Muerto en museo"
            elif estado == 5:
                estadoStr = "Muerto"
            else:
                estadoStr = ""
            pdf.drawString(220, y, estadoStr)
        y -= 12
    return y - 8

def generarPDFEstadisticaPorCalificacion():
    """
    Funcionalidad:
    - Genera un PDF con la estadística de animales por calificación.

    Entradas:
    - Ninguna.

    Salidas:
    - No retorna valor. Crea el PDF y muestra mensaje.
    """
    inventario = cargarInventario()
    if not inventario:
        messagebox.showerror("Error", "No hay inventario para generar PDF.")
        return

    clasificaciones = {
        1: "No marcado",
        2: "Me gusta",
        3: "Favorito",
        4: "Me entristece",
        5: "Me enoja"
    }
    animalesPorCalificacion = {}
    for k in clasificaciones:
        animalesPorCalificacion[k] = []
    for animal in inventario:
        calif = animal.obtenerCalificacion()
        if calif in animalesPorCalificacion:
            animalesPorCalificacion[calif].append(animal)

    pdf = canvas.Canvas("estadisticaPorCalificacion.pdf", pagesize=letter)
    pdf.setTitle("Estadística por Calificación")
    y = 760
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(40, y, "Estadística por Calificación")
    y -= 30

    y = seccionCalificacionPDF(pdf, animalesPorCalificacion[1], "No marcado", y)
    y = seccionCalificacionPDF(pdf, animalesPorCalificacion[2], "Me gusta", y)
    y = seccionCalificacionPDF(pdf, animalesPorCalificacion[3], "Favorito", y)
    y = seccionCalificacionPDF(pdf, animalesPorCalificacion[4], "Me entristece", y, mostrarEstado=True)
    y = seccionCalificacionPDF(pdf, animalesPorCalificacion[5], "Me enoja", y, mostrarEstado=True)

    # Totales
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(40, y, "Totales:")
    y -= 15
    pdf.setFont("Helvetica", 10)
    pdf.drawString(60, y, f"No marcado: {len(animalesPorCalificacion[1])}   Me gusta: {len(animalesPorCalificacion[2])}   Favorito: {len(animalesPorCalificacion[3])}")
    y -= 12
    pdf.drawString(60, y, f"Me entristece: {len(animalesPorCalificacion[4])}   Me enoja: {len(animalesPorCalificacion[5])}")

    pdf.save()
    messagebox.showinfo("Éxito", "PDF generado como 'estadisticaPorCalificacion.pdf'.")

#========================================== 7. generar csv ===================================

"""
indicaciones: como ya es de su conocimiento, exporte la lista completa de objetos a un .csv, separado por comas,
para que pueda ser abierto en 'Excel' y se pueda corroborar la correctitud de cada reporte.
"""
def exportarInventarioACSV():
    """
    Funcionalidad:
    - Exporta el inventario de animales a un archivo CSV para Excel.

    Entradas:
    - Ninguna.

    Salidas:
    - No retorna valor. Crea el archivo CSV.
    """
    try:
        with open("inventario.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        
        datos_convertidos = []
        for linea in lineas:
            linea = linea.strip()
            if not linea:
                continue  # Saltar líneas vacías 
            try:
                item = ast.literal_eval(linea)
                
                if isinstance(item, list) and len(item) == 3:
                    (nombre, familia) = item[0]
                    fila, columna, estado, peso = item[1]
                    url = item[2]

                    # Añadir fila a lista
                    datos_convertidos.append([
                        nombre, familia, fila, columna, estado, peso, url
                    ])
                else:
                    print(f"Línea malformada: {linea}") 
            except Exception as e:
                print(f"❌ Error al procesar línea:\n{linea}\nDetalles: {e}")

        # Verificamos si se recolectaron datos
        if not datos_convertidos:
            print("⚠️ No se encontraron datos válidos para exportar.")
            return

        # Escribir en CSV
        with open("inventario.csv", "w", newline="", encoding="utf-8") as csvfile:
            escritor = csv.writer(csvfile)
            escritor.writerow(["Nombre", "Familia", "Fila", "Columna", "Estado", "Peso", "Imagen URL"])
            escritor.writerows(datos_convertidos)

        print("✅ Archivo 'inventario.csv' creado correctamente con datos.")
    
    except FileNotFoundError:
        print("❌ El archivo 'inventario.txt' no fue encontrado.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

#======================================= 8. busqueda por Orden ================================
def buscarPorOrdenES():
    """
    Funcionalidad:
    - Permite buscar animales por orden (carnívoro, herbívoro, omnívoro) y genera un HTML con los resultados.

    Entradas:
    - Ninguna (interfaz gráfica).

    Salidas:
    - No retorna valor. Muestra ventana y genera HTML si hay resultados.
    """
    import webbrowser
    from tkinter import ttk, messagebox
    import tkinter as tk  # Se debe importar para evitar errores si se ejecuta esta función de forma independiente

    # Diccionario que mapea la primera letra del tipo de alimentación con su nombre completo
    ordenMapeo = {
        "c": "Carnívoro",
        "h": "Herbívoro",
        "o": "Omnívoro"
    }

    def generarHTML(animales, ordenSeleccionado):
        """
        Esta función recibe una lista de animales y el nombre del orden seleccionado.
        Luego, genera un archivo HTML que muestra los animales de ese orden en una tabla,
        con su nombre común, nombre científico y una imagen.
        """
        nombreArchivo = f"animales_{ordenSeleccionado.lower()}.html"

        with open(nombreArchivo, "w", encoding="utf-8") as archivo:
            # Estructura básica del HTML
            archivo.write("<!DOCTYPE html>\n<html lang='es'>\n<head>\n")
            archivo.write("<meta charset='UTF-8'>\n<title>Animales por Orden</title>\n")
            archivo.write("<style>\n")
            archivo.write("table { border-collapse: collapse; width: 100%; }\n")
            archivo.write("th, td { border: 1px solid black; padding: 8px; text-align: center; }\n")
            archivo.write("th { background-color: #ccc; }\n")
            archivo.write("tr:nth-child(even) {background-color: #d0e7ff; }\n") #colores de las filas 
            archivo.write("tr:nth-child(odd) { background-color: #ffffff; }\n") #colores de las filas
            archivo.write("caption { font-size: 20px; font-weight: bold; margin-bottom: 10px; color: red; }\n")
            archivo.write("</style>\n</head>\n<body>\n")

            # Cabecera de la tabla
            archivo.write(f"<table>\n<caption>Animales {ordenSeleccionado}s</caption>\n")
            archivo.write("<tr><th>Código</th><th>Nombre común</th><th>Nombre científico</th><th>Foto</th></tr>\n")

            # Se recorren los animales y se agregan a la tabla
            for i, animal in enumerate(animales, start=1):
                nombreComun = animal[0][0]
                nombreCientifico = animal[0][1]
                url = animal[2]

                # Si no hay imagen, se pone una imagen genérica
                if url.strip() == "":
                    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Image_not_available.png/480px-Image_not_available.png"

                archivo.write(f"<tr><td>{i}</td><td>{nombreComun}</td><td>{nombreCientifico}</td>")
                archivo.write(f"<td><img src='{url}' alt='Imagen' width='100'></td></tr>\n")

            archivo.write("</table>\n</body>\n</html>")

        # Abre automáticamente el archivo HTML generado
        webbrowser.open(nombreArchivo)

    def mostrar():
        """
        Esta función se activa al presionar el botón 'Mostrar'. 
        Verifica si el orden es válido, filtra los animales y llama a la función de generar HTML.
        """
        seleccion = comboOrden.get()

        if seleccion not in ("Carnívoro", "Herbívoro", "Omnívoro"):
            messagebox.showwarning("Selección inválida", "Por favor seleccione un orden válido.")
            return

        # Encuentra la letra que representa el orden (c, h, o)
        letraOrden = ""
        for k, v in ordenMapeo.items():
            if v == seleccion:
                letraOrden = k
                break

        # Carga todo el inventario
        animales = cargarMostrarInventario()

        # Filtra los animales que coinciden con el orden
        filtrados = []
        for a in animales:
            if a[1][2].lower() == letraOrden:
                filtrados.append(a)

        # Muestra mensaje si no hay resultados
        if not filtrados:
            mensaje = f"No hay animales del orden {seleccion}."
            messagebox.showinfo("Sin resultados", mensaje)
        else:
            generarHTML(filtrados, seleccion)

    def limpiar():
        """
        Limpia la selección del combobox.
        """
        comboOrden.set("==Seleccionar==")

    # ================== Interfaz gráfica ==================
    ventana = tk.Toplevel()
    ventana.title("Mostrar por Orden")
    ventana.geometry("300x150")

    tk.Label(ventana, text="Orden").pack(pady=5)

    # Combobox para seleccionar el orden
    comboOrden = ttk.Combobox(ventana, state="readonly", values=["Carnívoro", "Herbívoro", "Omnívoro"])
    comboOrden.set("--Seleccionar--")
    comboOrden.pack()

    # Botones
    marcoBotones = tk.Frame(ventana)
    marcoBotones.pack(pady=10)

    btnMostrar = tk.Button(marcoBotones, text="Mostrar", command=mostrar)
    btnMostrar.pack(side="left", padx=5)

    btnLimpiar = tk.Button(marcoBotones, text="Limpiar", command=limpiar)
    btnLimpiar.pack(side="left", padx=5)