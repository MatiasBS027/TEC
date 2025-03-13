# Elaborado por: Matias Benavides
# Fecha de creacion: 11/3/2025 11:50am
# Fecha de ultima modificacion: 11/3/2025 12:11am
# Version de Python: 3.13.2

def determinarNumero(pa, pb, pc):
    '''
    Funionamiento: Calcula cual de los tres numeros es el mayor
    Entradas:
    -pa(float):Numero a evaluar
    -pb(float):Numero a evaluar 
    -pc(float):Numero a evaluar
    Salidas:
    -a es el mayor(str): Si a es el mayor
    -b es el mayor(str): Si b es el mayor
    -c es el mayor(str): Si c es el mayor
    -cualquier combinacion de los anteriores(str): Si hay empate
    '''

    if pa > pb: # Compara si 'a' es mayor que 'b'
        if pa > pc: # Si 'a' es mayor que 'b', verifica si 'a' es mayor que 'c'
            return "a es el mayor"
        else:
            if pa == pc: # Si 'a' es igual a 'c', ambos son los mayores
                return "a y c son los mayores"
            else:
                return "c es el mayor"
    else:
        if pa == pb: # Si 'a' es igual a 'b', verifica si 'a' es mayor que 'c'
            if pa > pc:
                return "a y b son los mayores"
            else:
                if pa == pc: # Si 'a' es igual a 'c', todos son iguales
                    return "a, b y c son iguales"
                else:
                    return "c es el mayor"
        else:
            if pb > pc: # Si 'b' es mayor que 'c', 'b' es el mayor
                return "b es el mayor"
            else:
                if pb == pc: # Si 'b' es igual a 'c', ambos son los mayores
                    return "b y c son los mayores"
                else:
                    return "c es el mayor"

def determinarNumeroAUX(pa, pb, pc):
    if type(pa) != float or type(pb) != float or type(pc) != float:
        return "Los tres numeros deben ser numeros flotantes"
    elif pa <=0.0 or pb <=0.0 or pc <=0.0:
        return "Los tres numeros deben ser mayores a 0"
    else:
        return determinarNumero(pa,pb,pc)

def determinarNumeroES():
    # Solicita al usuario que ingrese los valores de 'a', 'b' y 'c'
    a = float(input("Digite el valor de a: "))
    b = float(input("Digite el valor de b: "))
    c = float(input("Digite el valor de c: "))
    # Imprime el resultado de la función 'determinarNumero'
    return print(determinarNumeroAUX(a, b, c))    
determinarNumeroES()
