# Elaborado por Luis Tinoco y Matias Benavides
# Fecha de elaboración 04/05/2025
# Última modificación 08/05/2025 19:50
# Python 3.13.21
from procesos import *


"""
Propósito:
- Controlar el menú principal y la navegación entre opciones.
- Gestionar variables globales para la base de datos y listas de unicidad.
"""

# Variables globales
def cargarSedes():
    try:
        with open("sedes.txt", "r", encoding="utf-8") as archivo:
            sedes = []
            for linea in archivo:
                if linea.strip():
                    sedes.append(linea.strip())
            if not sedes:
                print("Error: El archivo 'sedes.txt' está vacío o tiene líneas en blanco.")
                exit(1)
            return sedes
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'sedes.txt' en el directorio actual.")
        exit(1)


# Listas globales
estudiantes = []
carnetsUsados = []
correosUsados = []
sedes = cargarSedes()
porcentajes = [30, 30, 40]  # porcentajes de evaluaciones

# Funciones de ES y Aux
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
    datosCrudos = leerDatosCsv(rutaArchivo)
    datosFiltrados = filtrarDatosCompletos(datosCrudos)
    estudiantesProcesados=[]
    estudiantesProcesados = []
    for fila in datosFiltrados:
        # Primero procesamos cada fila
        estudianteProcesado = procesarEstudianteHtmlCsv(fila)
        # Luego verificamos si el resultado no es False
        if estudianteProcesado is not False:
            # Añadimos el estudiante a la lista de procesados
            estudiantesProcesados.append(estudianteProcesado)
    if not estudiantesProcesados:
        print("No hay datos válidos para procesar")
        return
    estadisticas = calcularEstadisticas(estudiantesProcesados)
    generarHtml(estudiantesProcesados, estadisticas)
    generarCsv(estudiantesProcesados)
    print("Reportes generados exitosamente")

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

# Función principal del menú
def menuPrincipal():
    while True:
        print("""
    --------- MENÚ PRINCIPAL ---------
    1. Crear BD dinámica
    2. Registrar un estudiante
    3. Generar reporte HTML y .csv
    4. Respaldar en XML
    5. Reporte por género (.txt)
    6. Gestionar curva
    7. Envío de correos para reposición
    8. Aplazados en al menos 2 exámenes (.pdf)
    9. Estadística por generación
    10. Reporte por sede con buen rendimiento
    11. Salir
    """)
        opcion = input("Seleccione una opción: ")
        try:
            if opcion == "1":
                crearBasedeDatosEs()
            elif opcion == "2":
                registrarEstudiante(estudiantes, carnetsUsados, correosUsados, sedes, porcentajes)
            elif opcion == "3":
                # Generar reporte HTML y CSV
                ejecutarFlujoPrincipal("BasedeDatos.csv")
                print("Reporte generado correctamente.")
            elif opcion == "4":
                respaldarXml("BasedeDatos.csv", "reporte.xml")
                print("Respaldo XML generado: reporte.xml")
            elif opcion == "5":
                generarReporteGenero(estudiantes, porcentajes)
            elif opcion == "6":
                curva()
            elif opcion == "7":
                enviarCorreosReposicion(estudiantes)
            elif opcion == "8":
                filas = leerBaseDatos()
                resultados = procesarEstudiantes(filas)
                generarReportePdf(resultados, 'ReporteAplazados.pdf')
                print('PDF de aplazados generado: ReporteAplazados.pdf')
            elif opcion == "9":
                estadisticaGeneracion(estudiantes)
            elif opcion == "10":
                reporteSedeBuenRendimiento(estudiantes, sedes)
            elif opcion == "11":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")


menuPrincipal()