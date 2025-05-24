# Elaborado por Luis Tinoco y Matias Benavides
# Fecha de elaboración 04/05/2025
# Última modificación 08/05/2025 19:50
# Python 3.13.2

import csv
import random
import re
import smtplib #para poder hacer el envio de los correos reales facilita la comunicación con un servidor SMTP
import names
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from docx import Document

# ==================== BD.py ====================

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
        # Verifica si hay líneas disponibles
        if lineas:
            # Obtiene y divide la línea i por comas, eliminando espacios en blanco al inicio y final
            linea = lineas[i].strip().split(",")
        else:
            # Si no hay líneas, se asigna una lista vacía
            linea = []
        # Si la línea contiene al menos un elemento, se toma como nombre; de lo contrario, se genera un nombre aleatorio
        if linea:
            nombre = linea[0]
        else:
            nombre = names.get_first_name()
        # Si la línea contiene al menos dos elementos, se toma como primer apellido; si no, se genera uno aleatorio
        if linea:
            apellido1 = linea[1]
        else:
            apellido1 = names.get_last_name()
        # Si la línea contiene más de dos elementos, se toma el tercer como segundo apellido; de lo contrario, se genera uno aleatorio
        if len(linea) > 2:
            apellido2 = linea[2]
        else:
            apellido2 = names.get_last_name()
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
        for i in range(round(obtenerCantidad(pCantidad, pPorcentaje))):
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
    porcentaje = round(cant * (porc / porcentajeTotal))
    return porcentaje

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
        codigo=[]
        for i in range(len(sedes)):
            codigo.append(f"{i+1:02}")
        return codigo
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




# =============================================== reto2.py ==================================================0

# registrarEstudiante
"""
Solicita al usuario la información básica de un estudiante,
valida el carné y correo, calcula la nota final y el estado,
y guarda la información en la lista de estudiantes.
"""
nombreArchivoBD = "BaseDeDatos.csv"


def registrarEstudiante(estudiantes, carnetsUsados, correosUsados, sedes, porcentajes):
    print("Ejemplo de ingreso de datos para registrar un estudiante:")
    print("Nombre completo: Juan Pérez Rodríguez")
    print("Género (Masculino/Femenino): Masculino")
    print("Carné (formato AAAA SS XXXX): 2023011234")
    print("Correo electrónico: jperez1234@estudiantec.cr")
    print("Nota 1: 85")
    print("Nota 2: 90")
    print("Nota 3: 78")
    nombre = input("Nombre completo: ").strip()
    genero = input("Género (Masculino/Femenino): ").capitalize().strip()
    carne = input("Carné (formato AAAA SS XXXX): ").strip()
    correo = input("Correo electrónico: ").strip()
    nota1 = int(input("Nota 1: ").strip())
    nota2 = int(input("Nota 2: ").strip())
    nota3 = int(input("Nota 3: ").strip())
    
    if not re.match(r"^\d{4}(01|02|03)\d{4}$", carne) or carne in carnetsUsados:
        print("Carné inválido o repetido.")
        return
    
    if not re.match(r"^[a-z]+\d+@estudiantec\.cr$", correo) or correo in correosUsados:
        print("Correo inválido o repetido.")
        return
    
    total = (nota1 * porcentajes[0] / 100) + (nota2 * porcentajes[1] / 100) + (nota3 * porcentajes[2] / 100)
    estudiantes.append([nombre.split(), genero, carne, correo, (nota1, nota2, nota3, total, total)])
    carnetsUsados.append(carne)
    correosUsados.append(correo)
    print("Estudiante registrado exitosamente.")


