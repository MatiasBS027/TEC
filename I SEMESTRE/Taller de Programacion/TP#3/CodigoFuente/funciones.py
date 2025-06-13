# Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
# Fecha de creación: 11/06/2025
# Última modificación: 11/06/2025 21:15
# Python versión 3.13.2

import tkinter as tk            # Se usa para la interfaz gráfica
from tkinter import messagebox  # Se usa para mostrar mensajes emergentes al usuario
import os                       # Se usa para verificar si existe un archivo y manejar rutas del sistema
import random                      # Se usa para generar valores aleatorios (estado, peso, ID)
import google.generativeai as genai  # Se usa para configurar la API de Gemini
from google.generativeai import GenerativeModel  # Se usa para crear un modelo generativo como 'gemini-pro'
from PIL import Image, ImageTk  # Se usa para manejar imágenes
# puede ser necesario usar 'pip install -U google-generativeai' para actualizar la biblioteca gemini v1
import json

"""
Clase Animal que representa un objeto del inventario del zoológico.
Cada animal posee:
- Un ID único basado en su nombre común.
- Una tupla con su nombre común y nombre científico.
- Una URL con la imagen del animal.
- Una lista con información adicional: estado, calificación, orden y peso.
"""

class Animal:
    contadorGlobal = 1  # Atributo de clase para llevar la secuencia de IDs

    def __init__(self, nombreComun, nombreCientifico, url, orden):
        """
        Constructor que inicializa un objeto Animal.
        Se le asigna automáticamente:
        - Un ID según la convención: primera y última letra del nombre + número secuencial.
        - Un estado aleatorio (entre 1 y 5).
        - Un peso aleatorio según el orden del animal.
        """
        self.__id = self.crearId(nombreComun)
        self.__nombres = (nombreComun, nombreCientifico)
        self.__url = url
        self.__info = [0, 1, '', 0.0]  # [estado, calificación, orden, peso]
        self.asignarEstadoAleatorio()
        self.asignarOrdenYPeso(orden)

    # =================== ID ===================
    def crearId(self, nombre):
        """
        Crea un ID basado en la primera y última letra del nombre común,
        más un número secuencial no repetido.
        """
        nombre = nombre.strip().lower()
        primera = nombre[0]
        ultima = nombre[-1]
        codigo = f"{primera}{ultima}{Animal.contadorGlobal:02}"
        Animal.contadorGlobal += 1
        return codigo

    def obtenerId(self):
        return self.__id

    def mostrarId(self):
        print(self.__id)

    # =================== Nombres ===================
    def asignarNombres(self, nombreComun, nombreCientifico):
        """
        Asigna una nueva tupla de nombres al animal.
        """
        self.__nombres = (nombreComun, nombreCientifico)

    def obtenerNombres(self):
        return self.__nombres

    def mostrarNombres(self):
        print(self.__nombres[0])
        print(self.__nombres[1])

    # =================== URL ===================
    def asignarUrl(self, nuevaUrl):
        """
        Actualiza la URL de la imagen del animal.
        """
        self.__url = nuevaUrl

    def obtenerUrl(self):
        return self.__url

    def mostrarUrl(self):
        print(self.__url)

    # =================== Estado ===================
    def asignarEstadoAleatorio(self):
        """
        Asigna un estado aleatorio entre 1 y 5 al animal:
        1=vivo, 2=enfermo, 3=trasladado, 4=muerto en museo, 5=muerto
        """
        import random
        self.__info[0] = random.randint(1, 5)

    def obtenerEstado(self):
        return self.__info[0]

    def mostrarEstado(self):
        print(self.__info[0])

    # =================== Calificación ===================
    def asignarCalificacion(self, valor):
        """
        Asigna una calificación del usuario, si es válida según el estado:
        1=No marcado, 2=Me gusta, 3=Favorito, 4=Me entristece, 5=Me enoja
        Restricciones:
        - 4 solo si estado es 2 (enfermo) o 5 (muerto)
        - 5 solo si estado es 3 (trasladado)
        """
        estado = self.__info[0]
        if valor == 4 and estado not in [2, 5]:
            print("Solo puedes marcar 'me entristece' si está enfermo o muerto.")
            return
        if valor == 5 and estado != 3:
            print("Solo puedes marcar 'me enoja' si fue trasladado.")
            return
        if valor < 1 or valor > 5:
            print("Calificación no válida.")
            return
        self.__info[1] = valor

    def obtenerCalificacion(self):
        return self.__info[1]

    def mostrarCalificacion(self):
        print(self.__info[1])

    # =================== Orden y Peso ===================
    def asignarOrdenYPeso(self, orden):
        """
        Asigna el orden del animal y su peso estimado:
        - 'h' (herbívoros): entre 80.0 y 100.0 kg
        - 'c' o 'o' (carnívoros u omnívoros): entre 0.0 y 80.0 kg
        """
        import random
        orden = orden.lower()
        if orden not in ['c', 'h', 'o']:
            print("Orden debe ser 'c', 'h' u 'o'.")
            return
        self.__info[2] = orden
        if orden == 'h':
            self.__info[3] = round(random.uniform(80.0, 100.0), 2)
        else:
            self.__info[3] = round(random.uniform(0.0, 80.0), 2)

    def obtenerOrdenYPeso(self):
        return self.__info[2], self.__info[3]

    def mostrarOrdenYPeso(self):
        print(self.__info[2])
        print(self.__info[3])

    # =================== Todo el objeto ===================
    def obtenerDatos(self):
        """
        Devuelve todos los atributos del objeto en una lista.
        Orden: id, nombre común, nombre científico, url, estado, calificación, orden, peso
        """
        return [
            self.__id,
            self.__nombres[0],
            self.__nombres[1],
            self.__url,
            self.__info[0],
            self.__info[1],
            self.__info[2],
            self.__info[3]
        ]

    def mostrarDatos(self):
        """
        Muestra en consola todos los atributos del objeto.
        """
        self.mostrarId()
        self.mostrarNombres()
        self.mostrarUrl()
        self.mostrarEstado()
        self.mostrarCalificacion()
        self.mostrarOrdenYPeso()

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
    try:
        cantidad = int(cantidadTexto)
        if cantidad <= 0:
            return False, "Debe ingresar un número mayor a 0."
        return True, cantidad
    except ValueError:
        return False, "Por favor, ingrese un número válido."

        #====== Función central: pedir nombres a Gemini=======================
