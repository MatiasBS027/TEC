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
from archivos import *
# ==========================
# MÓDULOS PARA IMÁGENES (esto se usó principalmente para la estética usando imagenes)
# ==========================
from PIL import ImageTk, Image  # Procesamiento de imágenes (requiere pip install pillow en caso de no tenerlo)
import requests  # Para descargar imágenes desde URLs (requiere pip install requests en caso de no tenerlo)
from io import BytesIO  # Conversión de bytes a imagen 
import urllib.request  # Alternativa para descarga de imágenes
import os  # Manejo de rutas y archivos
import ast

# ==========================
# FUNCIONES UTILITARIAS UNIFICADAS
# ==========================

def obtenerInfoPokemon(idPoke, esShiny=False, soloBasico=False):
    """
    Funcionamiento:
    Obtiene la información de un Pokémon desde la API de PokeAPI y la retorna en un diccionario o tupla.

    Entradas:
    - idPoke: ID del Pokémon a consultar.
    - esShiny: Booleano, si es True retorna la imagen shiny.
    - soloBasico: Booleano, si es True retorna solo (id, nombre, totalEstats).

    Salidas:
    - Diccionario con la información del Pokémon, o tupla si soloBasico es True.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
    try:
        respuesta = requests.get(url, timeout=8)
        datos = respuesta.json()
        idApi = datos['id']
        nombre = datos['name']
        estadisticas = datos['stats']
        statsOrden = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
        statsValores = []
        for statNombre in statsOrden:
            for stat in estadisticas:
                if stat['stat']['name'] == statNombre:
                    statsValores.append(stat['base_stat'])
                    break
        totalEstats = sum(statsValores)
        statsTupla = tuple(statsValores)
        tiposLista = []
        for tipo in datos['types']:
            tiposLista.append(tipo['type']['name'])
        tipos = tuple(tiposLista)
        if soloBasico:
            return (idApi, nombre, totalEstats)
        peso = datos['weight']
        altura = datos['height']
        if esShiny:
            urlImagen = datos['sprites']['front_shiny']
        else:
            urlImagen = datos['sprites']['front_default']
        return {
            idApi: [
                nombre,
                (esShiny, peso, altura),
                [totalEstats, statsTupla],
                tipos,
                urlImagen
            ]
        }
    except Exception as e:
        print(f"Error al obtener info de Pokémon {idPoke}: {e}")
        return None

def buscarHuidos():
    """
    Funcionamiento:
    Busca y retorna una lista de Pokémon que han huido, leyendo el archivo 'MisPokemon.txt'.

    Entradas:
    - Ninguna.

    Salidas:
    - Lista de tuplas (id, nombre) de Pokémon huidos.
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
    except FileNotFoundError:
        pass
    return pokemonesHuidos

def dividirPaginas(lista, tamano):
    """
    Funcionamiento:
    Divide una lista en sublistas (páginas) de tamaño especificado.

    Entradas:
    - lista: Lista a dividir.
    - tamano: Tamaño de cada página.

    Salidas:
    - Lista de páginas (listas).
    """
    paginas = []
    inicio = 0
    while inicio < len(lista):
        fin = inicio + tamano
        pagina = lista[inicio:fin]
        paginas.append(pagina)
        inicio = fin
    return paginas

# ##################################################
# 1 Busqueda de pokémons 
# ##################################################

def ejecutarBusqueda(pokepad):
    """
        Funcionamiento:
        Muestra una ventana para buscar y guardar una cantidad de Pokémon aleatorios en 'MisPokemon.txt'.

        Entradas:
        - pokepad: Instancia principal de la interfaz.

        Salidas:
        - Ninguna (guarda datos en archivo y muestra mensajes).
    """
    ventanaEmergente = tk.Toplevel(pokepad.ventana)
    ventanaEmergente.title("Búsqueda de Pokémon")
    ventanaEmergente.geometry("300x200")
    

    ttk.Label(ventanaEmergente, text="Cantidad de Pokémon deseada:").pack(pady=10)
    entradaCantidad = ttk.Entry(ventanaEmergente)
    entradaCantidad.pack(pady=5)

    def buscar():
        try:
            cantidadDeseada = int(entradaCantidad.get())
            if cantidadDeseada <= 0 or cantidadDeseada > 1025:
                raise ValueError("La cantidad debe estar entre 1 y 1025.")

            # Generar IDs aleatorios únicos
            idRandom = random.sample(range(1, 1026), cantidadDeseada)

            # Ruta al archivo en la misma carpeta del script
            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaArchivo = os.path.join(rutaBase, "MisPokemon.txt")

            with open(rutaArchivo, "w", encoding="utf-8") as archivoTexto:
                for i in idRandom:
                    try:
                        respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}", timeout=5)
                        if respuesta.status_code == 200:
                            datos = respuesta.json()
                            nombre = datos["name"]
                            archivoTexto.write(f"{i}^{nombre}\n")
                        else:
                            print(f"No se pudo obtener el Pokémon con ID {i}")
                    except Exception as e:
                        print(f"Error con el ID {i}: {e}")

            messagebox.showinfo("Éxito", f"Se guardaron {cantidadDeseada} Pokémon en:\n{rutaArchivo}")
            ventanaEmergente.destroy()

        except ValueError as errorValor:
            messagebox.showerror("Error de entrada", str(errorValor))
        except Exception as errorGeneral:
            messagebox.showerror("Error", str(errorGeneral))

    def limpiar():
        entradaCantidad.delete(0, tk.END)

    marcoBotones = ttk.Frame(ventanaEmergente)
    marcoBotones.pack(pady=15)
    ttk.Button(marcoBotones, text="Buscar", command=buscar).pack(side="left", padx=10)
    ttk.Button(marcoBotones, text="Limpiar", command=limpiar).pack(side="left", padx=10)

# ##################################################
# 2 Atrapar Pokemon 
# ##################################################

