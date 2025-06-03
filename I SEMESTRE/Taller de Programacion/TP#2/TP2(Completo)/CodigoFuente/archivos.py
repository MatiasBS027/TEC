import os
import random
import requests

def guardarPokemon(pokemonInfo):
    """
    Funcionamiento:
    Guarda la información de un Pokémon en los archivos 'MisPokemon.txt' y 'DiccionarioPokemon.txt'.

    Entradas:
    - pokemonInfo: Diccionario con la información del Pokémon (id, nombre, esShiny, peso, altura, stats, tipos, imagen).

    Salidas:
    - Ninguna (guarda datos en archivos).
    """
    
    rutaBase = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(rutaBase, "MisPokemon.txt"), "a", encoding="utf-8") as archivo:
        archivo.write(f"{pokemonInfo['id']}^{pokemonInfo['nombre']}^a\n")
    statsTupla = tuple(pokemonInfo['stats'])
    totalStats = sum(pokemonInfo['stats'])
    with open(os.path.join(rutaBase, "DiccionarioPokemon.txt"), "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{pokemonInfo['id']}^{pokemonInfo['nombre']}^"
            f"({pokemonInfo['esShiny']}, {pokemonInfo['peso']}, {pokemonInfo['altura']})^"
            f"[{totalStats}, {statsTupla}]^"
            f"{pokemonInfo['tipos']}^"
            f"{pokemonInfo['imagen']}\n"
        )

def pokemonYaExiste(idPoke):
    """
    Funcionamiento:
    Verifica si un Pokémon con el ID dado ya existe en el archivo 'MisPokemon.txt'.

    Entradas:
    - idPoke: ID del Pokémon a verificar.

    Salidas:
    - True si el Pokémon ya existe, False en caso contrario.
    """
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "MisPokemon.txt")
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split("^")
                if partes and partes[0] == str(idPoke):
                    return True
    return False

def obtenerDatosPokemon(idPoke):
    """
    Funcionamiento:
    Obtiene los datos de un Pokémon desde la API de PokeAPI y los organiza en un diccionario.

    Entradas:
    - idPoke: ID del Pokémon a consultar.

    Salidas:
    - Diccionario con los datos del Pokémon (id, nombre, esShiny, peso, altura, stats, tipos, imagen) o None si falla.
    """
    respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{idPoke}", timeout=10)
    if respuesta.status_code != 200:
        return None
    datos = respuesta.json()
    stats = []
    for s in datos['stats']:
        stats.append(s['base_stat'])
    tipos = []
    for t in datos['types']:
        tipos.append(t['type']['name'])
    return {
        'id': idPoke,
        'nombre': datos['name'].capitalize(),
        'esShiny': random.choice([True, False]),
        'peso': datos['weight'] * 10,
        'altura': datos['height'] * 10,
        'stats': stats,
        'tipos': tipos,
        'imagen': datos['sprites']['front_default']
    }

def leerDiccionario():
    diccPoke = {}
    try:
        rutaBase = os.path.dirname(os.path.abspath(__file__))
        rutaArchivo = os.path.join(rutaBase, "DiccionarioPokemon.txt")
        with open(rutaArchivo, "r", encoding="utf-8") as file:
            for line in file:
                partes = line.strip().split("^")
                if len(partes) == 6:
                    idPoke = int(partes[0])
                    nombre = partes[1]
                    tupla = eval(partes[2])
                    estadisticas = eval(partes[3])
                    tipos = eval(partes[4])
                    url = partes[5]
                    diccPoke[idPoke] = [nombre, tupla, estadisticas, tipos, url]
    except Exception as e:
        print(f"Error al leer el diccionario: {e}")
    return diccPoke

