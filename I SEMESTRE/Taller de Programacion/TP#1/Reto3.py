import csv

def generarReporteHTMLyCSV():
    # Leer los datos de la base de datos dinámica
    estudiantes = []
    with open("BDDinamica.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            estudiantes.append(fila)

    # Calcular estadísticas
    total_estudiantes = len(estudiantes)
    aprobados = sum(1 for estudiante in estudiantes if float(estudiante[6].split(",")[3]) > 70)
    en_reposicion = sum(1 for estudiante in estudiantes if 60 <= float(estudiante[6].split(",")[3]) <= 70)
    reprobados = total_estudiantes - aprobados - en_reposicion

    porcentaje_aprobados = round((aprobados / total_estudiantes) * 100, 2)
    porcentaje_reposicion = round((en_reposicion / total_estudiantes) * 100, 2)
    porcentaje_reprobados = round((reprobados / total_estudiantes) * 100, 2)

    # Generar archivo HTML
    with open("Reporte.html", "w", encoding="utf-8") as archivo_html:
        archivo_html.write("<html>\n<head>\n<title>Reporte de Notas</title>\n</head>\n<body>\n")
        archivo_html.write("<h1>Reporte de Notas</h1>\n")
        archivo_html.write("<table border='1'>\n<tr><th>Nombre</th><th>Apellidos</th><th>Género</th><th>Carné</th><th>Correo</th><th>Notas</th><th>Estado</th></tr>\n")
        
        for estudiante in estudiantes:
            nombre, apellido1, apellido2, estado, carne, correo, notas = estudiante
            notas_split = notas.split(",")
            estado_texto = "Aprobado" if float(notas_split[3]) > 70 else "Reposición" if 60 <= float(notas_split[3]) <= 70 else "Reprobado"
            archivo_html.write(f"<tr><td>{nombre}</td><td>{apellido1} {apellido2}</td><td>{estado}</td><td>{carne}</td><td>{correo}</td><td>{notas}</td><td>{estado_texto}</td></tr>\n")
        
        archivo_html.write("</table>\n")
        archivo_html.write(f"<p>La base de datos posee {total_estudiantes} estudiantes, de los cuales hay:</p>\n")
        archivo_html.write(f"<ul>\n<li>{aprobados} aprobados para un {porcentaje_aprobados}%</li>\n")
        archivo_html.write(f"<li>{en_reposicion} en reposición para un {porcentaje_reposicion}%</li>\n")
        archivo_html.write(f"<li>{reprobados} reprobados para un {porcentaje_reprobados}%</li>\n</ul>\n")
        archivo_html.write("</body>\n</html>")

    # Generar archivo CSV
    with open("Reporte.csv", "w", newline="", encoding="utf-8") as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(["Nombre", "Apellidos", "Género", "Carné", "Correo", "Notas", "Estado"])
        for estudiante in estudiantes:
            nombre, apellido1, apellido2, estado, carne, correo, notas = estudiante
            notas_split = notas.split(",")
            estado_texto = "Aprobado" if float(notas_split[3]) > 70 else "Reposición" if 60 <= float(notas_split[3]) <= 70 else "Reprobado"
            escritor.writerow([nombre, f"{apellido1} {apellido2}", estado, carne, correo, notas, estado_texto])

# Llamar a la función para generar los reportes
generarReporteHTMLyCSV()