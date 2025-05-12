import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def leerDatosCsv(nombreArchivo):
    """
    Función:
    - Lee y carga los datos de un archivo CSV.
    Entradas:
    - nombreArchivo: str, ruta del archivo CSV a leer.
    Salidas:
    - Retorna una lista con todas las filas del archivo CSV.
    """
    try:
        with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
            return list(csv.reader(archivo))
    except FileNotFoundError:
        print(f"\nError: El archivo '{nombreArchivo}' no fue encontrado.")
        return False

def parsearNotas(notasStr):
    """
    Función:
    - Convierte un string de notas en formato "(n1, n2, n3)" a una tupla de floats.
    Entradas:
    - notasStr: str, cadena con las notas en formato específico.
    Salidas:
    - Retorna una tupla de 3 floats con las notas o False si hay error.
    """
    try:
        notasStr = notasStr.strip('()')
        partes = [p.strip() for p in notasStr.split(',')]
        return tuple(map(float, partes[:3]))
    except (ValueError, AttributeError):
        return False

def calcularAplazos(notas):
    """
    Función:
    - Calcula cuántas notas son aplazos (<70) y filtra las notas de aplazos.
    Entradas:
    - notas: tupla de floats con las 3 notas del estudiante.
    Salidas:
    - Retorna tupla con (cantidad de aplazos, lista de notas de aplazos).
    """
    notasAplazos = [nota for nota in notas if nota < 70]
    return len(notasAplazos), notasAplazos

def crearTuplaEstudiante(fila, notas, numAplazos):
    """
    Función:
    - Crea una estructura de datos para representar un estudiante.
    Entradas:
    - fila: lista con datos del estudiante desde CSV.
    - notas: tupla con las 3 notas del estudiante.
    - numAplazos: int, cantidad de notas <70.
    Salidas:
    - Retorna tupla con (nombre, carne, correo, notas, cantidadAplazos).
    """
    return (f"{fila[0]} {fila[1]} {fila[2]}",fila[4],fila[5],notas,numAplazos)  # cantidadAplazos, notas (tupla), correo, carne, nombreCompleto

def procesarEstudiantes(filas):
    """
    Función:
    - Procesa todos los estudiantes y filtra aquellos con 2+ aplazos.
    Entradas:
    - filas: lista de filas del CSV con datos de estudiantes.
    Salidas:
    - Retorna tupla con (estudiantesConAplazos, totalEstudiantes, 
    cantidad2Aplazos, cantidad3Aplazos, notaMinAplazos, notaMaxAplazos).
    """
    estudiantes = []
    totalEstudiantes = 0
    cantidadAplazos2 = 0
    cantidadAplazos3 = 0
    todasNotasAplazos = []
    for fila in filas:
        if len(fila) < 7:
            continue
        totalEstudiantes += 1
        notas = parsearNotas(fila[6])
        if notas is False:
            continue
        numAplazos, notasAplazos = calcularAplazos(notas)
        if numAplazos >= 2:
            estudiante = crearTuplaEstudiante(fila, notas, numAplazos)
            if numAplazos == 2:
                cantidadAplazos2 += 1
            else:
                cantidadAplazos3 += 1
            todasNotasAplazos.extend(notasAplazos)
            estudiantes.append(estudiante)
    notaMin = min(todasNotasAplazos) if todasNotasAplazos else 0
    notaMax = max(todasNotasAplazos) if todasNotasAplazos else 0
    return (estudiantes,totalEstudiantes,cantidadAplazos2,cantidadAplazos3,notaMin,notaMax)

def crearEstiloTitulo(estilos):
    """
    Función:
    - Define el estilo de texto para el título del reporte PDF.
    Entradas:
    - estilos: objeto stylesheet de ReportLab.
    Salidas:
    - Retorna objeto ParagraphStyle configurado para títulos.
    """
    return ParagraphStyle('Titulo',parent=estilos['Title'],fontSize=18,alignment=1,spaceAfter=20)

