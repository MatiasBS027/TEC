# Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
# Fecha de creación 20/05/2025
# Última modificación 21/05/2025
# Python versión 3.13.2

#importacion
from archivos import *
from clase import *
import re

#Funciones
def buscarCedula():
    """
    Solicita al usuario ingresar una cédula válida.
    La cédula debe tener 9 dígitos y el primero no puede ser 0.

    Entradas:
    - None (input desde consola)

    Salidas:
    - str: cédula válida si la entrada es correcta.
    - None: si la cédula es inválida, muestra mensaje y retorna None.
    """
    cedula = input("Ingrese la cédula a validar (9 dígitos, primero no 0): ").strip()
    if re.fullmatch(r"[1-9][0-9]{8}", cedula):
        return cedula
    else:
        print("Cédula inválida. Debe tener 9 dígitos y el primero no puede ser 0.")
        return

def buscarPersona(equipo, cedula):
    """
    Busca una persona en el equipo por su cédula.

    Entradas:
    - equipo (list): lista de objetos tipoPersonalidad.
    - cedula (str): cédula a buscar.

    Salidas:
    - tipoPersonalidad: objeto persona encontrada.
    - None: si no se encuentra la persona, imprime mensaje y retorna None.
    """
    for persona in equipo:
        if persona.mostrarCedula() == cedula:
            return persona
    print(f"No se encontró ninguna persona con la cédula {cedula}.")
    return None

def insertarMiembro(equipo, cantidad):
    """
    Inserta una cantidad de miembros generados aleatoriamente al equipo,
    mostrando su información y guardando los datos en archivo.

    Entradas:
    - equipo (list): lista donde se agregarán los miembros.
    - cantidad (int): número de miembros a generar e insertar.

    Salidas:
    - None (imprime información y mensajes).
    """
    for i in range(cantidad):
        persona = generarPersona()
        equipo.append(persona)

        nombre = persona.mostrarName()
        cedula = persona.mostrarCedula()
        personalidad = persona.mostrarPersonalidad()
        profesion = persona.mostrarProfesion()
        estado = persona.mostrarEstado()

        nombreCompleto = f"{nombre[0]} {nombre[1]} {nombre[2]}"
        personalidadStr = f"[{personalidad[0]},\"{personalidad[1]}\"]"
        print(f"Nombre: {nombreCompleto}, Cédula: {cedula}, Personalidad: {personalidadStr}, Profesión: {profesion}, Estado: {estado}")

    mensaje = guardarArchivo(equipo)
    print(mensaje)

def cambiarNombre(equipo, cedula, nuevoNombre):
    """
    Cambia el nombre completo (nombre y dos apellidos) de la persona con la cédula dada.

    Entradas:
    - equipo (list): lista de personas.
    - cedula (str): cédula de la persona a modificar.
    - nuevoNombre (str): cadena con tres palabras (nombre y dos apellidos).

    Salidas:
    - None (imprime mensajes de éxito o error).
    """
    personaEncontrada = buscarPersona(equipo, cedula)
    if not personaEncontrada:
        print(f"No se encontró persona con cédula {cedula}.")
        return
    partes = nuevoNombre.split()
    if len(partes) != 3:
        print("Debe ingresar exactamente 3 palabras: nombre y dos apellidos.")
        return
    personaEncontrada.asignarName(tuple(partes))
    guardarArchivo(equipo)
    print(f"Nombre actualizado correctamente.")

def eliminarMiembro(equipo, cedula):
    """
    Cambia el estado de una persona a "Inactivo",.

    Entradas:
    - equipo (list): lista de personas.
    - cedula (str): cédula de la persona a eliminar.

    Salidas:
    - imprime mensajes de éxito o error.
    """
    personaEncontrada = buscarPersona(equipo, cedula)
    if not personaEncontrada:
        print(f"No se encontró persona con cédula {cedula}.")
        return
    estadoActual = personaEncontrada.mostrarEstado()
    if estadoActual == "Inactivo":
        print("La persona ya está eliminada (estado Inactivo). No es posible eliminarla nuevamente.")
        return
    personaEncontrada.asignarEstado("Inactivo")
    guardarArchivo(equipo)
    print(f"La persona con cédula {cedula} ha sido eliminada.")

