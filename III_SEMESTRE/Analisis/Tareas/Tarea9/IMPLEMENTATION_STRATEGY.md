# IMPLEMENTATION_STRATEGY.md

## Objetivo
Definir cómo construir la solución de Knapsack en wxMaxima paso a paso, sin violar ninguna restricción del SPEC.

## Orden Exacto de Implementación

### 1. Definir el contrato de entrada
- Confirmar la forma `ks(capacidad, objetos)`.
- Verificar que cada objeto tenga el formato `[nombre, [valor, peso]]`.

### 2. Preparar la representación interna
- Elegir listas anidadas como estructura base.
- Definir cómo se almacenará cada celda de la tabla.
- Evitar estructuras externas o dependencias de biblioteca.

### 3. Construir la primera fila / caso base
- Manejar capacidad cero.
- Manejar ausencia de objetos.
- Confirmar que la base produce selección vacía.

### 4. Implementar la transición DP
- Para cada objeto y capacidad, calcular excluir e incluir.
- Elegir la mejor alternativa.
- Guardar el resultado en la tabla.

### 5. Agregar trazabilidad de objetos
- Conservar la lista de objetos elegidos para cada celda.
- Mantener coherencia entre valor y selección.
- Resolver empates de manera estable.

### 6. Formatear la salida
- Construir el encabezado de capacidades.
- Organizar filas por objeto.
- Reproducir el estilo de salida de los ejemplos oficiales.

### 7. Probar incrementalmente
- Probar primero con el ejemplo de 4 objetos y capacidad 4.
- Luego con el segundo ejemplo del SPEC.
- Después con el ejemplo de capacidad 8.

### 8. Validar restricciones finales
- Confirmar que no existe `load(...)`.
- Confirmar que no existe memoization.
- Confirmar que el algoritmo es tabular y `O(n*w)`.
- Confirmar que el archivo final sigue siendo `.mac`.

## Validaciones Progresivas
1. Validación de contrato de datos.
2. Validación de la recurrencia.
3. Validación de la matriz DP.
4. Validación de la selección de objetos.
5. Validación del formato final.

## Puntos de Verificación
- La tabla debe crecer fila por fila.
- Cada celda debe corresponder a un subproblema real.
- El resultado debe ser determinista.
- El formato debe coincidir con el SPEC.

## Riesgos Técnicos
- Guardar solo valores y perder la ruta de objetos.
- Desalinear índices de capacidad.
- Generar un formato que wxMaxima no imprima igual al del SPEC.
- Introducir una solución recursiva por accidente.
- Romper el orden esperado en los casos empatados.

## Regla de Seguridad
No pasar a la implementación definitiva hasta que la documentación y el modelo DP estén alineados con los ejemplos oficiales.
