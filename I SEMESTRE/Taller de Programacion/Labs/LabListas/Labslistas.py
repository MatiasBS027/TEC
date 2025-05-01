#Elaborado por Luis Tinoco
#Fecha de creación 30/04/2025 07:30
#última modificación 30/04/2025 20:00
#python versió 3.13

import re

""" Esta función revisa si una cédula es válida:
Debe tener 9 dígitos y no puede comenzar con 0."""
def esCedulaValida(cedula):
    return re.fullmatch(r"^[1-9]\d{8}$", cedula) is not None

# Esta función recibe el primer dígito de la cédula y devuelve el nombre de la provincia correspondiente.
def nombreProvincia(numero):
    provincias = {"1": "San José", "2": "Alajuela", "3": "Cartago",
        "4": "Heredia", "5": "Guanacaste", "6": "Puntarenas",
        "7": "Limón", "8": "Naturalizados", "9": "Partida especial"}
    return provincias.get(numero, "Desconocida")

# Permite al usuario ingresar 4 nuevas cédulas válidas y no repetidas para agregarlas a la lista.
def agregarDonantes(lista):
    for i in range(4):
        while True:
            cedula = input(f"Ingrese la cédula #{i+1}: ")
            if not esCedulaValida(cedula):
                print("Formato inválido. Debe tener 9 dígitos y no iniciar con 0.")
            elif cedula in lista:
                print("Esta cédula ya está registrada.")
            else:
                lista.append(cedula)
                break
    print("Donantes registrados satisfactoriamente.\n")

# Muestra de qué provincia es el donante, así como su tomo y asiento, si la cédula existe en la lista.
def mostrarDatosDonante(lista):
    cedula = input("Ingrese la cédula a decodificar: ")
    if not esCedulaValida(cedula):
        print("Formato inválido.")
    elif cedula not in lista:
        print("El donador no es un donante aún.")
    else:
        provincia = nombreProvincia(cedula[0])
        tomo = cedula[1:5]
        asiento = cedula[5:]
        print(f"Usted es de {provincia}, está registrado en el tomo {tomo}, y el asiento {asiento}.")

# Filtra y muestra los donantes según el número de provincia que indique el usuario.
def mostrarPorProvincia(lista):
    codigo = input("Ingrese el código de provincia (1-9): ")
    if codigo not in "123456789":
        print("Código inválido.")
        return
    encontrados = [c for c in lista if c.startswith(codigo)]
    if encontrados:
        print(f"Los donadores de la provincia de {nombreProvincia(codigo)}, son {len(encontrados)} con las cédulas:")
        for c in encontrados:
            print(" -", c)
    else:
        print("Aún no hay personas donadoras de esa naturalización.")

# Muestra todos los donantes, agrupados por provincia.
def mostrarTodos(lista):
    for i in range(1, 10):
        codigo = str(i)
        encontrados = [c for c in lista if c.startswith(codigo)]
        if encontrados:
            print(f"Los donadores de la provincia de {nombreProvincia(codigo)}, son {len(encontrados)} con las cédulas:")
            for c in encontrados:
                print(" -", c)

# Muestra los donantes que tienen códigos especiales: naturalizados (8) o partida especial (9).
def mostrarNoTipicos(lista):
    for codigo in ["8", "9"]:
        encontrados = [c for c in lista if c.startswith(codigo)]
        if encontrados:
            print(f"Los donadores de la provincia de {nombreProvincia(codigo)}, son {len(encontrados)} con las cédulas:")
            for c in encontrados:
                print(" -", c)

"""Este es el menú principal que permite al usuario interactuar con el programa.
 El usuario puede elegir entre las diferentes opciones para trabajar con la lista de donantes."""
def menu():
    lista = ["303500621", "101110218", "412340987", "267893456",
        "154328765", "534561234", "187674329", "265437654",
        "243214321", "187654321", "187659870", "687659870",
        "887659870", "945659823"]
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar donantes")
        print("2. Decodificar donador")
        print("3. Listar por provincia")
        print("4. Listar todos los donantes")
        print("5. Listar donantes no típicos")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            agregarDonantes(lista)
        elif opcion == "2":
            mostrarDatosDonante(lista)
        elif opcion == "3":
            mostrarPorProvincia(lista)
        elif opcion == "4":
            mostrarTodos(lista)
        elif opcion == "5":
            mostrarNoTipicos(lista)
        elif opcion == "6":
            print("Gracias por donar su sangre, ahora fuiste tú, luego espero poder ser yo.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Llamamos directamente al menú para que el programa empiece desde ahí
menu()
