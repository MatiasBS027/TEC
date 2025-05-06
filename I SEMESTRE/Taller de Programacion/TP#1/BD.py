# Elaborado por Matias Benavides
# iniciado el 10-04-2025
# última modificación el
# versión de python 3.13.2

# bloque import
import names  
import csv
import random

#Definición de funciones
def agregarEstudiantes(writer, lineas, cantidad, anno1, anno2, n1, n2, n3):
    """
    Funcionamiento:
    - Agrega estudiantes a la base de datos en un archivo CSV.
    - Genera datos aleatorios o utiliza datos de un archivo de texto para los estudiantes.
    Entradas:
    - writer: objeto csv.writer para escribir en el archivo CSV.
    - lineas: lista de líneas del archivo de texto con datos de estudiantes.
    - cantidad: int, cantidad de estudiantes a agregar.
    - anno1: int, año inicial para generar el carné.
    - anno2: int, año final para generar el carné.
    - n1, n2, n3: int, pesos de las evaluaciones.
    Salidas:
    - Escribe los datos de los estudiantes en el archivo CSV.
    """
    dominioCorreo = "@estudiantec.cr"
    for i in range(cantidad):
        linea = lineas[i].strip().split(",") if lineas else []
        nombre = linea[0] if linea else names.get_first_name()
        apellido1 = linea[1] if linea else names.get_last_name()
        apellido2 = linea[2] if len(linea) > 2 else names.get_last_name()
        estado = random.choice([True, False])  # Generar True/False aleatoriamente
        # Generar carné, correo y notas
        carne = generarCarne(random.randint(anno1, anno2))
        correo = generarCorreo(nombre, apellido1, carne, dominioCorreo)
        nota = generarNota(n1, n2, n3)
        # Escribir en el archivo CSV
        writer.writerow([nombre, apellido1, apellido2, estado, carne, correo, nota])

