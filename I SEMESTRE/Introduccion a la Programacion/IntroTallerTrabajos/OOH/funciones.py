#Elaborado por Luis Tinoco y Matías Benavides
#Fecha de creacón 22/05/2025
#última actualización 23/05/2025 10:54
#python versión 3.13.2

from minecraftclass import HerramientaArma, HerramientaArmadura

# ==========================
# Validaciones
# ==========================

def validarMetal(metal):
    """
    Valida si el metal es uno de los permitidos: oro, diamante o hierro.
    metal: str
    return: bool
    """
    return metal.lower() in ["oro", "diamante", "hierro"]

def validarColor(color):
    """
    Valida si el color es uno de los permitidos: azul, amarillo o gris.
    color: str
    return: bool
    """
    return color.lower() in ["azul", "amarillo", "gris"]

def validarDano(dano):
    """
    Valida si el daño está dentro de los valores permitidos: 7, 8 o 9.
    dano: int
    return: bool
    """
    return dano in [7, 8, 9]

def validarVelocidad(velocidad):
    """
    Valida si la velocidad está dentro del rango permitido: 0.1 a 0.3.
    velocidad: float
    return: bool
    """
    return 0.1 <= velocidad <= 0.3

def validarDefensa(defensa):
    """
    Valida si la defensa está dentro de los valores permitidos: 4, 5 o 6.
    defensa: int
    return: bool
    """
    return defensa in [4, 5, 6]

# ==========================
# Crear objetos de clase hija HerramientaArma
# ==========================

def crearArma(idHerramienta, metal, color, dano, velocidad):
    """
    Crea un objeto de tipo HerramientaArma con los parámetros dados.
    Valida cada atributo antes de asignarlo.
    idHerramienta: str
    metal: str
    color: str
    daño: int
    velocidad: float
    return: HerramientaArma
    Lanza ValueError si algún atributo no es válido.
    """
    arma = HerramientaArma()
    arma.asignarIdHerramienta(idHerramienta)
    arma.asignarDurabilidad()

    if validarMetal(metal):
        arma.asignarMetal(metal)
    else:
        raise ValueError("Metal invalido.")

    if validarColor(color):
        arma.asignarColor(color)
    else:
        raise ValueError("Color invalido.")

    if validarDano(dano):
        arma.asignarDano(dano)
    else:
        raise ValueError("Daño invalido.")

    if validarVelocidad(velocidad):
        arma.asignarVelocidadAtaque(velocidad)
    else:
        raise ValueError("Velocidad invalida.")

    return arma

# ==========================
# Crear objetos de clase hija HerramientaArmadura
# ==========================

def crearArmadura(idHerramienta, metal, color, defensa):
    """
    Crea un objeto de tipo HerramientaArmadura con los parámetros dados.
    Valida cada atributo antes de asignarlo.
    idHerramienta: str
    metal: str
    color: str
    defensa: int
    return: HerramientaArmadura
    Lanza ValueError si algún atributo no es válido.
    """
    armadura = HerramientaArmadura()
    armadura.asignarIdHerramienta(idHerramienta)
    armadura.asignarDurabilidad()

    if validarMetal(metal):
        armadura.asignarMetal(metal)
    else:
        raise ValueError("Metal invalido.")

    if validarColor(color):
        armadura.asignarColor(color)
    else:
        raise ValueError("Color invalido.")

    if validarDefensa(defensa):
        armadura.asignarDefensa(defensa)
    else:
        raise ValueError("Defensa invalida.")

    return armadura

# ==========================
# Mostrar cualquier objeto
# ==========================

def mostrarObjeto(objeto):
    """
    Muestra los datos de un objeto, ya sea HerramientaArma o HerramientaArmadura.
    objeto: instancia de HerramientaArma o HerramientaArmadura
    """
    if isinstance(objeto, HerramientaArma):
        print("Tipo: Arma")
        print(f"ID: {objeto.mostrarIdHerramienta()}")
        print(f"Durabilidad: {objeto.mostrarDurabilidad()}")
        print(f"Metal: {objeto.mostrarMetal()}")
        print(f"Color: {objeto.mostrarColor()}")
        print(f"Daño: {objeto.mostrarDano()}")
        print(f"Velocidad de ataque: {objeto.mostrarVelocidadAtaque()}")
    
    elif isinstance(objeto, HerramientaArmadura):
        print("Tipo: Armadura")
        print(f"ID: {objeto.mostrarIdHerramienta()}")
        print(f"Durabilidad: {objeto.mostrarDurabilidad()}")
        print(f"Metal: {objeto.mostrarMetal()}")
        print(f"Color: {objeto.mostrarColor()}")
        print(f"Defensa: {objeto.mostrarDefensa()}")
    
    else:
        print(">> Objeto desconocido.")
