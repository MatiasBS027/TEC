# Elaborado por Luis Tinoco y Matias Benavides  
# Fecha de creación: 16/05/2025
# Última modificación: 16/05/2025 15:08
# Python version: 3.13.2

#importar librerias
import random
import requests

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

def listaAtrapados(atrapados):
    listaIds = []
    for poke in atrapados:
        idPoke = int(poke[0])
        listaIds.append(idPoke)
    return listaIds

def obtenerInfoPokemon(idPoke):
    url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        idApi = datos['id']
        nombre = datos['name']
        esShiny = random.choice([True, False])
        peso = datos['weight']  *10
        altura = datos['height']  *10
        estadisticas = datos['stats']
        stats = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
        statsValores = []
        for statNombre in stats:
            for stat in estadisticas:
                if stat['stat']['name'] == statNombre:
                    statsValores.append(stat['base_stat'])
                    break
        totalEstats = sum(statsValores)
        statsTupla = tuple(statsValores)  # (PS, A, D, AE, DE, V)
        tipos = []
        for tipo in datos['types']:
            nombreTipo = tipo['type']['name']
            tipos.append(nombreTipo)
        if esShiny:
            urlImagen = datos['sprites']['front_shiny']
        else:
            urlImagen = datos['sprites']['front_default']
        infoPokemon = {
            idApi: [
                nombre,
                (esShiny, peso, altura),
                [totalEstats, statsTupla],
                tipos,
                urlImagen]}
        return infoPokemon
    except Exception as e:
        print(f"Error al obtener info de Pokémon {idPoke}: {e}")
        return None

def imprimirInfoPokemon(diccPoke):
    for idPoke, datos in diccPoke.items():
        nombre = datos[0]
        esShiny, peso, altura = datos[1]
        totalEstad, stats = datos[2]
        tipos = datos[3]
        urlImagen = datos[4]
        
        print(f"ID: {idPoke}:")
        print("[")
        print(f"  '{nombre}',")
        print(f"  ({esShiny}, {peso}, {altura}),")
        print(f"  [{totalEstad}, {stats}],")
        print(f"  {tipos},")
        print(f"  '{urlImagen}'")
        print("]")
        print()

def shinys(diccPoke):
    shinys = {}
    for idPoke, datos in diccPoke.items():
        esShiny = datos[1][0]
        if esShiny == True:
            shinys[idPoke] = datos
    return shinys

def dividirPaginas(lista, tamano):
    paginas = []
    inicio = 0
    while inicio < len(lista):
        fin = inicio + tamano
        pagina = lista[inicio:fin]
        paginas.append(pagina)
        inicio = fin
    return paginas


def generarHtml(pagina, numeroPagina):
    nombreArchivo = f"Shinys{numeroPagina}.html"

    archivo = open(nombreArchivo, "w", encoding="utf-8")

    encabezado = """<!DOCTYPE html>
<html>
<head>
    <title>Pokémon Shinys</title>
    <style>
        table { border-collapse: collapse; width: 100%; }
        th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
        th { background-color: #ffcc00; color: black; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        img { width: 80px; }
    </style>
</head>
<body>
    <h1>Lista de Pokémon Shiny</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Shiny</th>
            <th>Peso (kg)</th>
            <th>Altura (cm)</th>
            <th>Estadísticas</th>
            <th>Total</th>
            <th>Tipos</th>
            <th>Imagen</th>
        </tr>
"""
    archivo.write(encabezado)
    for idPoke, datos in pagina:
        nombre = datos[0]
        tupla = datos[1]
        shiny = tupla[0]
        peso = tupla[1]
        altura = tupla[2]

        estadisticas = datos[2]
        total_stats = estadisticas[0]
        stats = estadisticas[1]
        tiposLista = datos[3]
        tipos = ', '.join(tiposLista)
        url = datos[4]

        filaHtml = f"""
        <tr>
            <td>{idPoke}</td>
            <td>{nombre}</td>
            <td>{shiny}</td>
            <td>{peso}</td>
            <td>{altura}</td>
            <td>{stats}</td>
            <td>{total_stats}</td>
            <td>{tipos}</td>
            <td><img src="{url}" alt="{nombre}"></td>
        </tr>
"""
        archivo.write(filaHtml)
    cierre = """
    </table>
</body>
</html>
"""
    archivo.write(cierre)
    archivo.close()

def generarReportes(diccPoke):
    shinysFiltrados = shinys(diccPoke)
    listaShinys = list(shinysFiltrados.items())
    paginas = dividirPaginas(listaShinys, 100)
    contador = 1
    for pagina in paginas:
        generarHtml(pagina, contador)
        contador += 1
    cantidadPaginas = len(paginas)
    print(f"Se generaron {cantidadPaginas} archivo(s) HTML con Pokémon shiny.")

resultado = atraparPokeES()
if isinstance(resultado, tuple):
    atrapados, huidos = resultado
    print("Proceso de captura completado.")
    listaIdAtrapados = listaAtrapados(atrapados)
    diccPoke = {}
    for id in listaIdAtrapados:
        info = obtenerInfoPokemon(id)
        if info:
            diccPoke.update(info)
    imprimirInfoPokemon(diccPoke)

    # Ahora generamos reportes aquí
    if diccPoke:
        shinysFiltrados = shinys(diccPoke)
        if shinysFiltrados:
            generarReportes(diccPoke)
        else:
            print("No se encontraron Pokémon shiny para generar reportes HTML.")
    else:
        print("No hay datos de Pokémon para generar reportes.")
else:
    print(resultado)