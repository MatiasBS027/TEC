# Elaborado por: Matias Benavides
# Fecha de creacion: 10/3/2025 7:30pm
# Fecha de ultima modificacion: 10/3/2025 7:51pm
# Version de Python: 3.13.2

matrtricula= (int(input("Ingrese su matrícula: ")))   #Se pide al usuario que digite su matricula
carrera= str(input("Ingrese la carrera a la que desea ingresar: "))   #Se pide al usuario que digite la carrera a la que desea ingresar
semestre= int(input("Ingrese el semestre que cursa: "))   #Se pide al usuario que digite el semestre que cursa
promedio= float(input("Ingrese su promedio: "))   #Se pide al usuario que digite su promedio
#Se imprime la matricula, la carrera y se dice que fue aceptado
#Tener en cuenta las tildes y las mayusculas, por que en el diagrama de flujo original vienen asi
if carrera == "Economía":
    if semestre >= 6 and promedio >= 8.8:
        print("Matrícula: "+str(matrtricula)+"\nCarrera: "+carrera+"\nEstado: ACEPTADO")   
elif carrera == "Computación":
    if semestre > 6 and promedio > 8.5:
        print("Matrícula: "+str(matrtricula)+"\nCarrera: "+carrera+"\nEstado: ACEPTADO")
elif carrera == "Administración":
    if semestre > 5 and promedio > 8.5:
        print("Matrícula: "+str(matrtricula)+"\nCarrera: "+carrera+"\nEstado: ACEPTADO")
elif carrera == "Contabilidad":
    if semestre > 5 and promedio > 8.5: 
        print("Matrícula: "+str(matrtricula)+"\nCarrera: "+carrera+"\nEstado: ACEPTADO")
