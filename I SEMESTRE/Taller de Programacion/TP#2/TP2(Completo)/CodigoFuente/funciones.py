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

# ##################################################3
# 1 Busqueda de pokémons 
# ##################################################

def ejecutarBusqueda(pokepad):
    """
        Ventana emergente para buscar pokémon y guardar resultados en un archivo.
        Si el usuario selecciona la opción 1, 
        se abrirá una ventana emergente donde
        se le solicitará la cantidad de pokemon que desea buscar,
        Función para solicitar cantidad de pokemon que se extraeran de Pokeapi, mientras estase a >0 y < pokeapi arroja
        estos pokemon se extraeran de la página  "PokeAPI: https://pokeapi.co/" y dependiendo la cantidad solicitada por el usuario se guardará en un archivo .txt llamado 
        "Mis Pokemones.txt"
        todo esto mediante una caja de texto con el siguiente formato:
        -título "busqueda de pokémons"
        -texto "cantidad de pokémons deseada": -celda para escribir la cantidad de pokémons deseada
        -botón "buscar" - botón "Limpiar"
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

# =============================2 Atrapar pokémons =============================
def ejecutarAtrapar(pokepad):
    """
    Ventana emergente para atrapar Pokémon según porcentaje indicado por el usuario.
    Muestra los resultados y modifica el estado en el archivo MisPokemon.txt.
    """
    ventanaAtrapar = tk.Toplevel(pokepad.ventana)
    ventanaAtrapar.title("Atrapar Pokémon")
    ventanaAtrapar.geometry("420x320")

    ttk.Label(ventanaAtrapar, text="¿Qué porcentaje de Pokémon quieres atrapar?").pack(pady=10)
    entradaPorcentaje = ttk.Entry(ventanaAtrapar)
    entradaPorcentaje.pack(pady=5)

    areaResultado = tk.Text(ventanaAtrapar, height=12, width=55, state="disabled")
    areaResultado.pack(pady=8)

    def buscarTxt():
        pokemon = []  # Lista para guardar tuplas (id, nombre)
        try:
            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaArchivo = os.path.join(rutaBase, "MisPokemon.txt")
            with open(rutaArchivo, "r") as file:
                for line in file:
                    linea = line.strip()  # Elimina espacios y saltos de línea
                    if linea:  # Si la línea no está vacía
                        partes = linea.split("^")  # Separa por el carácter ^
                        if len(partes) == 2:
                            idPokedex = partes[0].strip()
                            nombre = partes[1].strip()
                            pokemon.append((idPokedex, nombre))
                        elif len(partes) == 3:
                            idPokedex = partes[0].strip()
                            nombre = partes[1].strip()
                            # Ignora el estado anterior, lo sobreescribiremos
                            pokemon.append((idPokedex, nombre))
                        else:
                            print(f"Línea mal formada: {linea}")
            if not pokemon:
                print("El archivo está vacío o no contiene datos válidos.")
        except FileNotFoundError:
            print("El archivo 'MisPokemon.txt' no existe.")
        return pokemon  # Retornamos la lista (vacía si falla)

    def guardarEstadosPokemon(atrapados, huidos):
        rutaBase = os.path.dirname(os.path.abspath(__file__))
        nombreArchivo = os.path.join(rutaBase, "MisPokemon.txt")
        todos = []
        for idPoke, nombre in atrapados: #Pokemon atrapados
            idPoke = int(idPoke)
            estado = "a"
            todos.append((idPoke, nombre, "a")) #Pokemon que huyeron
        for idPoke, nombre in huidos:
            idPoke = int(idPoke)
            estado = "h"
            todos.append((idPoke, nombre, "h"))
        todos.sort(key=lambda x: x[0])
        with open(nombreArchivo, "w") as file:
            for idPoke, nombre, estado in todos:
                file.write(f"{idPoke}^{nombre}^{estado}\n")

    def atraparPokeAux(porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            return "Porcentaje no válido. Debe estar entre 0 y 100."
        else:
            print(f"Porcentaje válido. Procediendo a atrapar el {porcentaje} de los Pokémon.")
            return atraparPoke(porcentaje)

    def atraparPoke(porcentaje):
        pokemon = buscarTxt()
        if not pokemon:
            return "No hay Pokémon para atrapar."
        totalPokemon = len(pokemon)
        cantidadAtrapados  = round((porcentaje / 100) * totalPokemon)
        cantidadHuyeron = totalPokemon - cantidadAtrapados
        atrapados = random.sample(pokemon, cantidadAtrapados)
        huidos = []
        for poke in pokemon:
            if poke not in atrapados:
                huidos.append(poke)
        print(f"Pokémon atrapados: {cantidadAtrapados}")
        print(f"Pokémon que huyeron: {cantidadHuyeron}")
        for idPoke, nombre in atrapados:
            print(f"ID: {idPoke}, Nombre: {nombre}")
        print("Pokémon que huyeron:")
        for idPoke, nombre in huidos:
            print(f"ID: {idPoke}, Nombre: {nombre}")
        guardarEstadosPokemon(atrapados, huidos)
        return atrapados, huidos

    def listaAtrapados(atrapados):
        listaIds = []
        for poke in atrapados:
            idPoke = int(poke[0])
            listaIds.append(idPoke)
        return listaIds

    def obtenerInfoPokemon(idPoke):
        url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
        try:
            respuesta = requests.get(url, timeout=8)
            datos = respuesta.json()

            idApi = datos['id']
            nombre = datos['name']
            esShiny = random.choice([True, False])
            peso = datos['weight'] * 10  # en gramos
            altura = datos['height'] * 10  # en centímetros

            # Estadísticas ordenadas
            statsOrden = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
            statsValores = []
            for statNombre in statsOrden:
                for stat in datos['stats']:
                    if stat['stat']['name'] == statNombre:
                        statsValores.append(stat['base_stat'])
                        break

            totalEstats = sum(statsValores)
            statsTupla = tuple(statsValores)

            # Obtener los tipos del Pokémon desde la estructura de datos
            tipos = []
            for tipo_info in datos['types']:
                tipo_nombre = tipo_info['type']['name']
                tipos.append(tipo_nombre)
            tipos = tuple(tipos)  # Convertimos la lista a una tupla para que sea inmutable

            # Determinar la URL de la imagen según si el Pokémon es shiny o no
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

    def imprimirInfoPokemon(diccPoke):
        for idPoke, datos in diccPoke.items():
            nombre = datos[0]
            esShiny, peso, altura = datos[1]
            totalEstad, stats = datos[2]
            tipos = datos[3]
            urlImagen = datos[4]
            print(f"ID: {idPoke}:")
            print("[")
            print(f"  '{nombre}',")
            print(f"  ({esShiny}, {peso}, {altura}),")
            print(f"  [{totalEstad}, {stats}],")
            print(f"  {tipos},")
            print(f"  '{urlImagen}'")
            print("]")
            print()

    def ejecutarCaptura():
        # Habilita el área de resultados para poder escribir en ella.
        areaResultado.config(state="normal")
        # Limpia el área de resultados antes de mostrar nuevos resultados.
        areaResultado.delete("1.0", tk.END)
        try:
            # Intenta convertir el valor ingresado por el usuario a entero.
            porcentaje = int(entradaPorcentaje.get())
            # Llama a la función que valida el porcentaje y ejecuta la lógica de captura.
            resultado = atraparPokeAux(porcentaje)
            # Si la función retorna una tupla, significa que la captura fue exitosa.
            if isinstance(resultado, tuple):
                atrapados, huidos = resultado
                # Muestra la cantidad de Pokémon atrapados en el área de resultados.
                areaResultado.insert(tk.END, f"Pokémon atrapados: {len(atrapados)}\n")
                # Muestra la cantidad de Pokémon que huyeron.
                areaResultado.insert(tk.END, f"Pokémon que huyeron: {len(huidos)}\n")
                # Lista los Pokémon atrapados.
                for idPoke, nombre in atrapados:
                    areaResultado.insert(tk.END, f"ID: {idPoke}, Nombre: {nombre}\n")
                # Encabezado para los Pokémon que huyeron.
                areaResultado.insert(tk.END, "Pokémon que huyeron:\n")
                # Lista los Pokémon que huyeron.
                for idPoke, nombre in huidos:
                    areaResultado.insert(tk.END, f"ID: {idPoke}, Nombre: {nombre}\n")
                # Mensaje de proceso completado.
                areaResultado.insert(tk.END, "Proceso de captura completado.\n\n")
                # Obtiene los IDs de los Pokémon atrapados.
                listaIdAtrapados = listaAtrapados(atrapados)
                diccPoke = {}
                # Obtiene la información detallada de cada Pokémon atrapado desde la API.
                for id in listaIdAtrapados:
                    info = obtenerInfoPokemon(id)
                    if info:
                        diccPoke.update(info)
                """estos imports son para poder imprimir el diccionario en el área de resultados en la interfaz gráfica en el cuadro de texto
                pero no afecta en nada al funcionamiento del programa, solo es para que se vea más bonito y que las salidas se vean no solo modifican el .txt
                """
                import io
                import sys
                buffer = io.StringIO()
                sys_stdout = sys.stdout
                sys.stdout = buffer
                imprimirInfoPokemon(diccPoke)
                sys.stdout = sys_stdout
                areaResultado.insert(tk.END, buffer.getvalue())
            else:
                # Si el resultado no es una tupla, es un mensaje de error o advertencia.
                areaResultado.insert(tk.END, f"{resultado}\n")
        except ValueError:
            # Si el usuario no ingresó un número válido, muestra un mensaje de error.
            areaResultado.insert(tk.END, "Por favor, ingresa un número válido.\n")
        # Deshabilita el área de resultados para evitar que el usuario la edite.
        areaResultado.config(state="disabled")

    def limpiar():
        entradaPorcentaje.delete(0, tk.END)
        areaResultado.config(state="normal")
        areaResultado.delete("1.0", tk.END)
        areaResultado.config(state="disabled")

    marcoBotones = ttk.Frame(ventanaAtrapar)
    marcoBotones.pack(pady=5)
    ttk.Button(marcoBotones, text="Atrapar", command=ejecutarCaptura).pack(side="left", padx=10)
    ttk.Button(marcoBotones, text="Limpiar", command=limpiar).pack(side="left", padx=10)
    ttk.Button(marcoBotones, text="Cerrar", command=ventanaAtrapar.destroy).pack(side="left", padx=10)

#==================================== 3. Pokédex ============================



def ejecutarPokedex(pokePad):
    ventanaPokedex = tk.Toplevel()
    ventanaPokedex.title("Pokédex")
    ventanaPokedex.configure(bg="white")

    # Parámetros de visualización
    filas, columnas = 5, 5
    porPagina = filas * columnas
    paginaActual = [0]

    # URL de imagen de interrogación
    URL_INTERROGACION = "https://upload.wikimedia.org/wikipedia/commons/5/55/Question_Mark.svg"

    # Cargar imagen de interrogación desde la web
    interrogacionPil = Image.open(BytesIO(requests.get(URL_INTERROGACION).content))
    interrogacionPil.thumbnail((90, 90), Image.LANCZOS)
    interrogacionImg = ImageTk.PhotoImage(interrogacionPil)

    # Leer pokémones desde archivo
    try:
        with open("MisPokemon.txt", "r", encoding="utf-8") as archivo:
            listaPokemones = [line.strip() for line in archivo if line.strip()]
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo MisPokemon.txt")
        ventanaPokedex.destroy()
        return

    totalPaginas = (len(listaPokemones) + porPagina - 1) // porPagina
    imagenesCache = {}

    frameMatriz = tk.Frame(ventanaPokedex, bg="white")
    frameMatriz.pack(pady=20)

    def obtenerImagenPokemon(idPoke):
        if idPoke in imagenesCache:
            return imagenesCache[idPoke]
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
            respuesta = requests.get(url, timeout=5)
            datos = respuesta.json()
            urlImg = datos['sprites']['front_default']
            if urlImg:
                imgPil = Image.open(BytesIO(requests.get(urlImg, timeout=5).content))
                imgPil.thumbnail((90, 90), Image.LANCZOS)
                imgTk = ImageTk.PhotoImage(imgPil)
                imagenesCache[idPoke] = imgTk
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
                        if estado.strip().lower() == "a":
                            imagen = obtenerImagenPokemon(pokeId.strip())
                            tk.Label(celda, image=imagen, bg="white").pack()
                            tk.Label(celda, text=nombre.strip(), bg="white", font=("Arial", 12)).pack()
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



    
#======================  4. Detalle ============================

#==========================5. Descarga ============================
"""
Descarga “Mis Pokémos” (siguiendo el simulacro, los 700 Pokémos), es decir, pasa toda la 
información del diccionario a un .csv, todo separado por comas. Esto durante la revisión, 
permite controlar datos desde Excel, facilitando así la revisión en tiempo real. Al dar click al 
botón se activa una ventana con mensaje de confirmación y ya. 
"""

def ejecutarDescarga(pokepad):
    """
    Ventana emergente para descargar los Pokémon a un archivo CSV.
    Muestra un mensaje de confirmación y guarda los datos en un archivo.
    """
    ventanaDescarga = tk.Toplevel(pokepad.ventana)
    ventanaDescarga.title("Descargar Pokémon")
    ventanaDescarga.geometry("300x200")

    def descargar():
        try:
            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaArchivo = os.path.join(rutaBase, "MisPokemon.csv")
            with open(rutaArchivo, "w", encoding="utf-8") as file:
                file.write("ID,Nombre,Estado\n")  # Encabezados del CSV
                with open("MisPokemon.txt", "r", encoding="utf-8") as pokemonFile:
                    for line in pokemonFile:
                        if line.strip():  # Ignorar líneas vacías
                            partes = line.strip().split("^")
                            if len(partes) == 3:
                                idPoke, nombre, estado = partes
                                file.write(f"{idPoke},{nombre},{estado}\n")
            messagebox.showinfo("Éxito", f"Pokémon guardados en:\n{rutaArchivo}")
            ventanaDescarga.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    def confirmarDescarga():
        if messagebox.askyesno("Confirmar descarga", "¿Deseas descargar los Pokémon a un archivo CSV?"):
            descargar()

    ttk.Button(ventanaDescarga, text="Descargar Pokémon", command=confirmarDescarga).pack(pady=20)
#========================= 6. XML ============================

def ejecutarXML(pokepad):
    """
    Ventana emergente para exportar los Pokémon huidos a un archivo XML.
    """
    ventanaXML = tk.Toplevel(pokepad.ventana)
    ventanaXML.title("Exportar Pokémon huidos a XML")
    ventanaXML.geometry("320x180")

    def obtenerInfoPokemon(idPoke):
        url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
        try:
            respuesta = requests.get(url, timeout=8)
            datos = respuesta.json()

            idApi = datos['id']
            nombre = datos['name']
            esShiny = random.choice([True, False])
            peso = datos['weight'] * 10  # en gramos
            altura = datos['height'] * 10  # en centímetros

            # Estadísticas ordenadas
            statsOrden = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
            statsValores = []
            for statNombre in statsOrden:
                for stat in datos['stats']:
                    if stat['stat']['name'] == statNombre:
                        statsValores.append(stat['base_stat'])
                        break

            totalEstats = sum(statsValores)
            statsTupla = tuple(statsValores)

            # Obtener los tipos del Pokémon desde la estructura de datos
            tipos = []
            for tipo_info in datos['types']:
                tipo_nombre = tipo_info['type']['name']
                tipos.append(tipo_nombre)
            tipos = tuple(tipos)  # Convertimos la lista a una tupla para que sea inmutable

            # Determinar la URL de la imagen según si el Pokémon es shiny o no
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

    def buscarHuidos():
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
        for idPoke, _ in huidos:
            info = obtenerInfoPokemon(idPoke)
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
# ========================== 7. HTML Descarga ==========================
"""
Lea el XML de los que huyeron y genere un .html ordenado de mayor a menor por el total de 
estadísticas, enumere de 1 al N todos los Pokémos. Muestre máximo 100 datos por tabla en 
archivo HTML. Es decir, al ser 175 Pokémons, debe crear 2 archivos .html con el nombre que 
desee pero que se identifique el primero tiene 100 y el segundo tiene los 75 restantes. En el 
primero enumera de 1 a 100 y en el segundo archivo enumera de 101 a 175. Al dar click al 
botón se activa una ventana con mensaje de confirmación y ya. 
"""
def ejecutarHTML(pokepad):
    """
    Ventana emergente para generar un archivo HTML con los Pokémon huidos.
    Muestra un mensaje de confirmación y genera el archivo HTML.
    """
    ventanaHTML = tk.Toplevel(pokepad.ventana)
    ventanaHTML.title("Generar HTML de Pokémon Huidos")
    ventanaHTML.geometry("300x200")

    def buscarHuidos():
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

    def obtenerInfoPokemon(idPoke):
        url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
        try:
            respuesta = requests.get(url, timeout=8)
            datos = respuesta.json()

            idApi = datos['id']
            nombre = datos['name']
            esShiny = random.choice([True, False])
            peso = datos['weight'] * 10  # en gramos
            altura = datos['height'] * 10  # en centímetros

            # Estadísticas ordenadas
            statsOrden = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
            statsValores = []
            for statNombre in statsOrden:
                for stat in datos['stats']:
                    if stat['stat']['name'] == statNombre:
                        statsValores.append(stat['base_stat'])
                        break

            totalEstats = sum(statsValores)
            statsTupla = tuple(statsValores)

            # Obtener los tipos del Pokémon desde la estructura de datos
            tipos = []
            for tipo_info in datos['types']:
                tipo_nombre = tipo_info['type']['name']
                tipos.append(tipo_nombre)
            tipos = tuple(tipos)  # Convertimos la lista a una tupla para que sea inmutable

            # Determinar la URL de la imagen según si el Pokémon es shiny o no
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
            info = obtenerInfoPokemon(idPoke)
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
# ========================= 8. esShiny ==========================
"""
Lea en Diccionario y muestre únicamente la información completa de los Pokémons con 
esShiny, muestre toda la información en una tabla HTML. Recuerde no colocar más de 100 
por tabla HTML. Al dar click al botón se activa una ventana con mensaje de confirmación y 
ya.  
"""

def ejecutarEsShiny(pokepad):
    """
    Ventana emergente para generar archivos HTML con los Pokémon shiny.
    Genera automáticamente DiccionarioPokemon.txt antes de mostrar la ventana.
    """
    ventanaShiny = tk.Toplevel(pokepad.ventana)
    ventanaShiny.title("Generar HTML de Pokémon Shiny")
    ventanaShiny.geometry("300x200")

    def leerDiccionario():
        """
        Lee el diccionario de Pokémon desde DiccionarioPokemon.txt.
        Devuelve un diccionario con la estructura:
        {idPoke: [nombre, (esShiny, peso, altura), [totalEstad, stats], tipos, urlImagen]}
        """
        diccPoke = {}
        try:
            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaArchivo = os.path.join(rutaBase, "DiccionarioPokemon.txt")
            with open(rutaArchivo, "r", encoding="utf-8") as file:
                for line in file:
                    partes = line.strip().split("^")
                    if len(partes) == 6:
                        idPoke = int(partes[0])
                        nombre = partes[1]
                        tupla = eval(partes[2])
                        estadisticas = eval(partes[3])
                        tipos = eval(partes[4])
                        url = partes[5]
                        diccPoke[idPoke] = [nombre, tupla, estadisticas, tipos, url]
                    elif len(partes) == 5:
                        # Si el archivo no tiene la URL separada, intenta extraerla del campo tipos
                        idPoke = int(partes[0])
                        nombre = partes[1]
                        tupla = eval(partes[2])
                        estadisticas = eval(partes[3])
                        tipos = eval(partes[4])
                        url = ""
                        if isinstance(tipos, list) and tipos and isinstance(tipos[-1], str) and tipos[-1].startswith("http"):
                            url = tipos[-1]
                            tipos = tipos[:-1]
                        diccPoke[idPoke] = [nombre, tupla, estadisticas, tipos, url]
        except Exception as e:
            print(f"Error al leer el diccionario: {e}")
        return diccPoke

    def shinys(diccPoke):
        shinys = {}
        for idPoke, datos in diccPoke.items():
            esShiny = datos[1][0]
            if esShiny:
                shinys[idPoke] = datos
        return shinys

    def dividirPaginas(lista, tamano):
        paginas = []
        inicio = 0
        while inicio < len(lista):
            fin = inicio + tamano
            pagina = lista[inicio:fin]
            paginas.append(pagina)
            inicio = fin
        return paginas

    def generarHtml(pagina, numeroPagina):
        rutaBase = os.path.dirname(os.path.abspath(__file__))
        nombreArchivo = os.path.join(rutaBase, f"Shinys_{numeroPagina}.html")
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
                total_stats = estadisticas[0]
                stats = estadisticas[1]
                tiposLista = datos[3]
                tipos = ', '.join(tiposLista)
                url = datos[4]
                filaHtml = f"""
        <tr>
            <td>{idPoke}</td>
            <td>{nombre}</td>
            <td>{shiny}</td>
            <td>{peso}</td>
            <td>{altura}</td>
            <td>{stats}</td>
            <td>{total_stats}</td>
            <td>{tipos}</td>
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



