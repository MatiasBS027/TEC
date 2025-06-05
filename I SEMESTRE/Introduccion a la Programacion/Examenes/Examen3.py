#Elaborado por Matias Beanvides S
#=====Reto 1=====
def comparar(pal1,pal2):
    pal1 = pal1.lower()
    pal2 = pal2.lower()
    cont = 0
    for i in range(len(pal1)):
        letra = pal1[i]
        if letra in pal2:
            cont+=1
        if cont == len(pal2) and cont == len(pal1):
            return True

def convertirLSaLT(lista):
    nLista = []
    for i in range(len(lista)):
        palabra = lista[i]
        for j in range(len(lista)):
            palabra2 = lista[j]
            if comparar(palabra,palabra2) == True:
                if palabra != palabra2:
                    if (palabra,palabra2) not in nLista and (palabra2,palabra) not in nLista :
                        nLista.append((palabra, palabra2))
        palabra = ""
    return nLista
print(convertirLSaLT(["Amor","romA","Perro","mOra","raMo","aRomA"]))

#======Reto 2======
def diccAdicc(dicc, diccLetras):
    nuevoDicc = {}
    for i in diccLetras:
        listaN= []
        i=i.upper()

        for j in dicc.keys():
            if i.upper() == j[0].upper():
                listaN.append((j.upper(), diccionario[j]))

        nuevoDicc[i] = listaN
    print(nuevoDicc)
    
def diccAdiccAux(dicc, diccLetras):
    if dicc == {} or diccLetras == {}:
        return "El diccionario no puede estar vacio para poder hacer la conversion"
    else:
        return diccAdicc(dicc, diccLetras)
    
diccionario = {"wifi": "Wireless Fidelity",
    "DVD": "Disco Versatil Digital",
    "SIM": "Subscriber Identity Module",
    "SMS": "Short Message Service",
    "WWW": "World Wide Web",
    "ok": "oll korrect",
    "pdf": "Portable Document Format",
    "GPS": "Global Positioning System",
    "HDMI": "High-Definition Multimedia Interface",
    "USB": "Universal Serial Bus",
    "LED": "Light Emitting Diode"}
diccLetras= {"W","D","S","O","P","G","H","U","L",}
diccAdiccAux(diccionario, diccLetras)

#=====Reto 3=====

def elevarAlCubo(n):
    cubo=1
    for i in range(3):
        cubo*=n
    return cubo

def esNumNarcisista(lista):
    listaFinal = []
    for num in lista:
        total = 0
        for digito in str(num):
            total += elevarAlCubo(int(digito))
        if total == num:
            listaFinal.append([True, num])
        else:
            listaFinal.append([False, num])
    return listaFinal

listaNum= [153,200,50,371]
print(esNumNarcisista(listaNum))