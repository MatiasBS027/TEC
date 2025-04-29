#Elaborado por: Matias Benavides, Ignacio Elizondo, Sebastian Mora

#Importacion de librerias
import re
import time
from datetime import date
from funciones import *

#----------------Reto 4-------------------
#Definicion de funciones
def calcularEdadAUX(fechaNacimiento):
    if fechaNacimiento == "":
        return "No se ha ingresado una fecha de nacimiento"
    else:
        return calcularEdad(fechaNacimiento)

def calcularEdadES(fechaNacimiento):
    while True:
        try:
            #fechaNacimiento = input("Ingrese su fecha de nacimiento (aaaa-mm-dd): ")
            resultado = calcularEdadAUX(fechaNacimiento)
            if isinstance(resultado, int):
                return f"{resultado} años"
            else:
                return resultado
        except ValueError:
            print("Formato de fecha inválido. Por favor, use el formato aaaa-mm-dd.")

print("\n========= Calculo de Edad ===========")
fechaNacimiento = "1978-11-03"
print("Para la entrada:",fechaNacimiento)
print(calcularEdadES(fechaNacimiento),"\n")
fechaNacimiento = "2000-01-04"
print("Para la entrada:",fechaNacimiento)
print(calcularEdadES(fechaNacimiento),"\n")
fechaNacimiento = "2026-08-26"
print("Para la entrada:",fechaNacimiento)
print(calcularEdadES(fechaNacimiento),"\n")
fechaNacimiento = "2025-01-03"
print("Para la entrada:",fechaNacimiento)
print(calcularEdadES(fechaNacimiento),"\n")

#----------------Reto 7-------------------
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

def EncriptarAux(mensaje, valor):
    if mensaje == "":
        return "No se ha ingresado un mensaje"
    elif not isinstance(mensaje, str):
        return "El mensaje debe ser una cadena de texto"
    else:
        return Encriptar(mensaje, valor)

def EncriptarES():
    while True:
        try:
            mensaje = input("Ingrese el mensaje a desencriptar: ")
            valor = int(input("Ingrese el valor de desplazamiento: "))
            resultado = EncriptarAux(mensaje, valor)
            return resultado
        except ValueError:
            print("Error: El valor de desplazamiento debe ser un número entero.")

print("\n========= Desencriptar ===========")
print(EncriptarES())
