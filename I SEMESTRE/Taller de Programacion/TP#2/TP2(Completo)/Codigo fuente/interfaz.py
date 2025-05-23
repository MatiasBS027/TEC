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

"""
###################
Clase principal de la interfaz Poképad
###################
"""

class Pokepad:
    """
    Clase principal que gestiona la ventana y los elementos de la interfaz gráfica
    de la aplicación Poképad.
    """
    def __init__(self):
        """
        Inicializa la aplicación, configura la ventana, estilos y widgets.
        """
        self.ventana = tk.Tk()
        self.configurarVentana()
        self.cargarEstilos()
        self.crearWidgets()
        self.ventana.mainloop()

    def configurarVentana(self):
        """
        Configuración inicial de la ventana principal:
        - Título, tamaño, icono, paleta de colores y fondo.
        """
        self.ventana.title("Poképad Ventana principal")
        self.ventana.geometry("700x600")
        self.ventana.resizable(False, False)
        
        # Configuración del icono 
        icono = self.obtenerIcono()
        if icono:
            try:
                self.ventana.iconbitmap(icono)
            except Exception as e:
                print(f"No se pudo cargar el icono: {e}")
        
        # Paleta de colores para la interfaz
        self.colores = {
            'fondo': '#1a1a2e',        # Fondo principal
            'boton': '#e74c3c',        # Color de los botones
            'texto': '#000000',        # Color del texto
            'hover': '#c0392b',        # Color al pasar el mouse sobre el botón
            'borde': '#3498db',        # Color de borde
            'exito': '#2ecc71',        # Color para mensajes de éxito (muchos detalles no juzgue)
            'error': '#e74c3c',        # Color para mensajes de error (muchos detalles no juzgue x2)
            'fondoTexto': '#ffffff'   # Fondo para el área de resultados
        }
        
        # Cargar imagen de fondo
        self.cargarFondo()

    def obtenerIcono(self):
        """
        Intenta cargar un icono para la ventana.
        Retorna la ruta si existe, sino None.
        """
        rutaIcono = "pokeball.ico"
        if os.path.exists(rutaIcono):
            return rutaIcono
        return None

    def cargarFondo(self):
        """
        Carga y muestra la imagen de fondo en la ventana principal.
        Si falla, usa un color sólido de fondo.
        """
        try:
            url = "https://i.pinimg.com/736x/20/72/bf/2072bf31916fe07aa69fed32a9319372.jpg"
            respuesta = requests.get(url, timeout=5)
            imagen = Image.open(BytesIO(respuesta.content))
            self.imgFondo = ImageTk.PhotoImage(imagen.resize((700, 600), Image.LANCZOS))
            tk.Label(self.ventana, image=self.imgFondo).place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error cargando fondo: {e}")
            self.ventana.config(bg=self.colores['fondo'])

    def cargarImagenTitulo(self):
        """
        Descarga y ajusta la imagen del título Poképad.
        Retorna un objeto PhotoImage listo para usar en un Label.
        """
        try:
            url = "https://static.wikia.nocookie.net/ultimate-pokemon-fanon/images/c/ca/Pok%C3%A9Pad.PNG/revision/latest?cb=20150206145041"
            respuesta = requests.get(url, timeout=5)
            imagen = Image.open(BytesIO(respuesta.content))
            
            # Ajustar tamaño proporcionalmente 
            anchoOriginal, altoOriginal = imagen.size
            nuevoAlto = 80  # Puedes aumentar este valor para hacer la imagen más grande
            nuevoAncho = int((nuevoAlto / altoOriginal) * anchoOriginal)
            
            imagen = imagen.resize((nuevoAncho, nuevoAlto), Image.LANCZOS)
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"Error cargando imagen de título: {e}")
            return None

    def cargarEstilos(self):
        """
        Configura los estilos visuales de los widgets usando ttk.Style.
        """
        estilo = ttk.Style()
        
        # Estilo para botones principales 
        estilo.configure('Pokepad.TButton',
                        foreground=self.colores['texto'],
                        background=self.colores['boton'],
                        font=('Times New Roman', 8, 'bold'), 
                        padding=4,  
                        borderwidth=1,
                        relief='raised')
        
        estilo.map('Pokepad.TButton',
                 background=[('active', self.colores['hover'])],
                 foreground=[('active', self.colores['texto'])])
        
        estilo.configure('Resultado.TLabel',
                       foreground='#000000',
                       background=self.colores['fondoTexto'],
                       font=('Helvetica', 10), 
                       padding=6,
                       relief='sunken',
                       borderwidth=1)

    def crearWidgets(self):
        """
        Crea todos los elementos de la interfaz:
        - Marco principal
        - Título con imagen
        - Botones de menú
        - Área de resultados
        """
        # Marco principal para contener los widgets 
        self.marcoPrincipal = ttk.Frame(self.ventana)
        self.marcoPrincipal.pack(pady=10, padx=10, fill='none', expand=False)  
        # Título con imagen
        self.mostrarTitulo()
        
        # Crear botones del menú
        self.crearBotones()
        
        # Área de resultados con fondo blanco
        self.crearAreaResultado()

    def mostrarTitulo(self):
        """
        Muestra el título con la imagen del Poképad en la parte superior.
        Si no se puede cargar la imagen, muestra solo el texto.
        """
        marcoTitulo = ttk.Frame(self.marcoPrincipal)
        marcoTitulo.pack(pady=10)
        
        imgTitulo = self.cargarImagenTitulo()
        if imgTitulo:
            # Mostrar imagen si se cargó correctamente (me mandó 5000 errroes para cargar la imagen)
            lblTitulo = tk.Label(marcoTitulo, image=imgTitulo, bg=self.colores['fondo'])
            lblTitulo.image = imgTitulo  # Mantener referencia para evitar que se borre
            lblTitulo.pack()
        else:
            # Fallback a texto si no se pudo cargar la imagen
            ttk.Label(marcoTitulo, 
                     text="Poképad", 
                     font=('Helvetica', 16, 'bold'),
                     foreground=self.colores['texto']).pack()

    def crearAreaResultado(self):
        """
        Crea el área de resultados donde se muestran mensajes y feedback de acciones.
        """
        self.textoResultado = tk.StringVar(value="Seleccione una opción")
        lblResultado = ttk.Label(
            self.marcoPrincipal,
            textvariable=self.textoResultado,
            style='Resultado.TLabel',
            anchor='center'
        )
        lblResultado.pack(pady=8, fill='x', ipady=4)  

    def crearBotones(self):
        """
        Crea la matriz de botones del menú principal.
        Cada botón ejecuta una acción diferente según la opción seleccionada.
        """
        marcoBotones = ttk.Frame(self.marcoPrincipal)
        marcoBotones.pack(fill='none', expand=False)  
        # Opciones del menú (pares de botones por fila)
        opciones = [
            ["1. Búsqueda", "8. esShiny"],
            ["2. Atrapar", "9. Convertidor"],
            ["3. Pokédex", "10. Desconvertidor"],
            ["4. Detalle", "11. Virus"],
            ["5. Descarga", "12. Agregar"],
            ["6. XML", "13. Créditos"],
            ["7. HTML Desc", "14. Salir"]
        ]
        
        for fila, (opcionIzquierda, opcionDerecha) in enumerate(opciones):
            ttk.Button(
                marcoBotones,
                text=opcionIzquierda,
                style='Pokepad.TButton',
                command=lambda o=opcionIzquierda: self.accionBoton(o),
                width=14  
            ).grid(row=fila, column=0, padx=2, pady=2, sticky='ew')
            
            ttk.Button(
                marcoBotones,
                text=opcionDerecha,
                style='Pokepad.TButton',
                command=lambda o=opcionDerecha: self.accionBoton(o),
                width=14
            ).grid(row=fila, column=1, padx=2, pady=2, sticky='ew')
        
        marcoBotones.columnconfigure(0, weight=1)
        marcoBotones.columnconfigure(1, weight=1)

    def accionBoton(self, opcion):
        """
        Maneja las acciones de los botones del menú.
        Si la opción es 'Salir', pregunta confirmación y cierra la ventana.
        Para otras opciones, muestra el nombre de la acción en el área de resultados.
        """
        if "14" in opcion:
            if messagebox.askyesno("Salir", "¿Está seguro que desea salir?"):
                self.ventana.destroy()
        elif "1. Búsqueda" in opcion:
            self.textoResultado.set("Ejecutando: Búsqueda")
            self.mostrarFeedback("Búsqueda")
            ejecutarBusqueda(self)
        elif "2. Atrapar" in opcion:
            self.textoResultado.set("Ejecutando: Atrapar")
            self.mostrarFeedback("Atrapar")
            ejecutarAtrapar(self)

        elif "3. Pokédex" in opcion:
            self.textoResultado.set("Ejecutando: Pokédex")
            self.mostrarFeedback("Pokédex")
            ejecutarPokedex(self)
        else:
            accion = opcion.split('. ')[1]
            self.textoResultado.set(f"Ejecutando: {accion}")
            self.mostrarFeedback(accion)

    def mostrarFeedback(self, accion):
        """
        Muestra feedback visual de la acción ejecutada en el área de resultados.
        """
        self.ventana.after(100, lambda: self.textoResultado.set(f"seleccionó: {accion}"))



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

            urlApi = f"https://pokeapi.co/api/v2/pokemon?limit={cantidadDeseada}"
            respuestaApi = requests.get(urlApi, timeout=10)
            if respuestaApi.status_code != 200:
                raise Exception("No se pudo conectar a la PokéAPI.")

            datosJson = respuestaApi.json()
            listaResultados = datosJson.get("results", [])
            if not listaResultados:
                raise Exception("No se encontraron Pokémon.")

            rutaBase = os.path.dirname(os.path.abspath(__file__))
            rutaArchivo = os.path.join(rutaBase, "MisPokemon.txt") #estas dos lineas son para guardar el archivo en la misma carpeta que el script

            with open(rutaArchivo, "w", encoding="utf-8") as archivoTexto:
                for pokemon in listaResultados:
                    try:
                        respuestaDetalle = requests.get(pokemon["url"], timeout=5)
                        if respuestaDetalle.status_code == 200:
                            datosPokemon = respuestaDetalle.json()
                            idPokedex = datosPokemon["id"]
                            nombrePokemon = datosPokemon["name"]
                            archivoTexto.write(f"{idPokedex}^{nombrePokemon}\n")
                        else:
                            print(f"No se pudo acceder a {pokemon['url']}")
                    except Exception as errorDetalle:
                        print(f"Error al obtener detalles de {pokemon['name']}: {errorDetalle}")

            messagebox.showinfo("Éxito", f"Se guardaron {len(listaResultados)} Pokémon en:\n{rutaArchivo}")
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
        print("Pokémon atrapados:")
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
            respuesta = requests.get(url)
            datos = respuesta.json()
            idApi = datos['id']
            nombre = datos['name']
            esShiny = random.choice([True, False])
            peso = datos['weight']  *10
            altura = datos['height']  *10
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
            print("]\n")


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
    """
    Ventana emergente para mostrar Pokédex con matriz 5x5 de Pokémon
    """
    try:
        # Leer archivo de Pokémon
        with open("MisPokemon.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            listaPokemones = []
            for linea in lineas:
                if linea.strip():
                    partes = linea.strip().split("^")
                    listaPokemones.append(partes)
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo MisPokemon.txt no encontrado")
        return

    # Configuración de ventana (más ancha para mejor visualización)
    ventanaPokedex = tk.Toplevel(pokePad.ventana)
    ventanaPokedex.title("Pokédex")
    ventanaPokedex.geometry("850x700")  # Aumentamos el ancho
    ventanaPokedex.resizable(False, False)

    # Variables de paginación
    pokemonesPorPagina = 25
    totalPaginas = (len(listaPokemones) + pokemonesPorPagina - 1) // pokemonesPorPagina
    paginaActual = tk.IntVar(value=1)

    # Marco principal
    marcoPrincipal = ttk.Frame(ventanaPokedex)
    marcoPrincipal.pack(fill="both", expand=True, padx=10, pady=10)

    # Título
    titulo = ttk.Label(marcoPrincipal, text="Pokédex", font=("Arial", 20, "bold"))
    titulo.pack(pady=10)

    # Marco para la matriz (con más espacio)
    marcoMatriz = ttk.Frame(marcoPrincipal)
    marcoMatriz.pack(pady=10)

    # Configurar tamaño de celdas
    for i in range(5):
        marcoMatriz.rowconfigure(i, weight=1, minsize=120)  # Aumentamos altura mínima
    for j in range(5):
        marcoMatriz.columnconfigure(j, weight=1, minsize=150)  # Aumentamos ancho mínimo

    # Marco para controles
    marcoControles = ttk.Frame(marcoPrincipal)
    marcoControles.pack(pady=10)

    # Botones de navegación
    btnAtras = ttk.Button(marcoControles, text="← Atrás")
    btnAtras.pack(side="left", padx=10)

    lblPagina = ttk.Label(marcoControles, text="Página 1 de 1", font=("Arial", 12))
    lblPagina.pack(side="left", padx=10)

    btnSiguiente = ttk.Button(marcoControles, text="Siguiente →")
    btnSiguiente.pack(side="left", padx=10)

    def actualizarPokedex(*args):
        # Limpiar matriz
        for widget in marcoMatriz.winfo_children():
            widget.destroy()

        # Calcular rango de pokémons a mostrar
        inicio = (paginaActual.get() - 1) * pokemonesPorPagina
        fin = inicio + pokemonesPorPagina
        pokemonesPagina = listaPokemones[inicio:fin]

        # Crear matriz 5x5
        for fila in range(5):
            for columna in range(5):
                indice = fila * 5 + columna

                marcoCelda = ttk.Frame(marcoMatriz, relief="ridge", borderwidth=1)
                marcoCelda.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

                # Configurar celda para que el contenido se expanda
                marcoCelda.columnconfigure(0, weight=1)
                marcoCelda.rowconfigure(0, weight=1)
                marcoCelda.rowconfigure(1, weight=0)
                marcoCelda.rowconfigure(2, weight=0)
                marcoCelda.rowconfigure(3, weight=0)

                if indice < len(pokemonesPagina):
                    pokeData = pokemonesPagina[indice]
                    idPoke = pokeData[0]
                    nombrePoke = pokeData[1]
                    
                    # Verificar estado
                    if len(pokeData) > 2:
                        estadoPoke = pokeData[2]
                    else:
                        estadoPoke = "h"

                    if estadoPoke.lower() == 'a':
                        try:
                            # Obtener datos del pokémon
                            respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{idPoke}")
                            if respuesta.status_code == 200:
                                datosPoke = respuesta.json()
                                
                                # Determinar si es shiny
                                esShiny = random.choice([True, False])
                                
                                # Obtener imagen adecuada
                                if esShiny:
                                    urlImagen = datosPoke['sprites']['front_shiny']
                                else:
                                    urlImagen = datosPoke['sprites']['front_default']
                                
                                # Cargar imagen
                                datosImagen = requests.get(urlImagen).content
                                imagenPil = Image.open(BytesIO(datosImagen))
                                imagenPil.thumbnail((100, 100), Image.LANCZOS)
                                imagenTk = ImageTk.PhotoImage(imagenPil)
                                
                                # Marco interno para organizar mejor el contenido
                                marcoInterior = ttk.Frame(marcoCelda)
                                marcoInterior.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
                                marcoInterior.columnconfigure(0, weight=1)
                                
                                # Mostrar imagen (centrada)
                                lblImagen = ttk.Label(marcoInterior, image=imagenTk)
                                lblImagen.image = imagenTk
                                lblImagen.grid(row=0, column=0, pady=2)
                                
                                # Mostrar nombre (con ajuste de texto)
                                nombreMostrar = nombrePoke.capitalize()
                                if len(nombreMostrar) > 12:  # Acortar nombres muy largos
                                    nombreMostrar = nombreMostrar[:10] + "..."
                                
                                lblNombre = ttk.Label(marcoInterior, text=nombreMostrar, 
                                                    wraplength=120, justify="center")
                                lblNombre.grid(row=1, column=0, pady=2)
                                
                                # Mostrar ID
                                lblId = ttk.Label(marcoInterior, text=f"ID: {idPoke}", 
                                                font=("Arial", 8))
                                lblId.grid(row=2, column=0, pady=1)
                                
                                # Mostrar si es shiny
                                if esShiny:
                                    lblShiny = ttk.Label(marcoInterior, text="¡Shiny!", 
                                                        foreground="gold", font=("Arial", 8, "bold"))
                                    lblShiny.grid(row=3, column=0, pady=1)
                        except Exception as error:
                            marcoError = ttk.Frame(marcoCelda)
                            marcoError.grid(row=0, column=0, sticky="nsew")
                            
                            lblError = ttk.Label(marcoError, text="Error al cargar", 
                                            foreground="red")
                            lblError.pack()
                            lblNombre = ttk.Label(marcoError, text=nombrePoke.capitalize())
                            lblNombre.pack()
                    else:
                        # Marco para Pokémon no atrapados
                        marcoNoAtrapado = ttk.Frame(marcoCelda)
                        marcoNoAtrapado.grid(row=0, column=0, sticky="nsew")
                        
                        lblInterrogacion = ttk.Label(marcoNoAtrapado, text="?", 
                                                font=("Arial", 48))
                        lblInterrogacion.pack(pady=5)
                        lblTexto = ttk.Label(marcoNoAtrapado, text="No atrapado")
                        lblTexto.pack()
                else:
                    # Celda vacía
                    pass

        # Actualizar controles
        lblPagina.config(text=f"Página {paginaActual.get()} de {totalPaginas}")
        
        if paginaActual.get() <= 1:
            btnAtras.state(["disabled"])
        else:
            btnAtras.state(["!disabled"])
            
        if paginaActual.get() >= totalPaginas:
            btnSiguiente.state(["disabled"])
        else:
            btnSiguiente.state(["!disabled"])

    # Configurar comandos de botones
    btnAtras.config(command=lambda: paginaActual.set(paginaActual.get() - 1))
    btnSiguiente.config(command=lambda: paginaActual.set(paginaActual.get() + 1))

    # Observar cambios en la página actual
    paginaActual.trace_add("write", actualizarPokedex)

    # Mostrar primera página
    actualizarPokedex()

#======================  4. Detalle ============================


# ==========================
# EJECUCIÓN PRINCIPAL
# ==========================
if __name__ == "__main__":
    app = Pokepad()