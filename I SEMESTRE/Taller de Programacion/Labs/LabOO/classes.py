class personalidad:
    def __init__(self):
        self.name = ()
        self.cedula = ""
        self.personalidades = []
        self.profesion = ""
        self.estado = True

    def asignarName(self,pname):
        self.name = pname
        return
    def asignarCedula(self,pcedula):
        self.cedula = pcedula
        return
    def asignarPersonalidad(self,ppersonalidad):
        self.personalidades = ppersonalidad
        return
    def asignarProfesion(self,pprofesion):
        self.profesion = pprofesion
        return
    def asignarEstado(self,pestado):
        self.estado = pestado
        return
    
    def mostrarName(self):
        return self.name
    def mostrarCedula(self):
        return self.cedula
    def mostrarPersonalidad(self):
        return self.personalidades
    def mostrarProfesion(self):
        return self.profesion
    def mostrarEstado(self):
        return self.estado