def generarDiccionarioPokemon():
    """
    Genera DiccionarioPokemon.txt con todos los datos de los Pokémon atrapados (estado 'a').
    """
    rutaBase = os.path.dirname(os.path.abspath(__file__))
    rutaMisPokemon = os.path.join(rutaBase, "MisPokemon.txt")
    rutaDiccionario = os.path.join(rutaBase, "DiccionarioPokemon.txt")
    pokemones = []
    try:
        with open(rutaMisPokemon, "r", encoding="utf-8") as file:
            for line in file:
                partes = line.strip().split("^")
                # Solo agrega si tiene estado 'a' (atrapado)
                if len(partes) == 3 and partes[2].strip().lower() == "a":
                    idPoke = partes[0]
                    pokemones.append(idPoke)
    except Exception as e:
        print(f"Error al leer MisPokemon.txt: {e}")
        return

    with open(rutaDiccionario, "w", encoding="utf-8") as file:
        for idPoke in pokemones:
            try:
                url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
                respuesta = requests.get(url, timeout=8)
                datos = respuesta.json()
                nombre = datos['name']
                esShiny = random.choice([True, False])
                peso = datos['weight'] * 10
                altura = datos['height'] * 10
                estadisticas = datos['stats']
                stats = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
                statsValores = []
                for statNombre in stats:
                    for stat in estadisticas:
                        if stat['stat']['name'] == statNombre:
                            statsValores.append(stat['base_stat'])
                            break
                totalEstats = sum(statsValores)
                statsTupla = tuple(statsValores)
                tipos = [tipo['type']['name'] for tipo in datos['types']]
                urlImagen = datos['sprites']['front_shiny'] if esShiny else datos['sprites']['front_default']
                # Guardar en formato: id^nombre^(esShiny, peso, altura)^[total, (stats)]^['tipo1', ...]^url
                file.write(f"{idPoke}^{nombre}^{(esShiny, peso, altura)}^{[totalEstats, statsTupla]}^{tipos}^{urlImagen}\n")
            except Exception as e:
                print(f"Error al obtener info de Pokémon {idPoke}: {e}")
