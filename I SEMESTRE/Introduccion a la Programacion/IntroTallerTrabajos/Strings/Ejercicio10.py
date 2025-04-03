#Elaborado por: Matias Benavides, Ignacio Elizondo, Julio Barrios, Luis Alfaro, Sebastaian Mora
def encontrarPalabras(palabra):
    for i in range(len(palabra)):
        if palabra[i] == " ":
            return palabra[:i]
    return palabra

def quitarPrimeraPalabra(frase):
    for i in range(len(frase)):
        if frase[i] == " ":
            return frase[i+1:]
    return ""

def compararPalabras(frase1, frase2):
    contador = 0
    while frase1 != "":
        palabra = encontrarPalabras(frase1)
        if palabra in frase2:
            contador += 1
        frase1 = quitarPrimeraPalabra(frase1)
    return contador

print(compararPalabras("hola mundo feliz", "droppy es un perro feliz"))  #1