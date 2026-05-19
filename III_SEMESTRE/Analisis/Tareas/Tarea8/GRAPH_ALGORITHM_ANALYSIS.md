# GRAPH_ALGORITHM_ANALYSIS

## Contexto
TPS se refiere a Traveling Salesperson Problem (TSP). Se requiere:
- `tspPermu`: busqueda exhaustiva por permutaciones.
- `tspGreedy`: estrategia greedy (nearest neighbor).

## Representacion del grafo
Formato observado en SPEC.md:
```
[ [c1, [[c2,10],[c3,15],[c4,20]]],
  [c2, [[c1,10],[c3,35],[c4,25]]],
  ... ]
```
- Lista de nodos.
- Cada nodo tiene lista de pares [vecino, peso].
- Grafo completo y no dirigido (pesos simetricos en ejemplos).

## Enfoques posibles
1. Exhaustivo con permutaciones (obligatorio).
2. Greedy por vecino mas cercano (obligatorio).

## Estructuras necesarias
- Lista de nodos.
- Conjunto/lista de visitados.
- Funcion costoRuta(ruta, grafo).
- Funcion peso(u,v, grafo).

## Complejidad
### Exhaustivo
- Tiempo: O((n-1)! * n) por evaluar todas las rutas.
- Espacio: O((n-1)! * n) si se almacenan todas las rutas, o menor si se evalua en streaming.

### Greedy
- Tiempo: O(n^2) si en cada paso se busca el minimo en lista de vecinos.
- Espacio: O(n) para ruta y visitados.

## Casos borde
- Nodos repetidos en entrada (no esperado).
- Pesos iguales (desempate necesario).
- Grafo incompleto (no esperado segun enunciado).
- Nodo inicial no existe (no esperado).

## Pseudocodigo de alto nivel
### Exhaustivo (tspPermu)
```
func tspPermu(start, grafo):
  nodos = todos los nodos del grafo
  otros = nodos sin start
  rutas = []
  minCosto = infinito
  para cada perm in permutations(otros):
    ruta = [start] + perm + [start]
    costo = costoRuta(ruta, grafo)
    si costo < minCosto:
      rutas = [[ruta, costo]]
      minCosto = costo
    si costo == minCosto:
      agregar [ruta, costo]
  retornar rutas
```

### Greedy (tspGreedy)
```
func tspGreedy(start, grafo):
  ruta = [start]
  visitados = {start}
  actual = start
  mientras visitados != todos:
    vecinos = vecinos(actual)
    elegir vecino no visitado con menor peso
    agregar vecino a ruta y visitados
    actual = vecino
  cerrar ruta con start
  costo = costoRuta(ruta, grafo)
  retornar [ruta, costo]
```

## Integracion con Maxima
- Usar `permutations` y `listify` para generar permutaciones.
- Mantener listas puras (sin estructuras externas).
- Respetar formato exacto de salida en SPEC.md.
- Documentar criterio de desempate en greedy (orden de aparicion o `sort`).

## Supuestos documentados
- Entrada valida y grafo completo.
- Pesos positivos.
- Greedy usa desempate estable por orden de lista.
