#Elaborado por: Matias Benavides
#Fecha de creacion: 23/4/2024 6:00 PM
#Ultima modificacion: 23/4/2024 6:00 PM
# Version de Python: 3.13.2

#Importacion de librerias
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




#-------------Reto 2------------------
#Definicion de funciones