import google.generativeai as genai
from google.generativeai import GenerativeModel

def obtenernombresAnimales(cantidad):
    try:
        genai.configure(api_key="AIzaSyDVce9ynQYkU--tTfEiIwP9_BqjDAr9-tI")
        modelo = GenerativeModel('gemini-1.5-flash')  # ← cambio aqui el modelo usado (depende el que se use puede dar error)

        prompt = f"Proporcióname una lista exactamente de {cantidad} nombres comunes de animales en español, uno por línea, sin numeración ni explicaciones.(no me des nombres muy generales como 'mono').\n\n"
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
    # Verificar si el archivo ya existe
    if os.path.exists("nombresAnimales.txt"):
        messagebox.showinfo("Información", "El archivo de lista de animales ya existe y no se puede sobrescribir.")
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
def leerNombresAnimales():
    nombres = []
    if not os.path.exists("nombresAnimales.txt"):
        return nombres
    with open("nombresAnimales.txt", "r", encoding="utf-8") as f:
        for linea in f:
            nombre = linea.strip()
            if nombre != "":
                nombres.append(nombre)
    return nombres

def seleccionarNombresAleatorios(nombres, cantidad):
    if len(nombres) < cantidad:
        return []
    seleccionados = random.sample(nombres, cantidad)
    return seleccionados

def pedirDatosAnimalAGemini(nombreComun):
    prompt = (
        f"Dame la siguiente información del animal '{nombreComun}' en español, "
        "en formato JSON con las claves: nombre_cientifico, url_imagen, orden. "
        "El orden debe ser 'c' para carnívoro, 'h' para herbívoro, 'o' para omnívoro. "
        "Ejemplo: {\"nombre_cientifico\": \"Panthera leo\", \"url_imagen\": \"https://...\", \"orden\": \"c\"}"
    )
    genai.configure(api_key="AIzaSyDVce9ynQYkU--tTfEiIwP9_BqjDAr9-tI")
    modelo = GenerativeModel('gemini-1.5-flash')
    try:
        respuesta = modelo.generate_content(prompt)
        texto = respuesta.text.strip()
    except Exception as e:
        if "429" in str(e):
            raise RuntimeError("Has superado el límite de peticiones de Gemini. Intenta más tarde.")
        else:
            raise e
    if not texto:
        raise ValueError("Respuesta vacía de Gemini")
    # Extraer solo el JSON de la respuesta
    inicio = texto.find('{')
    fin = texto.rfind('}')
    if inicio != -1 and fin != -1 and fin > inicio:
        jsonTexto = texto[inicio:fin+1]
    else:
        print(f"Respuesta inesperada de Gemini para '{nombreComun}': {texto}")
        raise ValueError("No se encontró JSON válido en la respuesta de Gemini.")
    try:
        datos = json.loads(jsonTexto)
    except Exception as e:
        print(f"Respuesta inesperada de Gemini para '{nombreComun}': {jsonTexto}")
        raise e
    return datos

def crearAnimal(nombreComun, datos):
    nombreCientifico = datos.get("nombre_cientifico", "Desconocido")
    urlImagen = datos.get("url_imagen", "")
    orden = datos.get("orden", "o")
    animal = Animal(nombreComun, nombreCientifico, urlImagen, orden)
    return animal

def crearInventarioDesdeInterfaz(ventana):
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
        except Exception as e:
            print(f"Error obteniendo datos de '{nombre}': {e}")
            animal = Animal(nombre, "Desconocido", "", "o")
            inventario.append(animal)

    guardarInventario(inventario)  # Guardar en archivo
    messagebox.showinfo("Éxito", "Inventario de 20 animales creado correctamente.")
    ventana.destroy()
    return inventario

def guardarInventario(inventario, archivo="inventario.txt"):
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

def cargarInventario(archivo="inventario.txt"):
    if not os.path.exists(archivo):
        return []
    inventario = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                partes = linea.strip().split("],")
                nombres = partes[0].strip()[1:]  
                info = partes[1].split("],")[0].strip()[1:]  
                url = partes[2].strip()
                if url.startswith("'"):
                    url = url[1:]
                if url.endswith("']"):
                    url = url[:-2]
                elif url.endswith("'"):
                    url = url[:-1]
                # Procesar nombres
                nombres = nombres.split(",")
                nombreComun = nombres[0].strip().strip("'").strip('"')
                nombreCientifico = nombres[1].strip().strip("'").strip('"')
                # Procesar info
                info = info.split(",")
                estado = int(info[0].strip())
                calificacion = int(info[1].strip())
                orden = info[2].strip().strip("'").strip('"')
                peso = float(info[3].strip())

                animal = Animal(nombreComun, nombreCientifico, url, orden)
                # Asignar los valores leídos usando los métodos existentes
                animal.asignarEstadoAleatorio() 
                animal.asignarCalificacion(calificacion)
                animal.asignarOrdenYPeso(orden)  

                inventario.append(animal)
            except Exception as e:
                continue
    return inventario

# ...existing code...