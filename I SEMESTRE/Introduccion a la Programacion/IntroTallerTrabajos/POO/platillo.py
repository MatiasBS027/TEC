##Elaborado por: Matias Benavides y Santiago Pacheco

class Platillo():

    def __init__(self):
        self.idPlatillo = ""
        self.nombre = ""
        self.precio = 0
        self.ingredientes = []
        return
    
    def asignarIdPlatillo(self, pidPlatillo):
        self.idPlatillo = pidPlatillo
        return
    def asignarNombre(self, pnombre):
        self.nombre = pnombre
        return
    def asignarPrecio(self, pprecio):
        self.precio = pprecio
        return
    def asignarIngredientes(self, pingredientes):
        self.ingredientes = pingredientes
        return
    def mostrarIdPlatillo(self):
        return self.idPlatillo
    def mostrarNombre(self):
        return self.nombre
    def mostrarPrecio(self):
        return self.precio
    def mostrarIngredientes(self):
        return self.ingredientes
    
    def mostrarPlatillo(self):
        return f"ID: {self.idPlatillo}, Nombre: {self.nombre}, Precio: {self.precio}, Ingredientes: {self.ingredientes}"
    
##########################
#######Programa Principal####
##########################
vueltas = int(input("¿Cuántos platillos desea ingresar? "))
for i in range(vueltas):
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")    
    platillo=Platillo() #instaciación de la variable, llama al método init
    vIdPlatillo=input("Ingrese el ID del platillo: ")
    platillo.asignarIdPlatillo(vIdPlatillo)
    vNombre=input("Ingrese el nombre del platillo: ")
    platillo.asignarNombre(vNombre)
    vPrecio=int(input("Ingrese el precio del platillo (colones): "))
    platillo.asignarPrecio(vPrecio)
    vIngredientes=input("Ingrese los ingredientes del platillo (separados por comas): ")
    platillo.asignarIngredientes(vIngredientes.split(","))

    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"Se ha registrado correctamente el platillo: {platillo.mostrarNombre()}")
    print("Todos sus datos son: ")
    print(f"ID: {platillo.mostrarIdPlatillo()}, Nombre: {platillo.mostrarNombre()}, Precio: {platillo.mostrarPrecio()} colones, Ingredientes: {platillo.mostrarIngredientes()}")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
