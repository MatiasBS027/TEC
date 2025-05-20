import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Variables globales para mantener referencias a elementos de la interfaz
imagenPokemon = None  # Variable global para mantener referencia a la imagen

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

def cargarImagen(label, url):
    """
    Carga la imagen del Pokémon desde la URL en un label.
    
    Args:
        label: Label donde se mostrará la imagen
        url: URL de la imagen del Pokémon
    """
    global imagenPokemon
    try:
        respuesta = requests.get(url)
        datosImagen = Image.open(BytesIO(respuesta.content))
        imagenPokemon = ImageTk.PhotoImage(datosImagen)
        label.config(image=imagenPokemon)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

def cargarPokemon(idPokemon, nombreLabel, entradas, imagenLabel):
    """
    Carga los datos del Pokémon desde la API y actualiza la interfaz.
    
    Args:
        idPokemon: ID del Pokémon a cargar
        nombreLabel: Label para mostrar el nombre
        entradas: Diccionario de campos de entrada para los datos
        imagenLabel: Label para mostrar la imagen
    """
    try:
        datosPokemon = obtenerInfoPokemon(idPokemon)
        if datosPokemon:
            for id, datos in datosPokemon.items():
                nombreLabel.config(text=datos[0].capitalize())
                
                # Llenar campos
                esShiny, peso, altura = datos[1]
                totalEstad, stats = datos[2]
                tipos = datos[3]
                urlImagen = datos[4]
                
                entradas["Peso:"].delete(0, tk.END)
                entradas["Peso:"].insert(0, f"{peso/10:.1f} kg")
                
                entradas["Altura:"].delete(0, tk.END)
                entradas["Altura:"].insert(0, f"{altura/10:.1f} m")
                
                entradas["Tipos:"].delete(0, tk.END)
                # Lista original de tipos
                tiposCapitalizados = []
                for t in tipos:
                    tipoCap = t.capitalize()
                    # Agregar el resultado a la nueva lista
                    tiposCapitalizados.append(tipoCap)
                # Unir todos los elementos capitalizados usando "/" como separador
                tiposUnidos = "/".join(tiposCapitalizados)
                entradas["Tipos:"].insert(0, tiposUnidos)
                # Llenar estadísticas
                camposStats = ["PS:", "Ataque:", "Defensa:", "A Esp:", "D Esp:", "Veloc:"]
                for i, campoStat in enumerate(camposStats):
                    entradas[campoStat].delete(0, tk.END)
                    entradas[campoStat].insert(0, stats[i])
                entradas["Estad T:"].delete(0, tk.END)
                entradas["Estad T:"].insert(0, totalEstad)
                # Cargar la imagen
                cargarImagen(imagenLabel, urlImagen)
    except Exception as e:
        print(f"Error al cargar el Pokémon: {e}")

def mostrarDetallePokemon(idPokemon):
    """
    Muestra una ventana con los detalles del Pokémon.
    
    Args:
        idPokemon: ID del Pokémon a mostrar (por defecto: 16, Pidgey)
    """
    # Crear la ventana
    ventana = tk.Toplevel()
    ventana.title("Detalle del Pokémon")
    ventana.resizable(False, False)
    # Marco principal para el contenido
    marcoContenido = tk.Frame(ventana, bg="white")
    marcoContenido.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    # Marco para el nombre y la imagen
    marcoPokemon = tk.Frame(marcoContenido, bg="white")
    marcoPokemon.pack(fill=tk.X, padx=5, pady=5)
    
    # Nombre del Pokémon
    nombrePokemon = tk.Label(marcoPokemon, 
                        font=("Arial", 12, "bold"), bg="white")
    nombrePokemon.pack(side=tk.LEFT, padx=5)
    
    # Espacio para la imagen del Pokémon
    imagenLabel = tk.Label(marcoPokemon)
    imagenLabel.pack(side=tk.LEFT, padx=5)
    
    # Marco para los detalles
    marcoDetalles = tk.Frame(marcoContenido)
    marcoDetalles.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    # Campos de detalles
    campos = ["Peso:", "Altura:", "Tipos:", "PS:", "Ataque:", 
            "Defensa:", "A Esp:", "D Esp:", "Veloc:", "Estad T:"]
    entradas = {}
    
    for i, campo in enumerate(campos):
        tk.Label(marcoDetalles, text=campo, 
                anchor=tk.W).grid(row=i, column=0, sticky=tk.W, pady=2)
        
        entrada = tk.Entry(marcoDetalles, width=15, relief=tk.SUNKEN, bd=1)
        entrada.grid(row=i, column=1, sticky=tk.W, pady=2, padx=5)
        entradas[campo] = entrada
    
    # Botón de regresar
    tk.Button(marcoContenido, text="Regresar", 
            command=ventana.destroy).pack(pady=10)
    
    # Cargar los datos del Pokémon
    cargarPokemon(idPokemon, nombrePokemon, entradas, imagenLabel)
    
    # Centrar la ventana
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    
    return ventana

# Para usar el código directamente
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultar ventana raíz
    ventanaDetalle = mostrarDetallePokemon(1000)
    root.mainloop()