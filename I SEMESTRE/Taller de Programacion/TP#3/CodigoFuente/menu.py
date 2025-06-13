#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 11/06/2025
#última modificación 11/06/2025 20:00
#python versión 3.13.2

import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk 
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

tk.Label(tituloFrame, text="✨ Zooinventario", font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=10)

def accionBoton(numero):
    if numero == 1:
        ventanaObtenerLista()  
    elif numero == 2:
        botones[2]['state'] = 'normal'
        for i in range(3, 9):
            botones[i]['state'] = 'disabled'
        messagebox.showinfo("Acción", "Función para crear inventario (pendiente de implementar).")

def cerrarAplicacion():
    ventana.destroy()

botones = {}

etiquetas = [
    "1. Obtener lista",
    "2. Crear inventario",
    "3. Mostrar inventario",
    "4. Estadística * estado",
    "5. Crear HTML",
    "6. Generar PDF",
    "7. Generar .csv",
    "8. Búsqueda por orden"]

indice = 1
for texto in etiquetas:
    boton = tk.Button(ventana, text=texto, width=30, command=lambda n=indice: accionBoton(n))
    boton.pack(pady=2)
    botones[indice] = boton
    indice += 1

def verificarEstadoArchivo():
    if os.path.exists("nombresAnimales.txt"):
        botones[1]['state'] = 'disabled'
        botones[2]['state'] = 'normal'
        for i in range(3, 9):
            botones[i]['state'] = 'disabled'
    else:
        botones[1]['state'] = 'normal'
        for i in range(2, 9):
            botones[i]['state'] = 'disabled'


def ventanaObtenerLista():
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
