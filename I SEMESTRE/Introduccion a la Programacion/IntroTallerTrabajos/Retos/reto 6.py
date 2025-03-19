# Elaborado por Tinoco Vargas Luis Carlos
# Fecha de creación: 18/03/2025
# Última modificación: 18/03/2025 19:48
# Python version 3.13

""" En esta función en caso de dar un número con una letra le dice que debe corregir solo con números
y tambien divide con residuos para ir sacando los digitos y compararlos con el mayor"""
def determinarMayor(pnum):
    if not isinstance(pnum, int):
        return "El valor debe ser únicamente entero"
    
    maxDigito = 0
    while pnum != 0:
        digito = pnum % 10
        if digito > maxDigito:
            maxDigito = digito
        pnum = pnum // 10
    
    return maxDigito

# Función auxiliar para validar la entrada
def obtenerValorAux(pn):
    if not isinstance(pn, int):
        return "Debe ingresar un número entero"
    elif pn <= 0:
        return "Debe ingresar un número mayor a 0"
    else:
        return determinarMayor(pn)

# Entrada del usuario
num = input("Digite un número sin letras: ")

# Validar si la entrada es un número entero
if num.isdigit():
    num = int(num)
    print(obtenerValorAux(num))
else:
    print("El valor debe ser únicamente entero")