# DP_ANALYSIS.md

## Problema
Se desea resolver el Knapsack 0/1 usando Programación Dinámica tabular en wxMaxima. La salida debe conservar, para cada subproblema, el valor óptimo y el conjunto de objetos que produce ese valor.

## Modelo DP

### Estado
Sea `dp[i][w]` el mejor resultado usando los primeros `i` objetos con capacidad `w`.

### Interpretación
Cada celda representa un subproblema parcial.
- `i`: cantidad de objetos considerados.
- `w`: capacidad disponible.
- Valor de la celda: mejor ganancia posible.
- Selección asociada: lista de objetos usados para lograr esa ganancia.

### Caso base
- Sin objetos: valor `0` y selección vacía.
- Capacidad `0`: valor `0` y selección vacía.

### Transición
Para el objeto `i` con valor `v_i` y peso `p_i`:

- Si `p_i > w`, no cabe:
  - `dp[i][w] = dp[i-1][w]`
- Si `p_i <= w`, comparar:
  - No tomar: `dp[i-1][w]`
  - Tomar: `v_i + dp[i-1][w - p_i]`

La celda conserva el mejor de los dos resultados.

### Recurrencia formal
$$
DP(i, w) =
\begin{cases}
DP(i-1, w) & \text{si } p_i > w \\
\max\{DP(i-1, w),\ v_i + DP(i-1, w-p_i)\} & \text{si } p_i \le w
\end{cases}
$$

## Recorrido de la Matriz
- Se llena por filas, de arriba hacia abajo.
- Dentro de cada fila, se recorre la capacidad de izquierda a derecha.
- Cada nueva fila solo depende de la fila anterior.

## Decisión Include / Exclude
- `Exclude`: conservar la mejor solución previa sin el objeto actual.
- `Include`: sumar el valor actual y la mejor solución para la capacidad restante.
- Se selecciona la alternativa con mayor valor.
- En empate, se debe aplicar una regla estable consistente con los ejemplos.

## Pseudocódigo
```text
para cada objeto i:
  para cada capacidad w:
    si peso_i > w:
      copiar solución anterior
    si no:
      calcular excluir
      calcular incluir
      elegir mejor solución
      guardar valor y objetos elegidos
```

## Complejidad
- Tiempo: `O(n*w)` porque cada objeto se evalúa para cada capacidad.
- Espacio: `O(n*w)` si se guarda la tabla completa con reconstrucción de objetos.

## Casos Borde
- Mochila vacía: toda la tabla debe resolver a `0`.
- Lista vacía: no hay objetos que elegir.
- Objeto demasiado pesado: se hereda la celda anterior.
- Empates: deben resolverse de forma consistente y determinista.
- Capacidad pequeña: solo caben subcombinaciones parciales.
- Objetos con mismo peso o mismo valor: el DP sigue siendo válido porque compara por valor total.

## Comportamiento Esperado en los Ejemplos
- En el primer ejemplo, la matriz debe reproducir los valores y listas mostrados para capacidad 4.
- En el segundo ejemplo, la solución final debe coincidir con la tabla dada y su selección acumulada.
- En el tercer ejemplo, la tabla debe mostrar la progresión correcta de valores y objetos hasta capacidad 8.

## Observación Técnica para wxMaxima
La implementación futura debe construir la matriz usando listas anidadas compatibles con Máxima, sin bibliotecas externas. La estructura debe permitir acceder a filas, columnas y selección de objetos sin requerir memoization.
