#Elaborado por: Matias Benavides Sandoval
#Funciones
def esPrimo(num):
    if num%2==0 or num%3==0 or num%5==0:
        return False
    else:
        return True

def contarCaracteres(palabra):
    contador=0
    for i in palabra:
        contador+=1
    return contador

def palindromo(palabra):
    if palabra [::-1] == palabra:
        return True
    else:
        return False

#------------------Reto1-------------------
def palindromosMayores(oracion):
    oracion= oracion.lower()
    listaNum=[]
    listaPal=[]
    matriz = []
    contador = 0
    for i in oracion:
        contador+=1
        if i.isspace():
            palabra = oracion[:contador-1]
            if palindromo(palabra) == True:
                if contarCaracteres(palabra) >=4:
                    if palabra.isdigit():
                        listaNum.append(palabra)
                    elif palabra.isalpha():
                        listaPal.append(palabra)
            oracion = oracion[contador:]
            contador = 0
    matriz.append(listaPal)
    matriz.append(listaNum)
    return matriz

print("Reto 3")
oracion = "Ana compro 242 confites, ellos narran que nadan como el oro luego de recorrer 17371 millas o 1221 millas"
print("Para la entrada:", oracion)
print(palindromosMayores(oracion))
oracion = "En todas las sedes del Tec, somos ojo de aguila, para reconocer la calidad desde el 1991 "
print("Para la entrada:", oracion)
print(palindromosMayores(oracion))
oracion = "Somos calidad Tec"
print("Para la entrada:", oracion)
print(palindromosMayores(oracion))
oracion = "Si Ana nacio en 1831, tiene 191 años"
print("Para la entrada:", oracion)
print(palindromosMayores(oracion))

#-----------Reto2-----------------
def quienSeRepiteMas(lista):
    nuevaLista = []
    listaF =[]
    for i in lista:
        if i in nuevaLista:
            if i in listaF:
                listaF=listaF
            else:
                repetido=i
                listaF.append(i)
        nuevaLista.append(i)
    if len(listaF) == 0:
        return "No hay elementos repetidos"
    if len(listaF) == 1:
        return repetido
    else:
        return(listaF)

def quienSeRepiteMasAux(lista):
    if len(lista) ==0:
        return "La lista no tiene elementos"
    else:
        return quienSeRepiteMas(lista)

def RepiteMasEs(lista):
    #lista = input("Ingrese una lista: ")
    return quienSeRepiteMasAux(lista)

print("Reto 2")
lista = [1,2,3,2,5,8,"a",90,"b",2]
print("Para la entrada:",lista)
print(RepiteMasEs(lista))
lista = ["a",2,3,2,"a",90,"a",2,2]
print("Para la entrada:",lista)
print(RepiteMasEs(lista))

#---------------Reto3-------------------
def primosGemelos(num1, num2):
    lista = []
    for i in range(num1, num2):
        if esPrimo(i) and esPrimo(i + 2):
            lista.append((i, i + 2))
    return lista

def primosGemelosAux(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        return "La entrada debe ser unicamente numeros enteros mayores a 2"
    if num2 <= num1:
        return "El primer numero debe ser menor al segundo"
    if num1 < 2 or num2 < 2:
        return "La entrada debe ser numeros enteros mayores a 2"
    else:
        return primosGemelos(num1, num2)
print("Reto 3")
print(primosGemelosAux(2,20))
#---------------Reto4------------------
def tuplasPrimos(matriz):
    contador1 =0
    contador2 =0
    lista =[]
    for i in matriz:
        contador1 +=1
        for j in i:
            contador2+=1
            if esPrimo(j) == True:
                tupla = (contador1,contador2)
                lista.append(tupla)
        contador2=0
    return lista

def tuplasAux(matriz):
    if len(matriz)!=len(matriz[0]):
        return "No es una matriz cuadrada"
    else:
        return tuplasPrimos(matriz)

def tuplasPrimosES(matriz):
    #matriz = input("Ingrese una matriz")
    return tuplasAux(matriz)

print("Reto 4")
matriz = [[7,8,9],[10,11,13]]
print("Para la entrada:",matriz)
print(tuplasPrimosES(matriz))
matriz = [[7,8,9],[10,11,13],[25,50,30]]
print("Para la entrada:",matriz)
print(tuplasPrimosES(matriz))