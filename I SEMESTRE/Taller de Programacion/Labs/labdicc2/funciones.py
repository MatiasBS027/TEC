# Elaborado por Luis Tinoco y Matias Benavides 
# Fecha de elaboración: 11/05/2025
# Última modificación: 14/05/2025 19:32
# Versión de Python: 3.13.2

import re
from archivos import cargarDeportes, guardarDeportes

# Carga los deportes almacenados desde un archivo externo.
deportes = cargarDeportes()

def validarCodigo(codigo: str) -> bool:
    """
    Valida que el código del deporte siga el formato 'TEC##', donde ## son dos dígitos.

    Args:
        codigo (str): Código a validar.

    Returns:
        bool: True si el código es válido, False en caso contrario.
    """
    return re.match(r"^TEC\d{2}$", codigo) is not None

def validarLongitud(texto: str, minimo: int, maximo: int) -> bool:
    """
    Valida que la longitud de un texto esté dentro de un rango específico.

    Args:
        texto (str): Texto a validar.
        minimo (int): Longitud mínima permitida.
        maximo (int): Longitud máxima permitida.

    Returns:
        bool: True si la longitud es válida, False en caso contrario.
    """
    return minimo <= len(texto) <= maximo

def registrarDeporte(deportes: dict) -> None:
    """
    Registra un nuevo deporte en el diccionario de deportes.
    Solicita al usuario el código, nombre, explicación y lugar, validando cada campo.
    Guarda los cambios si el registro es exitoso.

    Args:
        deportes (dict): Diccionario de deportes.
    """
    codigo = input("Ingrese el código del deporte (ejem. TEC##): ").strip()
    if not validarCodigo(codigo):
        print("El código del deporte no es válido. Debe seguir el formato TEC##.")
        return
    if codigo in deportes:
        print("El código del deporte ya existe.")
        return

    nombre = input("Ingrese el nombre del deporte (mayor a 5 caracteres): ").strip()
    if not validarLongitud(nombre, 6, 50):
        print("El nombre del deporte debe tener más de 5 caracteres.")
        return

    explicacion = input("Ingrese una breve explicación del deporte (entre 6 y 250 caracteres): ").strip()
    if not validarLongitud(explicacion, 6, 250):
        print("La explicación debe tener entre 6 y 250 caracteres.")
        return

    lugar = input("Ingrese el lugar donde se desarrolla el deporte (entre 6 y 50 caracteres): ").strip()
    if not validarLongitud(lugar, 6, 50):
        print("El lugar debe tener entre 6 y 50 caracteres.")
        return

    # Agrega el nuevo deporte al diccionario
    deportes[codigo] = {
        'nombre': nombre,
        'explicacion': explicacion,
        'lugar': lugar,
        'estado': True
    }
    guardarDeportes(deportes)
    print("Éxito: El deporte ha sido registrado correctamente.")

def modificarDeporte(deportes: dict) -> None:
    """
    Modifica el nombre de un deporte existente y activo.
    Solicita el código del deporte y el nuevo nombre, validando la entrada.
    Guarda los cambios si la modificación es exitosa.

    Args:
        deportes (dict): Diccionario de deportes.
    """
    if not deportes:
        print("Aún no se han agregados nuevos deportes.")
        return

    codigo = input("Ingrese el código del deporte que desea modificar: ").strip()
    if codigo not in deportes or not deportes[codigo]['estado']:
        print("El código ingresado no existe o el deporte está inactivo.")
        return

    nuevoNombre = input("Ingrese el nuevo nombre del deporte (mayor a 5 caracteres): ").strip()
    if not validarLongitud(nuevoNombre, 6, 50):
        print("El nombre del deporte debe tener más de 5 caracteres.")
        return

    # Actualiza el nombre del deporte
    deportes[codigo]['nombre'] = nuevoNombre
    guardarDeportes(deportes)
    print(f"Éxito: El nombre del deporte con código {codigo} ha sido actualizado a '{nuevoNombre}'.")

def eliminarDeporte(deportes: dict) -> None:
    """
    Marca un deporte como inactivo (eliminado lógicamente).
    Solicita el código del deporte y pide confirmación antes de eliminar.
    Guarda los cambios si la eliminación es confirmada.

    Args:
        deportes (dict): Diccionario de deportes.
    """
    if not deportes:
        print("Aún no se han agregados nuevos deportes.")
        return

    codigo = input("Ingrese el código del deporte que desea eliminar: ").strip()
    if codigo not in deportes or not deportes[codigo]['estado']:
        print("El código ingresado no existe o el deporte ya está inactivo.")
        return

    confirmar = input(f"¿Está seguro que desea eliminar el deporte '{deportes[codigo]['nombre']}'? (S/N): ").strip().upper()
    if confirmar == 'S':
        # Marca el deporte como inactivo
        deportes[codigo]['estado'] = False
        guardarDeportes(deportes)
        print("Deporte eliminado satisfactoriamente.")
    else:
        print("El deporte no se eliminó.")