def ejecutarAtrapar(pokepad):
    """
    Funcionamiento:
    Muestra una ventana para atrapar Pokémon según un porcentaje indicado por el usuario.
    Actualiza los archivos y genera el diccionario.

    Entradas:
    - pokepad: Instancia principal de la interfaz.

    Salidas:
    - Ninguna (actualiza archivos y muestra mensajes).
    """
    rutaBase = os.path.dirname(os.path.abspath(__file__))
    rutaDiccionario = os.path.join(rutaBase, "DiccionarioPokemon.txt")

    ventanaAtrapar = tk.Toplevel(pokepad.ventana)
    ventanaAtrapar.title("Atrapar Pokémon")
    ventanaAtrapar.geometry("420x320")

    ttk.Label(ventanaAtrapar, text="¿Qué porcentaje de Pokémon quieres atrapar?").pack(pady=10)
    entradaPorcentaje = ttk.Entry(ventanaAtrapar)
    entradaPorcentaje.pack(pady=5)

    areaResultado = tk.Text(ventanaAtrapar, height=12, width=55, state="disabled")
    areaResultado.pack(pady=8)

    def ejecutarCaptura():
        areaResultado.config(state="normal")
        areaResultado.delete("1.0", tk.END)

        try:
            porcentaje = int(entradaPorcentaje.get())
            if not (0 <= porcentaje <= 100):
                raise ValueError("El porcentaje debe estar entre 0 y 100")

            disponibles = leerPokemonesDisponibles()
            if not disponibles:
                areaResultado.insert(tk.END, "No hay Pokémon disponibles para atrapar\n")
                return

            total = len(disponibles)
            cantidadAtrapados = round((porcentaje / 100) * total)
            atrapados = random.sample(disponibles, cantidadAtrapados)
            huidos = []
            for poke in disponibles:
                if poke not in atrapados:
                    huidos.append(poke)

            areaResultado.insert(tk.END, f"Pokémon atrapados: {len(atrapados)}\n")
            areaResultado.insert(tk.END, f"Pokémon que huyeron: {len(huidos)}\n\n")

            areaResultado.insert(tk.END, "Atrapados:\n")
            for idPoke, nombre in atrapados:
                areaResultado.insert(tk.END, f"- {nombre} (ID: {idPoke})\n")

            areaResultado.insert(tk.END, "\nHuidos:\n")
            for idPoke, nombre in huidos:
                areaResultado.insert(tk.END, f"- {nombre} (ID: {idPoke})\n")

            atrapadosStr = []
            for id, nombre in atrapados:
                atrapadosStr.append((str(id), nombre))

            huidosStr = []
            for id, nombre in huidos:
                huidosStr.append((str(id), nombre))

            if guardarResultados(atrapadosStr, huidosStr, rutaBase):
                generarDiccionarioPokemon()

                if atrapadosStr:
                    messagebox.showinfo("¡Éxito!", f"¡Has atrapado {len(atrapadosStr)} Pokémon!")

                areaResultado.insert(tk.END, "\n¡Estados guardados correctamente!")

        except ValueError as e:
            areaResultado.insert(tk.END, f"Error: {str(e)}\n")
        finally:
            areaResultado.config(state="disabled")

    marcoBotones = ttk.Frame(ventanaAtrapar)
    marcoBotones.pack(pady=5)

    ttk.Button(marcoBotones, text="Atrapar", command=ejecutarCaptura).pack(side="left", padx=10)
    ttk.Button(marcoBotones, text="Limpiar", command=lambda: [
        entradaPorcentaje.delete(0, tk.END),
        areaResultado.config(state="normal"),
        areaResultado.delete("1.0", tk.END),
        areaResultado.config(state="disabled")
    ]).pack(side="left", padx=10)
    ttk.Button(marcoBotones, text="Cerrar", command=ventanaAtrapar.destroy).pack(side="left", padx=10)

