def eliminarVocales(texto):
    vocales = "aeiouAEIOU"
    contador=   0
    while contador < len(texto):
        if texto[contador] in vocales:
            texto = texto.replace(texto[contador], "")
        contador += 1
    return texto

texto = input("Ingrese un texto: ")
print(eliminarVocales(texto)) 