def crearBasedeDatos(pCantidad, pPorcentaje, pCantidad2, pPorcentaje2, n1, n2, n3, anno1, anno2):
    """
    Funcionamiento:
    - Procesa la información para generar una base de datos dinámica de estudiantes.
    - Combina datos generados aleatoriamente y datos de un archivo de texto.
    Entradas:
    - pCantidad: int, cantidad de estudiantes del primer recurso.
    - pPorcentaje: int, porcentaje de estudiantes del primer recurso.
    - pCantidad2: int, cantidad de estudiantes del segundo recurso.
    - pPorcentaje2: int, porcentaje de estudiantes del segundo recurso.
    - n1, n2, n3: int, pesos de las evaluaciones.
    - anno1: int, año inicial para generar el carné.
    - anno2: int, año final para generar el carné.
    Salidas:
    - Escribe los datos de los estudiantes en un archivo CSV.
    """
    # Estudiantes del primer recurso
    with open("BasedeDatos.csv", "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        for _ in range(round(obtenerCantidad(pCantidad, pPorcentaje))):
            nombre = names.get_first_name()
            apellido1 = names.get_last_name()
            apellido2 = names.get_last_name()
            estado = random.choice([True, False])  # Generar True/False aleatoriamente
            # Generar carné, correo y notas
            carne = generarCarne(random.randint(anno1, anno2))
            correo = generarCorreo(nombre, apellido1, carne, "@estudiantec.cr")
            nota = generarNota(n1, n2, n3)
            # Escribir en el archivo CSV
            writer.writerow([nombre, apellido1, apellido2, estado, carne, correo, nota])
    # Estudiantes del archivo estudiantes.txt
    with open("estudiantes.txt", "r", encoding="utf-8") as archivoEstudiantes:
        lineas = archivoEstudiantes.readlines()
    with open("BasedeDatos.csv", "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        agregarEstudiantes(writer, lineas, min(round(obtenerCantidad(pCantidad2, pPorcentaje2)), len(lineas)), anno1, anno2, n1, n2, n3)

def obtenerCantidad(cant, porc):
    """
    Funcionamiento:
    - Calcula la cantidad de estudiantes en función de un porcentaje.
    Entradas:
    - cant: int, cantidad total de estudiantes.
    - porc: int, porcentaje de estudiantes a calcular.
    Salidas:
    - int: cantidad calculada de estudiantes.
    """
    porcentajeTotal = 100
    return round(cant * (porc / porcentajeTotal))

def cargarSedes():
    """
    Funcionamiento:
    - Carga las sedes desde un archivo de texto y genera una lista de códigos de sede.
    Entradas:
    - Ninguna.
    Salidas:
    - list: lista de códigos de sede generados dinámicamente.
    - Imprime un mensaje de error si el archivo no se encuentra.
    """
    try:
        with open("sedes.txt", "r", encoding="utf-8") as archivo:
            sedes = archivo.readlines()
        # Generar códigos dinámicamente (01, 02, 03, ...)
        return [f"{i+1:02}" for i in range(len(sedes))]
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'sedes.txt'.")
        return []

def generarCarne(anno):
    """
    Funcionamiento:
    - Genera un carné único para un estudiante combinando año, sede y un número aleatorio.
    Entradas:
    - anno: int, año para generar el carné.
    Salidas:
    - str: carné único generado.
    - Lanza un error si no se cargan las sedes correctamente.
    """
    carnesGenerados = set()
    sedes = cargarSedes()
    if not sedes:
        raise ValueError("No se cargaron sedes. Verifique el archivo 'sedes.txt'.")
    while True:
        # Seleccionar un código de sede aleatorio
        sede = random.choice(sedes)
        # Generar los 4 dígitos aleatorios
        aleatorio = f"{random.randint(1000, 9999)}"
        # Formar el carné
        carne = f"{anno}{sede}{aleatorio}"
        # Verificar unicidad
        if carne not in carnesGenerados:
            carnesGenerados.add(carne)
            return carne

def generarCorreo(nom, ape, car, dominioCorreo):
    """
    Funcionamiento:
    - Genera un correo electrónico para un estudiante basado en su nombre, apellido y carné.
    Entradas:
    - nom: str, nombre del estudiante.
    - ape: str, apellido del estudiante.
    - car: str, carné del estudiante.
    - dominioCorreo: str, dominio del correo.
    Salidas:
    - str: correo electrónico generado.
    """
    correo = f"{nom[0]}{ape}{car[6:]}{dominioCorreo}"
    return correo.lower()

def generarNota(n1, n2, n3):
    """
    Funcionamiento:
    - Genera aleatoriamente las notas de un estudiante para tres evaluaciones.
    - Calcula el total ponderado según los pesos de las evaluaciones.
    Entradas:
    - n1, n2, n3: int, pesos de las evaluaciones.
    Salidas:
    - tuple: notas de las tres evaluaciones y el total ponderado.
    """
    nota1 = round(random.randint(0, 100), 1)
    nota2 = round(random.randint(0, 100), 1)
    nota3 = round(random.randint(0, 100), 1)
    total = round((n1 * (nota1 / 100) + n2 * (nota2 / 100) + n3 * (nota3 / 100)), 1)
    redondeo = round(total)
    return (nota1, nota2, nota3, total, redondeo)

def crearBasedeDatosAux(pCantidad, pPorcentaje, pCantidad2, pPorcentaje2, n1, n2, n3, anno1, anno2):
    """
    Funcionamiento:
    - Valida las variables ingresadas y llama a la función principal para crear la base de datos.
    Entradas:
    - pCantidad: int, cantidad de estudiantes del primer recurso.
    - pPorcentaje: int, porcentaje de estudiantes del primer recurso.
    - pCantidad2: int, cantidad de estudiantes del segundo recurso.
    - pPorcentaje2: int, porcentaje de estudiantes del segundo recurso.
    - n1, n2, n3: int, pesos de las evaluaciones.
    - anno1: int, año inicial para generar el carné.
    - anno2: int, año final para generar el carné.
    Salidas:
    - Llama a la función crearBasedeDatos si los datos son válidos.
    - Imprime mensajes de error si los datos no son válidos.
    """
    try:
        pCantidad = int(pCantidad)
        pPorcentaje = int(pPorcentaje)
        pCantidad2 = int(pCantidad2)
        pPorcentaje2 = int(pPorcentaje2)
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        anno1 = int(anno1)
        anno2 = int(anno2)
        if anno2 < anno1:
            print("El segundo año debe ser mayor que el primer año.")
            return 
        if pCantidad > 0 and pPorcentaje > 0:
            if n1 + n2 + n3 == 100:
                return crearBasedeDatos(pCantidad, pPorcentaje, pCantidad2, pPorcentaje2, n1, n2, n3, anno1, anno2)
            else:
                print("Los valores de las evaluaciones tienen que sumar exactamente 100 entre los tres.")
                return 
        else:
            print("Ingrese datos válidos.")
            return 
    except ValueError:
        print("Ingrese datos válidos.")
        return 

def crearBasedeDatosEs():
    """
    Funcionamiento:
    - Solicita al usuario los datos necesarios para crear la base de datos dinámica.
    - Valida las entradas del usuario.
    Entradas:
    - Ninguna (los datos se solicitan mediante input).
    Salidas:
    - Llama a la función crearBasedeDatosAux con los datos ingresados.
    - Imprime mensajes de error si las entradas no son válidas.
    """
    while True:
        try:
            cantidad1 = int(input("Ingrese la cantidad de alumnos que se tomaran de la primera fuente: "))
            porcentaje1 = int(input("Ingrese el porcentaje de esos alumnos que se tomaran de la primera fuente: "))
            cantidad2 = int(input("Ingrese la cantidad de alumnos que se tomaran de la segunda fuente: "))
            porcentaje2 = int(input("Ingrese el porcentaje de esos alumnos que se tomaran de la segunda fuente: "))
            n1 = int(input("Ingrese el valor de la primera evaluación: "))
            n2 = int(input("Ingrese el valor de la segunda evaluación: "))
            n3 = int(input("Ingrese el valor de la tercera evaluación: "))
            anno1 = int(input("Ingrese el primer año para el rango de carné (Debe ser el menor): "))
            anno2 = int(input("Ingrese el segundo año para el rango de carné (Debe ser el mayor): "))
            return crearBasedeDatosAux(cantidad1, porcentaje1, cantidad2, porcentaje2, n1, n2, n3, anno1, anno2)
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
            return

# programa principal
crearBasedeDatosEs()