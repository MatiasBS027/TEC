def esPar(pnum):
    if pnum %2 ==0:
        return True
    else:
        return False

def ultimoDigito(pnum):
    ultimo = pnum%10
    while pnum !=0:
        if esPar(ultimo) == True:
            print(ultimo)
    pnum=pnum//10
    return ""
print(ultimoDigito(1234))