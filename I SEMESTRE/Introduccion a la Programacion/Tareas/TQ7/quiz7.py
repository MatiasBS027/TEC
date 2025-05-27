#Elaborado por Matias Benavides y Brittany Rodriguez

#Reto 1

def clasificarOperadores(listaCarnets):
    generaciones = {}
    for carnet in listaCarnets:
        gen=int(carnet[:4])
        if gen not in generaciones:
            generaciones[gen]=[]
        generaciones[gen].append(carnet)
    texto=""
    for gen in sorted(generaciones):
        texto+=f"{gen}: {generaciones[gen]}\n"
    texto+=f"\nTenemos {len(generaciones)} generaciones.\n"
    cantidad=0
    for gen in generaciones:
        if len(generaciones[gen])>cantidad:
            cantidad=len(generaciones[gen])
            mayor=gen

    texto += f"Pero hay más operadores del {mayor}.\n"
    return texto

def clasificarOperadoresAux(listaCarnets):
    generaciones={}
    for carnet in listaCarnets:
        if type(carnet) != str:
            return "Debe ingresar únicamente valores de tipo strings"
        if not carnet.isdigit() or len(carnet) != 10:
            return "Todos los carnets deben ser textos con 10 valores que representen números."
        gen = int(carnet[:4])
        if gen not in generaciones:
            generaciones[gen] = []
        generaciones[gen].append(carnet)
    return clasificarOperadores(listaCarnets)

print("######Reto 1: Clasificación de Operadores######\n")
print("SALIDA 1")
print(clasificarOperadoresAux(["2022011234","202301543","2022017654"]))
print("SALIDA 2")
print(clasificarOperadoresAux(["2022011234",2023015432,"2022017654"]))
print("SALIDA 3")
print(clasificarOperadoresAux(["2022011234","2023015432","2022017654"]))
print("SALIDA 4")
print(clasificarOperadoresAux(["2022011234","2023015432","2022017654","2024017654","2024017765","2020016543"]))
print("SALIDA 5")
print(clasificarOperadoresAux(["2022011234","2023015432","2021017654","2024017654","2024017765","2020016543"]))

# Reto 2

def diccionarioAMatriz(diccionario):
    # Diccionario auxiliar para agrupar eventos por día
    agrupados = {}
    for categoria in diccionario:
        for dia, descripcion in diccionario[categoria]:
            if dia not in agrupados:
                agrupados[dia] = []
            agrupados[dia].append(descripcion)
    # Creamos una lista vacía para la matriz
    matriz = []
    # Recorremos cada clave y valor del diccionario 'agrupados'
    for dia, descripciones in agrupados.items():
    # Creamos una lista con el día y la lista de descripciones
        fila = [dia, descripciones]
    # Agregamos esa fila a la matriz
        matriz.append(fila)

    return matriz

diccionario = {
    "Lluvia": [
        (10, "Lluvia de meteoros Táuridas del Sur"),
        (21, "Lluvia de meteoros Oriónidas")
    ],
    "Conjunciones": [
        (21, "Conjunción de la Luna con Júpiter"),
        (23, "Conjunción de la Luna con Marte")
    ],
    "Otros": [
        (2, "La luna pasará frente al sol"),
        (3, "Galaxia del escultor"),
        (14, "Ocultación lunar"),
        (17, "Luna Llena"),
        (31, "El cúmulo doble de Perseo")
    ]
}


resultado = diccionarioAMatriz(diccionario)
print("######Reto 2: Diccionario a Matriz######\n")
for fila in resultado:
    print(fila)
