#Elaborado por: Matias Benavides
#Fecha de creacion: 23/4/2024 6:00 PM
#Ultima modificacion: 23/4/2024 6:00 PM
# Version de Python: 3.13.2

#importacion de librerias
from funciones import *
import re   

#----------------Reto 1-------------------
#Definicion de funciones
def diametroVarilla (diametro):
    '''
    Funcionamiento: Convierte el código numérico del diámetro a su descripción en pulgadas
    Entradas:
    -diametro(str): Código del diámetro de la varilla (3,4,5,6,8)
    Salidas:
    -diametro(str): Descripción del diámetro en formato de pulgadas
    '''
    if diametro == "3":
        diametro = "3/8 pulgadas"
    elif diametro == "4":
        diametro = "1/2 pulgadas"
    elif diametro == "5":
        diametro = "5/8 pulgadas"
    elif diametro == "6":
        diametro = "3/4 pulgadas"
    elif diametro == "8":
        diametro = "1 pulgada"
    return diametro

def fabricacionVarilla (fabricacion):
    '''
    Funcionamiento: Determina el tipo de acero y su característica de soldabilidad
    Entradas:
    -fabricacion(str): Código del tipo de fabricación (S,W)
    Salidas:
    -fabricacion(str): Descripción completa del tipo de acero y su soldabilidad
    '''
    if fabricacion == "S":
        fabricacion = "Acero al carbono no soldable a temperatura ambiente." 
    elif fabricacion == "W":
        fabricacion = "Acero al carbono soldablea temperatura ambiente"
    return fabricacion

def aceroVarilla (acero):
    '''
    Funcionamiento: Convierte el código de resistencia a su valor en kgf/cm2
    Entradas:
    -acero(str): Código de resistencia del acero (40,60,70)
    Salidas:
    -acero(str): Valor de resistencia en kgf/cm2
    '''
    if acero == "40":
        acero = "2800 kgf/cm2"
    elif acero == "60":
        acero = "4200 kgf/cm2"
    elif acero == "70":
        acero = "5000 kgf/cm2" 
    return acero

def nomenclatraVarilla (pcodigo):
    '''
    Funcionamiento: Descompone el código de la varilla en sus componentes
    Entradas:
    -pcodigo(str): Código completo de la varilla de 6 caracteres
    Salidas:
    -tuple: (fabricante, diametro, fabricacion, acero)
    '''
    fabricante = pcodigo[:2]
    diametro = diametroVarilla(pcodigo[2])
    fabricacion = fabricacionVarilla(pcodigo[3])
    acero = aceroVarilla(pcodigo[4:])

    return fabricante, diametro, fabricacion, acero

def nomenclatraVarillaAux (pcodigo):
    '''
    Funcionamiento: Valida que el código de la varilla cumpla con el formato requerido
    Entradas:
    -pcodigo(str): Código de la varilla a validar
    Salidas:
    -str: Mensaje de error si el código es inválido
    -tuple: Componentes de la varilla si el código es válido
    '''
    if len(pcodigo) != 6:
        return "Debe indicar 6 valores exactamente"
    if not pcodigo[:2].isalpha() or not pcodigo[:2].isupper():
        return "Valores deben ser sólo letras mayúsculas"
    elif pcodigo[2] not in "34568":
        return "El diámetro de entrada no es un valor permitido"
    elif pcodigo[3] not in "SW":
        return "Debe indicar el proceso de fabricación S o W"
    elif pcodigo[4:] not in ["40","60","70"]:
        return "El grado del acero no es un valor permitido"
    else:
        return nomenclatraVarilla(pcodigo)

def nomenclatraVarillaES (codigo):
    '''
    Funcionamiento: Genera una descripción legible de las características de la varilla
    Entradas:
    -codigo(str): Código completo de la varilla
    Salidas:
    -str: Descripción detallada de la varilla o mensaje de error
    '''
    #codigo = str(input("Ingrese el codigo de la varilla: "))
    resultado = nomenclatraVarillaAux(codigo)
    if isinstance(resultado, str):
        return resultado  # Retorna el mensaje de error directamente
    fabricante, diametro, fabricacion, acero = resultado
    return "El fabricante es: " + fabricante + "\nEl diametro de la varilla es: " + diametro + "\nProceso de Fabricación: " + fabricacion + "\nGrados de acero: " + acero

print("\n=== Nomenclatura de una varilla ===")
codigo= "SV5S6"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))
codigo= "SV9S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))
codigo= "SV5S55"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))
codigo= "SV5S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))


#-------------Reto 1 con ER------------------
#Definicion de funciones
def nomenclatraVarillaAux (pcodigo):
    '''
    Funcionamiento: Valida que el código de la varilla cumpla con el formato requerido
    Entradas:
    -pcodigo(str): Código de la varilla a validar
    Salidas:
    -str: Mensaje de error si el código es inválido
    -tuple: Componentes de la varilla si el código es válido
    '''
    if not re.match('.{6}', pcodigo):    # Valida longitud exacta de 6 caracteres
        return "Debe indicar 6 valores exactamente"
    if not re.match('[A-Z]{2}', pcodigo[0:2]):     # Valida que los primeros 2 caracteres sean letras mayúsculas
        return "Valores deben ser sólo letras mayúsculas"
    if not re.match('[34568]', pcodigo[2]):    # Valida el diámetro
        return "El diámetro de entrada no es un valor permitido"
    if not re.match('[SW]', pcodigo[3]):     # Valida el proceso de fabricación
        return "Debe indicar el proceso de fabricación S o W"
    if not re.match('(40|60|70)$', pcodigo[4:]):     # Valida el grado de acero
        return "El grado del acero no es un valor permitido"
    
    return nomenclatraVarilla(pcodigo)


def nomenclatraVarillaES (codigo):
    '''
    Funcionamiento: Genera una descripción legible de las características de la varilla
    Entradas:
    -codigo(str): Código completo de la varilla
    Salidas:
    -str: Descripción detallada de la varilla o mensaje de error
    '''
    #codigo = str(input("Ingrese el codigo de la varilla: "))
    resultado = nomenclatraVarillaAux(codigo)
    if isinstance(resultado, str):
        return resultado  # Retorna el mensaje de error directamente
    fabricante, diametro, fabricacion, acero = resultado
    return "El fabricante es: " + fabricante + "\nEl diametro de la varilla es: " + diametro + "\nProceso de Fabricación: " + fabricacion + "\nGrados de acero: " + acero

print("\n=== Nomenclatura de una varilla ===")
codigo= "SV5S6"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))
codigo= "SV9S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))
codigo= "SV5S55"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))
codigo= "SV5S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))