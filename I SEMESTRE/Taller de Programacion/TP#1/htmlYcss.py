import csv

def leerDatosCsv(rutaArchivo):
    """
    Función:
    - Lee datos desde un archivo CSV
    Responsabilidad:
    - Solo lectura de archivo CSV
    Entradas:
    - rutaArchivo: str, ubicación del archivo
    Salidas:
    - Retorna lista de listas con datos crudos
    """
    try:
        with open(rutaArchivo, "r", encoding="utf-8") as archivo:
            return list(csv.reader(archivo))
    except FileNotFoundError:
        print(f"Error: Archivo {rutaArchivo} no encontrado")
        return 
def filtrarDatosCompletos(datosCrudos):
    """
    Función:
    - Filtra filas con datos completos
    Responsabilidad:
    - Validar estructura de datos mínima
    Entradas:
    - datosCrudos: lista de listas con datos
    Salidas:
    - Retorna lista solo con filas válidas
    """
    return [fila for fila in datosCrudos if len(fila) >= 7]

def parsearNotas(notasStr):
    """
    Función:
    - Extrae y limpia notas de string
    Responsabilidad:
    - Procesamiento específico de notas
    Entradas:
    - notasStr: str con formato "n1,n2,n3,prom,notaFinal"
    Salidas:
    - Retorna tupla con (notasLimpias, notaFinal)
    """
    try:
        notasLimpias = [n.strip().replace("(", "").replace(")", "") 
                    for n in notasStr.split(",")]
        notaFinal = float(notasLimpias[3])
        return notasLimpias, notaFinal
    except (ValueError, IndexError):
        return False, False

def determinarEstado(notaFinal):
    """
    Función:
    - Determina estado académico
    Responsabilidad:
    - Solo evaluación de condición
    Entradas:
    - notaFinal: float, nota del estudiante
    Salidas:
    - Retorna str con estado ("Aprobado", etc.)
    """
    if notaFinal > 70:
        return "Aprobado"
    elif notaFinal >= 60:
        return "Reposición"
    return "Reprobado"

def procesarEstudiante(fila):
    """
    Función:
    - Procesa datos de un estudiante
    Responsabilidad:
    - Transformación de datos individual
    Entradas:
    - fila: lista con datos del estudiante
    Salidas:
    - Retorna tupla con datos procesados o False si hay error
    """
    try:
        nombre, ap1, ap2, genero, carne, correo, notasStr = fila
        notasLimpias, notaFinal = parsearNotas(notasStr)
        if notaFinal is False:
            return False
        estado = determinarEstado(notaFinal)
        generoTexto = "Masculino" if genero == "True" else "Femenino"
        return (f"{nombre} {ap1} {ap2}",generoTexto,carne,correo,notasStr,notaFinal,estado) # estado, notaFinal, notasOriginales, correo, carne, genero, nombreCompleto
    except ValueError:
        print(f"Error procesando fila: {fila}")
        return False

def calcularEstadisticas(estudiantesProcesados):
    """
    Función:
    - Calcula estadísticas académicas
    Responsabilidad:
    - Solo cómputo de estadísticas
    Entradas:
    - estudiantesProcesados: lista de tuplas procesadas
    Salidas:
    - Retorna tupla con (total, aprobados, reposicion, reprobados)
    """
    total = len(estudiantesProcesados)
    aprobados = sum(1 for e in estudiantesProcesados if e[6] == "Aprobado")
    reposicion = sum(1 for e in estudiantesProcesados if e[6] == "Reposición")
    reprobados = total - aprobados - reposicion
    return total, aprobados, reposicion, reprobados

def generarHtml(estudiantes, estadisticas):
    """
    Función:
    - Genera reporte HTML
    Responsabilidad:
    - Solo generación de HTML
    Entradas:
    - estudiantes: lista de tuplas procesadas
    - estadisticas: tupla con estadísticas
    Salidas:
    - Escribe archivo "Reporte.html"
    """
    total, aprobados, reposicion, reprobados = estadisticas
    with open("Reporte.html", "w", encoding="utf-8") as f:
        # Encabezado
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Reporte de Notas</title>
    <style>
        table { border-collapse: collapse; width: 100%; }
        th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
        th { background-color: #4CAF50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Reporte de Estudiantes</h1>
    <table>
        <tr>
            <th>Nombre</th>
            <th>Género</th>
            <th>Carné</th>
            <th>Correo</th>
            <th>Notas</th>
            <th>Estado</th>
        </tr>
""")
        # Datos
        for est in estudiantes:
            f.write(f"""
        <tr>
            <td>{est[0]}</td>
            <td>{est[1]}</td>
            <td>{est[2]}</td>
            <td>{est[3]}</td>
            <td>{est[4]}</td>
            <td>{est[6]}</td>
        </tr>
""")
        # Resumen
        f.write(f"""
    </table>
    <h2>Resumen Estadístico</h2>
    <p>Total estudiantes: {total}</p>
    <ul>
        <li>Aprobados: {aprobados} ({(aprobados/total*100):.1f}%)</li>
        <li>Reposición: {reposicion} ({(reposicion/total*100):.1f}%)</li>
        <li>Reprobados: {reprobados} ({(reprobados/total*100):.1f}%)</li>
    </ul>
</body>
</html>
""")

def generarCsv(estudiantes):
    """
    Función:
    - Genera reporte CSV
    Responsabilidad:
    - Solo generación de CSV
    Entradas:
    - estudiantes: lista de tuplas procesadas
    Salidas:
    - Escribe archivo "Reporte.csv"
    """
    with open("Reporte.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Género", "Carné", "Correo", "Notas", "Nota Final", "Estado"])
        for est in estudiantes:
            writer.writerow([est[0], est[1], est[2], est[3], est[4], est[5], est[6]])

def ejecutarFlujoPrincipal(rutaArchivo):
    """
    Función:
    - Orquesta el proceso completo
    Responsabilidad:
    - Coordinar flujo principal
    Entradas:
    - rutaArchivo: str, ubicación del archivo CSV
    Salidas:
    - Genera los archivos de reporte
    """
    # Extracción
    datosCrudos = leerDatosCsv(rutaArchivo)
    datosFiltrados = filtrarDatosCompletos(datosCrudos)
    # Transformación
    estudiantesProcesados = [e for e in 
    (procesarEstudiante(fila) for fila in datosFiltrados) 
    if e is not False]
    if not estudiantesProcesados:
        print("No hay datos válidos para procesar")
        return
    estadisticas = calcularEstadisticas(estudiantesProcesados)
    # Generación de reportes
    generarHtml(estudiantesProcesados, estadisticas)
    generarCsv(estudiantesProcesados)
    print("Reportes generados exitosamente")

# Punto de entrada
ejecutarFlujoPrincipal("BasedeDatos.csv")