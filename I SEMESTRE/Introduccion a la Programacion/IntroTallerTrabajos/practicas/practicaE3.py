def esPar(n):
    if n % 2 == 0:
        return True 
    return False

def esPrimo(n): 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def annoBisiesto(n):
    if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
        return True
    return False

def crearDiccionario(tupla):
    diccionario = {"pares": [], 
                "impares": [], 
                "primos": [], 
                "bisiestos": []}
    for i in tupla:
        if esPar(i):
            diccionario["pares"].append(i)
        else:
            diccionario["impares"].append(i)
        
        if esPrimo(i):
            diccionario["primos"].append(i)
        
        if annoBisiesto(i):
            diccionario["bisiestos"].append(i)
    return diccionario

def clasificacionAnno(edad):
    anno = 2024
    inicio = anno - edad
    tupla = ()
    print(f"Usted nació en el año {inicio}.")
    for anno in range(inicio, anno +1):
        tupla += (anno,)
    print(tupla)
    return crearDiccionario(tupla)

def clasificacionAnnoES():
    try:
        edad = int(input("Introduzca su edad: "))
        resutado = clasificacionAnno(edad)
        return resutado
    except ValueError:
        print("Por favor, introduzca un número válido.")
        return

print(clasificacionAnnoES())