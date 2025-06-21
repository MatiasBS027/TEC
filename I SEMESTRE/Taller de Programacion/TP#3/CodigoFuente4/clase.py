#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 11/06/2025
#última modificación 21/06/2025 20:00
#python versión 3.13.2


"""
Clase Animal que representa un objeto del inventario del zoológico.
Cada animal posee:
- Un ID único basado en su nombre común.
- Una tupla con su nombre común y nombre científico.
- Una URL con la imagen del animal.
- Una lista con información adicional: estado, calificación, orden y peso.
"""

class Animal:
    contadorGlobal = 1  # Atributo de clase para llevar la secuencia de IDs

    def __init__(self, nombreComun, nombreCientifico, url, orden):
        """
        Constructor que inicializa un objeto Animal.
        Se le asigna automáticamente:
        - Un ID según la convención: primera y última letra del nombre + número secuencial.
        - Un estado aleatorio (entre 1 y 5).
        - Un peso aleatorio según el orden del animal.
        """
        self.__id = self.crearId(nombreComun)
        self.__nombres = (nombreComun, nombreCientifico)
        self.__url = url
        self.__info = [0, 1, '', 0.0]  # [estado, calificación, orden, peso]
        self.asignarEstadoAleatorio()
        self.asignarOrdenYPeso(orden)

    # =================== ID ===================
    def crearId(self, nombre):
        """
        Crea un ID basado en la primera y última letra del nombre común,
        más un número secuencial no repetido.
        """
        nombre = nombre.strip().lower()
        primera = nombre[0]
        ultima = nombre[-1]
        codigo = f"{primera}{ultima}{Animal.contadorGlobal:02}"
        Animal.contadorGlobal += 1
        return codigo

    def obtenerId(self):
        return self.__id

    def mostrarId(self):
        print(self.__id)

    # =================== Nombres ===================
    def asignarNombres(self, nombreComun, nombreCientifico):
        """
        Asigna una nueva tupla de nombres al animal.
        """
        self.__nombres = (nombreComun, nombreCientifico)

    def obtenerNombres(self):
        return self.__nombres

    def mostrarNombres(self):
        print(self.__nombres[0])
        print(self.__nombres[1])

    # =================== URL ===================
    def asignarUrl(self, nuevaUrl):
        """
        Actualiza la URL de la imagen del animal.
        """
        self.__url = nuevaUrl

    def obtenerUrl(self):
        return self.__url

    def mostrarUrl(self):
        print(self.__url)

    # =================== Estado ===================
    def asignarEstadoAleatorio(self):
        """
        Asigna un estado aleatorio entre 1 y 5 al animal:
        1=vivo, 2=enfermo, 3=trasladado, 4=muerto en museo, 5=muerto
        """
        import random
        self.__info[0] = random.randint(1, 5)

    def obtenerEstado(self):
        return self.__info[0]

    def mostrarEstado(self):
        print(self.__info[0])

    # =================== Calificación ===================
    def asignarCalificacion(self, valor):
        """
        Asigna una calificación del usuario, si es válida según el estado:
        1=No marcado, 2=Me gusta, 3=Favorito, 4=Me entristece, 5=Me enoja
        Restricciones:
        - 4 solo si estado es 2 (enfermo) o 5 (muerto)
        - 5 solo si estado es 3 (trasladado)
        """
        estado = self.__info[0]
        if valor == 4 and estado not in [2, 5]:
            print("Solo puedes marcar 'me entristece' si está enfermo o muerto.")
            return
        if valor == 5 and estado != 3:
            print("Solo puedes marcar 'me enoja' si fue trasladado.")
            return
        if valor < 1 or valor > 5:
            print("Calificación no válida.")
            return
        self.__info[1] = valor

    def obtenerCalificacion(self):
        return self.__info[1]

    def mostrarCalificacion(self):
        print(self.__info[1])

    # =================== Orden y Peso ===================
    def asignarOrdenYPeso(self, orden):
        """
        Asigna el orden del animal y su peso estimado:
        - 'h' (herbívoros): entre 80.0 y 100.0 kg
        - 'c' o 'o' (carnívoros u omnívoros): entre 0.0 y 80.0 kg
        """
        import random
        orden = orden.lower()
        if orden not in ['c', 'h', 'o']:
            print("Orden debe ser 'c', 'h' u 'o'.")
            return
        self.__info[2] = orden
        if orden == 'h':
            self.__info[3] = round(random.uniform(80.0, 100.0), 2)
        else:
            self.__info[3] = round(random.uniform(0.0, 80.0), 2)

    def obtenerOrdenYPeso(self):
        return self.__info[2], self.__info[3]

    def mostrarOrdenYPeso(self):
        print(self.__info[2])
        print(self.__info[3])

    # =================== Todo el objeto ===================
    def obtenerDatos(self):
        """
        Devuelve todos los atributos del objeto en una lista.
        Orden: id, nombre común, nombre científico, url, estado, calificación, orden, peso
        """
        return [
            self.__id,
            self.__nombres[0],
            self.__nombres[1],
            self.__url,
            self.__info[0],
            self.__info[1],
            self.__info[2],
            self.__info[3]
        ]

    def mostrarDatos(self):
        """
        Muestra en consola todos los atributos del objeto.
        """
        self.mostrarId()
        self.mostrarNombres()
        self.mostrarUrl()
        self.mostrarEstado()
        self.mostrarCalificacion()
        self.mostrarOrdenYPeso()

    def asignarEstado(self, estado):
        self.__info[0] = estado

    def asignarPeso(self, peso):
        self.__info[3]