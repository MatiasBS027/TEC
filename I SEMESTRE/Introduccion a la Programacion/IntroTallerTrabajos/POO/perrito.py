###########################################################
#Elaborado por: XXX
#Fecha de Realización: XX/XX/XXXX XX:XX
#Última actualización: XX/XX/XXXX XX:XX
#Versión: 3.10.2
###########################################################

#Declaración de la clase
class Perro():
    """Definición de Atributos de la clase"""

    """Definición de los métodos de la clase"""
    def __init__(self):
        """
        F: Método constructor = Crea la estructura de la clase perro. Método que se llama al instanciar
        E: Apuntar al campo del objeto en memoria RAM
        S: NA
        """
        self.nombre=""
        self.raza=""
        self.color=0
        self.edad=0
        return

    def asignarNombre(self,pnombre):
        """
        F: Asigna el nombre a una mascota
        E: Apuntar al campo del objeto en memoria RAM, el nombre del perro (string)
        S: NA
        """   
        self.nombre=pnombre
        return 
    
    def asignarRaza(self,praza):
        """
        F: Asigna la raza de la mascota
        E: Apuntar al campo del objeto en memoria RAM, nombre de la raza del perro (string)
        S: NA
        """
        self.raza=praza
        return

    def asignarColor(self,pcolor):
        """
        F: Define el color del pelo del perro
        E: Apuntar al campo del objeto en memoria RAM, el código del color del perro (int)
        S: NA
        """ 
        self.color=pcolor
        return 

    def asignarEdad(self,pedad):
        """
        F: Asigna la Edad de la mascota
        E: Apuntar al campo del objeto en memoria RAM, la edad del perro (int)
        S: NA
        """
        self.edad=pedad
        #¿Será mejor guardar la edad o la fecha de nacimiento?
        return 

    def mostrarNombre(self):
        """
        F: Devuelve sólo el nombre del perro. 
        E: Apuntar al campo del objeto en memoria RAM
        S: Nombre del perro
        """
        return self.nombre
    
    def mostrarRaza(self):
        """
        F: Devuelve sólo el valor guardado en el campo de la raza del perro. 
        E: Apuntar al campo del objeto en memoria RAM
        S: Raza del perro
        """
        return self.raza

    def mostrarColor(self):
        """
        F: Devuelve sólo el valor guardado en el campo del color del perro. 
        E: Apuntar al campo del objeto en memoria RAM
        S: Color del perro
        """
        return self.color

    #...
    
    def indicarDatos(self):
        """
        F: Devuelve todos los datos que se almacenan en el objeto de forma grupal
        E: Apuntar al campo del objeto en memoria RAM
        S: Cada valor asignado a su respectivo campo de memoria
        """
        return self.nombre,self.raza,self.color,self.edad
        #No es conveniente usar la estrategia que se muestra a continuación, debe salir los datos lo más limpio posible. 
        #return "El perro: "+self.nombre+", es de la raza: "+self.raza+",su color de pelaje es:"+self.color+ " y su edad es:"+self.edad

#Definición de funciones
def definirColor(pcolor):
    """
    F: Convierte el código del color a un nombre comprensible para el usuario
    E: Código del color pcolor(int)
    S: Nombre del color (string)
    """
    if pcolor==1:
        return "Negro"
    elif pcolor==2:
        return "Blanco"
    elif pcolor==3:
       return "Gris"
    elif pcolor==4:
        return "Café"
    else:
        return "Combinado"
        
##########################
#######Programa Principal####
##########################
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")    
perrito=Perro() #instaciación de la variable, llama al método init

vnombre=input("Ingrese el nombre del perro: ")
perrito.asignarNombre(vnombre)

vraza=input("Ingrese la raza del perro: ")
perrito.asignarRaza(vraza)

vedad=int(input("Ingrese la edad del perro: ")) #Dato obsoleto, debo pedir fecha de nacimiento
perrito.asignarEdad(vedad)

print("---COLORES DE PELAJE---")
print("1-Negro")
print("2-Blanco")
print("3-Gris")
print("4-Café")
print("5-Combinado")
vcolor=int(input("Digite el número correspondiente al color del pelo: "))
perrito.asignarColor(vcolor)

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Se ha registrado correctamente el perro: ", perrito.mostrarNombre())
print("Todos sus datos son: ")
#print(f"el nombre es: {perrito.indicarDatos()[0]}, su raza: {perrito.indicarDatos()[1]}")
print(f"***El nombre es: {perrito.mostrarNombre()}, su raza: {perrito.mostrarRaza()}, su color es: {definirColor(perrito.mostrarColor())}")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")

perrito2=Perro()#instaciación de la variable, llama al método init

vnombre=input("Ingrese el nombre del perro: ")
perrito2.asignarNombre(vnombre)

vraza=input("Ingrese la raza del perro: ")
perrito2.asignarRaza(vraza)

vedad=int(input("Ingrese la edad del perro: "))
perrito2.asignarEdad(vedad)

print("---COLORES DE PELAJE---")
print("1-Negro")
print("2-Blanco")
print("3-Gris")
print("4-Café")
print("5-Combinado")
vcolor=int(input("Digite el número correspondiente al color del pelo del perro: "))
perrito2.asignarColor(vcolor)

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Se ha registrado correctamente el perro: ", perrito2.mostrarNombre())
print("Todos sus datos son: ")
print(perrito2.indicarDatos())
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
























        
