import re
import names
import random


class tipoPersonalidad:
    def __init__(self):
        self.name = ()
        self.cedula = ""
        self.personalidades = []
        self.profesion = ""
        self.estado = None # Dice que se debe asiganr aleatoriamente

    def asignarName(self, pname):
        self.name = pname
        return
    def asignarCedula(self, pcedula):
        self.cedula = pcedula
        return
    def asignarPersonalidad(self, ppersonalidad):
        self.personalidades = ppersonalidad
        return
    def asignarProfesion(self, pprofesion):
        self.profesion = pprofesion
        return
    def asignarEstado(self, pestado):
        self.estado = pestado
        return
    
    def mostrarName(self):
        return self.name
    def mostrarCedula(self):
        return self.cedula
    def mostrarPersonalidad(self):
        return self.personalidades
    def mostrarProfesion(self):
        return self.profesion
    def mostrarEstado(self):
        return self.estado

    def indicarDatos(self):
        return self.name, self.cedula, self.personalidades, self.profesion, self.estado


# Diccionario de personalidades simplificado
personalidades = {
    1: ('Analista', ['Arquitecto', 'Lógico', 'Comandante', 'Innovador']),
    2: ('Diplomático', ['Abogado', 'Mediador', 'Protagonista', 'Activista']),
    3: ('Centinela', ['Logístico', 'Defensor', 'Ejecutivo', 'Cónsul']),
    4: ('Explorador', ['Virtuoso', 'Aventurero', 'Emprendedor', 'Animador'])
}

# Lista de profesiones
profesiones= "Software Developer,Analyst,Engineer,Game designer,Web designer,Designer,Game programmer," 
"Webmaster,Web developer,Network administrator,Software Engineer,Scientist,Video game developer,"
"Data Engineer,Strategist,Web Application Developer,Java Developer"
listaDeProfesiones = profesiones.split(',')

#Definicion de funciones

def generarPersonalidad():
    idCategoria = random.randint(1, 4)
    temp = personalidades[idCategoria]
    tipos = temp[1]
    nombrePersonalidad = random.choice(tipos)
    resultado = [idCategoria, nombrePersonalidad[:2].lower()]
    return resultado

def generarProfesion():
    cantidad= len(listaDeProfesiones)
    ultimo = cantidad - 1
    posicion = random.randint(0, ultimo)
    profesionSeleccionada = listaDeProfesiones[posicion]
    return profesionSeleccionada #Retorna el nombre

def generarEstado():
    # Genera aleatoriamente True (Activo) o False (Inactivo)
    estado = random.choice([True, False])
    if estado == True:
        estado = "Activo"
    else:
        estado = "Inactivo"
    return estado


###### Programa Principal ######
personalidad = tipoPersonalidad()

# Generar nombre aleatorio con dos apellidos
nombre = names.get_first_name()
apellido1 = names.get_last_name()
apellido2 = names.get_last_name()
vnombre = (nombre, apellido1, apellido2)
personalidad.asignarName(vnombre)

# Generar cédula de 9 dígitos donde el primero no es 0
primerDigito = random.randint(1, 9)  # Aseguramos que no sea 0
digitos = []
for i in range(8):
    numero = random.randint(0, 9)
    digitos.append(str(numero))
restoDigitos = ''.join(digitos)
vcedula = f"{primerDigito}{restoDigitos}"
personalidad.asignarCedula(vcedula)

# Generar y asignar personalidad
vpersonalidad = generarPersonalidad()
personalidad.asignarPersonalidad(vpersonalidad)

# Generar profesión (solo el nombre)
vprofesion = generarProfesion()
personalidad.asignarProfesion(vprofesion)

# Asignar estado usando la función externa
vestado = generarEstado()
personalidad.asignarEstado(vestado)