def guardarResultados(atrapados, huidos, rutaBase):
    """
    Funcionamiento:
    Actualiza el estado de los Pokémon en 'MisPokemon.txt' según si fueron atrapados o huyeron.

    Entradas:
    - atrapados: Lista de tuplas (id, nombre) de Pokémon atrapados.
    - huidos: Lista de tuplas (id, nombre) de Pokémon huidos.
    - rutaBase: Ruta base donde se encuentran los archivos.

    Salidas:
    - True si se guardó correctamente, False si hubo error.
    """
    try:
        rutaArchivo = os.path.join(rutaBase, "MisPokemon.txt")
        lineasNuevas = []
        estadoActualizado = {}
        for idPoke, nombre in atrapados:
            estadoActualizado[(idPoke, nombre)] = 'a'
        for idPoke, nombre in huidos:
            estadoActualizado[(idPoke, nombre)] = 'h'
        with open(rutaArchivo, "r", encoding="utf-8") as file:
            for linea in file:
                partes = linea.strip().split("^")
                if len(partes) >= 2:
                    clave = (partes[0], partes[1])
                    if clave in estadoActualizado:
                        nuevaLinea = f"{partes[0]}^{partes[1]}^{estadoActualizado[clave]}\n"
                    elif len(partes) == 2:
                        # Si no está en atrapados/huidos, pero no tiene estado, agrégale vacío
                        nuevaLinea = f"{partes[0]}^{partes[1]}^\n"
                    else:
                        nuevaLinea = linea
                    lineasNuevas.append(nuevaLinea)
                else:
                    lineasNuevas.append(linea)
        with open(rutaArchivo, "w", encoding="utf-8") as file:
            file.writelines(lineasNuevas)
        return True
    except Exception as e:
        print(f"Error al guardar resultados: {e}")
        return False

def generarDiccionarioPokemon():
    """
    Funcionamiento:
    Genera el archivo 'DiccionarioPokemon.txt' con la información detallada de los Pokémon atrapados.

    Entradas:
    - Ninguna (lee 'MisPokemon.txt' para obtener los Pokémon atrapados).

    Salidas:
    - Ninguna (genera o actualiza el archivo 'DiccionarioPokemon.txt').
    """
    rutaBase = os.path.dirname(os.path.abspath(__file__))
    rutaMisPokemon = os.path.join(rutaBase, "MisPokemon.txt")
    rutaDiccionario = os.path.join(rutaBase, "DiccionarioPokemon.txt")
    pokemones = []
    try:
        with open(rutaMisPokemon, "r", encoding="utf-8") as file:
            for line in file:
                partes = line.strip().split("^")
                if len(partes) == 3 and partes[2].strip().lower() == "a":
                    idPoke = partes[0]
                    pokemones.append(idPoke)
    except Exception as e:
        print(f"Error al leer MisPokemon.txt: {e}")
        return
    with open(rutaDiccionario, "w", encoding="utf-8") as file:
        for idPoke in pokemones:
            try:
                url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
                respuesta = requests.get(url, timeout=8)
                datos = respuesta.json()
                nombre = datos['name']
                esShiny = random.choice([True, False])
                peso = datos['weight'] * 10
                altura = datos['height'] * 10
                estadisticas = datos['stats']
                stats = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
                statsValores = []
                for statNombre in stats:
                    for stat in estadisticas:
                        if stat['stat']['name'] == statNombre:
                            statsValores.append(stat['base_stat'])
                            break
                totalEstats = sum(statsValores)
                statsTupla = tuple(statsValores)
                tipos = []
                for tipo in datos['types']:
                    tipos.append(tipo['type']['name'])
                if esShiny:
                    urlImagen = datos['sprites']['front_shiny']
                else:
                    urlImagen = datos['sprites']['front_default']
                file.write(f"{idPoke}^{nombre}^{(esShiny, peso, altura)}^{[totalEstats, statsTupla]}^{tipos}^{urlImagen}\n")
            except Exception as e:
                print(f"Error al obtener info de Pokémon {idPoke}: {e}")

def leerPokemonesDisponibles():
    """
    Funcionamiento:
    Lee el archivo 'MisPokemon.txt' y retorna una lista de Pokémon que están disponibles para atrapar.

    Entradas:
    - Ninguna.

    Salidas:
    - Lista de tuplas (id, nombre) de Pokémon disponibles.
    """
    rutaBase = os.path.dirname(os.path.abspath(__file__))
    rutaArchivo = os.path.join(rutaBase, "MisPokemon.txt")
    disponibles = []
    try:
        with open(rutaArchivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split("^")
                if len(partes) == 2:
                    # Si solo hay id y nombre, se considera disponible
                    disponibles.append((int(partes[0]), partes[1]))
                elif len(partes) == 3:
                    # Si hay estado, solo agregar si no está atrapado ni ha huido
                    estado = partes[2].strip().lower()
                    if estado not in ("a", "h"):
                        disponibles.append((int(partes[0]), partes[1]))
    except FileNotFoundError:
        pass
    return disponibles