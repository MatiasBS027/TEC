# AGENTS.md

## Visión General
Este proyecto prepara la implementación de una solución de Knapsack con Programación Dinámica en wxMaxima. El objetivo es construir una función `ks(capacidad, objetos)` que produzca la matriz de decisión y selección de objetos exactamente en el formato solicitado por el SPEC.

## Stack Técnico
- Lenguaje: wxMaxima / Máxima
- Archivo principal: `.mac`
- Técnica: Programación Dinámica tabular sobre matriz
- Complejidad objetivo: `O(n*w)`

## Restricciones
- No usar `load(...)`.
- No usar bibliotecas externas.
- No usar memoization de wxMaxima.
- No usar un algoritmo distinto a DP matriz.
- No cambiar el contrato ni el formato esperado por el SPEC.
- No introducir dependencias adicionales fuera del lenguaje base.
- No modificar el comportamiento esperado de los ejemplos oficiales.

## Arquitectura Lógica
La solución futura debe separarse en responsabilidades claras:

1. Parsing de entrada
   - Leer capacidad y lista de objetos.
   - Extraer nombre, valor y peso de cada objeto.

2. Construcción de matriz DP
   - Crear la tabla por filas y capacidades.
   - Resolver cada subproblema con include/exclude.

3. Transición DP
   - Comparar tomar vs. no tomar el objeto actual.
   - Mantener el valor óptimo y la selección asociada.

4. Selección de objetos
   - Conservar la lista de objetos elegidos para cada celda.
   - Respetar el formato de salida de los ejemplos.

5. Formateo de salida
   - Construir la matriz final con encabezado y filas.
   - Devolver exactamente lo solicitado por `ks(...)`.

## Roadmap Técnico
- Fase 1: Modelar el contrato y la representación interna.
- Fase 2: Diseñar la recurrencia y casos base.
- Fase 3: Definir la estructura de la matriz en listas Maxima.
- Fase 4: Implementar el llenado fila por fila.
- Fase 5: Verificar reconstrucción de objetos elegidos.
- Fase 6: Ajustar el formato final a los ejemplos.
- Fase 7: Probar con los tres casos oficiales y casos borde.

## Riesgos
- Desalineación entre la salida generada y el formato exacto del SPEC.
- Errores al representar la matriz usando listas anidadas.
- Empates no resueltos de forma consistente.
- Mezclar valor óptimo con reconstrucción de objetos.
- Introducir accidentalmente lógica recursiva o memoization.
- Confundir el índice de capacidad con el índice de columna.
