# Elaborado por Luis Tinoco y Matias Benavides
# Fecha de creación: 16/05/2025
# Última modificación: 18/05/2025 20:02
# Python version: 3.13.2

# ==========================
# MÓDULOS PRINCIPALES
# ==========================
from funciones import *  # Importa todas las funciones del módulo funciones.py
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
        Funcionamiento:
        Configura la ventana principal de la aplicación, incluyendo título, tamaño, icono, paleta de colores y fondo.

        Entradas:
        - Ninguna (usa atributos de la clase).

        Salidas:
        - Ninguna (modifica la ventana principal).
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
        Funcionamiento:
        Intenta cargar el icono de la ventana principal si el archivo existe.

        Entradas:
        - Ninguna.

        Salidas:
        - Ruta del icono si existe, None en caso contrario.
        """
        rutaIcono = "pokeball.ico"
        if os.path.exists(rutaIcono):
            return rutaIcono
        return None

    def cargarFondo(self):
        """
        Funcionamiento:
        Carga y muestra la imagen de fondo en la ventana principal. Si falla, usa un color sólido.

        Entradas:
        - Ninguna.

        Salidas:
        - Ninguna (modifica la ventana principal).
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
        Funcionamiento:
        Descarga y ajusta la imagen del título Poképad para mostrarla en la interfaz.

        Entradas:
        - Ninguna.

        Salidas:
        - Objeto PhotoImage listo para usar en un Label, o None si falla.
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
        Funcionamiento:
        Configura los estilos visuales de los widgets usando ttk.Style.

        Entradas:
        - Ninguna.

        Salidas:
        - Ninguna (modifica estilos globales de la interfaz).
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
        Funcionamiento:
        Crea y organiza todos los elementos de la interfaz: marco principal, título, botones de menú y área de resultados.

        Entradas:
        - Ninguna.

        Salidas:
        - Ninguna (agrega widgets a la ventana principal).
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
        Funcionamiento:
        Muestra el título con la imagen del Poképad en la parte superior de la ventana.

        Entradas:
        - Ninguna.

        Salidas:
        - Ninguna (agrega widgets al marco principal).
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
        Funcionamiento:
        Crea el área de resultados donde se muestran mensajes y feedback de acciones.

        Entradas:
        - Ninguna.

        Salidas:
        - Ninguna (agrega un label al marco principal).
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
        Funcionamiento:
        Crea la matriz de botones del menú principal, cada uno asociado a una acción diferente.

        Entradas:
        - Ninguna.

        Salidas:
        - Ninguna (agrega botones al marco principal).
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
        Funcionamiento:
        Maneja las acciones de los botones del menú. Ejecuta la función correspondiente según la opción seleccionada.

        Entradas:
        - opcion: Texto de la opción seleccionada.

        Salidas:
        - Ninguna (ejecuta funciones y actualiza el área de resultados).
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
        elif "5. Descarga" in opcion:
            self.textoResultado.set("Ejecutando: Descarga")
            self.mostrarFeedback("Descarga")
            ejecutarDescarga(self)
        elif "6. XML" in opcion:
            self.textoResultado.set("Ejecutando: XML")
            self.mostrarFeedback("XML")
            ejecutarXML(self)
        elif "7. HTML Desc" in opcion:
            self.textoResultado.set("Ejecutando: HTML Desc")
            self.mostrarFeedback("HTML Desc")
            ejecutarHTML(self)
        elif "8. esShiny" in opcion:
            self.textoResultado.set("Ejecutando: esShiny")
            self.mostrarFeedback("esShiny")
            ejecutarEsShiny(self)
        elif "9. Convertidor" in opcion:
            self.textoResultado.set("Ejecutando: Convertidor")
            self.mostrarFeedback("Convertidor")
            ejecutarConvertidor(self)
        elif "10. Desconvertidor" in opcion:
            self.textoResultado.set("Ejecutando: Desconvertidor")
            self.mostrarFeedback("Desconvertidor")
            ejecutarDesconvertidor(self)
        elif "11. Virus" in opcion:
            self.textoResultado.set("Ejecutando: Virus")
            self.mostrarFeedback("Virus")
            ejecutarVirus(self)
        elif "12. Agregar" in opcion:
            self.textoResultado.set("Ejecutando: Agregar")
            self.mostrarFeedback("Agregar")
            ejecutarAgregar(self)
        elif "13. Créditos" in opcion:
            self.textoResultado.set("Ejecutando: Créditos")
            self.mostrarFeedback("Créditos")
            ejecutarCreditos(self)
        else:
            accion = opcion.split('. ')[1]
            self.textoResultado.set(f"Ejecutando: {accion}")
            self.mostrarFeedback(accion)

    def mostrarFeedback(self, accion):
        """
        Funcionamiento:
        Muestra feedback visual de la acción ejecutada en el área de resultados.

        Entradas:
        - accion: Nombre de la acción ejecutada.

        Salidas:
        - Ninguna (actualiza el área de resultados).
        """
        self.ventana.after(100, lambda: self.textoResultado.set(f"seleccionó: {accion}"))
# ==========================
# EJECUCIÓN PRINCIPAL
# ==========================
app = Pokepad()