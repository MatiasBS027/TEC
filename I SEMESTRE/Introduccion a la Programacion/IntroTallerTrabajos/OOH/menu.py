#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creación 24/05/2025
#última actualización 24/05/2025
#python versión 3.13.2

from funciones import crearArma, crearArmadura, mostrarObjeto, validarMetal, validarColor, validarDano, validarVelocidad, validarDefensa

# ==========================
# ES
# ==========================

def herramientaES():
    idHerramienta = input("Ingrese el ID de la herramienta: ")
    
    while True:
        metal = input("Ingrese el tipo de metal (oro, diamante, hierro): ")
        if validarMetal(metal):
            break
        print("Metal inválido. Intente de nuevo.")
    
    while True:
        color = input("Ingrese el color (azul, amarillo, gris): ")
        if validarColor(color):
            break
        print("Color inválido. Intente de nuevo.")
    
    return idHerramienta, metal, color

# ==========================
# Crear arma
# ==========================

def crearArmaMenu():
    while True:
        try:
            idHerramienta, metal, color = herramientaES()
            
            while True:
                try:
                    dano = int(input("Ingrese el daño (7, 8, 9): "))
                    if validarDano(dano):
                        break
                    else:
                        print("Daño inválido. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un número entero válido.")
            
            while True:
                try:
                    velocidad = float(input("Ingrese la velocidad de ataque (0.1 a 0.3): "))
                    if validarVelocidad(velocidad):
                        break
                    else:
                        print("Velocidad inválida. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un número decimal válido.")
            
            arma = crearArma(idHerramienta, metal, color, dano, velocidad)
            mostrarObjeto(arma)
            break  # salir del ciclo si se creó exitosamente
        except ValueError as error:
            print(f"Error: {error}. Intente de nuevo.\n")

# ==========================
# Crear armadura
# ==========================

def crearArmaduraMenu():
    while True:
        try:
            idHerramienta, metal, color = herramientaES()
            
            while True:
                try:
                    defensa = int(input("Ingrese la defensa (4, 5, 6): "))
                    if validarDefensa(defensa):
                        break
                    else:
                        print("Defensa inválida. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un número entero válido.")
            
            armadura = crearArmadura(idHerramienta, metal, color, defensa)
            mostrarObjeto(armadura)
            break  # salir del ciclo si se creó exitosamente
        except ValueError as error:
            print(f"Error: {error}. Intente de nuevo.\n")

# ==========================
# Función principal
# ==========================

def main():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Crear arma")
        print("2. Crear armadura")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crearArmaMenu()
        elif opcion == "2":
            crearArmaduraMenu()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

main()
