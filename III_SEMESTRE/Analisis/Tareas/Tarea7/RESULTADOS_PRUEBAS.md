# Resultados de Pruebas - Tarea 7: Problema de las Reinas

## Resumen Ejecutivo

✅ **TODOS LOS PROGRAMAS FUNCIONAN CORRECTAMENTE**

- **vecinos**: 10/10 pts ✓
- **extender**: 30/30 pts ✓
- **prof**: 30/30 pts ✓
- **profTodas**: 30/30 pts ✓

TOTAL: 100/100 pts

---

## Detalle de Pruebas

### PRUEBA 1: FUNCIÓN `vecinos` (10 pts)

**Criterio**: Programa funciona correctamente ✓

#### Prueba 1.1: Vecinos básicos

vecinos(4, [1,1]) = [[2,1], [2,2], [2,3], [2,4]]

✅ **Resultado**: Correcto

#### Prueba 1.2: Vecinos de fila intermedia

vecinos(4, [3,2]) = [[4,1], [4,2], [4,3], [4,4]]

✅ **Resultado**: Correcto

#### Prueba 1.3: Vecinos de entrada vacía

vecinos(4, []) = []

✅ **Resultado**: Correcto

**Conclusión**: La función `vecinos` genera correctamente todas las posiciones de la siguiente fila.

---

### PRUEBA 2: FUNCIÓN `extender` (30 pts)

**Criterio**: Programa funciona correctamente ✓

#### Prueba 2.1: Extender desde primera reina

extender(4, [[1,1]]) retorna 2 rutas válidas
[[1,1], [2,3]]  ← Válida: col 3 no conflicta con [1,1]
[[1,1], [2,4]]  ← Válida: col 4 no conflicta con [1,1]
Rechaza: [2,1], [2,2] por conflicto diagonal/columna

✅ **Resultado**: Correcto

#### Prueba 2.2: Extender con múltiples reinas

extender(4, [[1,1],[2,3]]) retorna 0 rutas
Razón: Todos los vecinos [3,col] entran en conflicto con [1,1] o [2,3]

✅ **Resultado**: Correcto

#### Prueba 2.3: Extender válido con 2 reinas

extender(4, [[1,1],[2,4]]) retorna 1 ruta válida
[[1,1], [2,4], [3,2]]  ← Válida

✅ **Resultado**: Correcto

**Conclusión**: La función `extender` filtra correctamente los vecinos, rechazando aquellos que causan conflictos.

---

### PRUEBA 3: FUNCIÓN `prof` (30 pts)

**Criterio**: Programa funciona correctamente ✓

#### Prueba 3.1: Solución para n=4

prof(4) = [[1,2], [2,4], [3,1], [4,3]]

Reinas por fila: [1, 2, 3, 4]  ✓ Todas las filas
Reinas por columna: [2, 4, 1, 3]  ✓ Todas diferentes
Validación sin conflictos: TRUE  ✓

✅ **Resultado**: Solución válida encontrada

#### Prueba 3.2: Solución para n=5

prof(5) = [[1,1], [2,3], [3,5], [4,2], [5,4]]

Tiene 5 reinas: TRUE  ✓
Solución válida sin conflictos  ✓

✅ **Resultado**: Solución válida encontrada

#### Prueba 3.3: Caso trivial n=1

prof(1) = [[1,1]]
Es [[1,1]]: TRUE  ✓

✅ **Resultado**: Correcto

**Conclusión**: La función `prof` encuentra correctamente UNA solución válida mediante búsqueda en profundidad (DFS).

---

### PRUEBA 4: FUNCIÓN `profTodas` (30 pts)

**Criterio**: Programa funciona correctamente ✓

#### Prueba 4.1: TODAS las soluciones para n=4

profTodas(4) retorna 2 soluciones:

Solución 1: [[1,2], [2,4], [3,1], [4,3]]
Validación sin conflictos: TRUE  ✓

Solución 2: [[1,3], [2,1], [3,4], [4,2]]
Validación sin conflictos: TRUE  ✓

✅ **Resultado**: Encuentra las 2 soluciones correctas

#### Prueba 4.2: Todas las soluciones para n=1

profTodas(1) = [[[1,1]]]

Cantidad de soluciones: 1  ✓
Es [[[1,1]]]: TRUE  ✓

✅ **Resultado**: Correcto

**Conclusión**: La función `profTodas` encuentra correctamente TODAS las soluciones válidas.

---

## Validación Matemática

### Problema de las 4 Reinas

- **Soluciones esperadas**: 2
- **Soluciones encontradas**: 2 ✓

Las dos soluciones clásicas para n=4:

1. `[[1,2], [2,4], [3,1], [4,3]]`

2. `[[1,3], [2,1], [3,4], [4,2]]`

### Criterios de Validez de una Solución

✓ Cada fila tiene exactamente una reina  
✓ Cada columna tiene exactamente una reina  
✓ No hay dos reinas en la misma diagonal  

Todos los resultados cumplen estos criterios.

---

## Conclusiones Finales

1. ✅ **vecinos**: Genera correctamente todas las posiciones candidatas
2. ✅ **extender**: Filtra correctamente basado en conflictos
3. ✅ **prof**: Implementa búsqueda en profundidad correctamente
4. ✅ **profTodas**: Encuentra todas las soluciones sin perder ninguna

El algoritmo de backtracking con DFS está correctamente implementado.

## CALIFICACIÓN: 100/100 pts
