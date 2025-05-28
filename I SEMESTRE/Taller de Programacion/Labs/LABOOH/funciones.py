#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creacón 22/05/2025
#última actualización 27/05/2025
#python versión 3.13.2

import csv
from minecraftclass import HerramientaArma, HerramientaArmadura
from archivo import crearBaseDeDatos

# ==========================
# Validaciones
# ==========================

def validarMetal(metal):
    return metal.lower() in ["oro", "diamante", "hierro"]

def validarColor(color):
    return color.lower() in ["azul", "amarillo", "gris"]

def validarDano(dano):
    return dano in [7, 8, 9]

def validarVelocidad(velocidad):
    return 0.1 <= velocidad <= 0.3

def validarDefensa(defensa):
    return defensa in [4, 5, 6]

# ==========================
# Crear objetos
# ==========================

def crearArma(idHerramienta, metal, color, dano, velocidad):
    arma = HerramientaArma()
    arma.asignarIdHerramienta(idHerramienta)
    arma.asignarDurabilidad()

    if validarMetal(metal):
        arma.asignarMetal(metal)
    else:
        raise ValueError("Metal invalido.")

    if validarColor(color):
        arma.asignarColor(color)
    else:
        raise ValueError("Color invalido.")

    if validarDano(dano):
        arma.asignarDano(dano)
    else:
        raise ValueError("Daño invalido.")

    if validarVelocidad(velocidad):
        arma.asignarVelocidadAtaque(velocidad)
    else:
        raise ValueError("Velocidad invalida.")

    return arma

def crearArmadura(idHerramienta, metal, color, defensa):
    armadura = HerramientaArmadura()
    armadura.asignarIdHerramienta(idHerramienta)
    armadura.asignarDurabilidad()

    if validarMetal(metal):
        armadura.asignarMetal(metal)
    else:
        raise ValueError("Metal invalido.")

    if validarColor(color):
        armadura.asignarColor(color)
    else:
        raise ValueError("Color invalido.")

    if validarDefensa(defensa):
        armadura.asignarDefensa(defensa)
    else:
        raise ValueError("Defensa invalida.")

    return armadura

# ==========================
# Guardar en archivo
# ==========================

def guardarEnBaseDatos(archivo, objeto):
    with open(archivo, 'a', newline='') as file:
        writer = csv.writer(file)
        if isinstance(objeto, HerramientaArma):
            writer.writerow([
                objeto.mostrarIdHerramienta(),
                objeto.mostrarDurabilidad(),
                objeto.mostrarMetal(),
                objeto.mostrarColor(),
                objeto.mostrarDano(),
                objeto.mostrarVelocidadAtaque(),
                "",
                "activo"
            ])
            print("Arma guardada exitosamente.")
        elif isinstance(objeto, HerramientaArmadura):
            writer.writerow([
                objeto.mostrarIdHerramienta(),
                objeto.mostrarDurabilidad(),
                objeto.mostrarMetal(),
                objeto.mostrarColor(),
                "",
                "",
                objeto.mostrarDefensa(),
                "activo"
            ])
            print("Armadura guardada exitosamente.")

# ==========================
# Mostrar objeto
# ==========================

def mostrarObjeto(objeto):
    if isinstance(objeto, HerramientaArma):
        print("Tipo: Arma")
        print(f"ID: {objeto.mostrarIdHerramienta()}")
        print(f"Durabilidad: {objeto.mostrarDurabilidad()}")
        print(f"Metal: {objeto.mostrarMetal()}")
        print(f"Color: {objeto.mostrarColor()}")
        print(f"Daño: {objeto.mostrarDano()}")
        print(f"Velocidad de ataque: {objeto.mostrarVelocidadAtaque()}")
    elif isinstance(objeto, HerramientaArmadura):
        print("Tipo: Armadura")
        print(f"ID: {objeto.mostrarIdHerramienta()}")
        print(f"Durabilidad: {objeto.mostrarDurabilidad()}")
        print(f"Metal: {objeto.mostrarMetal()}")
        print(f"Color: {objeto.mostrarColor()}")
        print(f"Defensa: {objeto.mostrarDefensa()}")
    else:
        print(">> Objeto desconocido.")