# ##################################################3
# 3 Pokédex
# ##################################################
def ejecutarPokedex(pokePad):
    """
    Funcionamiento:
    Muestra una ventana con la Pokédex, permitiendo navegar entre páginas de Pokémon.

    Entradas:
    - pokePad: Instancia principal de la interfaz.

    Salidas:
    - Ninguna (muestra ventana con Pokédex).
    """
    ventanaPokedex = tk.Toplevel()
    ventanaPokedex.title("Pokédex")
    ventanaPokedex.configure(bg="white")

    # Cargar diccionarioPokemon desde DiccionarioPokemon.txt
    diccionarioPokemon = leerDiccionario()
    if not diccionarioPokemon:
        messagebox.showerror("Error", "No se pudo cargar el diccionario.")
        ventanaPokedex.destroy()
        return
    filas, columnas = 5, 5
    porPagina = filas * columnas
    paginaActual = [0]

    INTERROGACION = "interrogacion.png"
    interrogacionPil = Image.open(INTERROGACION)
    interrogacionPil.thumbnail((90, 90), Image.LANCZOS)
    interrogacionImg = ImageTk.PhotoImage(interrogacionPil)

    try:
        with open("MisPokemon.txt", "r", encoding="utf-8") as archivo:
            listaPokemones = []
            for line in archivo:
                if line.strip():
                    listaPokemones.append(line.strip())
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo MisPokemon.txt")
        ventanaPokedex.destroy()
        return

    def obtenerId(linea):
        partes = linea.split("^")
        if partes and partes[0].isdigit():
            return int(partes[0])
        return 0

    listaPokemones.sort(key=obtenerId)

    totalPaginas = (len(listaPokemones) + porPagina - 1) // porPagina
    imagenesCache = {}

    frameMatriz = tk.Frame(ventanaPokedex, bg="white")
    frameMatriz.pack(pady=20)

    def obtenerImagenPokemon(idPoke, esShiny=False):
        idPokeInt = int(idPoke)  # Asegurarse que es int
        if idPokeInt in imagenesCache:
            return imagenesCache[idPokeInt]
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{idPokeInt}"
            respuesta = requests.get(url, timeout=5)
            datos = respuesta.json()
            if esShiny:
                urlImg = datos['sprites']['front_shiny'] 
            else:
                urlImg = datos['sprites']['front_default']
            if urlImg:
                imgPil = Image.open(BytesIO(requests.get(urlImg, timeout=5).content))
                imgPil.thumbnail((90, 90), Image.LANCZOS)
                imgTk = ImageTk.PhotoImage(imgPil)
                imagenesCache[idPokeInt] = imgTk
                return imgTk
        except Exception:
            pass
        return interrogacionImg

    def mostrarPagina():
        for widget in frameMatriz.winfo_children():
            widget.destroy()

        inicio = paginaActual[0] * porPagina
        fin = inicio + porPagina
        pokemonesPagina = listaPokemones[inicio:fin]

        while len(pokemonesPagina) < porPagina:
            pokemonesPagina.append(None)

        for i in range(filas):
            for j in range(columnas):
                idx = i * columnas + j
                pokeData = pokemonesPagina[idx]
                celda = tk.Frame(frameMatriz, bg="white")
                celda.grid(row=i, column=j, padx=8, pady=8)

                if pokeData:
                    partes = pokeData.strip().split("^")
                    if len(partes) == 3:
                        pokeId, nombre, estado = partes
                        pokeId = pokeId.strip()
                        nombre = nombre.strip()
                        estado = estado.strip().lower()

                        if estado == "a":
                            esShiny = False
                            if pokeId.isdigit():
                                pokeIdInt = int(pokeId) 
                            else:
                                pokeIdInt = 0
                            if pokeIdInt in diccionarioPokemon:
                                esShiny = diccionarioPokemon[pokeIdInt][1][0]

                            imagen = obtenerImagenPokemon(pokeIdInt, esShiny=esShiny)
                            # Botón para mostrar detalle al hacer click
                            btn = tk.Button(
                                celda,
                                image=imagen,
                                bg="white",
                                borderwidth=0,
                                command=lambda idpoke=pokeIdInt, shiny=esShiny: mostrarDetallePokemon(idpoke, shiny))
                            btn.image = imagen  # guardar referencia para que no se borre
                            btn.pack()
                            tk.Label(celda, text=nombre, bg="white", font=("Arial", 12)).pack()
                        else:
                            tk.Label(celda, image=interrogacionImg, bg="white").pack()
                            tk.Label(celda, text="no encontrado", bg="white", font=("Arial", 12)).pack()
                    else:
                        tk.Label(celda, image=interrogacionImg, bg="white").pack()
                        tk.Label(celda, text="no encontrado", bg="white", font=("Arial", 12)).pack()
                else:
                    tk.Label(celda, image=interrogacionImg, bg="white").pack()
                    tk.Label(celda, text="no encontrado", bg="white", font=("Arial", 12)).pack()

        etiquetaPagina.config(text=f"Página {paginaActual[0] + 1}/{totalPaginas}")

    def siguiente():
        if paginaActual[0] < totalPaginas - 1:
            paginaActual[0] += 1
            mostrarPagina()

    def anterior():
        if paginaActual[0] > 0:
            paginaActual[0] -= 1
            mostrarPagina()

    frameControles = tk.Frame(ventanaPokedex, bg="white")
    frameControles.pack(pady=10)
    btnAtras = tk.Button(frameControles, text="Atrás", command=anterior, font=("Arial", 14), width=10)
    btnAtras.pack(side="left", padx=40)
    etiquetaPagina = tk.Label(frameControles, text="", font=("Arial", 14), bg="white")
    etiquetaPagina.pack(side="left", padx=10)
    btnSiguiente = tk.Button(frameControles, text="Siguiente", command=siguiente, font=("Arial", 14), width=10)
    btnSiguiente.pack(side="left", padx=40)
    mostrarPagina()
# ##################################################
# 4 Detalle 
# ##################################################
imagenPokemon = None  # Variable global para mantener referencia a la imagen
def cargarImagen(label, url):
    """
    Funcionamiento:
    Carga una imagen desde una URL y la muestra en un label de Tkinter.

    Entradas:
    - label: Label de Tkinter donde se mostrará la imagen.
    - url: URL de la imagen.

    Salidas:
    - Ninguna (actualiza el label).
    """
    global imagenPokemon
    try:
        respuesta = requests.get(url)
        datosImagen = Image.open(BytesIO(respuesta.content))
        imagenPokemon = ImageTk.PhotoImage(datosImagen)
        label.config(image=imagenPokemon)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

def cargarPokemon(idPokemon, nombre, entradas, imagen, esShiny=False):
    """
    Funcionamiento:
    Carga los datos de un Pokémon y actualiza los campos de la interfaz gráfica.

    Entradas:
    - idPokemon: ID del Pokémon.
    - nombre: Label para el nombre.
    - entradas: Diccionario de entradas de la interfaz.
    - imagen: Label para la imagen.
    - esShiny: Booleano, si es True muestra la imagen shiny.

    Salidas:
    - Ninguna (actualiza la interfaz).
    """
    try:
        datosPokemon = obtenerInfoPokemon(idPokemon, esShiny)
        if datosPokemon:
            for id, datos in datosPokemon.items():
                nombre.config(text=datos[0].capitalize())
                esShiny, peso, altura = datos[1]
                totalEstad, stats = datos[2]
                tipos = datos[3]
                urlImagen = datos[4]
                entradas["Peso:"].insert(0, f"{peso/10:.1f} kg")
                entradas["Altura:"].insert(0, f"{altura/10:.1f} m")
                tiposCap = []
                for t in tipos:
                    tipoCap = t.capitalize()
                    tiposCap.append(tipoCap)
                tiposStr = ""
                for i, tipo in enumerate(tiposCap):
                    tiposStr += tipo
                    if i < len(tiposCap) - 1:
                        tiposStr += "/"
                entradas["Tipos:"].insert(0, tiposStr)
                camposStats = ["PS:", "Ataque:", "Defensa:", "A Esp:", "D Esp:", "Veloc:"]
                for i, campoStat in enumerate(camposStats):
                    entradas[campoStat].insert(0, stats[i])
                entradas["Estad T:"].insert(0, totalEstad)
                cargarImagen(imagen, urlImagen)
    except Exception as e:
        print(f"Error al cargar el Pokémon: {e}")

