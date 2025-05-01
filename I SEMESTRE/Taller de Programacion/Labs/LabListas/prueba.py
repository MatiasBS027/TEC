#Elaborado por Luis Tinoco y Matias Benavides
#Fecha de creación 30/04/2025 07:30
#última modificación 30/04/2025 20:00
#python versió 3.13

#Importando librerías 
try:
    from funcionesLab import *
    print("Funciones importadas correctamente")
except ImportError as e:
    print(f"Error al importar las funciones: {e}")
import re
#Definición de funciones
def menu():
    """
    Funcionamiento: Maneja la interfaz principal del programa y el flujo de operaciones
    Entradas:
    - Ninguna
    Salidas:
    - str: Mensaje de despedida al finalizar el programa
    """
    lista = ["303500621", "101110218", "412340987", "267893456",
        "154328765", "534561234", "187674329", "265437654",
        "243214321", "187654321", "187659870", "687659870",
        "887659870", "945659823"]
    
    while True:
        menuTexto = "\n--- Menú Principal ---\n" + \
                    "1. Agregar donantes\n" + \
                    "2. Decodificar donador\n" + \
                    "3. Listar por provincia\n" + \
                    "4. Listar todos los donantes\n" + \
                    "5. Listar donantes no típicos\n" + \
                    "6. Salir"
        print(menuTexto)
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            resultado = agregarDonantes(lista)
        elif opcion == "2":
            resultado = mostrarDatosDonante(lista)
        elif opcion == "3":
            resultado = mostrarPorProvincia(lista)
        elif opcion == "4":
            resultado = mostrarTodos(lista)
        elif opcion == "5":
            resultado = mostrarNoTipicos(lista)
        elif opcion == "6":
            return "Gracias por donar su sangre, ahora fuiste tú, luego espero poder ser yo."
        else:
            resultado = "Opción inválida. Intente nuevamente."
        print(resultado)

print(menu())