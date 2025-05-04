import csv
import re

def leer_csv(archivoCsv):
    """
    Lee el archivo CSV y devuelve las filas como una lista.
    """
    with open(archivoCsv, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        return list(lector)

def calcular_estado(notas):
    """
    Calcula si el estudiante está aprobado, reprobado o en reposición.
    """
    nota_final = float(notas[-5:-1])
    if nota_final > 70:
        return "Aprobado"
    elif nota_final > 60:
        return "Reposición"
    else:
        return "Reprobado"

def calcular_anno(carne):
    """
    Calcula el año de ingreso del estudiante a partir del carné.
    """
    return carne[:4]

def calcular_notas(notas):
    """
    Extrae las notas de la cadena de texto.
    """
    notas = ""
    for i in notas:
        if re.match(r"\d|,|\s|\.", i):
            notas += f"{i}"
    return notas

def procesar_estudiante(fila):
    """
    Procesa una fila del CSV y devuelve el estudiante en formato XML y su año de generación.
    """
    n, a1, a2, genero, carne, correo, notas = fila
    estado = calcular_estado(notas)
    anno = calcular_anno(carne)
    estudiante = f"""
        <Estudiante carne="{carne}">
            <nombre>{n} {a1} {a2}</nombre>
            <genero>{genero}</genero>
            <correo>{correo}</correo>
            <notas>{calcular_notas(notas)}</notas>
            <estado>{estado}</estado>
        </Estudiante>"""
    return anno, estudiante

def agrupar_por_generacion(filas):
    """
    Agrupa los estudiantes por generación.
    """
    generaciones = {"2021": [], "2022": [], "2023": [], "2024": [], "2025": []}
    for fila in filas:
        anno, estudiante = procesar_estudiante(fila)
        if anno in generaciones:
            generaciones[anno].append(estudiante)
    return generaciones

def construir_xml(generaciones):
    """
    Construye el contenido del archivo XML a partir de las generaciones.
    """
    xml = '<?xml version="1.0" encoding="utf-8"?>\n<Estudiantes>\n'
    for anno, estudiantes in generaciones.items():
        xml += f'    <Generacion anno="{anno}">\n'
        xml += "\n".join(estudiantes)
        xml += f"\n    </Generacion>\n"
    xml += "</Estudiantes>"
    return xml

def escribir_xml(archivoXml, contenido):
    """
    Escribe el contenido en un archivo XML.
    """
    with open(archivoXml, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

def respaldar_xml(archivoCsv, archivoXml):
    """
    Genera el respaldo de la base de datos en formato XML.
    """
    filas = leer_csv(archivoCsv)
    generaciones = agrupar_por_generacion(filas)
    xml_contenido = construir_xml(generaciones)
    escribir_xml(archivoXml, xml_contenido)

# Llamar a la función para generar el XML
respaldar_xml("BasedeDatos.csv", "reporte.xml")