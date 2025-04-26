#Elaborado por: Matias Benavides y Luis Carlos Tinoco Vargas
#Fecha de creacion: 23/4/2024 6:00 PM
#Ultima modificacion: 26/4/2024 12:00 PM
# Version de Python: 3.13.2

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

#----------------Reto 2-------------------
#Definicion de funciones
def reconocerTarjeta(ptarjeta):
    micro = "MicroSD"
    capacidad = "16MB, 32MB, etc"
    bus = "sin bus UHS"
    velMin = "10MB/s"
    velMax = "104MB/s"
    velMinEsc = "2"

    if ptarjeta.startswith("MicroSDHC"):
        micro += "HC"
        capacidad = "4GB, 8GB, 16GB, etc"
        bus = "con bus de UHS"
    elif ptarjeta.startswith("MicroSDXC"):
        micro += "XC"
        capacidad = "64GB, 128GB, etc"
        bus = "con bus de UHS"
    if "U3" in ptarjeta:
        velMin = "30MB/s"
    if "II" in ptarjeta:
        velMax = "312MB/s"
    if "4" in ptarjeta:
        velMinEsc = "4"
    elif "6" in ptarjeta:
        velMinEsc = "6"
    elif "10" in ptarjeta:
        velMinEsc = "10"

    return micro, capacidad, bus, velMin, velMax, velMinEsc


#-------------Reto 3------------------
#Definicion de funciones
def anchuraLlanta(codigo):
    '''
    Funcionamiento: Obtiene el ancho de la llanta en milímetros
    Entradas:
    -codigo(str): Código completo del neumático
    Salidas:
    -str: Ancho de la llanta en milímetros
    '''
    if codigo[0:3] == "195":
        return "195"
    elif codigo[0:3] == "165":
        return "165"

def alturaAncho(codigo):
    '''
    Funcionamiento: Obtiene la relación de aspecto entre altura y ancho
    Entradas:
    -codigo(str): Código completo del neumático
    Salidas:
    -str: Porcentaje de la relación altura/ancho
    '''
    if codigo[3:5] == "55":
        return "55%"
    elif codigo[3:5] == "70":
        return "70%"

def construccion(codigo):
    '''
    Funcionamiento: Determina el tipo de construcción del neumático
    Entradas:
    -codigo(str): Código completo del neumático
    Salidas:
    -str: Tipo de construcción (Radial o Diagonal)
    '''
    if codigo[5] == "R":
        return "Radial"
    elif codigo[5] == "D":
        return "Diagonal"

def diametroLlanta(codigo):
    '''
    Funcionamiento: Obtiene el diámetro de la llanta en pulgadas
    Entradas:
    -codigo(str): Código completo del neumático
    Salidas:
    -str: Diámetro de la llanta en pulgadas
    '''
    if codigo[6:8] == "16":
        return "16"
    elif codigo[6:8] == "14":
        return "14"

def capacidadCarga(codigo):
    '''
    Funcionamiento: Convierte el índice de carga a su equivalente en kilogramos
    Entradas:
    -codigo(str): Código completo del neumático
    Salidas:
    -str: Capacidad de carga en kilogramos
    '''
    if codigo[8:10] == "70":
        return "335"
    elif codigo[8:10] == "71":
        return "345"
    elif codigo[8:10] == "72":
        return "355"
    elif codigo[8:10] == "73":
        return "365"
    elif codigo[8:10] == "74":
        return "375"
    elif codigo[8:10] == "75":
        return "387"
    elif codigo[8:10] == "76":
        return "400"
    elif codigo[8:10] == "77":
        return "412"
    elif codigo[8:10] == "78":
        return "425"
    elif codigo[8:10] == "79":
        return "437"
    elif codigo[8:10] == "80":
        return "450"
    elif codigo[8:10] == "81":
        return "462"
    elif codigo[8:10] == "82":
        return "475"
    elif codigo[8:10] == "83":
        return "487"
    elif codigo[8:10] == "84":
        return "500"
    elif codigo[8:10] == "85":
        return "515"
    elif codigo[8:10] == "86":
        return "530"
    elif codigo[8:10] == "87":
        return "545"
    elif codigo[8:10] == "88":
        return "560"
    elif codigo[8:10] == "89":
        return "580"
    else:
        return "600"

def velocidadMax(codigo):
    '''
    Funcionamiento: Convierte el código de velocidad a kilómetros por hora
    Entradas:
    -codigo(str): Código completo del neumático
    Salidas:
    -str: Velocidad máxima en km/h
    '''
    if codigo[10:] == "K":
        return "110"
    elif codigo[10:] == "L":
        return "120"
    elif codigo[10:] == "M":
        return "130"
    elif codigo[10:] == "N":
        return "140"
    elif codigo[10:] == "P":
        return "150"
    elif codigo[10:] == "Q":
        return "160"
    elif codigo[10:] == "R":
        return "170"
    elif codigo[10:] == "S":
        return "180"
    elif codigo[10:] == "T":
        return "190"
    elif codigo[10:] == "U":
        return "200"
    elif codigo[10:] == "H":
        return "210"
    elif codigo[10:] == "V":
        return "240"
    elif codigo[10:] == "W":
        return "270"
    elif codigo[10:] == "Y":
        return "300"
    else:
        return "más de 240"


def decodificarNeumáticos(codigo):
    '''
    Funcionamiento: Descompone el código del neumático en sus componentes
    Entradas:
    -codigo(str): Código completo del neumático
    Salidas:
    -tuple: (altura, anchura, radial, diametro, capacidad, velocidad)
    '''
    anchura = anchuraLlanta(codigo)
    altura = alturaAncho(codigo)
    radial = construccion(codigo)
    diametro = diametroLlanta(codigo)
    capacidad = capacidadCarga(codigo)
    velocidad = velocidadMax(codigo)
    return altura, anchura, radial, diametro, capacidad, velocidad