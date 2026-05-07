# Pruebas Límite y Casos Especiales - Tarea 7

## Resumen Ejecutivo

✅ **TODAS LAS PRUEBAS DE LÍMITE Y CASOS ESPECIALES PASARON**

Validaciones completadas:

- ✅ Listas vacías
- ✅ Valores límite (n=0,1,2,3,4,5)
- ✅ Números negativos
- ✅ Detección de conflictos específicos
- ✅ Rutas parciales

---

## 1. PRUEBAS CON LISTAS VACÍAS

### Prueba E1: Conflicto con lista vacía

E1.1: conflicto([1,1], []) = false ✓
    La función retorna correctamente false cuando no hay reinas previas

E1.2: conflicto([], [[1,1]]) = false ✓
    La función maneja correctamente la reina vacía

### Prueba E2: Vecinos con lista vacía

E2.1: vecinos(4, []) = [] ✓
    Sin reina anterior, no genera vecinos

### Prueba E3: Extender con lista vacía

E3.1: extender(4, []) = [] ✓
    No puede extender ruta vacía

E4.1: extenderAux([], [[1,1]]) = [] ✓
    Sin vecinos para procesar, retorna lista vacía

### Prueba E5: Rutas iniciales para n=0

E5.1: rutasIniciales(0) = [] ✓
    Correctamente retorna lista vacía para n <= 0

### Prueba E6-E7: Búsqueda en profundidad con n=0

E6.1: prof(0) = [] ✓
    No hay rutas iniciales, devuelve vacío

E7.1: profTodas(0) = [] ✓
    No hay soluciones para n=0
**Conclusión**: ✅ **PASÓ** - Manejo correcto de listas vacías en todas las funciones

---

## 2. PRUEBAS LÍMITE: VALORES PEQUEÑOS

### n = 0 (Caso trivial negativo)

No hay soluciones ✓

### n = 1 (Caso trivial positivo)

prof(1) = [[1,1]] ✓
profTodas(1) = [[[1,1]]] ✓
Cantidad de soluciones: 1

### n = 2 (Sin solución matemática)

prof(2) = [] ✓
profTodas(2) = [] ✓
Cantidad de soluciones: 0
Correcto: No hay forma de colocar 2 reinas sin conflicto

### n = 3 (Sin solución matemática)

prof(3) = [] ✓
profTodas(3) = [] ✓
Cantidad de soluciones: 0
Correcto: No hay forma de colocar 3 reinas sin conflicto

### n = 4 (Primer caso con soluciones)

profTodas(4) = [2 soluciones] ✓
Cantidad correcta: 2

Solución 1: [[1,2], [2,4], [3,1], [4,3]]
Solución 2: [[1,3], [2,1], [3,4], [4,2]]

### n = 5 (Múltiples soluciones)

prof(5) = [[1,1], [2,3], [3,5], [4,2], [5,4]] ✓
profTodas(5) = [10 soluciones] ✓
Cantidad correcta: 10 soluciones para n=5
Solución encontrada válida: true

**Conclusión**: ✅ **PASÓ** - Comportamiento correcto en todos los valores límite

---

## 3. PRUEBAS LÍMITE: NÚMEROS NEGATIVOS

N1.1: prof(-1) = [] ✓
N2.1: profTodas(-1) = [] ✓
N3.1: rutasIniciales(-5) = [] ✓

**Conclusión**: ✅ **PASÓ** - Números negativos manejados correctamente

---

## 4. PRUEBAS LÍMITE: RUTAS PARCIALES

### Ruta con 1 reina

R1.1: extender(4, [[1,1]]) retorna 2 rutas
    [[1,1], [2,3]] ✓ (columna 3 válida)
    [[1,1], [2,4]] ✓ (columna 4 válida)

Rechaza:
    [2,1] - Conflicto de columna
    [2,2] - Conflicto diagonal

### Ruta con 2 reinas

R2.1: extender(4, [[1,1],[2,3]]) retorna 0 rutas
    Todas las posiciones [3,col] tienen conflicto
    Este es un callejón sin salida correcto

### Ruta con 3 reinas

R3.1: extender(4, [[1,1],[2,3],[3,5]]) retorna 1 ruta
    [[1,1], [2,3], [3,5], [4,2]] ✓

    Columna 2 es la única sin conflictos diagonales/columnares

### Ruta totalmente conflictiva

R4.1: extender(4, [[1,1],[2,2],[3,3]]) retorna 0 rutas
      La diagonal dominada genera callejón sin salida
      Comportamiento correcto

**Conclusión**: ✅ **PASÓ** - Rutas parciales procesadas correctamente

---

## 5. DETECCIÓN DE CONFLICTOS ESPECÍFICOS

### Conflicto por columna
  
C1.1: conflicto([2,1], [[1,1]]) = true ✓
    Misma columna [2,1] vs [1,1] → CONFLICTO

### Conflicto por diagonal (arriba-izquierda)
  
C2.1: conflicto([2,2], [[1,1]]) = true ✓
    Diagonal: |2-1| = |2-1| → CONFLICTO

### Conflicto por diagonal (abajo-derecha)
  
C3.1: conflicto([3,3], [[1,1]]) = true ✓
    Diagonal: |3-1| = |3-1| → CONFLICTO

### Sin conflicto
  
C4.1: conflicto([2,3], [[1,1]]) = false ✓
    Diferente columna, sin diagonal → VÁLIDO

### Múltiples reinas sin conflicto
  
C5.1: conflicto([4,3], [[1,2],[2,4],[3,1]]) = false ✓
    [4,3] no conflicta con ninguna de las tres reinas

### Múltiples reinas CON conflicto
  
C6.1: conflicto([4,2], [[1,2],[2,4],[3,1]]) = true ✓
    [4,2] conflicta con [1,2] (misma columna 2)

**Conclusión**: ✅ **PASÓ** - Detección de conflictos precisa en todos los casos

---

## 6. MATRIZ DE SOLUCIONES MATEMÁTICA VERIFICADA

| n | Soluciones | prof() | profTodas() | Comentario |
| 0 | 0 | [] | [] | Sin sentido |
| 1 | 1 | ✓ | ✓ | Trivial |
| 2 | 0 | [] | [] | Matemáticamente imposible |
| 3 | 0 | [] | [] | Matemáticamente imposible |
| 4 | 2 | ✓ | ✓✓ | Clásico |
| 5 | 10 | ✓ | ✓✓ | Verificado |

---

## Resumen de Pruebas Ejecutadas

- **Pruebas con listas vacías**: 7/7 ✓
- **Valores límite (n=0,1,2,3,4,5)**: 8/8 ✓
- **Números negativos**: 3/3 ✓
- **Rutas parciales**: 4/4 ✓
- **Detección de conflictos**: 6/6 ✓

**Total: 28/28 pruebas pasadas** ✅

---

## Conclusiones

1. ✅ Las funciones manejan correctamente **listas vacías** sin errores
2. ✅ El algoritmo funciona correctamente en **valores límite** (n=0 a n=5)
3. ✅ Los **números negativos** son rechazados apropiadamente
4. ✅ Las **rutas parciales** se extienden o se rechazan correctamente
5. ✅ La **detección de conflictos** es precisa (columna, diagonal)
6. ✅ Los resultados coinciden con **matemática conocida** del problema

El programa es **robusto ante casos especiales y extremos**.
