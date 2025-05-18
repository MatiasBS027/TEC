# Elaborado por Luis Tinoco y Matias Benavides  
# Fecha de creación: 16/05/2025
# Última modificación: 16/05/2025 15:08
# Python version: 3.13.2

#importar librerias
import random


#definición de funciónes 
def buscarTxt():
    pokemon = []  # Lista para guardar tuplas (id, nombre)
    try:
        with open("MisPokemon.txt", "r") as file:
            pokemon = []  # Lista para guardar tuplas (id, nombre)
            for line in file:
                linea = line.strip()  # Elimina espacios y saltos de línea5
                if linea:  # Si la línea no está vacía
                    partes = linea.split("^")  # Separa por el carácter ^
                    if len(partes) == 2:
                        idPokedex = partes[0].strip()
                        nombre = partes[1].strip()
                        pokemon.append((idPokedex, nombre))
                    else:
                        print(f"Línea mal formada: {linea}")
        if not pokemon:
            print("El archivo está vacío o no contiene datos válidos.")
    except FileNotFoundError:
        print("El archivo 'MisPokemon.txt' no existe.")
    return pokemon  # Retornamos la lista (vacía si falla)

def guardarEstadosPokemon(atrapados, huidos):
    nombreArchivo="MisPokemon.txt"
    todos = []
    for idPoke, nombre in atrapados: #Pokemon atrapados
        idPoke = int(idPoke)
        estado = "a"
        todos.append((idPoke, nombre,"a")) #Pokemon que huyeron
    for idPoke, nombre in huidos:
        idPoke = int(idPoke)
        estado = "h"
        todos.append((idPoke, nombre,"h"))
    todos.sort(key=lambda x: x[0])
    with open(nombreArchivo, "w") as file:
        for idPoke, nombre, estado in todos:
            file.write(f"{idPoke}^{nombre}^{estado}\n")

def atraparPokeES():
    try:
        porcentaje = int(input("Que porcentaje de Pokemon quieres atrapar? "))
        return atraparPokeAux(porcentaje)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

def atraparPokeAux(porcentaje):
    if porcentaje < 0 or porcentaje > 100:
        return "Porcentaje no válido. Debe estar entre 0 y 100."
    else:
        print(f"Porcentaje válido. Procediendo a atrapar el {porcentaje} de los Pokémon.")
        return atraparPoke(porcentaje)

def atraparPoke(porcentaje):
    pokemon = buscarTxt()
    if not pokemon:
        return "No hay Pokémon para atrapar."
        return
    totalPokemon = len(pokemon)
    cantidadAtrapados  = round((porcentaje / 100) * totalPokemon)
    cantidadHuyeron = totalPokemon - cantidadAtrapados
    atrapados = random.sample(pokemon, cantidadAtrapados)
    huidos = []
    for poke in pokemon:
        if poke not in atrapados:
            huidos.append(poke)
    print(f"Pokémon atrapados: {cantidadAtrapados}")
    print(f"Pokémon que huyeron: {cantidadHuyeron}")
    for idPoke, nombre in atrapados:
        print(f"ID: {idPoke}, Nombre: {nombre}")
    print("Pokémon que huyeron:")
    for idPoke, nombre in huidos:
        print(f"ID: {idPoke}, Nombre: {nombre}")
    guardarEstadosPokemon(atrapados, huidos)
    return atrapados, huidos


resultado = atraparPokeES()
if isinstance(resultado, tuple):
    atrapados, huidos = resultado
    print("Proceso de captura completado.")
else:
    print(resultado)  # Mensaje de error