def mostrarDetallePokemon(idPokemon, esShiny):
    """
    Funcionamiento:
    Muestra una ventana con los detalles de un Pokémon específico.

    Entradas:
    - idPokemon: ID del Pokémon.
    - esShiny: Booleano, si es True muestra la imagen shiny.

    Salidas:
    - Ventana de detalle de Pokémon.
    """
    ventana = tk.Toplevel()
    ventana.title("Detalle del Pokémon")
    ventana.resizable(False, False)

    marcoContenido = tk.Frame(ventana, bg="white")
    marcoContenido.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    marcoPokemon = tk.Frame(marcoContenido, bg="white")
    marcoPokemon.pack(fill=tk.X, padx=5, pady=5)

    nombrePokemon = tk.Label(marcoPokemon, font=("Arial", 12, "bold"), bg="white")
    nombrePokemon.pack(side=tk.LEFT, padx=5)

    labelShiny = tk.Label(marcoPokemon, font=("Arial", 10, "italic"), bg="white", fg="goldenrod")
    labelShiny.pack(side=tk.LEFT, padx=5)

    imagenLabel = tk.Label(marcoPokemon)
    imagenLabel.pack(side=tk.LEFT, padx=5)

    marcoDetalles = tk.Frame(marcoContenido)
    marcoDetalles.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    campos = ["Peso:", "Altura:", "Tipos:", "PS:", "Ataque:", "Defensa:", "A Esp:", "D Esp:", "Veloc:", "Estad T:"]
    entradas = {}
    for i, campo in enumerate(campos):
        tk.Label(marcoDetalles, text=campo, anchor=tk.W).grid(row=i, column=0, sticky=tk.W, pady=2)
        entrada = tk.Entry(marcoDetalles, width=15, relief=tk.SUNKEN, bd=1)
        entrada.grid(row=i, column=1, sticky=tk.W, pady=2, padx=5)
        entradas[campo] = entrada

    tk.Button(marcoContenido, text="Regresar", command=ventana.destroy).pack(pady=10)
    cargarPokemon(idPokemon, nombrePokemon, entradas, imagenLabel, esShiny)

    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    return ventana
# ##################################################
# 5 Descarga 
# ##################################################
"""
Descarga “Mis Pokémos” (siguiendo el simulacro, los 700 Pokémos), es decir, pasa toda la 
información del diccionario a un .csv, todo separado por comas. Esto durante la revisión, 
permite controlar datos desde Excel, facilitando así la revisión en tiempo real. Al dar click al 
botón se activa una ventana con mensaje de confirmación y ya. 
"""
def ejecutarDescarga(pokePad):
    """
    Funcionamiento:
    Muestra una ventana para descargar los Pokémon a un archivo CSV.

    Entradas:
    - pokePad: Instancia principal de la interfaz.

    Salidas:
    - Ninguna (genera archivo CSV y muestra mensajes).
    """
    ventanaDescarga = tk.Toplevel(pokePad.ventana)
    ventanaDescarga.title("Descargar Pokémon")
    ventanaDescarga.geometry("300x200")

    def descargar():
        try:
            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaArchivo = os.path.join(rutaBase, "MisPokemon.csv")
            rutaDiccionario = os.path.join(rutaBase, "DiccionarioPokemon.txt")
            with open(rutaArchivo, "w", encoding="utf-8") as archivoCsv:
                # Encabezados del CSV
                archivoCsv.write("id,nombre,shiny,peso,altura,total,ps,a,d,ae,de,v,tipos,url,estado\n")
                # Leer DiccionarioPokemon.txt para obtener toda la información
                if not os.path.exists(rutaDiccionario):
                    messagebox.showerror("Error", "No se encontró DiccionarioPokemon.txt. Genere el diccionario primero.")
                    return
                # Leer estados desde MisPokemon.txt
                estados = {}
                with open(os.path.join(rutaBase, "MisPokemon.txt"), "r", encoding="utf-8") as misPokemon:
                    for linea in misPokemon:
                        partes = linea.strip().split("^")
                        if len(partes) == 3:
                            estados[partes[0]] = partes[2]
                # Leer y escribir toda la info
                with open(rutaDiccionario, "r", encoding="utf-8") as diccionario:
                    for linea in diccionario:
                        partes = linea.strip().split("^")
                        if len(partes) == 6:
                            idPoke = partes[0]
                            nombre = partes[1]
                            tupla = eval(partes[2])
                            esShiny = tupla[0]
                            peso = tupla[1]
                            altura = tupla[2]
                            totalStats = eval(partes[3])
                            total = totalStats[0]
                            stats = totalStats[1]
                            tipos = eval(partes[4])
                            tiposStr = ""
                            for i, tipo in enumerate(tipos):
                                tiposStr += str(tipo)
                                if i < len(tipos) - 1:
                                    tiposStr += "|"
                            url = partes[5]
                            estado = estados.get(idPoke, "")
                            statsStr = ""
                            for i, s in enumerate(stats):
                                statsStr += str(s)
                                if i < len(stats) - 1:
                                    statsStr += ","
                            archivoCsv.write(f"{idPoke},{nombre},{esShiny},{peso},{altura},{total},{statsStr},{tiposStr},{url},{estado}\n")
            messagebox.showinfo("Éxito", f"Pokémon guardados en:\n{rutaArchivo}")
            ventanaDescarga.destroy()
        except Exception as error:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {error}")

    def confirmarDescarga():
        if messagebox.askyesno("Confirmar descarga", "¿Deseas descargar los Pokémon a un archivo CSV?"):
            descargar()

    ttk.Button(ventanaDescarga, text="Descargar Pokémon", command=confirmarDescarga).pack(pady=20)
# ##################################################
# 6 XML
# ##################################################

