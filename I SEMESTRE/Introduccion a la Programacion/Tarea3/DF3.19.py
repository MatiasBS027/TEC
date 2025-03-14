# Elaborado por: Matias Benavides
# Fecha de creacion: 13/3/2025 6:30pm
# Fecha de ultima modificacion: 13/3/2025 7:29pm
# Version de Python: 3.13.2

def obtenerNumEmpleados(pnumEmpleados, psueldo, pi, pnumDelEmpleado, pmayorSueldo, pnumDelEmpleadoM):
    '''
    Funcionamiento: Calcula el empleado con el mayor sueldo
    Entradas:
    -pnumEmpleados(int):Numero de empleados
    -psueldo(int):Sueldo del empleado
    -pi(int):Contador
    -pnumDelEmpleado(int):Numero del empleado
    -pmayorSueldo(int):Mayor sueldo
    Salidas:
    -pnumDelEmpleadoM(int):Numero del empleado con el mayor sueldo
    '''
    while pi <= pnumEmpleados:                  # Itera mientras el contador sea menor o igual al número de empleados
        if psueldo > pmayorSueldo:             # Compara si el sueldo actual es mayor al máximo
            pmayorSueldo = psueldo             # Actualiza el mayor sueldo
            pnumDelEmpleadoM = pnumDelEmpleado # Guarda el número del empleado con mayor sueldo
        pi += 1                                # Incrementa el contador
    return ("" + str(pnumDelEmpleadoM) + " es el empleado con el mayor sueldo de: $" + str(pmayorSueldo))  # Retorna el resultado

def obtenerNumEmpleadosAux(pnumEmpleados, psueldo, pi, pnumDelEmpleado, pmayorSueldoM, pnumDelEmpleadoM):
    '''
    Funcionamiento: Verifica si los datos ingresados son correctos y llama a la función 'obtenerNumEmpleados'
    Entradas:
    -pnumEmpleados(int):Numero de empleados
    -psueldo(int):Sueldo del empleado
    -pi(int):Contador
    -pnumDelEmpleado(int):Numero del empleado
    -pmayorSueldoM(int):Mayor sueldo
    Salidas:
    -obtenerNumEmpleados(pnumEmpleados, psueldo, pi, pnumDelEmpleado, pmayorSueldoM): Llama a la función 'obtenerNumEmpleados'
    '''
    # Verifica que todos los parámetros sean enteros
    if type(pnumEmpleados) != int or type(psueldo) != int or type(pi) != int or type(pnumDelEmpleado) != int or type(pmayorSueldoM) != int or type(pnumDelEmpleadoM) != int:
        return "Los cinco numeros deben ser enteros"
    # Verifica que los números sean positivos
    elif pnumEmpleados <= 0 or psueldo <= 0:
        return "Los numeros deben ser mayores a 0"
    else:
        # Llama a la función principal con los parámetros validados
        return obtenerNumEmpleados(pnumEmpleados, psueldo, pi, pnumDelEmpleado, pmayorSueldoM, pnumDelEmpleadoM)

def obtenerNumEmpleadosES():
    '''
    Funcionamiento: Solicita al usuario que ingrese los datos para calcular el empleado con el mayor sueldo
    Entradas:
    -numEmpleados(int):Numero de empleados
    -numDelEmpleado(int):Numero del empleado
    -sueldo(int):Sueldo del empleado
    Salidas:
    -obtenerNumEmpleadosAux(numEmpleados, sueldo, i, numDelEmpleado): Llama a la función 'obtenerNumEmpleados'
    '''
    try:
        numEmpleados = int(input("Ingrese el numero de empleados: "))  # Solicita número de empleados
        mayorSueldo = 0        # Inicializa el mayor sueldo
        numDelEmpleadoM = 0    # Inicializa el número del empleado con mayor sueldo
        i = 1                  # Inicializa el contador
        
        for i in range(numEmpleados):          # Itera por cada empleado
            # Solicita datos de cada empleado
            numDelEmpleado = int(input(f"Ingrese el numero del empleado {i+1}: "))
            sueldo = int(input(f"Ingrese el sueldo del empleado {i+1}: $"))
            
            if sueldo > mayorSueldo:           # Compara el sueldo actual con el mayor
                mayorSueldo = sueldo           # Actualiza el mayor sueldo
                numDelEmpleadoM = numDelEmpleado  # Actualiza el número del empleado
                
    except ValueError:         # Maneja errores de tipo de dato
        return "Los datos deben ser numeros enteros"
    else:                     # Si no hay errores, llama a la función auxiliar
        return obtenerNumEmpleadosAux(numEmpleados, sueldo, i, numDelEmpleado, mayorSueldo, numDelEmpleadoM)

# Inicia la ejecución del programa
print(obtenerNumEmpleadosES())  # Imprime el resultado

