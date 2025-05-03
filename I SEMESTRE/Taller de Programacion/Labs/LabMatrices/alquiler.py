#Elaborado por Luis Tinoco y Matias Benavides
#Fecha de creación 2/5/2025 07:30
#última modificación 2/5/2025 20:00
#python versión 3.13

#importar librerías
from funciones import *

#definición de funciones
def menuPrincipal(edificio):
    while True:        
        try:
            menu = "\n--- Menú Principal ---\n" + \
                    "1. Alquilar apartamento\n" + \
                    "2. Modificar Renta\n" + \
                    "3. Desalojar\n" + \
                    "4. Indicar ingreso por alquiler\n" + \
                    "5. Reporte total del edificio\n" + \
                    "6. Salir"
            print(menu)
            opcion = input("Seleccione una opción (1-6): ")
            if opcion == "1":
                resultado = alquilarApartamento(edificio)
            elif opcion == "2":
                resultado = modificarRenta(edificio)
            elif opcion == "3":
                resultado = desalojar(edificio)
            elif opcion == "4":
                resultado = ingresoAlquilerMenu(edificio)
            elif opcion == "5":
                resultado = reporteTotalEdificio(edificio)
            elif opcion == "6":
                return "Gracias por usar el sistema. ¡Hasta luego!"
            else:
                resultado = "Opción inválida. Intente nuevamente."
            print(resultado)
        except ValueError:
            print("Debe ingresar un número entero.")


def alquilerEs():
    while True:
        try:
            pisos = int(input("Ingrese el número de pisos del edificio: "))
            apartamentos = int(input("Ingrese el número de apartamentos por piso: "))
            edificio = alquilarAux(pisos, apartamentos)
            if isinstance(edificio, str):
                return edificio
            else:
                resultado = menuPrincipal(edificio)
                return resultado
        except ValueError:
            print("Debe ingresar un número entero.")
        
print (alquilerEs())
