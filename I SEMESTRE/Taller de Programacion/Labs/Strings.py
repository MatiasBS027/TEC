#Elaborado por: Matias Benavides y Luis Carlos Tinoco Vargas
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
    return (
        f"El fabricante es: {fabricante}\n"
        f"El diametro de la varilla es: {diametro}\n"
        f"Proceso de Fabricación: {fabricacion}\n"
        f"Grados de acero: {acero}")

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
    return (
    f"El fabricante es: {fabricante}\n"
    f"El diametro de la varilla es: {diametro}\n"
    f"Proceso de Fabricación: {fabricacion}\n"
    f"Grados de acero: {acero}")

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

#----------------Reto 2-------------------
#Definicion de funciones
def reconocerTarjetaAux(ptarjeta):
    '''
    Funcionamiento: Valida que el texto de la tarjeta cumpla con el formato requerido.
    Entradas:
    - ptarjeta (str): Texto de la tarjeta a validar.
    Salidas:
    - str: Mensaje de error si el texto es inválido.
    - función: Llama a la función `reconocerTarjeta` si el texto es válido.
    '''
    if not ptarjeta.startswith("Micro"):
        return "Debe ingresar un texto para poder decodificar.\nEl texto brindado no es posible de decodificar."
    elif not (ptarjeta.startswith("MicroSD") and (ptarjeta[7:9] in ["HC", "XC"] or ptarjeta[7] in ["U", "I"])):
        return "El tipo de tarjeta no es un nombre existente correctamente."
    elif not ("U1" in ptarjeta or "U3" in ptarjeta):
        return "El número de la clase UHS incluído no es correcto (U1 o U3)."
    elif not ("II" in ptarjeta or "I" in ptarjeta):
        return "El número de Bus UHS incluído no es correcto (I o II)."
    else:
        return reconocerTarjeta(ptarjeta)

def reconocerTarjetaES(tarjeta):
    '''
    Funcionamiento: Genera una descripción legible de las características de la tarjeta.
    Entradas:
    - tarjeta (str): Texto completo de la tarjeta.
    Salidas:
    - str: Descripción detallada de la tarjeta o mensaje de error si el texto es inválido.
    '''
    #tarjeta = input("ingrese su tarjeta: ")
    resultado = reconocerTarjetaAux(tarjeta)
    if isinstance(resultado, str):
        return resultado
    micro, capacidad, bus, velMin, velMax, velMinEsc  = resultado
    return (
    f"Usted está usando:\n"
    f"Una tarjeta: {micro} con capacidad de {capacidad} {bus}.\n"
    f"Velocidad mínima de escritura: {velMin}\n"
    f"Velicidad máxima de lectura/escritura: {velMax}\n"
    f"Velocidad mínima de escritura: {velMinEsc}" )

print("\n========= Decodificando la micro sin ER ===========")
codigo= "micro"
print("Para la entrada:",codigo)
print(reconocerTarjetaES(codigo),"\n")
codigo= "MicroDU1I10"
print("Para la entrada:",codigo)
print(reconocerTarjetaES(codigo),"\n")
codigo= "MicroSDU1I10"
print("Para la entrada:",codigo)
print(reconocerTarjetaES(codigo),"\n")
codigo= "MicroSDXCU3II6"
print("Para la entrada:",codigo)
print(reconocerTarjetaES(codigo),"\n")



#----------------Reto 2 con ER-------------------
#Definicion de funciones
def reconocerTarjetaAux(ptarjeta):
    '''
    Funcionamiento: Valida que el texto de la tarjeta cumpla con el formato requerido.
    Entradas:
    - ptarjeta (str): Texto de la tarjeta a validar.
    Salidas:
    - str: Mensaje de error si el texto es inválido.
    - función: Llama a la función `reconocerTarjeta` si el texto es válido.
    '''
    if not re.search("^Micro", ptarjeta):
        return "Debe ingresar un texto para poder decodificar.\nEl texto brindado no es posible de decodificar."
    elif not re.search("^MicroSD(HC|XC)?", ptarjeta):
        return "El tipo de tarjeta no es un nombre existente correctamente."
    elif not re.search("U[13]", ptarjeta):
        return "El número de la clase UHS incluído no es correcto (U1 o U3)."
    elif not re.search("II?", ptarjeta):
        return "El número de Bus UHS incluído no es correcto (I o II)."
    elif not re.search("2|4|6|10", ptarjeta):
        return "La clase incluída no es correcta (2,4,6 o 10)."
    else:
        return reconocerTarjeta(ptarjeta)

def reconocerTarjetaES(tarjeta):
    '''
    Funcionamiento: Genera una descripción legible de las características de la tarjeta.
    Entradas:
    - tarjeta (str): Texto completo de la tarjeta.
    Salidas:
    - str: Descripción detallada de la tarjeta o mensaje de error si el texto es inválido.
    '''
    #tarjeta = input("ingrese su tarjeta: ")
    resultado = reconocerTarjetaAux(tarjeta)
    if isinstance(resultado, str):
        return resultado
    micro, capacidad, bus, velMin, velMax, velMinEsc  = resultado
    return (
    f"Usted está usando:\n"
    f"Una tarjeta: {micro} con capacidad de {capacidad} {bus}.\n"
    f"Velocidad mínima de escritura: {velMin}\n"
    f"Velicidad máxima de lectura/escritura: {velMax}\n"
    f"Velocidad mínima de escritura: {velMinEsc}")


print("\n========= Decodificando la micro con ER ===========")
codigo= "micro"
print("Para la entrada:",codigo)
print(reconocerTarjetaES(codigo),"\n")
codigo= "MicroDU1I10"
print("Para la entrada:",codigo)
print(reconocerTarjetaES(codigo),"\n")
codigo= "MicroSDU1I10"
print("Para la entrada:",codigo)
print(reconocerTarjetaES(codigo),"\n")
codigo= "MicroSDXCU3II6"
print("Para la entrada:",codigo)
print(reconocerTarjetaES(codigo),"\n")


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