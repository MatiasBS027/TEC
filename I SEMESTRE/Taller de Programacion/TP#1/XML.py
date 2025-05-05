import csv
import re

def leerCsv(archivoCsv):
    """
    Lee el archivo CSV y devuelve las filas como una lista.
    """
    with open(archivoCsv, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        return list(lector)

def calcularEstado(notas):
    """
    Calcula si el estudiante está aprobado, reprobado o en reposición.
    Args:
        notas (str): String con el formato "nota1, nota2, nota3, promedio, notaFinal"
    Returns:
        str: Estado del estudiante (Aprobado/Reposición/Reprobado)
    """
    try:
        # Dividimos por comas y limpia espacios
        numeros = [n.strip() for n in notas.split(',')]
        # Tomamos el último número (nota final)
        notaFinal = float(numeros[-1])
        if notaFinal >= 70:
            return "Aprobado"
        elif notaFinal >= 60:
            return "Reposición"
        else:
            return "Reprobado"
    except Exception:
        return "Error en nota"

def calcularAnno(carne):
    """
    Calcula el año de ingreso del estudiante a partir del carné.
    """
    return carne[:4]

def calcularNotas(notas):
    """
    Extrae las notas de la cadena de texto.
    """
    resultado = ""
    for caracter in notas:
        if re.match(r"\d|,|\s|\.", caracter):
            resultado += caracter
    return resultado

def procesarEstudiante(fila):
    """
    Procesa una fila del CSV y devuelve el estudiante en formato XML y su año de generación.
    """
    try:
        nombre, ap1, ap2, genero, carne, correo, notas = fila
        notasFormateadas = calcularNotas(notas)  # Formatea las notas para mostrar
        estado = calcularEstado(notasFormateadas)  # Calcula estado con las notas formateadas
        anno = calcularAnno(carne)
        estudiante = f"""
        <Estudiante carne="{carne}">
            <nombre>{nombre} {ap1} {ap2}</nombre>
            <genero>{genero}</genero>
            <correo>{correo}</correo>
            <notas>{notasFormateadas}</notas>
            <estado>{estado}</estado>
        </Estudiante>"""
        return anno, estudiante
    except Exception:
        return "", ""

def agruparPorGeneracion(filas):
    """
    Agrupa los estudiantes por generación usando listas.
    """
    generaciones = []
    annosUsados = []
    
    for fila in filas:
        anno, _ = procesarEstudiante(fila)
        if anno not in annosUsados:
            annosUsados.append(anno)
    
    annosUsados.sort()
    
    for anno in annosUsados:
        estudiantes = []
        for fila in filas:
            annoEst, estudiante = procesarEstudiante(fila)
            if annoEst == anno:
                estudiantes.append(estudiante)
        if estudiantes:
            generaciones.append((anno, estudiantes))
    
    return generaciones

def construirXml(generaciones):
    """
    Construye el contenido del archivo XML.
    """
    xml = '<?xml version="1.0" encoding="utf-8"?>\n<Estudiantes>\n'
    for anno, estudiantes in generaciones:
        xml += f'    <Generacion anno="{anno}">\n'
        xml += "\n".join(estudiantes)
        xml += f"\n    </Generacion>\n"
    xml += "</Estudiantes>"
    return xml

def escribirXml(archivoXml, contenido):
    """
    Escribe el contenido en un archivo XML.
    """
    with open(archivoXml, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

def respaldarXml(archivoCsv, archivoXml):
    """
    Genera el respaldo de la base de datos en formato XML.
    """
    filas = leerCsv(archivoCsv)
    generaciones = agruparPorGeneracion(filas)
    xmlContenido = construirXml(generaciones)
    escribirXml(archivoXml, xmlContenido)

# Llamar a la función para generar el XML
respaldarXml("BasedeDatos.csv", "reporte.xml")