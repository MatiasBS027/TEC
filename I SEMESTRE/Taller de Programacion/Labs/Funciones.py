#Elaborado por: Matias Benavides
#Fecha de creacion: 23/4/2024 6:00 PM
#Ultima modificacion: 23/4/2024 6:00 PM
# Version de Python: 3.13.2

#----------------Reto 1-------------------
#Definicion de funciones
def diametroVarilla (diametro):
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
    if fabricacion == "S":
        fabricacion = "Acero al carbono no soldable a temperatura ambiente." 
    elif fabricacion == "W":
        fabricacion = "Acero al carbono soldablea temperatura ambiente"
    return fabricacion

def aceroVarilla (acero):
    if acero == "40":
        acero = "2800 kgf/cm2"
    elif acero == "60":
        acero = "4200 kgf/cm2"
    elif acero == "70":
        acero = "5000 kgf/cm2" 
    return acero

def nomenclatraVarilla (pcodigo):
    fabricante = pcodigo[:2]
    diametro = diametroVarilla(pcodigo[2])
    fabricacion = fabricacionVarilla(pcodigo[3])
    acero = aceroVarilla(pcodigo[4:])

    return fabricante, diametro, fabricacion, acero

def nomenclatraVarillaAux (pcodigo):
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


#-------------Reto 2------------------
#Definicion de funciones
#-------------Reto 2------------------
def tipoTarjeta(tipo):
    if tipo == "MicroSDXC":
        tipo = "MicroSDXC"
    elif tipo == "MicroSD":
        tipo = "MicroSD"
    return tipo

def capacidadTarjeta(tipo, numero):
    if tipo == "MicroSD" and numero == "1":
        capacidad = "16 MB"
    elif tipo == "MicroSD" and numero == "2":
        capacidad = "32 MB"
    elif tipo == "MicroSDXC" and numero == "1":
        capacidad = "64 GB"
    elif tipo == "MicroSDXC" and numero == "2":
        capacidad = "128 GB"
    return capacidad

def velocidadTarjeta(letra, numero):
    if letra == "U" and numero == "1":
        velocidad = "10 MB/s"
    elif letra == "U" and numero == "3":
        velocidad = "30 MB/s"
    elif letra == "I":
        velocidad = "104 MB/s"
    return velocidad

def decodificarMicro(codigo):
    tipo = tipoTarjeta(codigo[:8])
    bus = "sin bus UHS" if "SD" in codigo else "con bus UHS"
    clase = codigo[-2:]
    velocidadEscritura = f"{clase[1]} MB/s"
    velocidadLectura = velocidadTarjeta(codigo[-3], clase[1])
    capacidad = capacidadTarjeta(tipo, clase[1])
    
    return tipo, capacidad, bus, velocidadEscritura, velocidadLectura

def decodificarMicroAux(codigo):
    if not codigo:
        return "Debe ingresar un texto para poder decodificar."
    if not codigo.startswith(("MicroSDXC", "MicroSD")):
        return "El tipo de tarjeta no es un nombre existente correctamente."
    return decodificarMicro(codigo)

def decodificarMicroES(codigo):
    resultado = decodificarMicroAux(codigo)
    if isinstance(resultado, str):
        return resultado
    tipo, capacidad, bus, velEscritura, velLectura = resultado
    return (f"Usted está usando:\n"
            f"Una tarjeta: {tipo} con capacidad de: {capacidad}, {bus}\n"
            f"Velocidad mínima de escritura: {velEscritura}\n"
            f"Velocidad máxima de lectura/escritura: {velLectura}\n"
            f"Velocidad mínima de escritura: {velEscritura}")

print("\n=== Decodificando tarjetas micro ===")
codigo = "MicroSDU1I10"
print("Para la entrada:", codigo)
print(decodificarMicroES(codigo))
codigo = "MicroSDXCU3I16"
print("Para la entrada:", codigo)
print(decodificarMicroES(codigo))
codigo = ""
print("Para la entrada:", codigo)
print(decodificarMicroES(codigo))