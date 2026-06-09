# AGENTS.md

## Resumen del proyecto
Este proyecto prepara la implementacion de una solucion de KNN en wxMaxima para regresion sobre datos estructurados como listas. La meta es construir, en una segunda fase, un programa que reciba un registro de consulta `x`, un valor de `k` y un dataset `datos`, y retorne la estimacion producida por los `k` vecinos mas cercanos.

## Stack tecnico
- Lenguaje: wxMaxima / Maxima
- Archivo de entrega: `.mac`
- Algoritmo obligatorio: KNN
- Tipo de problema: regresion
- Representacion principal: listas anidadas

## Restricciones obligatorias
- No usar `load(...)`.
- No usar bibliotecas adicionales.
- No usar normalizacion de datos.
- No usar otro algoritmo distinto a KNN.
- No usar memoization de wxMaxima.
- Respetar exactamente los nombres de funciones solicitados: `ide(dat)`, `xs(dat)`, `ys(dat)`, `distancia(x1,x2)` y `knn(x,k,datos)`.
- Respetar la estructura de entrada dada por el SPEC.
- Respetar el formato de salida mostrado en los ejemplos.
- Entregar un archivo reconocible por wxMaxima.
- Mantener el encabezado de comentarios con nombre y carne al inicio del `.mac`.

## Contrato funcional esperado
- `ide(dat)` debe devolver el identificador del registro.
- `xs(dat)` debe devolver la lista de atributos predictivos.
- `ys(dat)` debe devolver la variable objetivo.
- `distancia(x1,x2)` debe calcular la distancia entre dos vectores de la misma dimensionalidad.
- `knn(x,k,datos)` debe seleccionar los `k` vecinos mas cercanos a `x` y regresar la regresion final.

## Arquitectura propuesta
La solucion futura debe separarse en responsabilidades pequenas y verificables:

1. Extraccion de datos
   - Leer el identificador del registro.
   - Separar atributos predictivos y valor objetivo.

2. Calculo de distancias
   - Comparar el vector de consulta con cada vector del dataset.
   - Trabajar con dimensionalidad variable.

3. Ordenamiento de vecinos
   - Asociar cada registro con su distancia.
   - Ordenar de menor a mayor distancia.
   - Mantener determinismo cuando existan empates.

4. Seleccion de vecinos
   - Tomar los primeros `k` elementos ordenados.
   - Manejar de forma segura casos como `k = 1` o `k > n`.

5. Regresion final
   - Combinar los valores objetivo de los vecinos seleccionados.
   - Producir un valor numerico final.

6. Salida
   - Devolver exactamente el valor esperado por el SPEC.

## Riesgos
- Confundir clasificacion con regresion.
- Promediar atributos en vez de promediar la variable objetivo.
- Ordenar sin preservar un criterio estable para empates.
- Romper el contrato de listas anidadas del dataset.
- Introducir normalizacion por error.
- Cambiar nombres de funciones o parametros.
- Usar una estructura que wxMaxima imprima distinto al ejemplo.

## Roadmap
- Fase 1: Analisis del dataset y del contrato.
- Fase 2: Definicion de helpers `ide`, `xs` y `ys`.
- Fase 3: Definicion formal de la distancia Euclidiana.
- Fase 4: Modelado de la busqueda de vecinos mas cercanos.
- Fase 5: Regresion KNN por promedio simple de vecinos.
- Fase 6: Validacion matematica con los ejemplos del SPEC.
- Fase 7: Pruebas finales y ajuste de formato.
