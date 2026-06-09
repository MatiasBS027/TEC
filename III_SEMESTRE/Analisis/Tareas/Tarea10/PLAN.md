# PLAN.md

## Objetivo
Preparar la solucion de KNN en wxMaxima sin implementar todavia el codigo final. Este plan organiza el trabajo desde el analisis del enunciado hasta la validacion matematica de los ejemplos.

## Fases del trabajo

| Fase | Nombre | Prioridad | Dependencias | Resultado esperado |
|---|---|---:|---|---|
| 1 | Analisis del dataset | Alta | Ninguna | Contrato claro de estructura de datos y variables |
| 2 | Funciones auxiliares | Alta | Fase 1 | Definicion de `ide`, `xs` y `ys` |
| 3 | Distancia Euclidiana | Alta | Fase 1 | Formula formal para `distancia(x1,x2)` |
| 4 | Busqueda de vecinos | Alta | Fase 3 | Lista ordenada de vecinos por distancia |
| 5 | Regresion KNN | Alta | Fases 3-4 | Regla exacta para producir el resultado final |
| 6 | Validacion | Alta | Fases 1-5 | Verificacion contra ejemplos del SPEC |
| 7 | Pruebas finales | Alta | Fases 1-6 | Revisión de casos borde y consistencia |

## Tareas detalladas

### Fase 1: Analisis del dataset
- Confirmar la estructura `[id, [x1, x2, ..., xn, y]]`.
- Identificar el identificador del registro.
- Separar atributos predictivos y variable objetivo.
- Verificar que la cantidad de atributos predictivos puede variar.

### Fase 2: Funciones auxiliares
- Definir `ide(dat)` como extractor del identificador.
- Definir `xs(dat)` como extractor de atributos predictivos.
- Definir `ys(dat)` como extractor del valor objetivo.
- Asegurar que la separacion no altera el orden de los atributos.

### Fase 3: Distancia Euclidiana
- Confirmar la formula de distancia para vectores del mismo tamano.
- Verificar que se calcula sobre los atributos predictivos, no sobre el id ni sobre `y`.
- Asegurar soporte para dimension variable.

### Fase 4: Busqueda de vecinos
- Calcular la distancia entre la consulta y cada elemento del dataset.
- Ordenar los vecinos de menor a mayor distancia.
- Preservar una regla estable de desempate.

### Fase 5: Regresion KNN
- Seleccionar los `k` vecinos mas cercanos.
- Obtener la variable objetivo de cada vecino seleccionado.
- Calcular la prediccion como promedio simple de esos valores.

### Fase 6: Validacion
- Validar el ejemplo que produce `225`.
- Validar el ejemplo que produce `185`.
- Validar el caso de 25 dimensiones que produce `100`.

### Fase 7: Pruebas finales
- Revisar casos borde de dataset vacio.
- Revisar `k = 1`.
- Revisar `k = n`.
- Revisar `k > n`.
- Revisar empates de distancia.
- Revisar una sola dimension y muchas dimensiones.

## Checkpoints
1. Contrato de datos cerrado.
2. Formula de distancia cerrada.
3. Regla de seleccion de vecinos cerrada.
4. Regla de regresion cerrada.
5. Validacion numerica completada.
6. Documento listo para implementacion.

## Milestones
- Milestone 1: El modelo del problema queda definido.
- Milestone 2: La arquitectura logica queda separada por responsabilidades.
- Milestone 3: La regresion KNN queda validada matematicamente.
- Milestone 4: El proyecto queda listo para escribir el `.mac` final.
