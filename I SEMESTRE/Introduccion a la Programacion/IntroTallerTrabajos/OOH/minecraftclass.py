#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creacón 22/05/2025
#última actualización 23/05/2025 10:54
#python versión 3.13.2

import random

# ==========================
# Clase padre o superclase
# ==========================
class Herramienta:
    """
    Clase padre: Herramienta
    Atributos: idHerramienta, durabilidad, metal, color
    Metodos: asignar y mostrar cada atributo individualmente
    """
    idsUsados = set()  # Atributo de clase para evitar IDs repetidos

    def __init__(self):
        """
        Inicializa una nueva herramienta con valores por defecto.
        idHerramienta: str, identificador único de la herramienta.
        durabilidad: int, valor de durabilidad de la herramienta.
        metal: str, tipo de metal de la herramienta.
        color: str, color de la herramienta.
        """
        self.idHerramienta = ""
        self.durabilidad = 0
        self.metal = ""
        self.color = ""

    def asignarIdHerramienta(self, idHerramienta):
        """
        Asigna un identificador único a la herramienta.
        Lanza ValueError si el ID ya ha sido usado.
        """
        if idHerramienta in Herramienta.idsUsados:
            raise ValueError("ID repetido.")
        self.idHerramienta = idHerramienta
        Herramienta.idsUsados.add(idHerramienta)

    def mostrarIdHerramienta(self):
        """
        Devuelve el identificador de la herramienta.
        """
        return self.idHerramienta

    def asignarDurabilidad(self):
        """
        Asigna un valor aleatorio de durabilidad entre 0 y 100.
        """
        self.durabilidad = random.randint(0, 100)

    def mostrarDurabilidad(self):
        """
        Devuelve la durabilidad de la herramienta.
        """
        return self.durabilidad

    def asignarMetal(self, metal):
        """
        Asigna el tipo de metal de la herramienta.
        metal: str
        """
        self.metal = metal

    def mostrarMetal(self):
        """
        Devuelve el tipo de metal de la herramienta.
        """
        return self.metal

    def asignarColor(self, color):
        """
        Asigna el color de la herramienta.
        color: str
        """
        self.color = color

    def mostrarColor(self):
        """
        Devuelve el color de la herramienta.
        """
        return self.color

    def mostrarDatosHerramienta(self):
        """
        Devuelve una cadena con todos los datos de la herramienta.
        """
        return {self.mostrarIdHerramienta()}, {self.mostrarDurabilidad()}, {self.mostrarMetal()}, {self.mostrarColor()}


# ==========================
# Clase hija: Arma
# ==========================
class HerramientaArma(Herramienta):
    """
    Clase hija: HerramientaArma
    Hereda de: Herramienta
    Atributos propios: dano, velocidadAtaque
    Metodos propios: asignarDano, mostrarDano, asignarVelocidadAtaque, mostrarVelocidadAtaque
    """
    def __init__(self):
        """
        Inicializa una nueva arma con daño y velocidad de ataque por defecto.
        """
        super().__init__()
        self.dano = 0
        self.velocidadAtaque = 0.0

    def asignarDano(self, dano):
        """
        Asigna el valor de daño del arma.
        dano: int
        """
        self.dano = dano

    def mostrarDano(self):
        """
        Devuelve el daño del arma.
        """
        return self.dano

    def asignarVelocidadAtaque(self, velocidad):
        """
        Asigna la velocidad de ataque del arma.
        velocidad: float
        """
        self.velocidadAtaque = velocidad

    def mostrarVelocidadAtaque(self):
        """
        Devuelve la velocidad de ataque del arma.
        """
        return self.velocidadAtaque

    def mostrarDatosArma(self):
        """
        Devuelve una cadena con todos los datos del arma, incluyendo los heredados.
        """
        return {self.mostrarDatosHerramienta()},{self.mostrarDano()},{self.mostrarVelocidadAtaque()}


# ==========================
# Clase hija: Armadura
# ==========================
class HerramientaArmadura(Herramienta):
    """
    Clase hija: HerramientaArmadura
    Hereda de: Herramienta
    Atributo propio: defensa
    Metodos propios: asignarDefensa, mostrarDefensa
    """
    def __init__(self):
        """
        Inicializa una nueva armadura con defensa por defecto.
        """
        super().__init__()
        self.defensa = 0

    def asignarDefensa(self, defensa):
        """
        Asigna el valor de defensa de la armadura.
        defensa: int
        """
        self.defensa = defensa

    def mostrarDefensa(self):
        """
        Devuelve el valor de defensa de la armadura.
        """
        return self.defensa

    def mostrarDatosArmadura(self):
        """
        Devuelve una cadena con todos los datos de la armadura, incluyendo los heredados.
        """
        return {self.mostrarDatosHerramienta()}, {self.mostrarDefensa()}