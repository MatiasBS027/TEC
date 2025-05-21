# Elaborado por: Matias Benavides
# Fecha de creacion: 11/3/2025 12:11am
# Fecha de ultima modificacion: 11/3/2025 12:11am
# Version de Python: 3.13.2

def definirNuevoSueldo(psueldo, pcategoria, phorasExtra):
    '''
    Funcionamiento: Calcula el nuevo sueldo de un trabajador
    Entradas:
    -psueldo(float):Sueldo del trabajador
    -pcategoria(int):Categoria del trabajador
    -phorasExtra(int):Horas extra trabajadas
    Salidas:
    -nuevoSueldo(float):Nuevo sueldo del trabajador
    '''

    if pcategoria == 1:
        precioHoraExtra = 30  # El precio por hora extra es 30
    elif pcategoria == 2:
        precioHoraExtra = 38  # El precio por hora extra es 38
    elif pcategoria == 3:
        precioHoraExtra = 50  # El precio por hora extra es 50
    elif pcategoria == 4:
        precioHoraExtra = 70  # El precio por hora extra es 70
    else:
        precioHoraExtra = 0  # No hay precio por hora extra
    if phorasExtra > 30:
        nuevoSueldo = psueldo + (30 * precioHoraExtra)  # Solo se pagan 30 horas extra
    else:
        nuevoSueldo = psueldo + (phorasExtra * precioHoraExtra)  # Se pagan todas las horas extra

    return nuevoSueldo

# Solicita al usuario que ingrese el sueldo, la categoria y las horas extra trabajadas
sueldo = float(input("Digite el sueldo del trabajador: "))
categoria = int(input("Digite la categoria del trabajador:|1|2|3|4|: "))
horasExtra = int(input("Digite las horas extra trabajadas: "))

# Imprime el nuevo sueldo del trabajador
print(f"El nuevo sueldo del trabajador es:", (definirNuevoSueldo(sueldo, categoria, horasExtra)))