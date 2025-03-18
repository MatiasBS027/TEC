# Elaborado por: Matias Benavides y Luis Carlos Tinoco Vargas
# Fecha de creacion: 13/3/2025 6:30pm
# Fecha de ultima modificacion: 16/3/2025 7:29pm
# Version de Python: 3.13.2

def obtenerNumEmpleados(psueldo, pnumDelEmpleado, pmayorSueldo, pnumDelEmpleadoM):
    '''
    Funcionamiento: Compara y actualiza el mayor sueldo entre los empleados
    Entradas:
    -psueldo(int): Sueldo del empleado actual
    -pnumDelEmpleado(int): Numero del empleado actual
    -pmayorSueldo(int): Mayor sueldo encontrado hasta el momento
    -pnumDelEmpleadoM(int): Numero del empleado con mayor sueldo
    Salidas:
    -El sueldo y el número del empleado con el mayor sueldo
    '''
    if psueldo > pmayorSueldo:
        return psueldo, pnumDelEmpleado
    return pmayorSueldo, pnumDelEmpleadoM

def obtenerNumEmpleadosAux(psueldo, pnumDelEmpleado, pmayorSueldoM, pnumDelEmpleadoM):
    '''
    Funcionamiento: Valida los datos de entrada antes de procesarlos
    Entradas:
    -psueldo(int): Sueldo del empleado actual
    -pnumDelEmpleado(int): Numero del empleado actual
    -pmayorSueldoM(int): Mayor sueldo encontrado hasta el momento
    -pnumDelEmpleadoM(int): Numero del empleado con mayor sueldo
    Salidas:
    -La función principal con los parámetros validados
    '''
    # Verifica que todos los parámetros sean enteros
    if type(psueldo) != int or type(pnumDelEmpleado) != int:
        return None
    # Verifica que los números sean positivos
    elif psueldo <= 0:
        return None
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
        if numEmpleados <= 0:
            return "El número de empleados debe ser mayor a 0" 
        mayorSueldo = 0
        numDelEmpleadoM = 0
        for i in range(numEmpleados):
            numDelEmpleado = int(input(f"Ingrese el numero del empleado {i+1}: "))
            sueldo = int(input(f"Ingrese el sueldo del empleado {i+1}: $"))
            
            resultado = obtenerNumEmpleadosAux(sueldo, numDelEmpleado, mayorSueldo, numDelEmpleadoM)  # Llama a la función auxiliar para procesar cada empleado
            if resultado is None:
                return "Los datos ingresados son inválidos"
                
            mayorSueldo, numDelEmpleadoM = resultado # Actualiza el mayor sueldo y el número del empleado correspondiente
        return f"{numDelEmpleadoM} es el codigo del empleado con el mayor sueldo de: ${mayorSueldo}" # Retorna el resultado final
    
    except ValueError:
        return "Los datos deben ser numeros enteros"

# Inicia la ejecución del programa
print(obtenerNumEmpleadosES())  # Imprime el resultado