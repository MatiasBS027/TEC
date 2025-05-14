#Elaborado por Luis Tinoco y Matias Benavides
#Fecha de creación 12/5/2025 07:30
#última modificación 12/5/2025 20:00
#python versión 3.13

#importacion de librerías

#definición de funciones

def reporteTotalEdificio(edificio):
    """
    Funcionamiento:
    - Genera un reporte del total de apartamentos alquilados y desocupados en el edificio.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - str: Mensaje con el total de apartamentos alquilados y desocupados, junto con sus porcentajes.
    """
    if hayEspacio(edificio) == False:
        return "No hay apartamentos ocupados para hacer un reporte."
    else:
        alquilados = 0
        desocupados = 0
        for i in range(len(edificio)):  # Itera manualmente con un índice
            for j in range(len(edificio[i])):  # Itera manualmente con un índice
                if edificio[i][j] != 0:
                    alquilados += 1
                else:
                    desocupados += 1
        total = alquilados + desocupados
        if total > 0:
            porcentajeA = round((alquilados / total) * 100, 0)
            porcentajeB = round((desocupados / total) * 100, 0)
        else:
            porcentajeA = porcentajeB = 0
        return (f"Total de apartamentos alquilados: {alquilados}, para un porcentaje de {porcentajeA}% \n"
                f"Total de apartamentos desocupados: {desocupados}, para un porcentaje de {porcentajeB}%")

def alquilerPorApartamento(edificio):
    """
    Funcionamiento:
    - Calcula el ingreso por alquiler de un apartamento específico.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - str: Mensaje con el monto de alquiler del apartamento seleccionado.
    """
    if hayEspacio(edificio) == False:
            return "No hay apartamentos ocupados para calcular el ingreso."
    else:
        while True:  # Bucle para seguir pidiendo datos válidos
            piso = pisoAux(edificio) - 1  # el -1 es para ajustar el índice a 0
            apartamento = apartamentoAux(edificio) - 1
            monto = edificio[piso][apartamento]
            estado = "Alquilado" if monto != 0 else "Libre"
            return f"El apartamento {apartamento+1} en el piso {piso+1} está {estado} por ${monto}."

def alquilerPorPiso(edificio):
    """
    Funcionamiento:
    - Calcula el ingreso total por alquiler de un piso específico.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - str: Mensaje con el monto total de alquiler del piso seleccionado.
    """
    if hayEspacio(edificio) == False:
        return "No hay apartamentos ocupados para calcular el ingreso."
    else:
        while True:  # Bucle para seguir pidiendo datos válidos
            piso = pisoAux(edificio) - 1  # el -1 es para ajustar el índice a 0
            apartamentosPiso = edificio[piso]  # Obtiene los apartamentos del piso
            totalAlquiler = 0
            for i in range(len(apartamentosPiso)):  # Itera manualmente con un índice
                monto = apartamentosPiso[i]
                estado = "Alquilado" if monto != 0 else "Libre"
                print(f"Piso #: {piso + 1}")
                print(f"Apartamento #: {i + 1}")
                print(f"Estado: {estado}")
                print(f"Monto de alquiler $: {monto}\n")
                totalAlquiler += monto  # Suma el monto al total del piso
            return(f"Para un total de ingresos del piso {piso+1} de ${totalAlquiler}")

def alquilerPorColumna(edificio):
    """
    Funcionamiento:
    - Calcula el ingreso total por alquiler de una columna específica (apartamentos en la misma posición en todos los pisos).
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - str: Mensaje con el monto total de alquiler de la columna seleccionada.
    """
    if hayEspacio(edificio) == False:
        return "No hay apartamentos ocupados para calcular el ingreso."
    else:
        while True:  # Bucle para seguir pidiendo datos válidos
            apartamento = apartamentoAux(edificio) - 1  # el -1 es para ajustar el índice a 0
            totalAlquiler = 0
            for i in range(len(edificio)):  # Itera manualmente con un índice
                monto = edificio[i][apartamento]
                estado = "Alquilado" if monto != 0 else "Libre"
                print(f"Piso #: {i + 1}")
                print(f"Apartamento #: {apartamento + 1}")
                print(f"Estado: {estado}")
                print(f"Monto de alquiler $: {monto}\n")
                totalAlquiler += monto  # Suma el monto al total de la columna
            return(f"Para un total de ingresos de la columna {apartamento+1} de ${totalAlquiler}")

