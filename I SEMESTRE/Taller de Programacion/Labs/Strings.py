#Elaborado por: Matias Benavides
#Fecha de creacion: 23/4/2024 6:00 PM
#Ultima modificacion: 23/4/2024 6:00 PM
# Version de Python: 3.13.2

#importacion de librerias
from funciones import *
import re   

#----------------Reto 1-------------------
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
    if len(pcodigo) != 6:
        return "Debe indicar 6 valores exactamente"
    if not pcodigo[:2].isalpha() or not pcodigo[:2].isupper():
        return "Valores deben ser sólo letras mayúsculas"
    elif pcodigo[2] not in "34568":
        return "El diámetro de entrada no es un valor permitido"
    elif pcodigo[3] not in "SW":
        return "Debe indicar el proceso de fabricación S o W"
    elif pcodigo[4:] not in ("40","60","70"): #La profe dejo usar tuplas en este caso
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

print("\n========= Nomenclatura de una varilla sin ER ==========")
codigo= "SV5S6"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo),"\n")
codigo= "SV9S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo),"\n")
codigo= "SV5S55"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo),"\n")
codigo= "SV5S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo),"\n")


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
    if not re.match('.{6}', pcodigo):   
        return "Debe indicar 6 valores exactamente"
    if not re.match('[A-Z]{2}', pcodigo[0:2]):    
        return "Valores deben ser sólo letras mayúsculas"
    if not re.match('[34568]', pcodigo[2]):    
        return "El diámetro de entrada no es un valor permitido"
    if not re.match('[SW]', pcodigo[3]):     
        return "Debe indicar el proceso de fabricación S o W"
    if not re.match('(40|60|70)$', pcodigo[4:]):     
        return "El grado del acero no es un valor permitido"
    
    return nomenclatraVarilla(pcodigo)


def nomenclatraVarillaES (codigo):
    '''
    Funcionamiento: Genera una descripción legible de las características de la varilla con expresiones regulares
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

print("\n========= Nomenclatura de una varilla con ER ==========")
codigo= "SV5S6"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo),"\n")
codigo= "SV9S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo),"\n")
codigo= "SV5S55"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo),"\n")
codigo= "SV5S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo),"\n")

#----------------Reto 3-------------------
#Definicion de funciones
def decodificarNeumáticosAUX(codigo):
    '''
    Funcionamiento: Valida que el código del neumático cumpla con el formato requerido
    Entradas:
    -codigo(str): Código del neumático a validar
    Salidas:
    -str: Mensaje de error si el código es inválido
    -tuple: Componentes del neumático si el código es válido
    '''
    carga = int(codigo[8:10])
    if len(codigo) == 12:
        if codigo[11] != "R":
            return "El código indicado no corresponde a una lectura correcta de un neumático. "
    if codigo[5] not in "RD":
        return "La construcción del radial es incorrecta para poder decodificar el neumático."
    if carga <70 or carga > 90:
        return "La capacidad de carga es incorrecta para poder decodificar el neumático. "
    return decodificarNeumáticos(codigo)

def decodificarNeumáticosES(codigo):
    '''
    Funcionamiento: Genera una descripción legible de las características del neumático
    Entradas:
    -codigo(str): Código completo del neumático
    Salidas:
    -str: Descripción detallada del neumático o mensaje de error si el código es inválido
    '''
    try:
        resultado = decodificarNeumáticosAUX(codigo)
        if isinstance(resultado, str):
            return resultado  
        altura, anchura, radial, diametro, capacidad, velocidad = resultado
        return (f"""El ancho de la llanta que usa su vehículo es: {anchura} milímetros
Para un {altura} de la relación altura y ancho
Con construcción {radial}
Su diámetro es de {diametro} pulgadas
Su índice de carga es de {codigo[8:10]}, por ende, permite un soporte de {capacidad} kg
Cuidado, la velocidad máxima que soporta su llanta es de {velocidad} Km/h""")

    except ValueError:
        return "El código indicado no corresponde a una lectura correcta de un neumático. "

print("\n========= Decodificacion de un Neumatico sin ER ===========")
codigo= "16570R1484T"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")
codigo= "19555D1687V"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")
codigo= "19555D1687AA"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")
codigo= "19555B1687ZR"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")
codigo= "16570R1450T"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")

#----------------Reto 3 con ER -------------------
#Definicion de funciones
def decodificarNeumáticosAUX(codigo):
    '''
    Funcionamiento: Valida que el código del neumático cumpla con el formato requerido con expresiones regulares
    Entradas:
    -codigo(str): Código del neumático a validar
    Salidas:
    -str: Mensaje de error si el código es inválido
    -tuple: Componentes del neumático si el código es válido
    '''
    if not re.search("^\d{5}", codigo):
        return "El ancho de la llanta o la relación de altura y ancho ingresados son incorrectos para poder decodificar el neumático."
    elif not re.search("^.{5}[RD]", codigo):
        return "La construcción del radial es incorrecta para poder decodificar el neumático."
    elif not re.search("1[4-7]", codigo):
        return "El diametro en pulgadas es incorrecto para poder decodificar el neumático."
    elif not re.search("(90|[7-8][0-9])", codigo[8:10]):
        return "La capacidad de carga es incorrecta para poder decodificar el neumático."
    elif not re.search("[KLMPQRSTUHVWYZR]", codigo):
        return "El código indicado no corresponde a una lectura correcta de un neumático."
    else:
        return decodificarNeumáticos(codigo)

def decodificarNeumáticosES(codigo):
    '''
    Funcionamiento: Genera una descripción legible de las características del neumático
    Entradas:
    -codigo(str): Código completo del neumático
    Salidas:
    -str: Descripción detallada del neumático o mensaje de error si el código es inválido
    '''
    try:
        resultado = decodificarNeumáticosAUX(codigo)
        if isinstance(resultado, str):
            return resultado  
        altura, anchura, radial, diametro, capacidad, velocidad = resultado
        return (f"""El ancho de la llanta que usa su vehículo es: {anchura} milímetros
Para un {altura} de la relación altura y ancho
Con construcción {radial}
Su diámetro es de {diametro} pulgadas
Su índice de carga es de {codigo[8:10]}, por ende, permite un soporte de {capacidad} kg
Cuidado, la velocidad máxima que soporta su llanta es de {velocidad} Km/h""")

    except ValueError:
        return "El código indicado no corresponde a una lectura correcta de un neumático. "

print("\n========= Decodificacion de un Neumatico con ER ===========")
codigo= "16570R1484T"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")
codigo= "19555D1687V"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")
codigo= "19555D1687AA"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")
codigo= "19555B1687ZR"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")
codigo= "16570R1450T"
print("Para la entrada:",codigo)
print(decodificarNeumáticosES(codigo),"\n")