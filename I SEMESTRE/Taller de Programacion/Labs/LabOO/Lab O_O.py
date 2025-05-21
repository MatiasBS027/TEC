#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 20/05/2025
#última modificación 20/05/2025 20:00
#python versión 3.13.2

class personalidad:
    def __init__(self):
        self.nombre= ""
        self.Cedula= ""
        self.cateYPerso= ""
        self.profesion= ""
        self.estado= ""

    def asignarNombre(self,pnombre):
        self.nombre= pnombre
        return self.nombre
    def asignarCedula(self,pCedula):
        self.Cedula= pCedula
        return self.Cedula
    def asignarCateYPerso(self,pcateYPerso):
        self.cateYPerso= pcateYPerso
        return self.cateYPerso
    def asignarProfesion(self,pprofesion):
        self.profesion= pprofesion
        return self.profesion
    def asignarEstado(self,pestado):
        self.estado= pestado
        return self.estado
    

    def obtenerNombre(self):
        return self.nombre
    def obtenerCedula(self):
        return self.Cedula
    def obtenerCateYPerso(self):
        return self.cateYPerso
    def obtenerProfesion(self):
        return self.profesion
    def obtenerEstado(self):
        return self.estado
    
    def indicarDatos(self):
        return "Su nombre: "+self.nombre,"Número de cedula: "+ self.Cedula,"Categoria: "+ self.cateYPerso,"Profesión: "+ self.profesion,"Estado: "+  self.estado

