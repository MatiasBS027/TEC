#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 11/06/2025
#última modificación 11/06/2025 20:00
#python versión 3.13.2

import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk 

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
        botones[2]['state'] = 'normal'
        for i in range(3, 9):
            botones[i]['state'] = 'disabled'
    elif numero == 2:
        for i in range(1, 9):
            botones[i]['state'] = 'normal'
    messagebox.showinfo("Acción", f"Presionaste opción {numero}")

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
    botones[1]['state'] = 'normal'
    for i in range(2, 9):
        botones[i]['state'] = 'disabled'

verificarEstadoArchivo()
ventana.mainloop()
