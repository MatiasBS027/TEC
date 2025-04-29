#Elaborado por: Matias Benavides, Ignacio Elizondo, Sebastian Mora

#Importacion de librerias
import time
from datetime import date

#----------------Reto 4-------------------
#Definicion de funciones
def obtenerFecha ():
    hoy = date.today()
    return str(hoy)

def calcularEdad(fechaNacimiento):
    fechaActual = obtenerFecha()
    if int(fechaActual[0:4]) > int(fechaNacimiento[0:4]):
        edad = int(fechaActual[0:4]) - int(fechaNacimiento[0:4])
        if int(fechaActual[5:7]) < int(fechaNacimiento[5:7]):
            edad -= 1
        elif int(fechaActual[5:7]) == int(fechaNacimiento[5:7]):
            if int(fechaActual[8:]) < int(fechaNacimiento[8:]):
                edad -= 1
        return edad
    elif int(fechaActual[0:4]) == int(fechaNacimiento[0:4]):
        if int(fechaActual[5:7]) > int(fechaNacimiento[5:7]):
            return "Tiene meses, no ha cumplido un año."
    else:
        return "No es posible calcular la edad, pues no ha podido nacer."
