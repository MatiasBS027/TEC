# AGENTS

## Vision general
Proyecto academico para implementar TSP (Traveling Salesperson Problem) en Maxima (wxMaxima). Se requieren dos enfoques: exhaustivo por permutaciones y greedy (nearest neighbor). El entregable es un unico archivo .mac con funciones especificas y salidas exactas.

## Arquitectura detectada
- No existe implementacion actual; solo cabecera en Tarea8.mac.
- Requisitos y ejemplos en SPEC.md.
- Referencia teorica en APUNTES.md y un PDF de apoyo.

## Objetivos tecnicos
- Implementar `tspPermu(start, grafo)` con busqueda exhaustiva por permutaciones.
- Implementar `tspGreedy(start, grafo)` con estrategia greedy vista en clase.
- Cumplir formato de entrada/salida mostrado en SPEC.md.
- No usar librerias externas (sin `load`), solo Maxima base.

## Stack usado
- Maxima / wxMaxima
- Archivo de entrega: Tarea8.mac

## Flujo de trabajo recomendado
1. Parsear y validar el formato del grafo.
2. Implementar utilidades de acceso a pesos y vecinos.
3. Implementar TSP exhaustivo (permutaciones).
4. Implementar TSP greedy (nearest neighbor).
5. Probar con ejemplos de SPEC.md.
6. Ajustar formato exacto de salida.

## Modulos necesarios (conceptuales)
- Parser del grafo (lista de adyacencia)
- Utilidades de costos (peso entre dos nodos)
- Enumeracion de rutas (permutaciones)
- Evaluacion de costo de ruta
- Seleccion greedy de siguiente nodo

## Responsabilidades por agente/subsistema
- Analisis de requisitos: mapear restricciones y formato de I/O.
- Modelo de datos: definir representacion exacta del grafo y ruta.
- Algoritmo exhaustivo: permutaciones, evaluacion, minima(s) ruta(s).
- Algoritmo greedy: criterio de seleccion y desempates.
- Verificacion: validar contra ejemplos oficiales.

## Riesgos tecnicos
- Desfase entre formato esperado y formato generado.
- Ambiguedad en desempates del greedy.
- Errores de indexacion en la lista de adyacencia.
- Complejidad alta del exhaustivo para grafos grandes.

## Dependencias
- Ninguna externa; solo funciones base de Maxima.
- Se permite `sort` y `permutations` (segun enunciado).

## Restricciones
- No usar `load(...)` ni librerias externas.
- Respetar nombres exactos de funciones y parametros.
- Salida debe coincidir exactamente con ejemplos.
- Codigo original.

## Convenciones importantes
- Grafo como lista: `[ [nodo, [[vecino, peso], ...]], ... ]`.
- TSP exhaustivo devuelve todas las rutas minimas.
- TSP greedy devuelve una sola ruta.

## Plan por fases
1. Preparacion: lectura de SPEC.md, definir supuestos.
2. Parsing: funciones para localizar nodos y pesos.
3. Modelado de grafo: helpers de acceso a vecinos/pesos.
4. Algoritmos: exhaustivo y greedy.
5. Integracion Maxima: funciones publicas finales.
6. Testing: ejemplos oficiales.
7. Validacion: revisar formato exacto.
8. Optimizacion: micro-mejoras sin cambiar algoritmo.
9. Entrega final: limpieza y comentarios iniciales.

## Supuestos y ambiguedades
- Entrada valida (nodo inicial existe y grafo completo).
- Pesos positivos y simetricos (por ejemplos).
- Desempate greedy por orden de aparicion (documentar).