def crearEstiloEstadisticas(estilos):
    """
    Función:
    - Define el estilo de texto para las estadísticas del reporte.
    Entradas:
    - estilos: objeto stylesheet de ReportLab.
    Salidas:
    - Retorna objeto ParagraphStyle configurado para estadísticas.
    """
    return ParagraphStyle('Estadisticas',parent=estilos['Normal'],fontSize=12,leading=14,spaceBefore=20)

def crearTablaEstudiantes(estudiantes):
    """
    Función:
    - Crea y formatea la tabla de estudiantes para el PDF.
    Entradas:
    - estudiantes: lista de tuplas con datos de estudiantes.
    Salidas:
    - Retorna objeto Table de ReportLab listo para agregar al PDF.
    """
    encabezados = ['Nombre', 'Carné', 'Correo', 'Nota 1', 'Nota 2', 'Nota 3']
    tablaDatos = [encabezados]
    for estudiante in estudiantes:
        fila = [estudiante[0],  # nombreCompleto
            estudiante[1],  # carne
            estudiante[2],  # correo
            f"{estudiante[3][0]:.1f}",  # nota1
            f"{estudiante[3][1]:.1f}",  # nota2
            f"{estudiante[3][2]:.1f}"]   # nota3
        tablaDatos.append(fila)
    tabla = Table(tablaDatos, colWidths=[1.8*inch, 1*inch, 2.2*inch, 0.7*inch, 0.7*inch, 0.7*inch])
    tabla.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#4B6C9E')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#E0EAF1')),
        ('GRID', (0,0), (-1,-1), 1, colors.black)]))
    return tabla

def generarTextoEstadisticas(resultados):
    """
    Función:
    - Genera el texto de las estadísticas para el reporte.
    Entradas:
    - resultados: tupla con datos estadísticos del procesamiento.
    Salidas:
    - Retorna lista de strings con las estadísticas formateadas.
    """
    return [f"Total de estudiantes en BD: {resultados[1]}",
    f"Estudiantes con 2 aplazos: {resultados[2]} ({(resultados[2]/resultados[1]*100):.1f}%)",
    f"Estudiantes con 3 aplazos: {resultados[3]} ({(resultados[3]/resultados[1]*100):.1f}%)",
    f"Nota más baja en aplazos: {resultados[4]:.1f}",
    f"Nota más alta en aplazos: {resultados[5]:.1f}" if resultados[5] < 70 
    else "No hay notas de aplazos (todas >=70)"]

def generarReportePdf(resultados, nombreSalida):
    """
    Función:
    - Genera el documento PDF con los resultados del análisis.
    Entradas:
    - resultados: tupla con todos los datos procesados.
    - nombreSalida: str, nombre del archivo PDF a generar.
    Salidas:
    - Crea un archivo PDF con el reporte en la ruta especificada.
    """
    doc = SimpleDocTemplate(nombreSalida, pagesize=letter)
    elementos = []
    estilos = getSampleStyleSheet()
    # Título
    elementos.append(Paragraph("Reporte de Estudiantes con 2 o más Aplazos", crearEstiloTitulo(estilos)))
    # Tabla de estudiantes
    if resultados[0]:
        elementos.append(crearTablaEstudiantes(resultados[0]))
        elementos.append(Spacer(1, 0.5*inch))
    # Estadísticas
    estiloEstadisticas = crearEstiloEstadisticas(estilos)
    for texto in generarTextoEstadisticas(resultados):
        elementos.append(Paragraph(texto, estiloEstadisticas))
    doc.build(elementos)

# Ejecución del flujo principal
Csv = leerDatosCsv('BasedeDatos.csv')
if Csv is False:
    print("No se pudo leer el archivo CSV.")
resultadosProcesamiento = procesarEstudiantes(Csv)
generarReportePdf(resultadosProcesamiento, 'ReporteAplazados.pdf')