#========================= 9. Convertidor ==========================

#========================= 12. Agregar Pokemon ==========================
def ejecutarAgregar(pokepad):
    """
    Permite agregar un nuevo Pokémon al diccionario si su ID no está registrado aún.
    """
    ventanaAgregar = tk.Toplevel(pokepad.ventana)
    ventanaAgregar.title("Agregar Pokémon")
    ventanaAgregar.geometry("320x180")

    ttk.Label(ventanaAgregar, text="Ingrese el ID del Pokémon a agregar:").pack(pady=10)
    entradaID = ttk.Entry(ventanaAgregar)
    entradaID.pack(pady=5)

    def obtenerInfoPokemon(idPoke):
        url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
        try:
            respuesta = requests.get(url, timeout=8)
            datos = respuesta.json()

            idApi = datos['id']
            nombre = datos['name']
            esShiny = random.choice([True, False])
            peso = datos['weight'] * 10  # en gramos
            altura = datos['height'] * 10  # en centímetros

            # Estadísticas ordenadas
            statsOrden = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
            statsValores = []
            for statNombre in statsOrden:
                for stat in datos['stats']:
                    if stat['stat']['name'] == statNombre:
                        statsValores.append(stat['base_stat'])
                        break

            totalEstats = sum(statsValores)
            statsTupla = tuple(statsValores)

            # Obtener los tipos del Pokémon desde la estructura de datos
            tipos = []
            for tipo_info in datos['types']:
                tipo_nombre = tipo_info['type']['name']
                tipos.append(tipo_nombre)
            tipos = tuple(tipos)  # Convertimos la lista a una tupla para que sea inmutable

            # Determinar la URL de la imagen según si el Pokémon es shiny o no
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

    def leerIDsDiccionario():
        ids = set()
        try:
            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaArchivo = os.path.join(rutaBase, "DiccionarioPokemon.txt")
            with open(rutaArchivo, "r", encoding="utf-8") as file:
                for line in file:
                    partes = line.strip().split("^")
                    if partes and partes[0].isdigit():
                        ids.add(int(partes[0]))
        except FileNotFoundError:
            pass
        return ids

    def agregar():
        try:
            idNuevo = int(entradaID.get())
            if not (1 <= idNuevo <= 1025):
                raise ValueError("El ID debe estar entre 1 y 1025.")

            idsRegistrados = leerIDsDiccionario()
            if idNuevo in idsRegistrados:
                messagebox.showwarning("Repetido", f"El Pokémon con ID {idNuevo} ya está registrado.")
                return

            info = obtenerInfoPokemon(idNuevo)
            if not info:
                raise ValueError("No se pudo obtener la información del Pokémon.")

            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaMisPokemon = os.path.join(rutaBase, "MisPokemon.txt")

            # Extraer datos del diccionario generado
            datos = info[idNuevo]
            nombre = datos[0]

            # Guardar en MisPokemon.txt como atrapado
            with open(rutaMisPokemon, "a", encoding="utf-8") as f:
                f.write(f"{idNuevo}^{nombre}^a\n")

            # Mostrar en consola (Shell) en formato solicitado
            print("{")
            print(f" {idNuevo}: [")
            print(f"  '{nombre}',")
            print(f"  {datos[1]},")
            print(f"  {datos[2]},")
            print(f"  {datos[3]},")
            print(f"  '{datos[4]}'")
            print(" ]")
            print("}")

            messagebox.showinfo("Éxito", f"Pokémon {nombre} agregado correctamente.")
            ventanaAgregar.destroy()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    ttk.Button(ventanaAgregar, text="Agregar", command=agregar).pack(pady=15)