def mostrarInfoCompleta(equipo):
    """
    Muestra en consola la información completa de todos los miembros del equipo.

    Entradas:
    - equipo (list): lista de personas.

    Salidas:
    - None (imprime la información).
    """
    if not equipo:
        print("No hay miembros en el equipo para mostrar.")
        return
    
    for idx, persona in enumerate(equipo, start=1):
        nombre = persona.mostrarName()
        cedula = persona.mostrarCedula()
        personalidad = persona.mostrarPersonalidad()
        profesion = persona.mostrarProfesion()
        estado = persona.mostrarEstado()

        nombreCompleto = f"{nombre[0]} {nombre[1]} {nombre[2]}"
        personalidadStr = f"[{personalidad[0]}, \"{personalidad[1]}\"]"

        print(f"Miembro #{idx}:")
        print(f"  Nombre completo: {nombreCompleto}")
        print(f"  Cédula: {cedula}")
        print(f"  Personalidad: {personalidadStr}")
        print(f"  Profesión: {profesion}")
        print(f"  Estado: {estado}")

def mostrarCategorias(equipo):
    """
    Permite al usuario seleccionar una categoría y muestra los miembros del equipo que pertenecen a ella.

    Entradas:
    - equipo (list): lista de personas.

    Salidas:
    - None (imprime lista de miembros por categoría o mensajes de error).
    """
    categorias = {
        "1": "Analistas",
        "2": "Diplomaticos",
        "3": "Centinelas",
        "4": "Exploradores"
    }
    print("Categorías disponibles:")
    for num, cate in categorias.items():
        print(f"{num}. {cate}")
    opcion = input("Seleccione una categoría por número: ").strip()
    if opcion not in categorias:
        print("Opción inválida. Intente nuevamente.")
        return
    categoriaElegida = opcion  # Será "1", "2", etc.
    print(f"\nMiembros del equipo en la categoría: {categorias[opcion]}\n")
    miembrosCategoria = []
    for persona in equipo:
        personalidad = persona.mostrarPersonalidad()  # [idCategoria, código]
        if str(personalidad[0]) == categoriaElegida:
            miembrosCategoria.append(persona)
    if not miembrosCategoria:
        print("No se encontraron miembros en esta categoría.")
        return
    for id, persona in enumerate(miembrosCategoria, start=1):
        nombre = persona.mostrarName()
        cedula = persona.mostrarCedula()
        personalidad = persona.mostrarPersonalidad()
        profesion = persona.mostrarProfesion()
        estado = persona.mostrarEstado()
        nombreCompleto = f"{nombre[0]} {nombre[1]} {nombre[2]}"
        personalidadStr = f"[{personalidad[0]}, \"{personalidad[1]}\"]"

        print(f"Miembro #{id}:")
        print(f"  Nombre completo: {nombreCompleto}")
        print(f"  Cédula: {cedula}")
        print(f"  Personalidad: {personalidadStr}")
        print(f"  Profesión: {profesion}")
        print(f"  Estado: {estado}")

def mostrarPersonaPorCedula(equipo):
    """
    Pide al usuario ingresar una cédula válida y muestra la información completa
    de la persona que coincida con esa cédula.

    Entradas:
    - equipo (list): lista de personas.

    Salidas:
    - None (imprime información o mensajes).
    """
    while True:
        print("\n--- Buscar Persona por Cédula ---")
        print("Digite una cédula válida")
        cedula = buscarCedula()
        if not cedula:
            return

        persona = buscarPersona(equipo, cedula)
        if not persona:
            continue  # Si no encuentra, pide otra cédula

        # Mostrar toda la información
        nombre = persona.mostrarName()
        cedula = persona.mostrarCedula()
        personalidad = persona.mostrarPersonalidad()
        profesion = persona.mostrarProfesion()
        estado = persona.mostrarEstado()

        nombreCompleto = f"{nombre[0]} {nombre[1]} {nombre[2]}"
        personalidadStr = f"[{personalidad[0]}, \"{personalidad[1]}\"]"

        print("\n--- Información del Miembro ---")
        print(f"Nombre Completo : {nombreCompleto}")
        print(f"Cédula          : {cedula}")
        print(f"Personalidad    : {personalidadStr}")
        print(f"Profesión       : {profesion}")
        print(f"Estado          : {estado}")

        break
