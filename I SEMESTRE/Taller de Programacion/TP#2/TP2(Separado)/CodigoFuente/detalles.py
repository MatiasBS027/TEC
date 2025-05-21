# Elaborado por Luis Tinoco y Matias Benavides  
# Fecha de creación: 16/05/2025
# Última modificación: 16/05/2025 15:08
# Python version: 3.13.2

#importar librerias
import random
import requests

#definición de funciónes 
def obtenerInfoPokemon(idPoke):
    url = f"https://pokeapi.co/api/v2/pokemon/{idPoke}"
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        idApi = datos['id']
        nombre = datos['name']
        esShiny = False  # Puedes cambiar a random si deseas
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


def detalles(diccPoke):
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

print(obtenerInfoPokemon(1))