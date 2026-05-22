# PLAN.md

## Objetivo
Construir una solución de Knapsack con Programación Dinámica en wxMaxima, siguiendo exactamente el SPEC y sin implementar todavía el código final.

## Fases del Trabajo

| Fase | Nombre | Prioridad | Dependencias | Resultado Esperado |
|---|---|---:|---|---|
| 1 | Modelado del problema | Alta | Ninguna | Contrato claro de entrada/salida y representación interna |
| 2 | Parsing del input | Alta | Fase 1 | Lectura de `capacidad` y `objetos` |
| 3 | Construcción de matriz DP | Alta | Fase 1 | Tabla con valores óptimos por subproblema |
| 4 | Tracking de objetos elegidos | Alta | Fase 3 | Cada celda conserva la combinación elegida |
| 5 | Formateo exacto de salida | Alta | Fases 3-4 | Matriz final alineada a los ejemplos oficiales |
| 6 | Pruebas contra ejemplos | Alta | Fases 3-5 | Validación contra los 3 casos del SPEC |
| 7 | Validación final | Alta | Fases 1-6 | Revisión completa de restricciones y formato |

## Tareas Detalladas

### Fase 1 — Modelado del problema
- Confirmar estructura de objetos: `[nombre, [valor, peso]]`.
- Definir el encabezado de la matriz y el significado de cada celda.
- Determinar cómo representar listas de objetos elegidos.

### Fase 2 — Parsing del input
- Validar que la capacidad sea un entero positivo.
- Leer la lista de objetos sin alterar el orden.
- Extraer nombre, valor y peso de cada elemento.

### Fase 3 — Construcción de matriz DP
- Inicializar la fila base.
- Iterar objeto por objeto y capacidad por capacidad.
- Calcular `max(no_tomar, tomar)` para cada celda.

### Fase 4 — Tracking de objetos elegidos
- Guardar junto al valor óptimo la lista de objetos que lo produce.
- Resolver empates de forma estable.
- Mantener coherencia con la trayectoria de la tabla.

### Fase 5 — Formateo exacto de salida
- Construir la fila de encabezado.
- Formatear cada celda como `valor` o `[valor, [objetos]]` según el ejemplo esperado.
- Reproducir la estructura de matriz mostrada en el SPEC.

### Fase 6 — Pruebas contra ejemplos
- Verificar el ejemplo de capacidad 4 con 4 objetos.
- Verificar el ejemplo de capacidad 4 con 5 objetos.
- Verificar el ejemplo de capacidad 8 con 4 objetos.

### Fase 7 — Validación final
- Confirmar ausencia de `load(...)`.
- Confirmar ausencia de memoization.
- Confirmar complejidad `O(n*w)`.
- Confirmar que el archivo sigue siendo válido para wxMaxima.

## Checkpoints
- Cierre del contrato funcional.
- Cierre del modelo DP.
- Cierre del formato de salida.
- Validación de los ejemplos oficiales.
- Revisión final de restricciones.

## Milestones
1. Especificación técnica completada.
2. Estructura de la solución definida.
3. Plan de implementación validado.
4. Código listo para escribirse después de la aprobación del diseño.
