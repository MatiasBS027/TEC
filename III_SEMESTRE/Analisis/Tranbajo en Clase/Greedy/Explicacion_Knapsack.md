# Implementación del Problema de la Mochila (Knapsack Problem)

## 📋 Tabla de Contenidos
1. [Análisis del Problema](#análisis-del-problema)
2. [Cómo Implementé el Código](#cómo-implementé-el-código)
3. [Explicación Detallada de las Soluciones](#explicación-detallada-de-las-soluciones)
4. [Comparación de Complejidades](#comparación-de-complejidades)
5. [Ejemplo Práctico](#ejemplo-práctico)

---

## Análisis del Problema

### ¿Qué es el Problema de la Mochila?

Imagina que eres un ladrón en un supermercado. Tienes una mochila que puede cargar **máximo 10 kilos**. 
Hay 5 artículos disponibles, cada uno con un **valor (ganancia)** y un **peso**:

| Artículo  | Valor ($) | Peso (kg) |
|-----------|-----------|----------|
| Apio      | 10        | 1        |
| Papas     | 40        | 2        |
| Bananos   | 20        | 1        |
| Pan       | 15        | 3        |
| Queso     | 60        | 5        |

**Objetivo:** Llenar la mochila con artículos que maximicen el valor total, sin exceder la capacidad.

### Restricciones
- ✅ Cada artículo existe en una **única unidad**
- ✅ NO se pueden fraccionar los artículos
- ✅ Capacidad máxima: 10 kilos

### Posibles Soluciones

#### Solución Óptima (Exhaustiva)
Revisar todos los 2⁵ = 32 subconjuntos posibles:
- **Mejor combinación:** [Queso (60, 5kg) + Papas (40, 2kg) + Bananos (20, 1kg) + Apio (10, 1kg)]
- **Valor total:** $130
- **Peso total:** 9 kg
- **Complejidad:** O(2ⁿ) ❌ Impráctica para n grande

---

## Cómo Implementé el Código

### Estándar Seguido

Analicé los otros archivos `.mac` en tu workspace (Fibonacci.mac, bubblesort.mac, lsearch.mac) y observé el patrón:

1. **Comentario inicial** con el nombre del algoritmo
2. **Funciones bien documentadas** con explicaciones
3. **Análisis de Big O detallado** al final del archivo
4. **Estructura limpia** y legible

### Decisiones de Diseño

#### 1️⃣ Creé 3 Implementaciones del Greedy

Porque el documento explica tres versiones con diferentes complejidades:

```
Solución 1: Greedy Sin Ordenar ........... O(n²)
Solución 2: Greedy Con Ordenamiento ..... O(n*log(n))
Solución 3: Greedy Optimizado (Ratio) ... O(n*log(n))
```

#### 2️⃣ Estructura de Datos para los Objetos

```maxima
objetos = [
    [nombre, [valor, peso]],
    [nombre, [valor, peso]],
    ...
]
```

Ejemplo:
```maxima
[apio, [10, 1]]  = artículo "apio" con valor $10 y peso 1kg
```

#### 3️⃣ Retorno de Resultados

```maxima
return [mochila, [valorTotal, pesoTotal]]
```

Esto permite acceder fácilmente a:
- La lista de artículos seleccionados
- El valor y peso totales

---

## Explicación Detallada de las Soluciones

### Solución 1: GREEDY SIN ORDENAR - O(n²)

#### Algoritmo

```
ENTRADA: capacidad, objetos
SALIDA: [mochila_final, [valor_total, peso_total]]

1. mochila ← lista vacía
2. MIENTRAS haya objetos disponibles HACER
     a. Buscar el artículo de mayor VALOR que cabe en la mochila
     b. SI encontramos uno ENTONCES
        - Agregarlo a la mochila
        - Eliminarlo de la lista de objetos
     c. SI NO encontramos ninguno ENTONCES
        - Salir del bucle
3. RETORNAR mochila y totales
```

#### Flujo Paso a Paso (del documento)

**Iteración 1:** Capacidad = 10kg
- Buscamos el mayor valor → Queso ($60, 5kg) ✅ Cabe
- Mochila: [Queso], Peso: 5kg, Valor: $60

**Iteración 2:**
- Buscamos el siguiente mayor → Papas ($40, 2kg) ✅ Cabe
- Mochila: [Queso, Papas], Peso: 7kg, Valor: $100

**Iteración 3:**
- Buscamos el siguiente → Bananos ($20, 1kg) ✅ Cabe
- Mochila: [Queso, Papas, Bananos], Peso: 8kg, Valor: $120

**Iteración 4:**
- Buscamos el siguiente → Pan ($15, 3kg) ❌ NO cabe (8+3 > 10)

**Iteración 5:**
- Buscamos el siguiente → Apio ($10, 1kg) ✅ Cabe
- Mochila: [Queso, Papas, Bananos, Apio], Peso: 9kg, Valor: $130

#### Análisis de Complejidad

```
Operación           | Costo  | Iteraciones
─────────────────────────────────────────
Búsqueda en bucle  | O(n)   | n veces
Eliminación        | O(n)   | n veces
─────────────────────────────────────────
Total: n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = O(n²)
```

❌ **Problema:** En cada iteración busca el máximo nuevamente. Con n artículos = n² operaciones.

---

### Solución 2: GREEDY CON ORDENAMIENTO - O(n*log(n))

#### Algoritmo

```
ENTRADA: capacidad, objetos
SALIDA: [mochila_final, [valor_total, peso_total]]

1. objetosOrdenados ← SORT(objetos por VALOR descendente)
2. mochila ← lista vacía
3. PARA cada objeto EN objetosOrdenados HACER
     SI cabe en la mochila ENTONCES
        - Agregarlo
        - Actualizar peso y valor
4. RETORNAR mochila y totales
```

#### Flujo Paso a Paso

**Ordenamiento previo (O(n*log(n))):**
```
Original: [Apio($10), Papas($40), Bananos($20), Pan($15), Queso($60)]
↓
Ordenado: [Queso($60), Papas($40), Bananos($20), Pan($15), Apio($10)]
```

**Una sola pasada (O(n)):**
```
1. Queso ($60, 5kg)   → Cabe (5 ≤ 10) ✅ Agregado
2. Papas ($40, 2kg)   → Cabe (7 ≤ 10) ✅ Agregado
3. Bananos ($20, 1kg) → Cabe (8 ≤ 10) ✅ Agregado
4. Pan ($15, 3kg)     → NO cabe (11 > 10) ❌ Descartado
5. Apio ($10, 1kg)    → Cabe (9 ≤ 10) ✅ Agregado
```

**Resultado:** Mochila final = [Queso, Papas, Bananos, Apio], Valor = $130

#### Complejidad

```
Operación          | Costo
──────────────────────────
Ordenamiento       | O(n*log(n))
Una pasada         | O(n)
──────────────────────────
Total: O(n*log(n)) + O(n) = O(n*log(n))
```

✅ **Mejora:** Solo se ordena una vez, luego se recorre una sola vez.

---

### Solución 3: GREEDY OPTIMIZADO - O(n*log(n)) ⭐ MÁS EFECTIVO

#### Algoritmo

```
ENTRADA: capacidad, objetos
SALIDA: [mochila_final, [valor_total, peso_total]]

1. PARA cada objeto HACER
     - Calcular ratio = valor / peso
2. objetosConRatio ← SORT(objetos por RATIO descendente)
3. mochila ← lista vacía
4. PARA cada objeto EN objetosConRatio HACER
     SI cabe en la mochila ENTONCES
        - Agregarlo
5. RETORNAR mochila y totales
```

#### ¿Por qué es mejor?

En lugar de solo considerar el **valor absoluto**, consideramos la **eficiencia**:
¿Cuánto valor obtenemos por cada kilo?

#### Ejemplo con Ratios

```
Artículo  | Valor | Peso | Ratio ($/kg)
──────────────────────────────────────
Apio      | $10   | 1    | 10.00
Papas     | $40   | 2    | 20.00
Bananos   | $20   | 1    | 20.00
Pan       | $15   | 3    | 5.00
Queso     | $60   | 5    | 12.00
```

**Ordenado por ratio (descendente):**
```
Bananos (20.00) → Papas (20.00) → Queso (12.00) → Apio (10.00) → Pan (5.00)
```

**Selección:**
```
1. Bananos (1kg, $20) → Cabe ✅
2. Papas (2kg, $40)   → Cabe ✅
3. Queso (5kg, $60)   → Cabe ✅
4. Apio (1kg, $10)    → Cabe ✅
Total: 9kg, $130 ✅
```

#### ¿Cuándo es mejor que Solución 2?

Considera este escenario diferente:
- Capacidad: 5kg
- Artículos: Queso ($60, 5kg), Papas ($40, 2kg), Pan ($30, 3kg)

**Solución 2 (por valor):**
- Elige Queso ($60, 5kg) → Llena la mochila
- Resultado: $60, 5kg

**Solución 3 (por ratio):**
- Ratios: Queso (12.00), Papas (20.00), Pan (10.00)
- Elige Papas (20.00) → $40, 2kg
- Elige Pan (10.00) → $30, 3kg (no cabe: 2+3=5kg) ✅
- Resultado: $70, 5kg ⭐ **MEJOR**

---

## Comparación de Complejidades

```
                   Complejidad | Ventajas           | Desventajas
───────────────────────────────────────────────────────────────────
Sin Ordenar        | O(n²)      | Simple             | Lenta para n grande
Con Ordenamiento   | O(n*log(n))| Mejor que O(n²)   | No optimiza ratios
Optimizado (Ratio) | O(n*log(n))| Mejor resultados  | Un poco más complejo
```

**Uso recomendado:**
- **n pequeño (< 10):** Solución 1 está bien
- **n mediano (10-1000):** Solución 2
- **n grande o precisión crítica:** Solución 3 ⭐

---

## Ejemplo Práctico

### Ejecución en Maxima

```maxima
/* Cargar el archivo */
load("KnapsackProblem.mac");

/* Crear objetos */
objetos: crearObjetos();

/* Ejecutar Solución 1: Sin Ordenar */
resultado1: knapsackGreedyNoOrdenado(10, objetos);
mostrarResultado("Greedy Sin Ordenar (O(n²))", resultado1);

/* Ejecutar Solución 2: Con Ordenamiento */
resultado2: knapsackGreedy(10, copy(objetos));
mostrarResultado("Greedy Con Ordenamiento (O(n*log(n)))", resultado2);

/* Ejecutar Solución 3: Optimizado */
resultado3: knapsackGreedyOptimizado(10, copy(objetos));
mostrarResultado("Greedy Optimizado - Ratio (O(n*log(n)))", resultado3);
```

### Output Esperado

```
=== Resultado de Greedy Sin Ordenar (O(n²)) ===
Artículos en la mochila:
  - queso: valor=$60, peso=5 kg
  - papas: valor=$40, peso=2 kg
  - bananos: valor=$20, peso=1 kg
  - apio: valor=$10, peso=1 kg

Valor Total: $130
Peso Total: 9 kg

=== Resultado de Greedy Con Ordenamiento (O(n*log(n))) ===
Artículos en la mochila:
  - queso: valor=$60, peso=5 kg
  - papas: valor=$40, peso=2 kg
  - bananos: valor=$20, peso=1 kg
  - apio: valor=$10, peso=1 kg

Valor Total: $130
Peso Total: 9 kg

=== Resultado de Greedy Optimizado - Ratio (O(n*log(n))) ===
Artículos en la mochila:
  - bananos: valor=$20, peso=1 kg
  - papas: valor=$40, peso=2 kg
  - queso: valor=$60, peso=5 kg
  - apio: valor=$10, peso=1 kg

Valor Total: $130
Peso Total: 9 kg
```

---

## 🎯 Resumen

| Aspecto | Detalle |
|---------|---------|
| **Problema** | Maximizar valor en mochila con capacidad limitada |
| **Naturaleza** | NP-Completo (sin solución óptima rápida) |
| **Estrategia** | Algoritmos Greedy (aproximados pero rápidos) |
| **Mejor Solución** | Ordenar por ratio valor/peso, O(n*log(n)) |
| **Implementación** | 3 versiones con complejidades diferentes |
| **Caso de Uso Real** | Logística, optimización de recursos, asignación de memoria |

