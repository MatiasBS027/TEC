def encontrarCero(pnum):
    while pnum !=0:
            digito =pnum%10               
            if digito ==0:
                return "Hay al menos un cero"
            else:
                return "No hay ningun cero"
            pnum//=10

print(encontrarCero(39123))