def totalidadEdificio(edificio):
    """
    Funcionamiento:
    - Calcula el ingreso total por alquiler de todos los apartamentos del edificio.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - str: Mensaje con el monto total de alquiler del edificio.
    """
    if hayEspacio(edificio) == False:
        return "No hay apartamentos ocupados para calcular el ingreso."
    else:
        totalAlquiler = 0
        for i in range(len(edificio)):  # Itera manualmente con un índice
            for j in range(len(edificio[i])):  # Itera manualmente con un índice
                monto = edificio[i][j]
                estado = "Alquilado" if monto != 0 else "Libre"
                print(f"Piso #: {i + 1}")
                print(f"Apartamento #: {j + 1}")
                print(f"Estado: {estado}")
                print(f"Monto de alquiler $: {monto}\n")
                totalAlquiler += monto  # Suma el monto al total del edificio
        return(f"Para un total de ganancias ${totalAlquiler}")
    
def desalojar(edificio):
    """
    Funcionamiento:
    - Permite desalojar un apartamento ocupado en el edificio.
    - Solicita al usuario el número de piso y apartamento, y confirma la operación antes de proceder.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - str: Mensaje indicando el éxito o cancelación de la operación.
    """
    if hayEspacio(edificio) == False:
        return "No hay apartamentos ocupados para desalojar."
    else:
        while True:  # Bucle para seguir pidiendo datos válidos
            piso = pisoAux(edificio) - 1  # el -1 es para ajustar el índice a 0
            apartamento = apartamentoAux(edificio) - 1
            if edificio[piso][apartamento] == 0:  # Cambiado de != 0 a == 0
                print(f"El apartamento {apartamento+1} en el piso {piso+1} no está alquilado. Intente nuevamente.")
            else:
                while True:
                    confirmar = input(f"¿Está seguro de que desea desalojar el apartamento {apartamento+1} en el piso {piso+1}? (si/no): ").lower()
                    if confirmar == "si":
                        edificio[piso][apartamento] = 0
                        return f"El apartamento {apartamento+1} en el piso {piso+1} ha sido desalojado con éxito."
                    elif confirmar == "no":
                        return "Operación cancelada."
                    else:
                        print("Opción inválida. Por favor, responda con 'si' o 'no'.")

def modificarRenta(edificio):
    """
    Funcionamiento:
    - Permite modificar el valor del alquiler de un apartamento ocupado en el edificio.
    - Solicita al usuario el número de piso y apartamento, y confirma la operación antes de proceder.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - str: Mensaje indicando el éxito o cancelación de la operación.
    """
    if not hayEspacio(edificio):
        return "No hay apartamentos ocupados para modificar el alquiler."   
    else:
        while True:
            piso = pisoAux(edificio) - 1
            apartamento = apartamentoAux(edificio) - 1
            if edificio[piso][apartamento] == 0:
                print(f"El apartamento {apartamento+1} en el piso {piso+1} no está alquilado. Intente nuevamente.")
            else:
                valor_actual = edificio[piso][apartamento]
                while True:
                    confirmar = input(f"¿Está seguro de que desea modificar el alquiler del apartamento {apartamento+1} en el piso {piso+1}? (si/no): ").lower()
                    if confirmar == "si":
                        nuevo_alquiler = nuevoValor(valor_actual)
                        edificio[piso][apartamento] = nuevo_alquiler
                        diferencia = nuevo_alquiler - valor_actual
                        if diferencia > 0:
                            return (f"El alquiler ha sido aumentado en ${diferencia}, con éxito.\n"
                                    f"El nuevo alquiler es ${nuevo_alquiler}.")
                        else:
                            return (f"El alquiler ha sido disminuido en ${-diferencia}, con éxito.\n"
                                    f"El nuevo alquiler es ${nuevo_alquiler}.")
                    elif confirmar == "no":
                        return "Operación cancelada."
                    else:
                        print("Opción inválida. Por favor, responda con 'si' o 'no'.")

