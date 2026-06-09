# IMPLEMENTATION_STRATEGY.md

## Objetivo
Definir como construir la solucion de KNN en wxMaxima paso a paso, respetando las restricciones del SPEC y sin implementar todavia el codigo final.

## Orden recomendado de construccion

### 1. Cerrar el contrato de datos
- Confirmar la estructura `[id, [x1, x2, ..., xn, y]]`.
- Confirmar que `x` es un vector de consulta independiente.
- Confirmar que `k` es un entero positivo.

### 2. Implementar los extractores basicos
- `ide(dat)` debe devolver el identificador.
- `xs(dat)` debe devolver los atributos predictivos.
- `ys(dat)` debe devolver la variable objetivo.
- Verificar que no se altere el orden interno.

### 3. Definir la distancia
- Implementar `distancia(x1,x2)` como distancia Euclidiana.
- Asegurar que ambos vectores tengan la misma dimensionalidad.
- Probar primero con el ejemplo `[5,1,0]` y `[3,1,1]`.

### 4. Construir la lista de vecinos
- Recorrer `datos` y calcular una tupla por registro.
- Guardar distancia, objetivo y, si hace falta, el registro completo para trazabilidad.
- Conservar un criterio estable en caso de empates.

### 5. Seleccionar los `k` vecinos mas cercanos
- Ordenar ascendentemente por distancia.
- Tomar los primeros `k` elementos.
- Definir una politica segura si `k > n`.

### 6. Implementar la regresion final
- Extraer los `ys` de los vecinos seleccionados.
- Calcular el promedio simple.
- Retornar el valor numerico final.

### 7. Validar con ejemplos oficiales
- Comprobar que el primer ejemplo produce `225` con `k = 3`.
- Comprobar que el primer ejemplo produce `185` con `k = 5`.
- Comprobar que el segundo ejemplo produce `100` con `k = 1`.

### 8. Cerrar formato y restricciones
- No usar `load(...)`.
- No usar bibliotecas externas.
- No normalizar datos.
- No cambiar nombres de funciones.
- No alterar el estilo de entrega en `.mac`.

## Validaciones progresivas
1. Validacion de estructura del dato.
2. Validacion de extraccion de atributos.
3. Validacion de distancia.
4. Validacion de ordenamiento de vecinos.
5. Validacion de promedio final.
6. Validacion del comportamiento frente a los ejemplos.

## Checkpoints
- El contrato de entrada y salida debe quedar cerrado antes de escribir codigo.
- La distancia debe validar sobre vectores de igual tamano.
- El algoritmo debe ser determinista en empates.
- La regresion final debe ser un promedio simple.
- La documentacion debe dejar listos los pasos para la implementacion.

## Riesgos tecnicos
- Promediar atributos en lugar de promediar `ys`.
- Incluir el identificador dentro del calculo de distancia.
- Cambiar la dimensionalidad de manera accidental.
- Ordenar vecinos sin preservar estabilidad.
- Intentar resolver el problema con un algoritmo distinto a KNN.
- Introducir normalizacion o ponderacion no solicitada.
- Romper el contrato exacto de nombres de funciones.

## Criterio de salida de esta fase
La fase documental termina cuando queda claro:
- que se usara KNN de regresion,
- que la distancia es Euclidiana,
- que el resultado se obtiene por promedio simple de los `k` vecinos mas cercanos,
- y que la implementacion futura puede hacerse directamente en wxMaxima sin bibliotecas externas.
