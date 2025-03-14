# Elaborado por: Matias Benavides
# Fecha de creacion: 13/3/2025 6:30pm
# Fecha de ultima modificacion: 13/3/2025 7:29pm
# Version de Python: 3.13.2

def obtenerNumEmpleados(psueldo, pnumDelEmpleado, pmayorSueldo, pnumDelEmpleadoM):
    '''
    Funcionamiento: Compara y actualiza el mayor sueldo entre los empleados
    Entradas:
    -pnumEmpleados(int): Numero de empleados
    -psueldo(int): Sueldo del empleado actual
    -pi(int): Contador actual
    -pnumDelEmpleado(int): Numero del empleado actual
    -pmayorSueldo(int): Mayor sueldo encontrado hasta el momento
    -pnumDelEmpleadoM(int): Numero del empleado con mayor sueldo
    Salidas:
    -str: Mensaje indicando el empleado con mayor sueldo y el monto
    '''
    if psueldo > pmayorSueldo:             # Compara el sueldo actual con el mayor
        pmayorSueldo = psueldo             # Actualiza el mayor sueldo
        pnumDelEmpleadoM = pnumDelEmpleado # Actualiza el número del empleado
    
    return ("" + str(pnumDelEmpleadoM) + "es el codigo del empleado con el mayor sueldo de: $" + str(pmayorSueldo))

def obtenerNumEmpleadosAux(psueldo, pnumDelEmpleado, pmayorSueldoM, pnumDelEmpleadoM):
    '''
    Funcionamiento: Valida los datos de entrada antes de procesarlos
    Entradas:
    -pnumEmpleados(int): Numero total de empleados
    -psueldo(int): Sueldo del empleado actual
    -pi(int): Contador actual
    -pnumDelEmpleado(int): Numero del empleado actual
    -pmayorSueldoM(int): Mayor sueldo encontrado hasta el momento
    -pnumDelEmpleadoM(int): Numero del empleado con mayor sueldo
    Salidas:
    -str: Mensaje de error si los datos son inválidos o el resultado del proceso
    '''
    # Verifica que todos los parámetros sean enteros
    if type(psueldo) != int or type(pnumDelEmpleado) != int or type(pmayorSueldoM) != int or type(pnumDelEmpleadoM) != int:
        return "Los cinco numeros deben ser enteros"
    # Verifica que los números sean positivos
    elif psueldo <= 0:
        return "Los numeros deben ser mayores a 0"
    else:
        # Llama a la función principal con los parámetros validados
        return obtenerNumEmpleados(psueldo, pnumDelEmpleado, pmayorSueldoM, pnumDelEmpleadoM)

def obtenerNumEmpleadosES():
    '''
    Funcionamiento: Maneja la entrada de datos por consola y el ciclo principal
    Entradas:
    -No recibe parámetros, obtiene datos por input()
    Salidas:
    -str: Mensaje de error si hay datos inválidos o el resultado del proceso
    '''
    try:
        numEmpleados = int(input("Ingrese el numero de empleados: "))
        mayorSueldo = 0
        numDelEmpleadoM = 0
        i = 1
        for i in range(numEmpleados):
            numDelEmpleado = int(input(f"Ingrese el numero del empleado "+ str(i+1)+ ": "))
            sueldo = int(input(f"Ingrese el sueldo del empleado"+ str(i+1)+": $"))
                
    except ValueError:
        return "Los datos deben ser numeros enteros"
    else:
        return obtenerNumEmpleadosAux(sueldo, numDelEmpleado, mayorSueldo, numDelEmpleadoM)

# Inicia la ejecución del programa
print(obtenerNumEmpleadosES())  # Imprime el resultado

