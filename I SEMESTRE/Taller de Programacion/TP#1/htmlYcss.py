import csv

def leerEstudiantes(archivoCsv):
    """Lee los datos de la base de datos dinámica y los retorna como una lista."""
    estudiantes = []
    with open(archivoCsv, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if len(fila) >= 7:  # Validar que la fila tenga al menos 7 columnas
                estudiantes.append(fila)
    return estudiantes

def calcularEstadisticas(estudiantes):
    """Calcula las estadísticas de los estudiantes y retorna los resultados."""
    totalEstudiantes = len(estudiantes)
    aprobados = 0
    enReposicion = 0
    reprobados = 0
    for estudiante in estudiantes:
        if len(estudiante) >= 7:  # Validar que la fila tenga al menos 7 columnas
            notas = estudiante[6].split(",")
            if len(notas) > 3:  # Validar que haya suficientes notas
                try:
                    # Limpiar caracteres no deseados de la nota
                    notaFinal = float(notas[3].strip().replace("(", "").replace(")", ""))
                    if notaFinal > 70:
                        aprobados += 1
                    elif 60 <= notaFinal <= 70:
                        enReposicion += 1
                    else:
                        reprobados += 1
                except ValueError:
                    print(f"Advertencia: Nota inválida para el estudiante {estudiante}")
    porcentajeAprobados = round((aprobados / totalEstudiantes) * 100, 2) if totalEstudiantes > 0 else 0
    porcentajeReposicion = round((enReposicion / totalEstudiantes) * 100, 2) if totalEstudiantes > 0 else 0
    porcentajeReprobados = round((reprobados / totalEstudiantes) * 100, 2) if totalEstudiantes > 0 else 0
    return totalEstudiantes, aprobados, enReposicion, reprobados, porcentajeAprobados, porcentajeReposicion, porcentajeReprobados

def generarReporte(estudiantes, estadisticas):
    """Genera un archivo HTML con el reporte de los estudiantes."""
    totalEstudiantes, aprobados, enReposicion, reprobados, porcentajeAprobados, porcentajeReposicion, porcentajeReprobados = estadisticas

    # Generar HTML
    with open("Reporte.html", "w", encoding="utf-8") as archivoHtml:
        archivoHtml.write("""
        <html>
        <head>
            <title>Reporte de Notas</title>
            <style>
                table { width: 100%; border-collapse: collapse; }
                th { background-color: #007BFF; color: white; padding: 8px; text-align: left; }
                tr:nth-child(even) { background-color: #D6EAF8; }
                tr:nth-child(odd) { background-color: #FFFFFF; }
                td { padding: 8px; text-align: left; border: 1px solid #ddd; }
            </style>
        </head>
        <body>
            <h1>Reporte de Notas</h1>
            <h2>Detalle de Estudiantes</h2>
            <table>
                <tr>
                    <th>Nombre</th>
                    <th>Apellidos</th>
                    <th>Género</th>
                    <th>Carné</th>
                    <th>Correo</th>
                    <th>Notas</th>
                    <th>Estado</th>
                </tr>
        """)

        for estudiante in estudiantes:
            try:
                nombre, apellido1, apellido2, estado, carne, correo, notas = estudiante
                notaFinal = float(notas.split(",")[3].strip().replace("(", "").replace(")", ""))
                estadoTexto = "Aprobado" if notaFinal > 70 else "Reposición" if 60 <= notaFinal <= 70 else "Reprobado"
                archivoHtml.write(f"<tr><td>{nombre}</td><td>{apellido1} {apellido2}</td><td>{estado}</td><td>{carne}</td><td>{correo}</td><td>{notas}</td><td>{estadoTexto}</td></tr>\n")
            except (ValueError, IndexError):
                archivoHtml.write(f"<tr><td colspan='7'>Datos inválidos</td></tr>\n")

        archivoHtml.write(f"""
            </table>
            <h2>Reporte General</h2>
            <p>La base de datos posee {totalEstudiantes} estudiantes, de los cuales hay:</p>
            <ul>
                <li>{aprobados} aprobados para un {porcentajeAprobados}%</li>
                <li>{enReposicion} en reposición para un {porcentajeReposicion}%</li>
                <li>{reprobados} reprobados para un {porcentajeReprobados}%</li>
            </ul>
        </body>
        </html>
        """)
    # Generar CSV
    with open("Reporte.csv", "w", newline="", encoding="utf-8") as archivoCsv:
        escritor = csv.writer(archivoCsv)
        escritor.writerow(["Nombre", "Apellidos", "Género", "Carné", "Correo", "Notas", "Estado"])
        for estudiante in estudiantes:
            try:
                nombre, apellido1, apellido2, estado, carne, correo, notas = estudiante
                notaFinal = float(notas.split(",")[3].strip().replace("(", "").replace(")", ""))
                estadoTexto = "Aprobado" if notaFinal > 70 else "Reposición" if 60 <= notaFinal <= 70 else "Reprobado"
                escritor.writerow([nombre, f"{apellido1} {apellido2}", estado, carne, correo, notas, estadoTexto])
            except (ValueError, IndexError):
                escritor.writerow([nombre, f"{apellido1} {apellido2}", estado, carne, correo, notas, "Datos inválidos"])

def calcularEstadisticas(estudiantes):
    """Calcula las estadísticas de los estudiantes."""
    totalEstudiantes = len(estudiantes)
    aprobados = enReposicion = reprobados = 0
    for estudiante in estudiantes:
        try:
            notas = estudiante[6].split(",")
            notaFinal = float(notas[3].strip().replace("(", "").replace(")", ""))
            if notaFinal > 70:
                aprobados += 1
            elif 60 <= notaFinal <= 70:
                enReposicion += 1
            else:
                reprobados += 1
        except (ValueError, IndexError):
            continue
    porcentajeAprobados = round((aprobados / totalEstudiantes) * 100, 2) if totalEstudiantes > 0 else 0
    porcentajeReposicion = round((enReposicion / totalEstudiantes) * 100, 2) if totalEstudiantes > 0 else 0
    porcentajeReprobados = round((reprobados / totalEstudiantes) * 100, 2) if totalEstudiantes > 0 else 0
    return totalEstudiantes, aprobados, enReposicion, reprobados, porcentajeAprobados, porcentajeReposicion, porcentajeReprobados

def leerEstudiantes(archivoCsv):
    """Lee los datos de los estudiantes desde un archivo CSV."""
    with open(archivoCsv, "r", encoding="utf-8") as archivo:
        return [fila for fila in csv.reader(archivo) if len(fila) >= 7]

# Función principal
def generarReporteHtmlYCsv():
    estudiantes = leerEstudiantes("BasedeDatos.csv")
    estadisticas = calcularEstadisticas(estudiantes)
    generarReporte(estudiantes, estadisticas)

# Llamar a la función principal
generarReporteHtmlYCsv()