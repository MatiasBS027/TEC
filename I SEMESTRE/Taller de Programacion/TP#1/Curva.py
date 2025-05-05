#importacion de librerias
import csv

# Definición de funciones
def obtenerCurvaES():
    """
    Funcionamiento:
    - Solicita el porcentaje de curva al usuario
    Entradas:
    - Ninguna (input del usuario)
    Salidas:
    - float: porcentaje ingresado por el usuario
    - None: si hay error en la entrada
    """
    try:
        porcentaje = float(input("Ingrese el porcentaje de curva a aplicar: "))
        return obtenerCurvaAux(porcentaje)
    except ValueError:
        print("Por favor ingrese un número válido")
        return None


def obtenerCurvaAux(porcentaje):
    """
    Funcionamiento:
    - Valida que el porcentaje esté en el rango correcto
    Entradas:
    - porcentaje: float, valor a validar
    Salidas:
    - float: porcentaje si es válido
    - None: si el porcentaje está fuera de rango
    """
    if 0 <= porcentaje <= 100:
        return porcentaje
    print("El porcentaje debe estar entre 0 y 100")
    return None

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
        notas = list(map(float, notas_str.split(',')))
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

# programa principal
def curva():
    """
    Función principal que coordina todo el proceso
    """
    porcentaje = obtenerCurvaES()
    if porcentaje is None:
        return
    
    estudiantes = leerBaseDatos()
    if not estudiantes:
        return
    
    archivo(estudiantes, porcentaje)

# Ejecutar el programa
curva()