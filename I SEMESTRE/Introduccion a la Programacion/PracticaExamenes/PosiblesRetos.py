# Reto 1: Sumar los dígitos de un número entero no negativo de forma recursiva
# Sumar los dígitos de un número entero no negativo de forma recursiva

def sumaDigitosFila(num):
    if num == 0:
        return 0
    else:
        return sumaDigitosFila(num // 10) + (num % 10)

def sumaDigitosFilaAux(num):
    if not isinstance(num, int) or num < 0:
        return "Ingrese un número entero no negativo."
    return sumaDigitosFila(num)

# Pruebas
print("=== Reto 1 ===")
print(sumaDigitosFilaAux(123))     # 6
print(sumaDigitosFilaAux(40201))   # 7
print(sumaDigitosFilaAux(-5))      # Error
# Reto 2: Contar los dígitos de un número entero no negativo de forma recursiva
# Contar los dígitos de un número entero no negativo de forma recursiva

def contarDigitosCola(num, acumulador=0):
    if num == 0:
        return acumulador
    else:
        return contarDigitosCola(num // 10, acumulador + 1)

def contarDigitosColaAux(num):
    if not isinstance(num, int) or num < 0:
        return "Ingrese un número entero no negativo."
    if num == 0:
        return 1  # El 0 tiene 1 dígito
    return contarDigitosCola(num)

# Pruebas
print("\n=== Reto 2 ===")
print(contarDigitosColaAux(12345))  # 5
print(contarDigitosColaAux(0))      # 1
print(contarDigitosColaAux(-9))     # Error

# Reto 3: Crear una clase Libro con atributos y métodos para manejar libros
# La clase debe permitir asignar título, autor, número de páginas y estado (dispon
class Libro:
    """
    Clase para representar un libro con título, autor, número de páginas y estado.

    Atributos:
    - titulo (str)
    - autor (str)
    - paginas (int)
    - estado (str): 'Disponible' o 'Prestado'
    """
    
    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.paginas = 0
        self.estado = None

    def asignarTitulo(self, ptitulo):
        self.titulo = ptitulo
        return
    
    def asignarAutor(self, pautor):
        self.autor = pautor
        return

    def asignarPaginas(self, ppaginas):
        self.paginas = ppaginas
        return
    
    def asignarEstado(self, pestado):
        self.estado = pestado
        return

    def mostrarTitulo(self):
        return self.titulo
    
    def mostrarAutor(self):
        return self.autor
    
    def mostrarPaginas(self):
        return self.paginas
    
    def mostrarEstado(self):
        return self.estado

    def indicarDatos(self):
        return self.titulo, self.autor, self.paginas, self.estado

# Pruebas
print("=== Reto 3 ===")
libro1 = Libro()
libro1.asignarTitulo("Crónica de una muerte anunciada")
libro1.asignarAutor("Gabriel García Márquez")
libro1.asignarPaginas(120)
libro1.asignarEstado("Disponible")

print("Título:", libro1.mostrarTitulo())
print("Autor:", libro1.mostrarAutor())
print("Páginas:", libro1.mostrarPaginas())
print("Estado:", libro1.mostrarEstado())
print("Todos los datos:", libro1.indicarDatos())
# Reto 4: Duplicar los números impares de una lista
# Duplicar los números impares de una lista recursivamente
def duplicarImpares(lista):
    if not lista:
        return []
    if lista[0] % 2 == 1:
        return [lista[0], lista[0]] + duplicarImpares(lista[1:])
    else:
        return [lista[0]] + duplicarImpares(lista[1:])

# Pruebas
print("=== Reto 5 ===")
print(duplicarImpares([1, 2, 3, 4]))          # [1, 1, 2, 3, 3, 4]
print(duplicarImpares([2, 4, 6]))             # [2, 4, 6]
print(duplicarImpares([1, 1, 1]))             # [1, 1, 1, 1, 1, 1]
print(duplicarImpares([]))                   # []

# Reto 5: Contar los dígitos múltiplos de 3 de un número entero no negativo
# Contar los dígitos múltiplos de 3 de un número entero no negativo
def contarMultiplosDe3(num, contador=0):
    if num == 0:
        return contador
    digito = num % 10
    if digito % 3 == 0:
        return contarMultiplosDe3(num // 10, contador + 1)
    else:
        return contarMultiplosDe3(num // 10, contador)

def contarMultiplosDe3Aux(num):
    if not isinstance(num, int) or num < 0:
        return "Debe ingresar un número entero no negativo."
    return contarMultiplosDe3(num)

# Pruebas
print("=== Reto 1 ===")
print(contarMultiplosDe3Aux(9364))    # 2
print(contarMultiplosDe3Aux(13579))   # 1
print(contarMultiplosDe3Aux(222))     # 0


# Reto 6: Eliminar de una lista todos los números mayores a un valor dado
# Eliminar de una lista todos los números mayores a un valor dado de forma recursiva
def eliminarMayoresA(n, lista):
    if not lista:
        return []
    if lista[0] > n:
        return eliminarMayoresA(n, lista[1:])
    else:
        return [lista[0]] + eliminarMayoresA(n, lista[1:])

# Pruebas
print("\n=== Reto 2 ===")
print(eliminarMayoresA(5, [3, 9, 5, 1, 7]))     # [3, 5, 1]
print(eliminarMayoresA(2, [1, 2, 3, 4]))        # [1, 2]
print(eliminarMayoresA(10, [20, 30, 5]))        # [5]

# Reto 7: Sumar todos los enteros de una lista, incluyendo listas anidadas
# Sumar todos los enteros de una lista, incluyendo listas anidadas de forma rec
def sumarEnteros(lista):
    if not lista:
        return 0
    if isinstance(lista[0], int):
        return lista[0] + sumarEnteros(lista[1:])
    elif isinstance(lista[0], list):
        return sumarEnteros(lista[0]) + sumarEnteros(lista[1:])
    else:
        return sumarEnteros(lista[1:])

def sumarEnterosAux(lista):
    if not isinstance(lista, list):
        return "Entrada inválida."
    return sumarEnteros(lista)

# Pruebas
print("\n=== Reto 3 ===")
print(sumarEnterosAux([[1, 2], 3, [4, [5, "hola"]]]))   # 15
print(sumarEnterosAux([["a", 5], [10]]))                # 15
print(sumarEnterosAux([]))                              # 0

# Reto 8: Crear una clase Vehiculo con atributos y métodos para manejar vehículos
# La clase debe permitir asignar marca, modelo, año y estado (activo o inactivo
class Vehiculo:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.anio = 0
        self.estado = ""

    def asignarMarca(self, pmarca):
        self.marca = pmarca
        return

    def asignarModelo(self, pmodelo):
        self.modelo = pmodelo
        return

    def asignarAnio(self, panio):
        self.anio = panio
        return

    def asignarEstado(self, pestado):
        self.estado = pestado
        return

    def mostrarMarca(self):
        return self.marca

    def mostrarModelo(self):
        return self.modelo

    def mostrarAnio(self):
        return self.anio

    def mostrarEstado(self):
        return self.estado

    def indicarDatos(self):
        return self.marca, self.modelo, self.anio, self.estado

# Pruebas
print("\n=== Reto 4 ===")
carro = Vehiculo()
carro.asignarMarca("Toyota")
carro.asignarModelo("Corolla")
carro.asignarAnio(2022)
carro.asignarEstado("Activo")
print("Marca:", carro.mostrarMarca())
print("Modelo:", carro.mostrarModelo())
print("Año:", carro.mostrarAnio())
print("Estado:", carro.mostrarEstado())
print("Todos los datos:", carro.indicarDatos())