# ==========================
# Funciones nuevas
# ==========================

def mostrarTodo(baseDatos):
    with open(baseDatos, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        print("\n--- INVENTARIO ACTUAL ---")
        for row in reader:
            if row[7] == 'activo':
                tipo = "Arma" if row[5] != '' else "Armadura"
                if tipo == "Arma":
                    print(f"Tipo: {tipo} | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Daño: {row[4]}, Velocidad: {row[5]}")
                else:
                    print(f"Tipo: {tipo} | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Defensa: {row[6]}")

def buscarPorID(baseDatos, idHerramienta):
    with open(baseDatos, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == idHerramienta and row[7] == 'activo':
                tipo = "Arma" if row[5] != '' else "Armadura"
                print(f"\n>> Herramienta encontrada")
                if tipo == "Arma":
                    print(f"Tipo: {tipo} | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Daño: {row[4]}, Velocidad: {row[5]}")
                else:
                    print(f"Tipo: {tipo} | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}, Defensa: {row[6]}")
                return
    print(">> ID no encontrado o herramienta eliminada.")

def mostrarArmasPorMetal(baseDatos, metal):
    if not validarMetal(metal):
        print("Metal inválido.")
        return

    with open(baseDatos, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        encontrado = False
        print(f"\n--- ARMAS DE {metal.upper()} ---")
        for row in reader:
            if row[2].lower() == metal.lower() and row[5] != '' and row[7] == 'activo':
                print(f"ID: {row[0]}, Durabilidad: {row[1]}, Color: {row[3]}, Daño: {row[4]}, Velocidad: {row[5]}")
                encontrado = True
        if not encontrado:
            print("No se encontraron armas de ese metal.")

def desgastarArmaPorID(baseDatos, idHerramienta):
    actualizado = []
    encontrado = False
    with open(baseDatos, 'r') as file:
        reader = csv.reader(file)
        encabezado = next(reader)
        for row in reader:
            if row[0] == idHerramienta and row[5] != '' and row[7] == 'activo':
                nueva_durabilidad = int(row[1]) - 25
                if nueva_durabilidad <= 0:
                    print("Durabilidad llegó a 0. El arma ha sido eliminada.")
                    row[7] = 'eliminado'
                else:
                    print(f"Durabilidad actualizada: {nueva_durabilidad}")
                    row[1] = str(nueva_durabilidad)
                encontrado = True
            actualizado.append(row)

    if not encontrado:
        return False

    with open(baseDatos, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(encabezado)
        writer.writerows(actualizado)

    return True

def eliminarPorID(baseDatos, idHerramienta):
    actualizado = []
    eliminado = False
    with open(baseDatos, 'r') as file:
        reader = csv.reader(file)
        encabezado = next(reader)
        for row in reader:
            if row[0] == idHerramienta and row[7] == 'activo':
                row[7] = 'eliminado'
                eliminado = True
            actualizado.append(row)

    with open(baseDatos, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(encabezado)
        writer.writerows(actualizado)

    return eliminado


def mostrarEliminados(baseDatos):
    with open(baseDatos, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Salta encabezado
        eliminados = [row for row in reader if row[7].strip().lower() == 'eliminado']

    print("\n--- HERRAMIENTAS ELIMINADAS ---")
    if eliminados:
        for row in eliminados:
            tipo = "Arma" if row[5].strip() != '' else "Armadura"
            print(f"Tipo: {tipo} | ID: {row[0]}, Durabilidad: {row[1]}, Metal: {row[2]}, Color: {row[3]}")
    else:
        print("No hay herramientas eliminadas registradas.")