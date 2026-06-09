# KNN_ANALYSIS.md

## 1. Objetivo tecnico
La tarea pide implementar KNN en wxMaxima sobre un dataset con registros de la forma:

```text
[id, [x1, x2, ..., xn, y]]
```

Donde:
- `id` es un identificador simbolico.
- `x1 ... xn` son atributos predictivos.
- `y` es la variable objetivo numerica.

El algoritmo requerido no es clasificacion, sino regresion: la salida final es un valor numerico obtenido a partir de los `k` vecinos mas cercanos.

## 2. Contrato de las funciones

### `ide(dat)`
Devuelve el identificador del registro.

Si `dat = [a, [5,1,0,300]]`, entonces:
- `ide(dat) = a`

### `xs(dat)`
Devuelve la lista de atributos predictivos, excluyendo el identificador y la variable objetivo.

Si `dat = [a, [5,1,0,300]]`, entonces:
- `xs(dat) = [5,1,0]`

### `ys(dat)`
Devuelve la variable objetivo del registro.

Si `dat = [a, [5,1,0,300]]`, entonces:
- `ys(dat) = 300`

### `distancia(x1,x2)`
Calcula la distancia entre dos vectores de la misma dimensionalidad.

La formula compatible con los ejemplos es la distancia Euclidiana:

$$
d(x, z) = \sqrt{\sum_{i=1}^{m}(x_i - z_i)^2}
$$

Donde `m` es la cantidad de atributos comparados.

### `knn(x,k,datos)`
Recibe:
- `x`: vector de consulta.
- `k`: cantidad de vecinos a usar.
- `datos`: lista de registros.

Devuelve la regresion KNN construida a partir de los `k` vecinos mas cercanos a `x`.

## 3. Estructura del dataset
La estructura general es:

```text
[id, [x1, x2, ..., xn, y]]
```

Por tanto:
- La primera posicion es el id.
- El vector interno contiene primero los atributos predictivos.
- El ultimo valor interno es la salida esperada.

Esto se confirma con el primer ejemplo:

```text
[a,[5,1,0,300]]
```

Aqui:
- `id = a`
- `X = [5,1,0]`
- `Y = 300`

## 4. Analisis matematico de los ejemplos

### 4.1 Primer ejemplo: salida 225
Consulta:

```text
x = [4,1,0]
```

Distancias a cada registro:

- a: `sqrt((4-5)^2 + (1-1)^2 + (0-0)^2) = 1`
- b: `sqrt((4-3)^2 + (1-1)^2 + (0-1)^2) = sqrt(2)`
- c: `sqrt((4-1)^2 + (1-1)^2 + (0-0)^2) = 3`
- d: `sqrt((4-3)^2 + (1-0)^2 + (0-1)^2) = sqrt(3)`
- e: `sqrt((4-4)^2 + (1-0)^2 + (0-0)^2) = 1`
- f: `sqrt((4-2)^2 + (1-0)^2 + (0-0)^2) = sqrt(5)`

Orden ascendente de vecinos:
- a: 1
- e: 1
- b: sqrt(2)
- d: sqrt(3)
- f: sqrt(5)
- c: 3

#### Caso `k = 3`
Los 3 vecinos mas cercanos son `a`, `e`, `b`.
Sus valores objetivo son:
- 300
- 150
- 225

Promedio simple:

$$
\frac{300 + 150 + 225}{3} = 225
$$

Esto explica la salida del ejemplo.

#### Caso `k = 5`
Los 5 vecinos mas cercanos son `a`, `e`, `b`, `d`, `f`.
Sus valores objetivo son:
- 300
- 150
- 225
- 200
- 50

Promedio simple:

$$
\frac{300 + 150 + 225 + 200 + 50}{5} = 185
$$

Esto explica la segunda salida del ejemplo.

### Conclusión matematica del primer ejemplo
La formula exacta usada por el SPEC es:
1. calcular distancia Euclidiana,
2. ordenar vecinos por distancia ascendente,
3. tomar los `k` primeros,
4. promediar sus valores objetivo.

No hay evidencia de ponderacion por distancia, ni de mediana, ni de suma, ni de otro criterio.

### 4.2 Segundo ejemplo: salida 100
La consulta es un vector de 25 dimensiones que representa una matriz 5x5 aplanada.

El dataset tambien contiene vectores de 25 dimensiones, por lo que la distancia se calcula dimension por dimension sobre toda la lista.

La vecina mas cercana es el registro `a`, cuyo valor objetivo es `100`. Por eso con `k = 1` la salida es:

```text
100
```

Esto confirma que el algoritmo trabaja con dimensionalidad variable y que la salida depende de la variable objetivo del vecino mas cercano.

## 5. Tipo de problema
Este problema es de **regresion** y no de clasificacion.

Justificacion:
- La salida esperada es numerica continua.
- Los ejemplos producen 225 y 185 mediante promedio.
- El tercer ejemplo produce 100 al tomar el valor objetivo del vecino mas cercano.

## 6. Flujo del algoritmo KNN

```text
entrada: x, k, datos

1. Extraer xs e ys de cada registro.
2. Calcular la distancia entre x y cada xs.
3. Asociar cada distancia con su registro original.
4. Ordenar por distancia ascendente.
5. Tomar los primeros k vecinos.
6. Obtener los ys de esos vecinos.
7. Calcular el promedio simple.
8. Retornar el resultado.
```

## 7. Pseudocodigo tecnico

```text
funcion knn(x, k, datos):
    vecinos = []
    para cada dato en datos:
        d = distancia(x, xs(dato))
        agregar (d, ys(dato), dato) a vecinos
    ordenar vecinos por d ascendente
    seleccionar los primeros k elementos
    respuesta = promedio de los ys seleccionados
    retornar respuesta
```

## 8. Complejidad
Sea:
- `n` = numero de registros en `datos`
- `m` = dimensionalidad de `x`

### Tiempo
- Calculo de distancias: `O(n*m)`
- Ordenamiento de vecinos: `O(n log n)` con ordenamiento comparativo
- Promedio final: `O(k)`

Complejidad total esperada:

$$
O(nm + n\log n + k)
$$

Si se reporta solo la parte dominante de KNN clasico, la implementacion sigue siendo lineal respecto al numero de registros para el calculo de distancias y logaritmica para el ordenamiento.

### Espacio
- Se necesita almacenar la lista de vecinos con sus distancias: `O(n)`
- Si se conserva informacion auxiliar de todos los registros, el espacio total sigue siendo `O(n)` adicional sobre la entrada.

## 9. Casos borde
- Dataset vacio: no hay vecinos que evaluar.
- `k = 1`: se devuelve el valor objetivo del vecino mas cercano.
- `k = n`: se promedian todos los valores objetivo.
- `k > n`: la implementacion debe definir una politica segura; la mas razonable es usar todos los vecinos disponibles.
- Distancias iguales: conviene usar un criterio estable por orden de aparicion.
- Atributos vacios: el contrato no los sugiere; deben tratarse como caso invalido.
- Una sola dimension: la distancia se reduce a `|x1 - x2|`.
- Muchas dimensiones: se aplica la misma formula de manera generica.

## 10. Validacion contra el SPEC
Los ejemplos oficiales se explican exactamente con el flujo anterior:
- distancia Euclidiana,
- ordenamiento ascendente,
- seleccion de `k` vecinos,
- promedio simple de `ys`.

Por tanto, la solucion futura debe construirse sobre ese contrato y no sobre una variante ponderada de KNN.
