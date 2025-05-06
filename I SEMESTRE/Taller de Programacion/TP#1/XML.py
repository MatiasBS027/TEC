import csv
import re

def leerCsv(archivoCsv):
    """
    Función:
    - Lee y carga los datos de un archivo CSV.
    Entradas:
    - archivoCsv: str, ruta del archivo CSV a leer.
    Salidas:
    - Retorna una lista con todas las filas del archivo CSV.
    - Muestra mensaje de error si el archivo no existe.
    """
    try:
        with open(archivoCsv, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            return list(lector)
    except FileNotFoundError:
        print(f"\nError: El archivo '{archivoCsv}' no fue encontrado.")
        return False

def calcularEstado(notas):
    """
    Función:
    - Determina el estado académico del estudiante basado en sus notas.
    Entradas:
    - notas: str, cadena con formato "nota1, nota2, nota3, promedio, notaFinal".
    Salidas:
    - Retorna str con estado: "Aprobado", "Reposición" o "Reprobado".
    - Retorna "Error en nota" si hay problemas al procesar.
    """
    try:
        numeros = [n.strip() for n in notas.split(',')]
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
    Función:
    - Extrae el año de ingreso del estudiante a partir de su carné.
    Entradas:
    - carne: str, número de carné del estudiante.
    Salidas:
    - Retorna str con los primeros 4 caracteres del carné (año de ingreso).
    """
    return carne[:4]

def calcularNotas(notas):
    """
    Función:
    - Filtra y limpia el string de notas, dejando solo números, comas, puntos y espacios.
    Entradas:
    - notas: str, cadena con las notas del estudiante.
    Salidas:
    - Retorna str con las notas formateadas correctamente.
    """
    resultado = ""
    for caracter in notas:
        if re.match(r"\d|,|\s|\.", caracter):
            resultado += caracter
    return resultado

def procesarEstudiante(fila):
    """
    Función:
    - Procesa una fila del CSV y genera la estructura XML para un estudiante.
    Entradas:
    - fila: list, contiene los datos de un estudiante.
    Salidas:
    - Retorna tupla con (añoGeneracion, xmlEstudiante).
    - Retorna tupla vacía si hay error en el procesamiento.
    """
    try:
        nombre, ap1, ap2, genero, carne, correo, notas = fila
        notasFormateadas = calcularNotas(notas)
        estado = calcularEstado(notasFormateadas)
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
    Función:
    - Organiza los estudiantes por año de generación.
    Entradas:
    - filas: list, contiene todas las filas del CSV.
    Salidas:
    - Retorna lista de tuplas (año, [estudiantesXML]) ordenadas por año.
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
    Función:
    - Construye el contenido completo del archivo XML.
    Entradas:
    - generaciones: list, lista de tuplas (año, [estudiantesXML]).
    Salidas:
    - Retorna str con el contenido XML completo.
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
    Función:
    - Escribe el contenido XML en un archivo.
    Entradas:
    - archivoXml: str, ruta del archivo XML a crear.
    - contenido: str, contenido XML a escribir.
    Salidas:
    - Crea/sobrescribe el archivo XML especificado.
    """
    with open(archivoXml, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

def respaldarXml(archivoCsv, archivoXml):
    """
    Función:
    - Orquesta todo el proceso de generación del respaldo XML.
    Entradas:
    - archivoCsv: str, ruta del archivo CSV de entrada.
    - archivoXml: str, ruta del archivo XML de salida.
    Salidas:
    - Genera un archivo XML con los datos organizados por generación.
    """
    filas = leerCsv(archivoCsv)
    if filas is False:
        return  # Termina si hay error al leer el CSV
    generaciones = agruparPorGeneracion(filas)
    xmlContenido = construirXml(generaciones)
    escribirXml(archivoXml, xmlContenido)

# Ejecución principal
respaldarXml("BasedeDatos.csv", "reporte.xml")