#Elaborado por Luis Tinoco
#Fecha de elaboración 11/05/2025
#Última modificación 11/05/2025 19:32
#python versión 3.13.2
import re
from deportes import deportes  # Importa el diccionario desde deportes.py


def registrarDeporte():
    """Registra un nuevo deporte en el inventario.
    Solicita los datos del deporte, valida su formato y los guarda en memoria secundaria.
    """
    # Solicitar y validar el código del deporte
    codigoDeporte = input("Ingrese el código del deporte a registrar (ejem. TEC##): ").strip()
    if not re.match(r"^TEC\d{2}$", codigoDeporte):
        print("Error: El código del deporte no es válido. Debe seguir el formato TEC##.")
        return
    if codigoDeporte in deportes:
        print("Error: El código del deporte ya existe.")
        return

    # Solicitar y validar el nombre del deporte
    nombreDeporte = input("Ingrese el nombre del deporte a registrar (mayor a 5 caracteres): ").strip()
    if len(nombreDeporte) <= 5:
        print("Error: El nombre del deporte debe tener más de 5 caracteres.")
        return

    # Solicitar y validar la explicación del deporte
    descripcionDeporte = input("Ingrese una breve explicación del deporte (entre 5 y 250 caracteres): ").strip()
    if len(descripcionDeporte) < 5 or len(descripcionDeporte) > 250:
        print("Error: La explicación debe tener entre 5 y 250 caracteres.")
        return

    # Solicitar y validar el lugar donde se desarrolla
    lugarDeporte = input("Ingrese el lugar donde se desarrolla el deporte (entre 5 y 50 caracteres): ").strip()
    if len(lugarDeporte) < 5 or len(lugarDeporte) > 50:
        print("Error: El lugar debe tener entre 5 y 50 caracteres.")
        return

    # Registrar el deporte en el diccionario
    deportes[codigoDeporte] = {
        'nombre': nombreDeporte,
        'descripcion': descripcionDeporte,
        'lugar': lugarDeporte,
        'estado': True  # Estado por omisión
    }

    # Guardar en memoria secundaria
    with open('deportes.py', 'r') as archivo:
        lineas = archivo.readlines()
    with open('deportes.py', 'w') as archivo:
        for linea in lineas:
            if not linea.strip().startswith("deportes ="):
                archivo.write(linea)
        archivo.write("deportes = {\n")
        for codigo, datos in deportes.items():
            archivo.write(f"    '{codigo}': {{\n")
            archivo.write(f"        'nombre': '{datos['nombre']}',\n")
            archivo.write(f"        'descripcion': '{datos['descripcion']}',\n")
            archivo.write(f"        'lugar': '{datos['lugar']}',\n")
            archivo.write(f"        'estado': {str(datos['estado']).lower()}\n")
            archivo.write("    },\n")
        archivo.write("}\n")
    print("Éxito: El deporte ha sido registrado correctamente.")


def modificarDeporte():
    """Modifica el nombre de un deporte registrado."""
    # Mostrar los deportes activos
    print("Deportes registrados (activos):")
    for codigo, datos in deportes.items():
        if datos['estado']:
            print(f"{codigo}: {datos['nombre']}")
    
    # Solicitar el código del deporte a modificar
    codigoDeporte = input("Ingrese el código del deporte que desea modificar: ").strip()
    if codigoDeporte not in deportes or not deportes[codigoDeporte]['estado']:
        print("Error: El código ingresado no existe o el deporte está inactivo.")
        return

    # Solicitar el nuevo nombre del deporte
    nuevoNombre = input("Ingrese el nuevo nombre del deporte (mayor a 5 caracteres): ").strip()
    if len(nuevoNombre) <= 5:
        print("Error: El nombre del deporte debe tener más de 5 caracteres.")
        return

    # Confirmar el cambio
    deportes[codigoDeporte]['nombre'] = nuevoNombre
    print(f"Éxito: El nombre del deporte con código {codigoDeporte} ha sido actualizado a '{nuevoNombre}'.")
    
    # Guardar cambios en deportes.py
    with open('deportes.py', 'r') as archivo:
        lineas = archivo.readlines()
    with open('deportes.py', 'w') as archivo:
        for linea in lineas:
            if not linea.strip().startswith("deportes ="):
                archivo.write(linea)
        archivo.write("deportes = {\n")
        for codigo, datos in deportes.items():
            archivo.write(f"    '{codigo}': {{\n")
            archivo.write(f"        'nombre': '{datos['nombre']}',\n")
            archivo.write(f"        'descripcion': '{datos['descripcion']}',\n")
            archivo.write(f"        'lugar': '{datos['lugar']}',\n")
            archivo.write(f"        'estado': {str(datos['estado']).lower()}\n")
            archivo.write("    },\n")
        archivo.write("}\n")


def eliminarDeporte():
    """Elimina un deporte del inventario cambiando su estado a False."""
    # Mostrar los deportes activos
    print("Deportes registrados (activos):")
    activos = {codigo: datos for codigo, datos in deportes.items() if datos['estado']}
    for codigo, datos in activos.items():
        print(f"{codigo}: {datos['nombre']}")

    # Solicitar código para eliminar
    codigoDeporte = input("Ingrese el código del deporte que desea eliminar: ").strip()
    if codigoDeporte not in activos:
        print("Error: El código ingresado no existe o el deporte ya está inactivo.")
        return

    # Confirmar eliminación
    confirmar = input(f"¿Está seguro que desea eliminar el deporte '{activos[codigoDeporte]['nombre']}'? (S/N): ").strip().upper()
    if confirmar == 'S':
        deportes[codigoDeporte]['estado'] = False
        print("Deporte eliminado satisfactoriamente.")
        
        # Guardar cambios en deportes.py
        with open('deportes.py', 'r') as archivo:
            lineas = archivo.readlines()
        with open('deportes.py', 'w') as archivo:
            for linea in lineas:
                if not linea.strip().startswith("deportes ="):
                    archivo.write(linea)
            archivo.write("deportes = {\n")
            for codigo, datos in deportes.items():
                archivo.write(f"    '{codigo}': {{\n")
                archivo.write(f"        'nombre': '{datos['nombre']}',\n")
                archivo.write(f"        'descripcion': '{datos['descripcion']}',\n")
                archivo.write(f"        'lugar': '{datos['lugar']}',\n")
                archivo.write(f"        'estado': {str(datos['estado']).lower()}\n")
                archivo.write("    },\n")
            archivo.write("}\n")
    else:
        print("El deporte no se eliminó.")
