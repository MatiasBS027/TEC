#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 20/05/2025
#última modificación 20/05/2025 20:00
#python versión 3.13.2

import re
import names
import random


class tipoPersonalidad:
    """
    Clase para representar una persona con tipo de personalidad, nombre, cédula, profesión y estado.

    Atributos:
    - name (tuple): nombre y apellidos (nombre, apellido1, apellido2).
    - cedula (str): número de identificación único.
    - personalidades (list): lista con categoría y abreviatura del tipo de personalidad.
    - profesion (str): profesión asignada.
    - estado (str): "Activo" o "Inactivo".
    """

    def __init__(self):
        self.name = ()
        self.cedula = ""
        self.personalidades = []
        self.profesion = ""
        self.estado = None  # Se asigna aleatoriamente

    def asignarName(self, pname):
        """
        Asigna el nombre completo a la persona.
        Entradas:
        - pname (tuple): tupla con (nombre, apellido1, apellido2).
        Salidas:
        - None
        """
        self.name = pname
        return

    def asignarCedula(self, pcedula):
        """
        Asigna la cédula a la persona.
        Entradas:
        - pcedula (str): cédula.
        Salidas:
        - None
        """
        self.cedula = pcedula
        return

    def asignarPersonalidad(self, ppersonalidad):
        """
        Asigna el tipo de personalidad a la persona.
        Entradas:
        - ppersonalidad (list): lista con datos de personalidad.
        Salidas:
        - None
        """
        self.personalidades = ppersonalidad
        return

    def asignarProfesion(self, pprofesion):
        """
        Asigna la profesión a la persona.
        Entradas:
        - pprofesion (str): nombre de profesión.
        Salidas:
        - None
        """
        self.profesion = pprofesion
        return

    def asignarEstado(self, pestado):
        """
        Asigna el estado a la persona.
        Entradas:
        - pestado (str): "Activo" o "Inactivo".
        Salidas:
        - None
        """
        self.estado = pestado
        return
    
    def mostrarName(self):
        """
        Devuelve el nombre completo.
        Entradas:
        - None
        Salidas:
        - tuple: nombre completo (nombre, apellido1, apellido2).
        """
        return self.name

    def mostrarCedula(self):
        """
        Devuelve la cédula.
        Entradas:
        - None
        Salidas:
        - str: cédula.
        """
        return self.cedula

    def mostrarPersonalidad(self):
        """
        Devuelve la personalidad.
        Entradas:
        - None
        Salidas:
        - list: datos de personalidad.
        """
        return self.personalidades

    def mostrarProfesion(self):
        """
        Devuelve la profesión.
        Entradas:
        - None
        Salidas:
        - str: profesión.
        """
        return self.profesion

    def mostrarEstado(self):
        """
        Devuelve el estado.
        Entradas:
        - None
        Salidas:
        - str: estado ("Activo" o "Inactivo").
        """
        return self.estado

    def indicarDatos(self):
        """
        Devuelve todos los datos de la persona en una tupla.
        Entradas:
        - None
        Salidas:
        - tuple: (nombre, cédula, personalidad, profesión, estado).
        """
        return self.name, self.cedula, self.personalidades, self.profesion, self.estado


# Diccionario de personalidades simplificado
personalidades = {
    1: ('Analista', ['Arquitecto', 'Lógico', 'Comandante', 'Innovador']),
    2: ('Diplomático', ['Abogado', 'Mediador', 'Protagonista', 'Activista']),
    3: ('Centinela', ['Logístico', 'Defensor', 'Ejecutivo', 'Cónsul']),
    4: ('Explorador', ['Virtuoso', 'Aventurero', 'Emprendedor', 'Animador'])
}

# Lista de profesiones
profesiones= "Software Developer,Analyst,Engineer,Game designer,Web designer,Designer,Game programmer," \
"Webmaster,Web developer,Network administrator,Software Engineer,Scientist,Video game developer," \
"Data Engineer,Strategist,Web Application Developer,Java Developer"
listaDeProfesiones = profesiones.split(',')

def generarPersonalidad():
    """
    Genera aleatoriamente una personalidad asignada a una categoría y una abreviatura.
    Entradas:
    - None
    Salidas:
    - list: [idCategoria (int), abreviatura de personalidad (str)]
    """
    idCategoria = random.randint(1, 4)
    temp = personalidades[idCategoria]
    tipos = temp[1]
    nombrePersonalidad = random.choice(tipos)
    resultado = [idCategoria, nombrePersonalidad[:2].lower()]
    return resultado

def generarProfesion():
    """
    Selecciona aleatoriamente una profesión de la lista predefinida.
    Entradas:
    - None
    Salidas:
    - str: nombre de la profesión seleccionada.
    """
    cantidad= len(listaDeProfesiones)
    ultimo = cantidad - 1
    posicion = random.randint(0, ultimo)
    profesionSeleccionada = listaDeProfesiones[posicion]
    return profesionSeleccionada

def generarEstado():
    """
    Genera aleatoriamente un estado "Activo" o "Inactivo".
    Entradas:
    - None
    Salidas:
    - str: "Activo" o "Inactivo".
    """
    estado = random.choice([True, False])
    if estado == True:
        estado = "Activo"
    else:
        estado = "Inactivo"
    return estado


def generarPersona():
    """
    Crea un objeto tipoPersonalidad con datos generados aleatoriamente:
    nombre completo, cédula, personalidad, profesión y estado.
    Entradas:
    - None
    Salidas:
    - tipoPersonalidad: objeto con datos asignados.
    """
    persona = tipoPersonalidad()

    # Generar nombre aleatorio con dos apellidos
    nombre = names.get_first_name()
    apellido1 = names.get_last_name()
    apellido2 = names.get_last_name()
    vnombre = (nombre, apellido1, apellido2)
    persona.asignarName(vnombre)

    # Generar cédula de 9 dígitos donde el primero no es 0
    primerDigito = random.randint(1, 9)  # Aseguramos que no sea 0
    digitos = []
    for i in range(8):
        numero = random.randint(0, 9)
        digitos.append(str(numero))
    restoDigitos = ''.join(digitos)
    vcedula = f"{primerDigito}{restoDigitos}"
    persona.asignarCedula(vcedula)

    # Generar y asignar personalidad
    vpersonalidad = generarPersonalidad()
    persona.asignarPersonalidad(vpersonalidad)

    # Generar profesión (solo el nombre)
    vprofesion = generarProfesion()
    persona.asignarProfesion(vprofesion)

    # Asignar estado usando la función externa
    vestado = generarEstado()
    persona.asignarEstado(vestado)

    return persona
