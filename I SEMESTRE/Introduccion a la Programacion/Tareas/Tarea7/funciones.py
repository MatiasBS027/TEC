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
#-------------- Reto 7 --------------
#Definicion de funciones
def desEncriptar(codASCII, valor):
    aceptar = input("¿Desea desencriptar el mensaje? SI/NO: ").lower()
    if aceptar == "si":
        nuevoMsj = ""
        for i in codASCII:
            if i in (" ", "," , "."): # Solo vamos a dejar igual a la coma, el espacio y el punto
                nuevoValor = ord(i)
                nuevoMsj+= str(chr(nuevoValor))
            else:
                nuevoValor = ord(i) - valor
                nuevoMsj += str(chr(nuevoValor))
        return (nuevoMsj)
    else:
        valor = 0
        return "Ya no puede desencriptar el mensaje."


def Encriptar(mensaje, valor):
    codASCII = ""
    for i in mensaje:
        if i in (" ", "," , "."): # Solo vamos a dejar igual a la coma, el espacio y el punto
            nuevoValor = ord(i)
            codASCII += str(chr(nuevoValor))
        else:
            nuevoValor = ord(i) + valor
            codASCII += str(chr(nuevoValor))

    print (codASCII)
    return desEncriptar(codASCII, valor)