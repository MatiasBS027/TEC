#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 11/06/2025
#última modificación 21/06/2025 20:00
#python versión 3.11.2

import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk #si no se instala de una usar "pip uninstall PIL Pillow"
from funciones import *

rutaListaAnimales = "listaAnimales.txt"

ventana = tk.Tk()
ventana.title("Zooinventario")
ventana.geometry("300x360")
ventana.resizable(False, False)

tituloFrame = tk.Frame(ventana)
tituloFrame.pack(pady=10)

# Cargar la imagen
imagen = Image.open("logo.png")  
imagen = imagen.resize((32, 32), Image.LANCZOS)  # Redimensionar la imagen
imagenTk = ImageTk.PhotoImage(imagen)

imagen = tk.Label(tituloFrame, image=imagenTk)
imagen.pack(side=tk.LEFT, padx=5)

tk.Label(tituloFrame, text="Zooinventario", font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=10)

def accionBoton(numero):
    """
    Funcionalidad:
    - Ejecuta la acción correspondiente según el botón presionado en la interfaz principal.

    Entradas:
    - numero: int, número del botón presionado.

    Salidas:
    - No retorna valor. Ejecuta funciones y muestra ventanas o mensajes según la opción.
    """
    if numero == 1:
        ventanaObtenerLista()
        if 2 in botones:
            botones[2]['state'] = 'normal'
    elif numero == 2:
        crearInventarioDesdeInterfaz(ventana)
        verificarEstadoArchivo()
    elif numero == 3:
        if os.path.exists("inventario.txt"):
            mostrarInventarioES()
        else:
            messagebox.showwarning("Advertencia", "Debes crear primero el inventario (opción 2).")
    elif numero == 4:
        mostrarEstadisticaPorEstado()
    elif numero == 5:
        crearHtmlInventario()
    elif numero == 6:
        generarPDFEstadisticaPorCalificacion()
    elif numero == 7:
        if os.path.exists("inventario.txt"):
            exportarInventarioACSV()
            messagebox.showinfo("CSV Generado", "Se ha creado el archivo 'inventario.csv' correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Debes crear primero el inventario (opción 2).")
    elif numero == 8:
        buscarPorOrdenES()
        
def cerrarAplicacion():
    """
    Funcionalidad:
    - Cierra la ventana principal de la aplicación.

    Entradas:
    - Ninguna.

    Salidas:
    - No retorna valor. Cierra la aplicación.
    """
    ventana.destroy()

botones = {}
etiquetas = [
    "1. Obtener lista",
    "2. Crear inventario",
    "3. Mostrar inventario",
    "4. Estadística por estado",
    "5. Crear HTML",
    "6. Generar PDF",
    "7. Generar .csv",
    "8. Búsqueda por orden"]

i = 1
for texto in etiquetas:
    if i == 1:
        estado = 'normal'
    else:
        estado = 'disabled'
    botones[i] = tk.Button(ventana, text=texto, width=25, state=estado, command=lambda n=i: accionBoton(n))
    botones[i].pack(pady=2)
    i += 1

def verificarEstadoArchivo():
    """
    Funcionalidad:
    - Verifica la existencia de archivos clave y habilita o deshabilita los botones de la interfaz según corresponda.

    Entradas:
    - Ninguna.

    Salidas:
    - No retorna valor. Modifica el estado de los botones en la interfaz.
    """
    if os.path.exists("nombresAnimales.txt"):
        try:
            botones[1]['state'] = 'disabled'
        except:
            pass
        if os.path.exists("inventario.txt"):
            try:
                botones[2]['state'] = 'disabled'
            except:
                pass
            for i in range(3, 9):
                try:
                    botones[i]['state'] = 'normal'
                except:
                    pass
        else:
            try:
                botones[2]['state'] = 'normal'
            except:
                pass
            for i in range(3, 9):
                try:
                    botones[i]['state'] = 'disabled'
                except:
                    pass
    else:
        try:
            botones[1]['state'] = 'normal'
        except:
            pass
        for i in range(2, 9):
            try:
                botones[i]['state'] = 'disabled'
            except:
                pass


def ventanaObtenerLista():
    """
    Funcionalidad:
    - Abre una ventana secundaria para solicitar la cantidad de nombres de animales a obtener de Wikipedia.

    Entradas:
    - Ninguna (interacción por interfaz gráfica).

    Salidas:
    - No retorna valor. Llama a la función para obtener la lista y cierra la ventana secundaria.
    """
    ventanaLista = tk.Toplevel(ventana)
    ventanaLista.title("Obtener lista de animales")
    ventanaLista.geometry("300x180")
    ventanaLista.resizable(False, False)
    
    # Frame principal
    framePrincipal = tk.Frame(ventanaLista)
    framePrincipal.pack(pady=20, padx=20, fill='both', expand=True)
    
    # Etiqueta e instrucción
    tk.Label(framePrincipal, 
            text="Ingrese la cantidad de nombres de animales\na obtener de Wikipedia:",
            justify='center').pack(pady=10)
    
    # Entrada para la cantidad
    entradaCantidad = tk.Entry(framePrincipal, width=10, justify='center')
    entradaCantidad.pack(pady=5)
    entradaCantidad.focus_set()  # Poner el foco en la entrada
    
    # Frame para botones
    frameBotones = tk.Frame(framePrincipal)
    frameBotones.pack(pady=10)
    
    # Botón Confirmar
    tk.Button(frameBotones, text="Confirmar", 
            command=lambda: obtenerListaES(entradaCantidad.get(), ventanaLista)).pack(side=tk.LEFT, padx=5)
    
    # Botón Cancelar
    tk.Button(frameBotones, text="Cancelar", 
            command=ventanaLista.destroy).pack(side=tk.LEFT, padx=5)
    
    # Vincular la tecla Enter al botón Confirmar
    ventanaLista.bind('<Return>', lambda e: obtenerListaES(entradaCantidad.get(), ventanaLista))


verificarEstadoArchivo()
ventana.mainloop()
