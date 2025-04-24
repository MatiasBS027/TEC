#Elaborado por: Matias Benavides
#Fecha de creacion: 23/4/2024 6:00 PM
#Ultima modificacion: 23/4/2024 6:00 PM
# Version de Python: 3.13.2

#Importar librerias
import re 

#----------------Reto 1-------------------
#Definicion de funciones
def diametroVarilla (diametro):
    if diametro == "3":
        diametro = "3/8 pulgadas"
    elif diametro == "4":
        diametro = "1/2 pulgadas"
    elif diametro == "5":
        diametro = "5/8 pulgadas"
    elif diametro == "6":
        diametro = "3/4 pulgadas"
    elif diametro == "8":
        diametro = "1 pulgada"
    return diametro

def fabricacionVarilla (fabricacion):
    if fabricacion == "S":
        fabricacion = "Acero al carbono no soldable a temperatura ambiente." 
    elif fabricacion == "W":
        fabricacion = "Acero al carbono soldablea temperatura ambiente"
    return fabricacion

def aceroVarilla (acero):
    if acero == "40":
        acero = "2800 kgf/cm2"
    elif acero == "60":
        acero = "4200 kgf/cm2"
    elif acero == "70":
        acero = "5000 kgf/cm2" 
    return acero

def nomenclatraVarilla (pcodigo):
    fabricante = pcodigo[:2]
    diametro = diametroVarilla(pcodigo[2])
    fabricacion = fabricacionVarilla(pcodigo[3])
    acero = aceroVarilla(pcodigo[4:])

    return fabricante, diametro, fabricacion, acero

def nomenclatraVarillaAux(pcodigo):
    if not re.match('.{6}', pcodigo):    # Valida longitud exacta de 6 caracteres
        return "Debe indicar 6 valores exactamente"
    if not re.match('[A-Z]{2}', pcodigo[0:2]):     # Valida que los primeros 2 caracteres sean letras mayúsculas
        return "Valores deben ser sólo letras mayúsculas"
    if not re.match('[34568]', pcodigo[2]):    # Valida el diámetro
        return "El diámetro de entrada no es un valor permitido"
    if not re.match('[SW]', pcodigo[3]):     # Valida el proceso de fabricación
        return "Debe indicar el proceso de fabricación S o W"
    if not re.match('(40|60|70)$', pcodigo[4:]):     # Valida el grado de acero
        return "El grado del acero no es un valor permitido"
    
    return nomenclatraVarilla(pcodigo)

def nomenclatraVarillaES (codigo):
        #codigo = str(input("Ingrese el codigo de la varilla: "))
        resultado = nomenclatraVarillaAux(codigo)
        if isinstance(resultado, str):
            return resultado  # Retorna el mensaje de error directamente
        fabricante, diametro, fabricacion, acero = resultado
        return "El fabricante es: " + fabricante + "\nEl diametro de la varilla es: " + diametro + "\nProceso de Fabricación: " + fabricacion + "\nGrados de acero: " + acero

print("\n=== Nomenclatura de una varilla ===")
codigo= "SV5S6"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))
codigo= "SV9S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))
codigo= "SV5S55"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))
codigo= "SV5S60"
print("Para la entrada:",codigo)
print(nomenclatraVarillaES(codigo))