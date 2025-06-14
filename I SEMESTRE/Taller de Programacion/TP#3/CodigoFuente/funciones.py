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
import io
import ast # se usa para poder evaluar la lista del archivo
import urllib.request
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

    def asignarEstado(self, estado):
        self.__info[0] = estado

    def asignarPeso(self, peso):
        self.__info[3] = peso

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
        #esta es la api key de gemini es creada personal y unicamente para la tp (que no se filtre) porque se debió pedir en la pagina de gemini
        #porque se necesita usar esa llave para poder usar la api de gemini 
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
        "Ejemplo: {\"nombre_cientifico\": \"Panthera leo\", \"url_imagen\": \"https://...\", \"orden\": \"c\"}")
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
            # Extraer primer objeto de la lista manualmente
            primerObjeto = texto[texto.find('{'):texto.find('}')+1]
            return json.loads(primerObjeto)
        else:
            return json.loads(jsonTexto)
    else:
        print(f"Respuesta inesperada de Gemini para '{nombreComun}': {texto}")
        raise ValueError("No se encontró JSON válido en la respuesta de Gemini.")

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

#=======================3. Mostrar inventario =========================
"""
instrucciones:crear una ventana 4 en 4 animales para ver el inventario
y para calificarlos. Dado obligfatoriamente son 20 y se mostrarán 4 por ventana,
debe tenerse 5 visualizaciones para moverse hacia adelante y hacia atras del inventario.
Aquí es dónde usted debe calificar al animal, pero 
validando que pueda calificarlo según el estado. Vaya 
a la definición de la clase y siga instrucciones. Llame al 
método correspondiente para modificar, no solicite 
confirmación. 
Claro estamos que en la funcionalidad 2 se guardó el URL 
que proporciona Wikipedia en cada objeto, pero… dado el 
estado fue aleatorio, use ello para mostrar aquí la 
imagen según se indica. Por lo visto, estos 4 animales 
están en estado “vivo”… 

ejemplo:
_______________________________________________________
estado                  |   imagen que mostrar
1.vivo                  |   muestre la imagen del url extraido de wikipedia
2.enfermo               |   una ambulancia
3.trasladado(a otro zoo)| una ambulancia
4.muerto en museo       |   Un simbolo de museo
5.muerto                |   una calavera

Los diferentes símbolos representan los emojis para calificarlo. Siga las 
limitantes de la definición de la clase indicadas arriba. Considere que al calificarse el emoji 
debe mostrarse por alguna estrategia como marcado al dar clic y ser la correcta calificación 
según el estado.  

"""
imagenesPorEstado = {
    2: "ambulancia.png",
    3: "ambulancia.png",
    4: "museo.png",
    5: "calavera.png"
}

# Cargar la lista del inventario desde el archivo de texto
def cargarInventario():
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


# Cargar la imagen ya sea desde internet o desde un archivo local
def cargarImagen(desdeUrlOArchivo):
    try:
        if desdeUrlOArchivo.startswith("http"):
            with urllib.request.urlopen(desdeUrlOArchivo) as respuesta:
                datosImagen = respuesta.read()
            imagen = Image.open(io.BytesIO(datosImagen))
        else:
            imagen = Image.open(desdeUrlOArchivo)

        imagenRedimensionada = imagen.resize((120, 120))
        imagenConvertida = ImageTk.PhotoImage(imagenRedimensionada)
        return imagenConvertida
    except:
        return None

