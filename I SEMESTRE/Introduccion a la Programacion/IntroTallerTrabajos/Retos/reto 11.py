def convertirBinario(pbinario, pdecimal):
    
    potencia = len(pbinario) - 1 # Calculamos la potencia inicial (longitud - 1)
    for digito in pbinario: # Recorremos cada dígito del número binario de izquierda a derecha
        if digito == '1': # Si el dígito es '1', sumamos 2 elevado a la potencia actual
            pdecimal += (2 ** potencia)
        potencia -= 1 # Reducimos la potencia en cada iteración
    return pdecimal

# Solicitar número binario al usuario
decimal = 0
binario = str(input("Digite un número binario: "))
resultado = convertirBinario(binario, decimal)
print(f"El número binario {binario} en decimal es: {resultado}")