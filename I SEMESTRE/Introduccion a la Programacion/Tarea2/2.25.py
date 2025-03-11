# Elaborado por: Matias Benavides
# Fecha de creacion: 11/3/2025 11:50am
# Fecha de ultima modificacion: 11/3/2025 12:11am
# Version de Python: 3.13.2

def determinarNumero(pa,pb,pc):

    if pa>pb:
        if pa>pc:
            return "a es el mayor"
        else:
            if pa==pc:
                return "a y c son los mayores"
            else:
                return "c es el mayor"
    else:
        if pa==pb:    
            if pa>pc:
                return "a y b son los mayores"
            else:
                if pa==pc:
                    return "a, b y c son iguales"
                else:
                    return "c es el mayor"
        else:
            if pb>pc:
                return "b es el mayor"
            else:
                if pb ==pc:
                    return "b y c son los mayores"
                else:
                    return "c es el mayor"

a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))
c = int(input("Digite el valor de c: "))
print(determinarNumero(a,b,c))
