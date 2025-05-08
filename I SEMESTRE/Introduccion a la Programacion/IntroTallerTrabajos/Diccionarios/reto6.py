import re

def separarPalabras(cadena):
    palabra = cadena.split()
    return palabra

def crearIndice(palabra):
    palabra = separarPalabras(palabra)
    diccionario = {}
    for i in palabra:
        inicial = i[0]
        if inicial not in diccionario:
            diccionario[inicial] = [i]
        elif i not in diccionario[inicial]:
            diccionario[inicial].append(i)
    diccionario = ordenar(diccionario)
    return diccionario  

def ordenar(diccionario):
    for i in diccionario:
        diccionario[i].sort()
        diccionarioOrdenado = dict(sorted(diccionario.items()))
    return diccionarioOrdenado

def validar(cadena):
    if cadena == "":
        return "Debe ingresar información para poder crear el diccionario alfabético."
    else:
        return crearIndice(cadena)

cadena = input("Ingrese una cadena de texto: ").lower()
print(validar(cadena))
