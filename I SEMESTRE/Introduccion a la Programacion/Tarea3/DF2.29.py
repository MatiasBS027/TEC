# Elaborado por: Matias Benavides
# Fecha de creacion: 13/3/2025 5:50pm
# Fecha de ultima modificacion: 13/3/2025 6:01pm
# Version de Python: 3.13.2

def costoEnfermedad(ptipoEnfermedad, pedad, pdias):
    '''
    Funionamiento: Calcula el costo total del trato por la enfermedad
    Entradas:
    -ptipoEnfermedad(int):Tipo de enfermedad
    -edad(int):Edad del paciente
    -dias(int):Dias de tratamiento
    Salidas:
    -costoTotal(int): Costo total del tratamiento
    '''
    # Verifica el tipo de enfermedad y calcula el costo total
    if ptipoEnfermedad == 1:
        costoTotal = 25 * pdias
    elif ptipoEnfermedad == 2:
        costoTotal = 16 * pdias
    elif ptipoEnfermedad == 3:
        costoTotal = 20 * pdias
    elif ptipoEnfermedad == 4:
        costoTotal = 32 * pdias
    if pedad >= 14 and pedad <= 22:
        costoTotal = costoTotal * 1.10
    return "El costo total del tratamiento es de: $"+ str(costoTotal) # Retorna el costo total del tratamiento(Al no venir el el diagrama voy a asumir que el costo se da en dolares)

def costoEnfermedadAux(ptipoEnfermedad, pedad, pdias): # Función auxiliar para verificar los tipos de datos
    '''
    Funionamiento: Verifica si los datos ingresados son correctos y llama a la función 'costoEnfermedad'
    Entradas:
    -ptipoEnfermedad(int):Tipo de enfermedad
    -edad(int):Edad del paciente
    -dias(int):Dias de tratamiento
    Salidas:
    -costoEnfermedad(ptipoEnfermedad, pedad, pdias): Llama a la función 'costoEnfermedad'
    '''
    if type(ptipoEnfermedad) != int or type(pedad) != int or type(pdias) != int: # Verifica si los datos ingresados son enteros
        return "Los tres numeros deben ser numeros enteros"
    elif ptipoEnfermedad <=0 or pedad <0 or pdias <=0: # Verifica si los datos ingresados son mayores a 0
        return "Los tres numeros deben ser mayores a 0"
    else:
        return costoEnfermedad(ptipoEnfermedad, pedad, pdias)

def costoEnfermedadES():
    '''
    Funionamiento: Solicita al usuario que ingrese los datos para calcular el costo total del tratamiento
    Entradas:
    -tipoEnfermedad(int):Tipo de enfermedad
    -edad(int):Edad del paciente
    -dias(int):Dias de tratamiento
    Salidas:
    -costoEnfermedad(): Llama a la función 'costoEnfermedadAux'
    '''
    while True:
        try:
            tipoEnfermedad = int(input("¿Cual es el tipo de enfermedad del paciente?:\nEnfermedad /1/2/3/4/:  ")) # Solicita al usuario que ingrese el tipo de enfermedad
            edad = int(input("¿Cual es la edad del paciente?: ")) # Solicita al usuario que ingrese la edad del paciente
            dias = int(input("¿Cuantos dias de tratamiento necesita el paciente?: ")) # Solicita al usuario que ingrese los dias de tratamiento
            break
        except ValueError:
            print("Todos los valores ingresados deben ser números enteros. Por favor, intente de nuevo.")
    
    return print(costoEnfermedadAux(tipoEnfermedad, edad, dias)) # Imprime el resultado de la función 'costoEnfermedad'

costoEnfermedadES() # Llama a la función 'costoEnfermedadES' para ejecutar el programa