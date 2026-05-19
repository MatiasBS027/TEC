# PLAN

## Roadmap detallado
| Fase | Objetivo | Dependencias | Dificultad |
| --- | --- | --- | --- |
| 1. Preparacion | Extraer requisitos y formato exacto | Ninguna | Baja |
| 2. Parsing | Localizar nodos y pesos en lista | 1 | Media |
| 3. Modelado grafo | Helpers de vecinos y costo de ruta | 2 | Media |
| 4. Algoritmo exhaustivo | Permutaciones y minimo(s) | 3 | Alta |
| 5. Algoritmo greedy | Seleccion nearest neighbor | 3 | Media |
| 6. Integracion Maxima | Funciones publicas y salidas | 4-5 | Media |
| 7. Testing | Ejemplos de SPEC.md | 6 | Media |
| 8. Validacion | Formato exacto y supuestos | 7 | Baja |
| 9. Optimizacion | Refactor sin cambiar algoritmo | 8 | Baja |
| 10. Entrega | Comentarios iniciales y limpieza | 9 | Baja |

## Tareas ordenadas
1. Releer SPEC.md y APUNTES.md, resumir restricciones.
2. Definir formato de grafo y ruta (lista de nodos, con retorno al inicio).
3. Diseñar helpers: obtener vecinos, peso(u,v), costoRuta.
4. Exhaustivo:
   - Generar permutaciones de nodos (sin repetir inicio).
   - Construir rutas completas y calcular costo.
   - Filtrar rutas minimas, devolver todas las de menor costo.
5. Greedy:
   - Iniciar en nodo base.
   - Elegir vecino no visitado de menor costo.
   - Cerrar ciclo al final.
6. Validar contra cuatro ejemplos de SPEC.md.
7. Ajustar formato exacto de salida.

## Prioridades
1. Formato de entrada/salida exacto.
2. Exhaustivo correcto.
3. Greedy correcto.
4. Helpers simples y legibles.

## Milestones
- M1: Helpers de acceso al grafo listos.
- M2: tspPermu devuelve rutas minimas correctas.
- M3: tspGreedy devuelve ruta greedy correcta.
- M4: Ejemplos oficiales pasan sin cambios.

## Dependencias entre tareas
- Greedy y exhaustivo dependen de helpers de grafo.
- Validacion depende de implementaciones completas.

## Orden recomendado de implementacion
1. Preparacion
2. Parsing
3. Modelado del grafo
4. Algoritmo Exhaustivo
5. Algoritmo Greedy
6. Integracion con Maxima
7. Testing
8. Validacion
9. Optimizacion
10. Entrega final

## Notas de estimacion
- Exhaustivo es la parte mas costosa por permutaciones.
- Greedy es mas simple, pero sensible a desempates.

## Supuestos
- Grafo completo y pesos validos.
- No se requiere manejo de errores para entradas invalidas (documentar si se implementa).