def generarReporteGenero(estudiantes, porcentajes):
    # Leer estudiantes desde BasedeDatos.csv
    estudiantes = []
    try:
        with open("BasedeDatos.csv", "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) >= 7:
                    # nombre, apellido1, apellido2, genero, carne, correo, notas
                    nombre = [fila[0], fila[1], fila[2]]
                    genero = "Masculino" if fila[3] == "True" else "Femenino"
                    carne = fila[4]
                    correo = fila[5]
                    # notas es una cadena, convertir a tupla de floats
                    notas = fila[6].strip("() ").split(",")
                    notas = [float(n.strip()) for n in notas]
                    total = notas[3]  # total ponderado
                    estudiante = [nombre, genero, carne, correo, (notas[0], notas[1], notas[2], total, total)]
                    estudiantes.append(estudiante)
    except FileNotFoundError:
        print("No se encontró el archivo BasedeDatos.csv")
        return

    hombres = []
    mujeres = []
    for est in estudiantes:
        datos = (est[4][-1], est[4], ' '.join(est[0]), est[2], est[3])
        if est[1] == 'Masculino':
            hombres.append(datos)
        else:
            mujeres.append(datos)

    def guardarTexto(nombreArchivo, datos):
        with open(nombreArchivo, "w", encoding="utf-8") as archivo:
            archivo.write("Reporte de " + nombreArchivo.replace(".txt", "") + "\n\n")
            datos.sort(reverse=True)
            for item in datos:
                archivo.write(f"Nota Acta: {item[0]}, Notas: {item[1]}, Nombre: {item[2]}, Carné: {item[3]}, Correo: {item[4]}\n")
            archivo.write(f"\n% Evaluaciones: {porcentajes}\n")
            archivo.write(f"Cantidad de estudiantes: {len(datos)}\n")

    guardarTexto("hombres.txt", hombres)
    guardarTexto("mujeres.txt", mujeres)
    print("Archivos 'hombres.txt' y 'mujeres.txt' generados exitosamente.\n")


def enviarCorreosReposicion(estudiantes):
    remitente = "tuCorreo@gmail.com"
    contrasena = "tuContrasenaAplicacion" 
    """se debe agregar el correo del que se enviarán los correos de reposición  
    para que funcione correctamente, si no es así se debe usar otro import y usar el localhost"""

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remitente, contrasena)
    except smtplib.SMTPAuthenticationError:
        print("Error: Fallo en la autenticación. Verifica el correo o la contraseña de aplicación.")
        return

    print("\n--- ENVIANDO CORREOS A ESTUDIANTES EN REPOSICIÓN ---")
    enviados = 0

    for estudiante in estudiantes:
        notaFinal = estudiante[4][-1]
        if 60 <= notaFinal < 70:
            nombreCompleto = " ".join(estudiante[0])
            correoDestino = estudiante[3]

            mensaje = EmailMessage()
            mensaje["Subject"] = "Notificación de Reposición"
            mensaje["From"] = remitente
            mensaje["To"] = correoDestino

            mensaje.set_content(f"""\
Estimado(a) {nombreCompleto},

Se le informa que su nota fue de {notaFinal:.2f}, por lo tanto debe presentarse a la reposición.

Día: X
Hora: Y
Lugar: Aula correspondiente

Atentamente,
Sistema de Gestión Estudiantil TEC
""")

            try:
                servidor.send_message(mensaje)
                print(f"Correo enviado a {correoDestino}")
                enviados += 1
            except Exception as e:
                print(f"Error al enviar a {correoDestino}: {e}")

    servidor.quit()
    print(f"\nCorreos enviados correctamente. Total enviados: {enviados}\n")



