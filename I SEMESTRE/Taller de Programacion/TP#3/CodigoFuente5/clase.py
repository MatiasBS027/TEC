#Elaborado por Luis Carlos Tinoco y Matías Benavides Sandoval
#fecha de creación 11/06/2025
#última modificación 21/06/2025 20:00
#python versión 3.11.2


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
        Funcionalidad:
        - Constructor que inicializa un objeto Animal con sus atributos principales.

        Entradas:
        - nombreComun: str, nombre común del animal.
        - nombreCientifico: str, nombre científico del animal.
        - url: str, URL de la imagen del animal.
        - orden: str, orden del animal ('c', 'h', 'o').

        Salidas:
        - No retorna valor. Inicializa los atributos del objeto.
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
        Funcionalidad:
        - Crea un ID basado en la primera y última letra del nombre común y un número secuencial.

        Entradas:
        - nombre: str, nombre común del animal.

        Salidas:
        - Retorna un string con el ID generado.
        """
        nombre = nombre.strip().lower()
        primera = nombre[0]
        ultima = nombre[-1]
        codigo = f"{primera}{ultima}{Animal.contadorGlobal:02}"
        Animal.contadorGlobal += 1
        return codigo

    def obtenerId(self):
        """
        Funcionalidad:
        - Retorna el ID del animal.

        Entradas:
        - Ninguna.

        Salidas:
        - Retorna el ID (str).
        """
        return self.__id

    def mostrarId(self):
        """
        Funcionalidad:
        - Muestra el ID del animal por consola.

        Entradas:
        - Ninguna.

        Salidas:
        - No retorna valor. Imprime el ID.
        """
        print(self.__id)

    # =================== Nombres ===================
    def asignarNombres(self, nombreComun, nombreCientifico):
        """
        Funcionalidad:
        - Asigna nuevos nombres al animal.

        Entradas:
        - nombreComun: str, nombre común.
        - nombreCientifico: str, nombre científico.

        Salidas:
        - No retorna valor. Actualiza los nombres.
        """
        self.__nombres = (nombreComun, nombreCientifico)

    def obtenerNombres(self):
        """
        Funcionalidad:
        - Retorna la tupla de nombres del animal.

        Entradas:
        - Ninguna.

        Salidas:
        - Retorna una tupla (nombreComun, nombreCientifico).
        """
        return self.__nombres

    def mostrarNombres(self):
        """
        Funcionalidad:
        - Muestra los nombres del animal por consola.

        Entradas:
        - Ninguna.

        Salidas:
        - No retorna valor. Imprime los nombres.
        """
        print(self.__nombres[0])
        print(self.__nombres[1])

    # =================== URL ===================
    def asignarUrl(self, nuevaUrl):
        """
        Funcionalidad:
        - Actualiza la URL de la imagen del animal.

        Entradas:
        - nuevaUrl: str, nueva URL.

        Salidas:
        - No retorna valor. Actualiza la URL.
        """
        self.__url = nuevaUrl

    def obtenerUrl(self):
        """
        Funcionalidad:
        - Retorna la URL de la imagen del animal.

        Entradas:
        - Ninguna.

        Salidas:
        - Retorna la URL (str).
        """
        return self.__url

    def mostrarUrl(self):
        """
        Funcionalidad:
        - Muestra la URL de la imagen por consola.

        Entradas:
        - Ninguna.

        Salidas:
        - No retorna valor. Imprime la URL.
        """
        print(self.__url)

    # =================== Estado ===================
    def asignarEstadoAleatorio(self):
        """
        Funcionalidad:
        - Asigna un estado aleatorio entre 1 y 5 al animal.

        Entradas:
        - Ninguna.

        Salidas:
        - No retorna valor. Modifica el estado.
        """
        import random
        self.__info[0] = random.randint(1, 5)

    def obtenerEstado(self):
        """
        Funcionalidad:
        - Retorna el estado actual del animal.

        Entradas:
        - Ninguna.

        Salidas:
        - Retorna el estado (int).
        """
        return self.__info[0]

    def mostrarEstado(self):
        """
        Funcionalidad:
        - Muestra el estado del animal por consola.

        Entradas:
        - Ninguna.

        Salidas:
        - No retorna valor. Imprime el estado.
        """
        print(self.__info[0])

    # =================== Calificación ===================
    def asignarCalificacion(self, valor):
        """
        Funcionalidad:
        - Asigna una calificación al animal, validando según el estado.

        Entradas:
        - valor: int, calificación a asignar.

        Salidas:
        - No retorna valor. Modifica la calificación si es válida.
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
        """
        Funcionalidad:
        - Retorna la calificación del animal.

        Entradas:
        - Ninguna.

        Salidas:
        - Retorna la calificación (int).
        """
        return self.__info[1]

    def mostrarCalificacion(self):
        """
        Funcionalidad:
        - Muestra la calificación del animal por consola.

        Entradas:
        - Ninguna.

        Salidas:
        - No retorna valor. Imprime la calificación.
        """
        print(self.__info[1])

    # =================== Orden y Peso ===================
    def asignarOrdenYPeso(self, orden):
        """
        Funcionalidad:
        - Asigna el orden y un peso aleatorio al animal según su tipo.

        Entradas:
        - orden: str, tipo de orden ('c', 'h', 'o').

        Salidas:
        - No retorna valor. Modifica el orden y el peso.
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
        """
        Funcionalidad:
        - Retorna el orden y el peso del animal.

        Entradas:
        - Ninguna.

        Salidas:
        - Retorna una tupla (orden, peso).
        """
        return self.__info[2], self.__info[3]

    def mostrarOrdenYPeso(self):
        """
        Funcionalidad:
        - Muestra el orden y el peso del animal por consola.

        Entradas:
        - Ninguna.

        Salidas:
        - No retorna valor. Imprime el orden y el peso.
        """
        print(self.__info[2])
        print(self.__info[3])

    # =================== Todo el objeto ===================
    def obtenerDatos(self):
        """
        Funcionalidad:
        - Devuelve todos los atributos del objeto en una lista.

        Entradas:
        - Ninguna.

        Salidas:
        - Retorna una lista con los datos del animal.
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
        Funcionalidad:
        - Muestra todos los atributos del animal por consola.

        Entradas:
        - Ninguna.

        Salidas:
        - No retorna valor. Imprime todos los datos.
        """
        self.mostrarId()
        self.mostrarNombres()
        self.mostrarUrl()
        self.mostrarEstado()
        self.mostrarCalificacion()
        self.mostrarOrdenYPeso()

    def asignarEstado(self, estado):
        """
        Funcionalidad:
        - Asigna un estado específico al animal.

        Entradas:
        - estado: int, nuevo estado.

        Salidas:
        - No retorna valor. Modifica el estado.
        """
        self.__info[0] = estado

    def asignarPeso(self, peso):
        """
        Funcionalidad:
        - Asigna un peso específico al animal.

        Entradas:
        - peso: float, nuevo peso.

        Salidas:
        - No retorna valor. Modifica el peso.
        """
        self.__info[3]