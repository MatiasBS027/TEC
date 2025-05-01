#Elaborado por Luis Tinoco y Matias Benavides
#Fecha de creación 30/04/2025 07:30
#última modificación 30/04/2025 20:00
#python versió 3.13

#Importando librerías 
import re

#Definición de funciones
def esCedulaValida(cedula):
    """
    Funcionamiento: Valida si una cédula tiene el formato correcto (9 dígitos, no inicia con 0)
    Entradas:
    - cedula (str): Número de cédula a validar
    Salidas:
    - bool: True si la cédula es válida, False si no lo es
    """
    return re.fullmatch(r"^[1-9]\d{8}$", cedula) is not None

def nombreProvincia(numero):
    """
    Funcionamiento: Obtiene el nombre de la provincia según su código numérico
    Entradas:
    - numero (str): Código de provincia (1-9)
    Salidas:
    - str: Nombre de la provincia o "Desconocida" si el código es inválido
    """
    provincias = ("San José", "Alajuela", "Cartago", "Heredia", 
            "Guanacaste", "Puntarenas", "Limón", 
            "Nacional o naturalizado", "Partida especial de nacimientos")
    try:
        return provincias[int(numero) - 1]
    except (ValueError, IndexError):
        return "Desconocida"

def agregarDonantes(lista):
    """
    Funcionamiento: Agrega 4 nuevos donantes a la lista, validando su formato y duplicidad
    Entradas:
    - lista (list): Lista actual de cédulas de donantes
    Salidas:
    - str: Mensaje indicando el resultado de la operación
    """
    mensajes = ""
    for i in range(4):
        while True:
            cedula = input(f"Ingrese la cédula #{i+1}: ")
            if not esCedulaValida(cedula):
                mensajes = "Formato inválido. Debe tener 9 dígitos y no iniciar con 0."
                print("Formato inválido. Debe tener 9 dígitos y no iniciar con 0.")
            elif cedula in lista:
                mensajes = "Esta cédula ya está registrada."
                print("Esta cédula ya está registrada.")
            else:
                lista.append(cedula)
                break
    mensajes = "Donantes registrados satisfactoriamente.\n"
    return mensajes

def mostrarDatosDonante(lista):
    """
    Funcionamiento: Muestra los detalles decodificados de un donante específico
    Entradas:
    - lista (list): Lista de cédulas de donantes
    Salidas:
    - str: Mensaje con los datos decodificados del donante o mensaje de error
    """
    cedula = input("Ingrese la cédula a decodificar: ")
    if not esCedulaValida(cedula):
        return "Formato inválido."
    if cedula not in lista:
        return "El donador no es un donante aún."
    
    provincia = nombreProvincia(cedula[0])
    tomo = cedula[1:5]
    asiento = cedula[5:]
    return f"\nUsted es de {provincia}, está registrado en el tomo {tomo}, y el asiento {asiento}."

def mostrarPorProvincia(lista):
    """
    Funcionamiento: Muestra los donantes de una provincia específica
    Entradas:
    - lista (list): Lista de cédulas de donantes
    Salidas:
    - str: Lista de donantes de la provincia seleccionada o mensaje si no hay donantes
    """
    menuTexto = "\nSeleccione una provincia:\n" + \
                "Codigo. Provincia\n" + \
                "1. San José\n2. Alajuela\n3. Cartago\n4. Heredia\n" + \
                "5. Guanacaste\n6. Puntarenas\n7. Limón\n" + \
                "8. Nacionalizado o naturalizado (Extranjero)\n" + \
                "9. Partida especial de nacimientos (Casos especiales)"
    print(menuTexto)
    
    codigo = input("Ingrese el código de provincia (1-9): ")
    if codigo not in "123456789":
        return "Código inválido."
    encontrados = [c for c in lista if c.startswith(codigo)]
    if encontrados:
        if len(encontrados) == 1:
            resultado = f"\nEl donador de la provincia de {nombreProvincia(codigo)}, es {len(encontrados)} con la cédula:"
        else:
            resultado = f"\nLos donadores de la provincia de {nombreProvincia(codigo)}, son {len(encontrados)} con las cédulas:"
        for cedula in encontrados:
            resultado += f"\n - {cedula}"
        return resultado
    else:
        return "Aún no hay personas donadoras de esa naturalización."

def mostrarTodos(lista):
    """
    Funcionamiento: Muestra todos los donantes organizados por provincia
    Entradas:
    - lista (list): Lista de cédulas de donantes
    Salidas:
    - str: Reporte completo de donantes por provincia
    """
    resultado = ""
    for i in range(1, 10):
        codigo = str(i)
        encontrados = [c for c in lista if c.startswith(codigo)]
        if encontrados:
            if len(encontrados) == 1:
                resultado += f"\nEl donador de la provincia de {nombreProvincia(codigo)}, es {len(encontrados)} con la cédula:"
            else:
                resultado += f"\nLos donadores de la provincia de {nombreProvincia(codigo)}, son {len(encontrados)} con las cédulas:"
            for c in encontrados:
                resultado += f"\n - {c}"
        else:
            resultado+= f"\nLos donadores de la provincia de {nombreProvincia(codigo)}, son {len(encontrados)} con las cédulas:\nAún no reporta donadores"
    return resultado

def mostrarNoTipicos(lista):
    """
    Funcionamiento: Muestra los donantes de casos especiales (códigos 8 y 9)
    Entradas:
    - lista (list): Lista de cédulas de donantes
    Salidas:
    - str: Lista de donantes no típicos o mensaje si no hay donantes
    """
    resultado = ""
    for codigo in ["8", "9"]:
        encontrados = [c for c in lista if c.startswith(codigo)]
        if encontrados:
            if len(encontrados) == 1:
                resultado += f"\nEl donador {nombreProvincia(codigo)}, es {len(encontrados)} con la cédula:"
            else:
                resultado += f"\nLos donadores {nombreProvincia(codigo)}, son {len(encontrados)} con las cédulas:"
            for c in encontrados:
                resultado += f"\n - {c}"
        else:
            resultado+= f"\nLos donadores de la provincia de {nombreProvincia(codigo)}, son {len(encontrados)} con las cédulas:\nAún no reporta donadores"
    return resultado