def alquilarApartamento(edificio, solicitarValorAlquilerFunc):
    """
    Funcionamiento:
    - Permite alquilar un apartamento en el edificio, verificando si está disponible.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - str: Mensaje indicando el éxito o error al alquilar el apartamento.
    """
    while True: 
        piso = pisoAux(edificio) - 1  # el -1 es para ajustar el índice a 0
        apartamento = apartamentoAux(edificio) - 1
        valorAlquiler = solicitarValorAlquilerFunc(piso)
        if edificio[piso][apartamento] != 0:
            print(f"El apartamento {apartamento+1} en el piso {piso+1} ya está alquilado. Intente nuevamente.")
        else:
            edificio[piso][apartamento] = valorAlquiler
            mensaje = f"El apartamento {apartamento+1} en el piso {piso+1} ha sido alquilado por ${valorAlquiler}, con éxito."
            return mensaje

def hayEspacio(edificio):
    """
    Funcionamiento:
    - Verifica si hay apartamentos ocupados en el edificio.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - bool: True si hay apartamentos ocupados, False en caso contrario.
    """
    if len(edificio) == 0 or all(all(apartamento == 0 for apartamento in piso) for piso in edificio):
        return False
    else:
        return True

def pisoAux(edificio):
    """
    Funcionamiento:
    - Solicita al usuario el número de piso y valida que sea válido.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - int: Número de piso válido ingresado por el usuario.
    """
    while True:
        try:
            piso = int(input("Ingrese el número de piso: "))
            if piso > len(edificio) or piso < 1:
                print ("Número de piso inválido. Intente nuevamente.")
            else:
                return piso
        except ValueError:
                print ("Debe ingresar un número entero.")

def apartamentoAux(edificio):
    """
    Funcionamiento:
    - Solicita al usuario el número de apartamento y valida que sea válido.
    Entradas:
    - edificio: list, matriz que representa el estado del edificio.
    Salidas:
    - int: Número de apartamento válido ingresado por el usuario.
    """
    while True:
        try:
            apartamento = int(input("Ingrese el número de apartamento: "))
            if apartamento > len(edificio[0]) or apartamento < 1:
                print("Número de apartamento inválido. Intente nuevamente.")
            else:
                return apartamento
        except ValueError:
            print("Debe ingresar un número entero.")

def solicitarValorAlquiler(piso):
    """
    Funcionamiento:
    - Solicita al usuario el valor del alquiler y valida que sea un número entero.
    Entradas:
    - piso: int, número del piso para calcular el valor actual del alquiler.
    Salidas:
    - int: Valor de alquiler ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input(f"Ingrese el valor del apartamento en el piso {piso+1}: "))
            if valor <= 0:
                print("El valor del alquiler debe ser mayor que cero. Intente nuevamente.")
            else:
                return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")

def nuevoValor(valorActual):
    """
    Funcionamiento:
    - Solicita al usuario un nuevo valor de alquiler y valida que sea diferente al actual.
    Entradas:
    - piso: int, número del piso para calcular el valor actual del alquiler.
    - valorActual: int, valor actual del alquiler.
    Salidas:
    - int: Nuevo valor de alquiler ingresado por el usuario.
    """
    while True:
        try:
            nuevo = int(input("Ingrese el nuevo valor del apartamento: "))
            if nuevo == valorActual:
                print("El nuevo valor no puede ser igual al valor actual. Intente nuevamente.")
            else:
                return nuevo
        except ValueError:
            print("Debe ingresar un número entero válido.")



def crearEdificio(pisos, apartamentos):
    """
    Funcionamiento:
    - Crea una matriz que representa el edificio con todos los apartamentos desocupados.
    Entradas:
    - pisos: int, número de pisos del edificio.
    - apartamentos: int, número de apartamentos por piso.
    Salidas:
    - list: Matriz que representa el edificio con todos los apartamentos inicializados en 0.
    """
    return [[0 for _ in range(apartamentos)] for _ in range(pisos)]

def alquilarAux(pisos, apartamentos):
    """
    Funcionamiento:
    - Valida los parámetros de entrada y crea un edificio si los valores son válidos.
    Entradas:
    - pisos: int, número de pisos del edificio.
    - apartamentos: int, número de apartamentos por piso.
    Salidas:
    - list: Matriz que representa el edificio si los valores son válidos.
    - str: Mensaje de error si los valores no son válidos.
    """
    if pisos < 1 or apartamentos < 1:
        return "El número de pisos y apartamentos debe ser mayor que cero."
    else:
        edificio = crearEdificio(pisos, apartamentos)
        return edificio