# Función principal que muestra el inventario en la ventana
def mostrarInventarioES():
    listaAnimales = cargarInventario()
    paginaMostrada = [0]  # Para manejar la navegación

    ventana = tk.Toplevel()
    ventana.title("Mostrar inventario")
    ventana.geometry("600x500")

    marcoPrincipal = tk.Frame(ventana)
    marcoPrincipal.pack(pady=10)

    listaCuadros = []  # Almacena los frames por animal

    def mostrarPagina():
        for elemento in marcoPrincipal.winfo_children():
            elemento.destroy()

        listaCuadros.clear()

        inicio = paginaMostrada[0] * 4
        final = inicio + 4
        animalesEnPagina = []

        for i in range(inicio, final):
            animalesEnPagina.append(listaAnimales[i])

        for posicion in range(len(animalesEnPagina)):
            animal = animalesEnPagina[posicion]
            nombres = animal[0]
            datos = animal[1]
            enlaceImagen = animal[2]

            estado = datos[0]
            calificacion = datos[1]
            orden = datos[2]
            peso = datos[3]

            cuadroAnimal = tk.Frame(marcoPrincipal, bd=2, relief="groove")
            fila = posicion // 2
            columna = posicion % 2
            cuadroAnimal.grid(row=fila, column=columna, padx=10, pady=10)

            if estado == 1:
                imagen = cargarImagen(enlaceImagen)
            else:
                imagenLocal = imagenesPorEstado[estado]
                imagen = cargarImagen(imagenLocal)

            if imagen is not None:
                etiquetaImagen = tk.Label(cuadroAnimal, image=imagen)
                etiquetaImagen.image = imagen
                etiquetaImagen.pack()

            nombreComun = nombres[0]
            nombreCientifico = nombres[1]

            tk.Label(cuadroAnimal, text=nombreComun, font=("Arial", 10, "bold")).pack()
            tk.Label(cuadroAnimal, text=nombreCientifico, font=("Arial", 9)).pack()

            marcoEmojis = tk.Frame(cuadroAnimal)
            marcoEmojis.pack()

            def aplicarCalificacion(valorEmoji, frame, posicionAnimal):
                datosAnimal = listaAnimales[inicio + posicionAnimal]
                estadoActual = datosAnimal[1][0]

                if valorEmoji == 4:
                    if estadoActual != 2 and estadoActual != 5:
                        return
                if valorEmoji == 5:
                    if estadoActual != 3:
                        return

                listaAnimales[inicio + posicionAnimal][1][1] = valorEmoji
                mostrarPagina()

            for valorEmoji in range(1, 6):
                if valorEmoji == 1:
                    emoji = "⭕"
                elif valorEmoji == 2:
                    emoji = "👍"
                elif valorEmoji == 3:
                    emoji = "⭐"
                elif valorEmoji == 4:
                    emoji = "😢"
                elif valorEmoji == 5:
                    emoji = "😡"

                estadoActual = listaAnimales[inicio + posicion][1][0]
                esPermitido = False

                if valorEmoji == 4:
                    if estadoActual == 2:
                        esPermitido = True
                    if estadoActual == 5:
                        esPermitido = True
                elif valorEmoji == 5:
                    if estadoActual == 3:
                        esPermitido = True
                elif valorEmoji == 1 or valorEmoji == 2 or valorEmoji == 3:
                    esPermitido = True

                botonEmoji = tk.Button(
                    marcoEmojis,
                    text=emoji,
                    width=3,
                    command=lambda v=valorEmoji, f=marcoEmojis, i=posicion: aplicarCalificacion(v, f, i)
                )

                calificacionActual = listaAnimales[inicio + posicion][1][1]
                if calificacionActual == valorEmoji:
                    botonEmoji.config(relief="sunken")

                if not esPermitido:
                    botonEmoji.config(state="disabled")

                botonEmoji.pack(side="left", padx=2)

    def avanzarPagina():
        paginaLimite = 4
        if paginaMostrada[0] < paginaLimite:
            paginaMostrada[0] += 1
            mostrarPagina()

    def retrocederPagina():
        if paginaMostrada[0] > 0:
            paginaMostrada[0] -= 1
            mostrarPagina()

    marcoNavegacion = tk.Frame(ventana)
    marcoNavegacion.pack(pady=5)

    botonAtras = tk.Button(marcoNavegacion, text="⬅️", command=retrocederPagina)
    botonAtras.pack(side="left", padx=10)

    botonSiguiente = tk.Button(marcoNavegacion, text="➡️", command=avanzarPagina)
    botonSiguiente.pack(side="left", padx=10)

    mostrarPagina()





#=======================4. Estadistica por Estado =========================
def mostrarEstadisticaPorEstado():
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