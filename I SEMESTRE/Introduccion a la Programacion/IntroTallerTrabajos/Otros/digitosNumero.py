
def digitosPares(pnum):
    pares=[]  
    digitos=0
    while pnum!=0:
        digitos=pnum%10
        pnum = pnum//10
        if esPar(digitos)==True:
            pares.append(digitos)
    return(pares)

def esPar(pnum):
    if pnum%2 == 0:
        return True
    else:
        return False

print(digitosPares(1234))