def estadisticaGeneracion(estudiantes):
    resumen = {}
    try:
        with open("BasedeDatos.csv", "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) >= 7:
                    carne = fila[4]
                    anio = carne[:4]
                    # Notas es una cadena, convertir a lista de floats
                    notas = fila[6].strip("() ").split(",")
                    notas = [float(n.strip()) for n in notas]
                    notaFinal = notas[3]
                    if anio not in resumen:
                        resumen[anio] = [0, 0, 0, 0]
                    if notaFinal >= 70:
                        resumen[anio][0] += 1
                    elif 60 <= notaFinal < 70:
                        resumen[anio][1] += 1
                    else:
                        resumen[anio][2] += 1
                    resumen[anio][3] += 1
    except FileNotFoundError:
        print("No se encontró el archivo BasedeDatos.csv")
        return

    print("\n--- ESTADÍSTICA POR GENERACIÓN ---")
    print("Año | Aprobados | Reposición | Reprobados | Total")
    for anio, datos in resumen.items():
        print(f"{anio} | {datos[0]} | {datos[1]} | {datos[2]} | {datos[3]}")
    print()


def reporteSedeBuenRendimiento(estudiantes, sedes):
    print("\n--- REPORTE POR SEDE CON BUEN RENDIMIENTO ---")
    print("Seleccione una sede:")
    for i, sede in enumerate(sedes, start=1):
        print(f"{i}. {sede}")
    opcion = int(input("Número de sede: ").strip()) - 1
    sedeElegida = sedes[opcion]
    buenos = []
    for est in estudiantes:
        if est[2][4:6] == sedeElegida[:2]:
            notas = est[4][:3]
            if min(notas) >= 70:
                buenos.append(est)
    print(f"\nEstudiantes con buen rendimiento en la sede {sedeElegida}:")
    for i, est in enumerate(buenos, start=1):
        print(f"{i}. {' '.join(est[0])} - {est[2]}")
    print()


def salirPrograma():
    print("\nGracias por utilizar el sistema. Que tenga un buen día.\n")
    exit()

# ========================================= htmlYcss.py ==============================================

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
    filtrados = []
    for fila in datosCrudos:
        if len(fila)>=7:
            filtrados.append(fila)
    return filtrados

def parsearNotasHtmlCsv(notasStr):
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
        # Elimina paréntesis y espacios, luego divide por comas
        notas = notasStr.strip("() ").split(",")
        # Crear una nueva lista para almacenar las notas sin espacios al principio ni al final
        notasLimpias = []
        # Recorrer cada nota en la lista original 'notas'
        for n in notas:
            # Eliminar los espacios en blanco alrededor de la nota y agregarla a la nueva lista
            notasLimpias.append(n.strip())
        # Reemplazar la lista original con la lista de notas limpias
        notas = notasLimpias
        return notas, float(notas[3])  # Retorna notas y el promedio
    except (ValueError, IndexError) as e:
        print(f"Error procesando notas: {notasStr} - {str(e)}")
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

def procesarEstudianteHtmlCsv(fila):
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
        notasLimpias, notaFinal = parsearNotasHtmlCsv(notasStr)
        if notaFinal is False:
            return False
        estado = determinarEstado(notaFinal)
        # Si 'genero' es igual a la cadena "True"
        if genero == "True":
            # Entonces asignamos "Masculino" a la variable 'generoTexto'
            generoTexto = "Masculino"
        else:
            # En cualquier otro caso, asignamos "Femenino"
            generoTexto = "Femenino"
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
    # Inicializar contador para estudiantes aprobados
    aprobados = 0
    # Reconoce cada estudiante en la lista 'estudiantesProcesados'
    for e in estudiantesProcesados:
        # Verificar si el estado del estudiante (posición 6 en la lista) es "Aprobado"
        if e[6] == "Aprobado":
            # Incrementar el contador de aprobados en 1
            aprobados += 1
    # Inicializa el contador para estudiantes en reposición
    reposicion = 0
    # Recorremos cada estudiante nuevamente para contar los que están en "Reposición"
    for e in estudiantesProcesados:
        # Verificar si el estado es "Reposición"
        if e[6] == "Reposición":
            # Incrementa el contador de reposición en 1
            reposicion += 1
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


# ==================== Aplazados.py ====================

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
            lector = csv.reader(archivo)
            next(lector)  # Omitir encabezado
            return list(lector)
    except FileNotFoundError:
        print(f"Error: Archivo '{nombreArchivo}' no encontrado.")
        return []
    
def parsearNotasAplazados(notasStr):
    """
    Esta función toma una cadena de texto con las notas de un estudiante, por ejemplo "(80, 65, 55)",
    y la convierte en una tupla de tres números decimales (floats).
    Parámetros:
    - notasStr: texto con las notas, separado por comas y entre paréntesis.
    Retorna:
    - Una tupla con las tres notas como floats, o False si ocurre algún error.
    """
    try:
        # Quitamos los paréntesis al inicio y final, si existen
        notasStr = notasStr.strip('()')
        # Creamos una lista para guardar las notas limpias
        partes = []
        # Separamos la cadena usando la coma
        notas = notasStr.split(',')
        # Limpiamos cada nota de espacios y la agregamos a la lista
        for p in notas:
            notasLimpias = p.strip()
            partes.append(notasLimpias)
        # Convertimos las tres primeras notas a float y las devolvemos como tupla
        nota1 = float(partes[0])
        nota2 = float(partes[1])
        nota3 = float(partes[2])
        return (nota1, nota2, nota3)
    except (ValueError, AttributeError, IndexError):
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
    # Crear una lista vacía para almacenar las notas que son menores a 70 (aplazos)
    notasAplazos = []
    # Recorrer cada nota en la lista 'notas'
    for nota in notas:
        # Verificar si la nota es menor que 70
        if nota < 70:
            # Si es menor, agregarla a la lista de notas aplazadas
            notasAplazos.append(nota)
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
        notas = parsearNotasAplazados(fila[6])
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
    if todasNotasAplazos:
        notaMin = min(todasNotasAplazos)
    else:
        notaMin = 0

    if todasNotasAplazos:
        notaMax = max(todasNotasAplazos)
    else:
        notaMax = 0

    return (estudiantes, totalEstudiantes, cantidadAplazos2, cantidadAplazos3, notaMin, notaMax)

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
    listaResultado = [f"Total de estudiantes en BD: {resultados[1]}",
    f"Estudiantes con 2 aplazos: {resultados[2]} ({(resultados[2]/resultados[1]*100):.1f}%)",
    f"Estudiantes con 3 aplazos: {resultados[3]} ({(resultados[3]/resultados[1]*100):.1f}%)",
    f"Nota más baja en aplazos: {resultados[4]:.1f}",]
    if resultados[5] < 70:
        listaResultado.append(f"Nota más alta en aplazos: {resultados[5]:.1f}")
    else:
        listaResultado.append("No hay notas de aplazos (todas >=70)")
    return listaResultado

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



# ==================== XML.py ====================

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
        partes = notas.split(',')
        numeros = []
        # Recorremos cada parte
        for n in partes:
            # Eliminar espacios en blanco al inicio y final de cada parte
            limpio = n.strip()
            # Añadir el número limpio a la lista 
            numeros.append(limpio)
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

def procesarEstudianteXml(fila):
    """
    Función:
    - Procesa una fila del CSV y genera la estructura XML para un estudiante.
    Entradas:
    - fila: list, contiene los datos de un estudiante.
    Salidas:
    - Retorna tupla con (añoGeneracion, xmlEstudiante).
    - Retorna tupla vacía si hay error en el procesamiento.
    """
    if fila[3] == "True":
        genero = "Masculino"
    else:
        genero = "Femenino"
    try:
        nombre, ap1, ap2, genero, carne, correo, notas = fila
        notasFormateadas = calcularNotas(notas)
        estado = calcularEstado(notasFormateadas)
        anno = calcularAnno(carne)
        estudiante = f"""
        <Estudiante carne=\"{carne}\">
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
        anno, _ = procesarEstudianteXml(fila)
        if anno not in annosUsados:
            annosUsados.append(anno)
    annosUsados.sort()
    for anno in annosUsados:
        estudiantes = []
        for fila in filas:
            annoEst, estudiante = procesarEstudianteXml(fila)
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



# ==================== Curvar.py ====================

# Definición de funciones
def leerBaseDatos():
    """
    Funcionamiento:
    - Lee y procesa los datos de estudiantes desde el archivo CSV.
    Entradas:
    - Ninguna (lee de BasedeDatos.csv).
    Salidas:
    - list: lista de estudiantes con sus datos.
    - list vacía si hay error al leer el archivo.
    """
    estudiantes = []
    try:
        with open("BasedeDatos.csv", "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for datos in lector:
                if len(datos) >= 7:
                    estudiantes.append(datos)
        return estudiantes
    except FileNotFoundError:
        print("No se encontró el archivo BasedeDatos.csv, debe crear uno antes de continuar.")
        return []

def aplicarCurva(estudiante, porcentaje):
    """
    Funcionamiento:
    - Calcula la nota final con el porcentaje de curva aplicado.
    Entradas:
    - estudiante: list, datos del estudiante.
    - porcentaje: float, porcentaje de curva a aplicar.
    Salidas:
    - float: nota final con la curva aplicada.
    """
    try:
        # Procesar las notas de forma segura
        notas_str = estudiante[6].strip("[]()")  # Eliminar corchetes o paréntesis
        partes = notas_str.split(',')
        # Crear lista para notas limpias
        notas = []
        # Recorremos cada parte para limpiar espacios y convertir a float
        for p in partes:
            limpio = p.strip()
            numero = float(limpio)
            notas.append(numero)
        notaFinal = notas[3]  # Asumiendo que la cuarta nota es el índice 3
        return notaFinal + (notaFinal * (porcentaje/100))
    except (IndexError, ValueError) as e:
        print(f"Error procesando notas del estudiante {estudiante}: {e}")
        return 0  # O manejar el error según sea necesario


def clasificarEstudiantes(estudiantes, porcentaje):
    """
    Funcionamiento:
    - Clasifica los estudiantes en tres categorías según su nota con curva.
    Entradas:
    - estudiantes: list, lista de estudiantes a clasificar.
    - porcentaje: float, porcentaje de curva a aplicar.
    Salidas:
    - tuple: tres listas (aprobados, reposición, reprobados).
    """
    aprobados = []
    reposicion = []
    reprobados = []
    
    for estudiante in estudiantes:
        notaConCurva = aplicarCurva(estudiante, porcentaje)
        estudianteConCurva = estudiante + [notaConCurva]
        
        if notaConCurva > 70:
            aprobados.append(estudianteConCurva)
        elif 60 <= notaConCurva <= 70:
            reposicion.append(estudianteConCurva)
        else:
            reprobados.append(estudianteConCurva)
            
    return aprobados, reposicion, reprobados

def generarTablaHtml(estudiantes):
    """
    Funcionamiento:
    - Genera el código HTML para la tabla de estudiantes.
    Entradas:
    - estudiantes: list, lista de estudiantes a mostrar.
    Salidas:
    - str: código HTML de la tabla.
    """
    tabla = ""
    for estudiante in estudiantes:
        tabla += f"""
            <tr>
                <td>{estudiante[0]}</td>
                <td>{estudiante[1]} {estudiante[2]}</td>
                <td>{"Masculino" if estudiante[3]=="True" else "Femenino"}</td>
                <td>{estudiante[4]}</td>
                <td>{estudiante[5]}</td>
                <td>{estudiante[6]}</td>
                <td>{estudiante[7]:.2f}</td>
            </tr>
        """
    return tabla

def generarArchivoHtml(nombreArchivo, estudiantes, porcentaje, estado , totalEstudiantes):
    """
    Funcionamiento:
    - Genera un archivo HTML con los datos de los estudiantes.
    Entradas:
    - nombreArchivo: str, nombre del archivo a generar.
    - estudiantes: list, lista de estudiantes a incluir.
    - porcentaje: float, porcentaje de curva aplicado.
    - titulo: str, título para el documento HTML.
    Salidas:
    - bool: True si se generó correctamente, False si hubo error.
    """
    try:
        with open(nombreArchivo, "w", encoding="utf-8") as  archivo:
            archivo.write(f"""
            <html>
            <head>
                <title>Estudianes {estado}</title>
                <style>
                    table {{ border-collapse: collapse; width: 100%; }}
                    th, td {{ border: 1px solid black; padding: 8px; text-align: left; }}
                    tr:nth-child(even) {{ background-color: #f2f2f2; }}
                </style>
            </head>
            <body>
                <h1>Estudiantes {estado}</h1>
                <h2>Porcentaje de curva aplicado: {porcentaje}%</h2>
                <table>
                    <tr>
                        <th>Nombre</th>
                        <th>Apellidos</th>
                        <th>Género</th>
                        <th>Carné</th>
                        <th>Correo</th>
                        <th>Notas</th>
                        <th>Nota con Curva</th>
                    </tr>
                    {generarTablaHtml(estudiantes)}
                </table>
                <div class="reporte">
                    <h3>Reporte</h3>
                    <p>Para el estado de {estado} hay {len(estudiantes)} estudiantes luego de la curva, del total de {totalEstudiantes} estudiantes</p>
                </div>
            </body>
            </html>
            """)
        return True
    except Exception as e:
        print(f"Error al generar archivo {nombreArchivo}: {str(e)}")
        return False

def archivo(estudiantes, porcentaje):
    aprobados, reposicion, reprobados = clasificarEstudiantes(estudiantes, porcentaje)
    
    archivos = [("aprobados.html", aprobados, "Aprobados"),
        ("reposicion.html", reposicion, "Reposición"),
        ("reprobados.html", reprobados, "Reprobados")]
    
    totalEstudiantes = len(estudiantes)  # Total de estudiantes original
    
    for nombre, lista, estado in archivos:
        if generarArchivoHtml(nombre, lista, porcentaje, estado, totalEstudiantes):
            print(f"Se generó correctamente el archivo {nombre}")
        else:
            print(f"Hubo un error al generar {nombre}")