def ejecutarXML(pokepad):
    """
    Funcionamiento:
    Muestra una ventana para exportar los Pokémon huidos a un archivo XML.
    Entradas:
    - pokepad: Instancia principal de la interfaz.
    Salidas:
    - Ninguna (genera archivo XML y muestra mensajes).
    """
    ventanaXML = tk.Toplevel(pokepad.ventana)
    ventanaXML.title("Exportar Pokémon huidos a XML")
    ventanaXML.geometry("320x180")
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
        with open(archivoXml, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

    def exportarXML():
        huidos = buscarHuidos()
        if not huidos:
            messagebox.showinfo("Sin huidos", "No hay Pokémon que hayan huido.")
            ventanaXML.destroy()
            return
        diccPokemones = {}
        for idPoke, i in huidos:
            info = obtenerInfoPokemon(idPoke, esShiny=random.choice([True, False]))
            if info:
                diccPokemones.update(info)
        if diccPokemones:
            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaArchivo = os.path.join(rutaBase, "pokemonesHuidos.xml")
            xml = construirXML(diccPokemones)
            escribirXml(rutaArchivo, xml)
            messagebox.showinfo("Éxito", f"Archivo XML generado en:\n{rutaArchivo}")
            ventanaXML.destroy()
        else:
            messagebox.showerror("Error", "No se pudo obtener información de los Pokémon.")

    def confirmarXML():
        if messagebox.askyesno("Confirmar exportación", "¿Deseas exportar los Pokémon huidos a XML?"):
            exportarXML()

    ttk.Button(ventanaXML, text="Exportar a XML", command=confirmarXML).pack(pady=30)
# ##################################################
# 7 HTML Descarga
# ##################################################
def ejecutarHTML(pokepad):
    """
    Funcionamiento:
    Muestra una ventana para generar archivos HTML con los Pokémon huidos.

    Entradas:
    - pokepad: Instancia principal de la interfaz.

    Salidas:
    - Ninguna (genera archivos HTML y muestra mensajes).
    """
    ventanaHTML = tk.Toplevel(pokepad.ventana)
    ventanaHTML.title("Generar HTML de Pokémon Huidos")
    ventanaHTML.geometry("300x200")

    def construirHTML(pokemones, desde):
        html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Pokémon Huidos</title>
    <style>
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: center; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Pokémon Huidos</h1>
        <table>
            <tr>
                <th>#</th>
                <th>ID</th>
                <th>Nombre</th>
                <th>Total Estadísticas</th>
            </tr>
"""
        for idx, (idPoke, nombre, totalEstats) in enumerate(pokemones, start=desde):
            html += f"""            <tr>
                <td>{idx}</td>
                <td>{idPoke}</td>
                <td style="text-transform:capitalize">{nombre}</td>
                <td>{totalEstats}</td>
            </tr>
"""
        html += """        </table>
    </div>
</body>
</html>"""
        return html

    def generarHTML():
        huidos = buscarHuidos()
        if not huidos:
            messagebox.showinfo("Sin huidos", "No hay Pokémon que hayan huido.")
            ventanaHTML.destroy()
            return

        listaPokemones = []
        for idPoke, _ in huidos:
            info = obtenerInfoPokemon(idPoke, soloBasico=True)
            if info and isinstance(info, tuple) and len(info) == 3:
                listaPokemones.append(info)

        if not listaPokemones:
            messagebox.showerror("Error", "No se pudo obtener información de los Pokémon.")
            return

        listaPokemones.sort(key=lambda x: x[2], reverse=True)

        bloque = 100
        total = len(listaPokemones)
        archivos = []
        for i in range(0, total, bloque):
            desde = i + 1
            pokesBloque = listaPokemones[i:i + bloque]
            html = construirHTML(pokesBloque, desde)
            rutaBase = os.path.dirname(os.path.abspath(__file__))
            nombreArchivo = os.path.join(rutaBase, f"pokemonesHuidos_{desde}_{desde+len(pokesBloque)-1}.html")
            with open(nombreArchivo, "w", encoding="utf-8") as f:
                f.write(html)
            archivos.append(nombreArchivo)

        messagebox.showinfo("Éxito", f"Se generaron {len(archivos)} archivos HTML en la carpeta del proyecto.")
        ventanaHTML.destroy()

    def confirmarHTML():
        if messagebox.askyesno("Confirmar generación", "¿Quiere generar el HTML de los pokémons huidos?"):
            generarHTML()

    ttk.Button(ventanaHTML, text="Generar HTML", command=confirmarHTML).pack(pady=20)

# ##################################################
# 8 HTML es Shiny
# ##################################################
def ejecutarEsShiny(pokepad):
    """
    Funcionamiento:
    Muestra una ventana para generar archivos HTML con los Pokémon shiny.
    """
    ventanaShiny = tk.Toplevel(pokepad.ventana)
    ventanaShiny.title("Generar HTML de Pokémon Shiny")
    ventanaShiny.geometry("300x200")

    diccPoke = leerDiccionario()

    def shinys(diccPoke):
        shinys = {}
        for idPoke, datos in diccPoke.items():
            esShiny = datos[1][0]
            if esShiny:
                shinys[idPoke] = datos
        return shinys

    def generarHtml(pagina, numeroPagina):
        rutaBase = os.path.dirname(os.path.abspath(__file__))
        nombreArchivo = os.path.join(rutaBase, f"Shinys{numeroPagina}.html")
        with open(nombreArchivo, "w", encoding="utf-8") as archivo:
            encabezado = """<!DOCTYPE html>
    <html>
    <head>
        <title>Pokémon Shinys</title>
        <style>
            table { border-collapse: collapse; width: 100%; }
            th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
            th { background-color: #ffcc00; color: black; }
            tr:nth-child(even) { background-color: #f2f2f2; }
            img { width: 80px; }
        </style>
    </head>
    <body>
        <h1>Lista de Pok&eacutemons Shiny</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Shiny</th>
                <th>Peso (g)</th>
                <th>Altura (cm)</th>
                <th>Estadísticas</th>
                <th>Total</th>
                <th>Tipos</th>
                <th>Imagen</th>
            </tr>
    """
            archivo.write(encabezado)
            for idPoke, datos in pagina:
                nombre = datos[0]
                tupla = datos[1]
                shiny = tupla[0]
                peso = tupla[1]
                altura = tupla[2]
                estadisticas = datos[2]
                totalStats = estadisticas[0]
                stats = estadisticas[1]
                tiposLista = datos[3]
                tiposStr = ""
                for i, tipo in enumerate(tiposLista):
                    if i > 0:
                        tiposStr += ", "
                    tiposStr += tipo
                url = datos[4]
                filaHtml = f"""
            <tr>
                <td>{idPoke}</td>
                <td>{nombre}</td>
                <td>{shiny}</td>
                <td>{peso}</td>
                <td>{altura}</td>
                <td>{stats}</td>
                <td>{totalStats}</td>
                <td>{tiposStr}</td>
                <td><img src="{url}" alt="{nombre}"></td>
            </tr>
    """
                archivo.write(filaHtml)
            cierre = """
        </table>
    </body>
    </html>
    """
            archivo.write(cierre)
    def generarReportes():
        diccPoke = leerDiccionario()
        shinysFiltrados = shinys(diccPoke)
        listaShinys = list(shinysFiltrados.items())
        if not listaShinys:
            messagebox.showinfo("Sin shinys", "No hay Pokémon shiny en el diccionario.")
            ventanaShiny.destroy()
            return
        paginas = dividirPaginas(listaShinys, 100)
        for idx, pagina in enumerate(paginas, start=1):
            generarHtml(pagina, idx)
        messagebox.showinfo("Éxito", f"Se generaron {len(paginas)} archivo(s) HTML con Pokémon shiny.")
        ventanaShiny.destroy()

    def confirmarShiny():
        if messagebox.askyesno("Confirmar generación", "¿Quiere generar el HTML de los pokémons shiny?"):
            generarReportes()

    ttk.Button(ventanaShiny, text="Generar HTML", command=confirmarShiny).pack(pady=20)

# ##################################################
# 9  Convertidor
# ##################################################

def ejecutarConvertidor(pokepad):
    """
    Convierte de diccionario a matriz y guarda en la memoria secundaria
    con el siguiente formato:
    [
        [
        id, nombre, [esShiny, peso, altura], 
        [totalE, [PS,A,D,AE,DE,V]],
        ["listaDeTipos","listaDeTipos"],
        url
        ]
    ]
    Al dar click al botón se activa una ventana con mensaje de confirmación y muestra en el shell
    la estructura creada. También modifica el archivo DiccionarioPokemon.txt para que se guarde en formato de matriz.
    """
    ventanaConvertidor = tk.Toplevel(pokepad.ventana)
    ventanaConvertidor.title("Convertidor de Diccionario a Matriz")
    ventanaConvertidor.geometry("300x200")

    matriz = []  # Se define aquí para que esté disponible en ambas funciones internas

    def convertir():
        rutaBase = os.path.dirname(os.path.abspath(__file__))
        rutaArchivo = os.path.join(rutaBase, "DiccionarioPokemon.txt")
        diccionario = {}

        try:
            with open(rutaArchivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    partes = linea.strip().split("^")
                    if len(partes) == 6:
                        idPoke = partes[0]
                        nombre = partes[1]
                        datosFisicos = eval(partes[2])
                        estadisticas = eval(partes[3])
                        tipos = eval(partes[4])
                        url = partes[5]
                        diccionario[idPoke] = [nombre, datosFisicos, estadisticas, tipos, url]
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
            ventanaConvertidor.destroy()
            return

        matriz.clear()
        for idPoke, datos in diccionario.items():
            nombre = datos[0]
            esShiny, peso, altura = datos[1]
            totalEstadisticas, statsTupla = datos[2]
            tipos = datos[3]
            url = datos[4]
            matriz.append([
                int(idPoke), 
                nombre,
                [esShiny, peso, altura],
                [totalEstadisticas, statsTupla],
                tipos,
                url
            ])
        print("Matriz generada:")
        for fila in matriz:
            print(fila)

        messagebox.showinfo("Éxito", "Conversión completada. Ver la terminal o shell para detalles.")

    def guardarEnArchivo():
        if not matriz:
            messagebox.showwarning("Advertencia", "Primero debes convertir antes de guardar.")
            return

        rutaBase = os.path.dirname(os.path.abspath(__file__))
        rutaArchivo = os.path.join(rutaBase, "DiccionarioPokemon.txt")
        try:
            with open(rutaArchivo, "w", encoding="utf-8") as archivo:
                for fila in matriz:
                    archivo.write(f"{fila}\n")
            messagebox.showinfo("Éxito", "Archivo guardado correctamente.")
            ventanaConvertidor.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
            ventanaConvertidor.destroy()

    ttk.Button(ventanaConvertidor, text="Convertir", command=convertir).pack(pady=20)
    ttk.Button(ventanaConvertidor, text="Guardar en archivo", command=guardarEnArchivo).pack(pady=20)

# ##################################################
# 10 Desconvertidor
# ##################################################
def ejecutarDesconvertidor(pokepad):
    """
    Funcionamiento:
    Muestra una ventana para convertir el archivo DiccionarioPokemon.txt a un diccionario en memoria.

    Entradas:
    - pokepad: Instancia principal de la interfaz.

    Salidas:
    - Ninguna (actualiza variable global y muestra mensajes).
    """
    ventanaDesconvertidor = tk.Toplevel(pokepad.ventana)
    ventanaDesconvertidor.title("Desconvertir Matriz a Diccionario")
    ventanaDesconvertidor.geometry("300x200")

    def desconvertir():
        rutaBase = os.path.dirname(os.path.abspath(__file__))
        rutaDiccionario = os.path.join(rutaBase, "DiccionarioPokemon.txt")
        nuevoDiccionario = {}

        try:
            if not os.path.exists(rutaDiccionario):
                messagebox.showwarning("Archivo no encontrado", "No se encontró el archivo DiccionarioPokemon.txt")
                return

            with open(rutaDiccionario, "r", encoding="utf-8") as file:
                lineas = file.readlines()

            for linea in lineas:
                fila = eval(linea.strip())  # Convierte la línea string (lista) a lista real de Python.
                if len(fila) == 6:
                    idPokemon = int(fila[0])
                    nombre = fila[1]
                    datosFisicos = tuple(fila[2])     # [esShiny, peso, altura]
                    estadisticas = fila[3]            # [totalE, [PS,A,D,AE,DE,V]]
                    tipos = fila[4]                   # ["tipo1", "tipo2"]
                    url = fila[5]

                    nuevoDiccionario[idPokemon] = [
                        nombre,
                        datosFisicos,
                        estadisticas,
                        tipos,
                        url
                    ]

            # Guardar nuevamente el archivo en el formato original
            with open(rutaDiccionario, "w", encoding="utf-8") as archivo:
                for idPoke, datos in nuevoDiccionario.items():
                    nombre = datos[0]
                    esShiny, peso, altura = datos[1]
                    estadisticas = datos[2]
                    tipos = datos[3]
                    url = datos[4]
                    linea = f"{idPoke}^{nombre}^{(esShiny, peso, altura)}^{estadisticas}^{tipos}^{url}\n"
                    archivo.write(linea)

            # Actualizar variable global
            global diccionarioPokemon
            diccionarioPokemon = nuevoDiccionario

            print(f"{diccionarioPokemon}\n")
            messagebox.showinfo("Éxito", "Diccionario restaurado correctamente y archivo reescrito.")
            ventanaDesconvertidor.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo desconvertir:\n{e}")

    ttk.Button(ventanaDesconvertidor, text="Desconvertir", command=desconvertir).pack(pady=20)

# ##################################################
# 11 Virus
# ##################################################
"""
el virus masivo requiere saber:
    A) si se aumenta o si disminuye
    B) el porcentaje
Las estadísticas de todo el diccionari. Luego de obtenida la información, afecte todo el diciconario
según corresponda en las estadísticas. Al dar click al botón se activa una ventana de confirmación
y muestra en el shell la estructura cambiada.
'todo se hará mediante botones de radio para cada opción, y un campo de texto para el porcentaje como 
numero entero.
y botones para ejecutar, limpiar y salir.'
"""
def ejecutarVirus(pokePad):
    """
    Funcionamiento:
    Muestra una ventana para aplicar un "virus" que aumenta o disminuye las estadísticas de todos los Pokémon según un porcentaje.

    Entradas:
    - pokePad: Instancia principal de la interfaz.

    Salidas:
    - Ninguna (modifica archivo y muestra mensajes).
    """
    ventanaVirus = tk.Toplevel(pokePad.ventana)
    ventanaVirus.title("Aplicar Virus a estadística de los Pokémons")
    ventanaVirus.geometry("480x420")
    ventanaVirus.minsize(480, 420)

    ventanaVirus.columnconfigure(0, weight=1)
    ventanaVirus.rowconfigure(4, weight=1)

    ttk.Label(ventanaVirus, text="Seleccione la acción del virus:").grid(row=0, column=0, pady=(20, 10), padx=20, sticky="ew")

    accionVirus = tk.StringVar(value="aumentar")
    frameRadios = ttk.Frame(ventanaVirus)
    frameRadios.grid(row=1, column=0, pady=5, padx=30, sticky="w")
    ttk.Radiobutton(frameRadios, text="Aumentar Estadísticas", variable=accionVirus, value="aumentar").pack(anchor=tk.W, pady=2)
    ttk.Radiobutton(frameRadios, text="Disminuir Estadísticas", variable=accionVirus, value="disminuir").pack(anchor=tk.W, pady=2)

    ttk.Label(ventanaVirus, text="Ingrese el porcentaje (número entero):").grid(row=2, column=0, pady=(20, 5), padx=20, sticky="ew")
    entradaPorcentajeVirus = ttk.Entry(ventanaVirus)
    entradaPorcentajeVirus.grid(row=3, column=0, pady=5, padx=30, sticky="ew")

    areaResultadoVirus = tk.Text(ventanaVirus, height=12, width=60, state="disabled")
    areaResultadoVirus.grid(row=4, column=0, pady=20, padx=20, sticky="nsew")

    frameBotonesVirus = ttk.Frame(ventanaVirus)
    frameBotonesVirus.grid(row=5, column=0, pady=(0, 20), sticky="ew")
    frameBotonesVirus.columnconfigure((0, 1, 2), weight=1)

    def ejecutarCapturaVirus():
        try:
            porcentajeStr = entradaPorcentajeVirus.get()
            if not porcentajeStr.isdigit():
                messagebox.showerror("Error", "Debe escriba solamente números donde se solicita el porcentaje")
                return
            porcentaje = int(porcentajeStr)
            if not (0 <= porcentaje <= 100):
                raise ValueError("El porcentaje debe estar entre 0 y 100.")

            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaDiccionario = os.path.join(rutaBase, "DiccionarioPokemon.txt")
            diccionarioPokemon = {}
            with open(rutaDiccionario, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    partes = linea.strip().split("^")
                    if len(partes) == 6:
                        idPoke = int(partes[0])
                        nombre = partes[1]
                        esShiny, peso, altura = eval(partes[2])  # Convierte el string de la tupla (esShiny, peso, altura) a tupla real.
                        totalEstadisticas, tuplaEstadisticas = eval(partes[3])  # Convierte el string de la lista [total, (stats...)] a lista real.
                        tipos = eval(partes[4])  # Convierte el string de la tupla de tipos a tupla real.
                        urlImagen = partes[5]
                        diccionarioPokemon[idPoke] = [
                            nombre,
                            (esShiny, peso, altura),
                            [totalEstadisticas, tuplaEstadisticas],
                            tipos,
                            urlImagen
                        ]
            for idPoke, datos in diccionarioPokemon.items():
                nombre = datos[0]
                esShiny, peso, altura = datos[1]
                totalEstadisticas, tuplaEstadisticas = datos[2]
                tipos = datos[3]
                urlImagen = datos[4]
                if accionVirus.get() == "aumentar":
                    porcentajeAjuste = 1 + (porcentaje / 100)
                else:
                    porcentajeAjuste = 1 - (porcentaje / 100)
                estadisticasAjustadas = []
                for stat in tuplaEstadisticas:
                    estadisticasAjustadas.append(int(stat * porcentajeAjuste))
                estadisticasAjustadas = tuple(estadisticasAjustadas)
                totalEstadisticasAjustadas = sum(estadisticasAjustadas)
                diccionarioPokemon[idPoke] = [
                    nombre,
                    (esShiny, peso, altura),
                    [totalEstadisticasAjustadas, estadisticasAjustadas],
                    tipos,
                    urlImagen
                ]
            with open(rutaDiccionario, "w", encoding="utf-8") as archivo:
                for idPoke, datos in diccionarioPokemon.items():
                    nombre = datos[0]
                    esShiny, peso, altura = datos[1]
                    totalEstadisticas, tuplaEstadisticas = datos[2]
                    tipos = datos[3]
                    urlImagen = datos[4]
                    archivo.write(f"{idPoke}^{nombre}^{(esShiny, peso, altura)}^{[totalEstadisticas, tuplaEstadisticas]}^{tipos}^{urlImagen}\n")
            areaResultadoVirus.config(state="normal")
            areaResultadoVirus.delete(1.0, tk.END)
            areaResultadoVirus.insert(tk.END, "Estructura de Pokémon después del virus:\n")
            for idPoke, datos in diccionarioPokemon.items():
                nombre = datos[0]
                esShiny, peso, altura = datos[1]
                totalEstadisticas, tuplaEstadisticas = datos[2]
                tipos = datos[3]
                urlImagen = datos[4]
                areaResultadoVirus.insert(tk.END, f"{idPoke}: [{nombre}, ({esShiny}, {peso}, {altura}), [{totalEstadisticas}, {tuplaEstadisticas}], {tipos}, '{urlImagen}']\n")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
        finally:
            areaResultadoVirus.config(state="disabled")

    def limpiarVirus():
        entradaPorcentajeVirus.delete(0, tk.END)
        areaResultadoVirus.config(state="normal")
        areaResultadoVirus.delete("1.0", tk.END)
        areaResultadoVirus.config(state="disabled")

    ttk.Button(frameBotonesVirus, text="Ejecutar Virus", command=ejecutarCapturaVirus).grid(row=0, column=0, padx=15, sticky="ew")
    ttk.Button(frameBotonesVirus, text="Limpiar", command=limpiarVirus).grid(row=0, column=1, padx=15, sticky="ew")
    ttk.Button(frameBotonesVirus, text="Cerrar", command=ventanaVirus.destroy).grid(row=0, column=2, padx=15, sticky="ew")

# ##################################################
# 12 Agregar pokemon
# ##################################################

def ejecutarAgregar(pokepad):
    """
    Funcionamiento:
    Muestra una ventana para agregar un nuevo Pokémon por ID si no existe.

    Entradas:
    - pokepad: Instancia principal de la interfaz.

    Salidas:
    - Ninguna (agrega Pokémon y muestra mensajes).
    """
    ventanaAgregar = tk.Toplevel(pokepad.ventana)
    ventanaAgregar.title("Agregar Pokémon")
    ventanaAgregar.geometry("400x250")

    ventanaAgregar.columnconfigure(0, weight=1)
    marco = ttk.Frame(ventanaAgregar, padding="10")
    marco.grid(row=0, column=0, sticky="nsew")

    ttk.Label(marco, text="Ingrese el ID del Pokémon a agregar:").grid(row=0, column=0, pady=5, sticky="w")
    entradaID = ttk.Entry(marco)
    entradaID.grid(row=1, column=0, pady=5, sticky="ew", columnspan=2)

    infoLabel = ttk.Label(marco, text="", wraplength=350)
    infoLabel.grid(row=2, column=0, columnspan=2, pady=10)

    marcoBotones = ttk.Frame(marco)
    marcoBotones.grid(row=3, column=0, columnspan=2, pady=10)

    ttk.Button(marcoBotones, text="Agregar", command=lambda: manejarAgregarPokemon(entradaID, infoLabel, ventanaAgregar)).grid(row=0, column=0, padx=5)
    ttk.Button(marcoBotones, text="Cancelar", command=ventanaAgregar.destroy).grid(row=0, column=1, padx=5)

def manejarAgregarPokemon(entradaID, infoLabel, ventanaAgregar):
    """
    Funcionamiento:
    Maneja la lógica para agregar un Pokémon desde la ventana de agregar.

    Entradas:
    - entradaID: Campo de entrada del ID.
    - infoLabel: Label para mostrar mensajes.
    - ventanaAgregar: Ventana de agregar Pokémon.

    Salidas:
    - Ninguna (agrega Pokémon y muestra mensajes).
    """
    def mostrarMensaje(label, texto, color):
        label.config(text=texto, foreground=color)
    try:
        idPoke = int(entradaID.get())
        if not 1 <= idPoke <= 1025:
            mostrarMensaje(infoLabel, "Error: El ID debe estar entre 1 y 1025", "red")
            return

        if pokemonYaExiste(idPoke):
            mostrarMensaje(infoLabel, f"Error: El Pokémon con ID {idPoke} ya existe", "red")
            return

        pokemonInfo = obtenerDatosPokemon(idPoke)
        if pokemonInfo is None:
            mostrarMensaje(infoLabel, f"Error: No se encontró Pokémon con ID {idPoke}", "red")
            return

        guardarPokemon(pokemonInfo)
        messagebox.showinfo("Éxito", f"¡{pokemonInfo['nombre']} agregado correctamente!")
        statsTupla = tuple(pokemonInfo['stats'])
        totalStats = sum(pokemonInfo['stats'])
        print(
            f"{pokemonInfo['id']}^{pokemonInfo['nombre']}^"
            f"({pokemonInfo['esShiny']}, {pokemonInfo['peso']}, {pokemonInfo['altura']})^"
            f"[{totalStats}, {statsTupla}]^"
            f"{pokemonInfo['tipos']}^"
            f"{pokemonInfo['imagen']}"
        )
        ventanaAgregar.destroy()
    except ValueError:
        mostrarMensaje(infoLabel, "Error: Ingrese un número válido", "red")
    except requests.RequestException:
        mostrarMensaje(infoLabel, "Error: No se pudo conectar con la API", "red")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo agregar el Pokémon: {str(e)}")

# ##################################################
# 13 Créditos
# ##################################################
"""
La pareja de programadores es libre de crear la ventana que gusten para indicar sus 
creadores intelectuales, pero ello debe construirse, al finalizar la totalidad de requerimientos 
que indicó el usuario. Para ello pueden crear la estrategia que gusten, claro está primero se 
cumple el 100% de los requerimientos con calidad.  
"""
def ejecutarCreditos(pokepad):
    """
    Funcionamiento:
    Muestra una ventana con los créditos de los creadores del programa.

    Entradas:
    - pokepad: Instancia principal de la interfaz.

    Salidas:
    - Ninguna (muestra ventana de créditos).
    """
    ventanaCréditos = tk.Toplevel(pokepad.ventana)
    ventanaCréditos.title("Créditos")
    ventanaCréditos.geometry("350x320")

    textoCreditos = (
        "Créditos:\n"
        "1. Búsqueda de Pokémon - Tinoco\n"
        "2. Atrapar Pokémon - Matias Benavides\n"
        "3. Pokédex - Tinoco\n"
        "4. Detalles - Matias Benavides\n"
        "5. Reportes - Tinoco\n"
        "6. XML - Matias Benavides\n"
        "7. HTML Descendente - Tinoco\n"
        "8. Shiny - Matias Benavides\n"
        "9. Convertidor - Tinoco\n"
        "10. Desconvertidor - Matias Benavides\n"
        "11. Virus - Tinoco\n"
        "12. Agregar Pokémon - Matias Benavides\n"
        "Interfaz - Tinoco\n"
    )

    label = ttk.Label(ventanaCréditos, text=textoCreditos, justify="left", anchor="w")
    label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
    ttk.Button(ventanaCréditos, text="Cerrar", command=ventanaCréditos.destroy).grid(row=1, column=0, pady=10)