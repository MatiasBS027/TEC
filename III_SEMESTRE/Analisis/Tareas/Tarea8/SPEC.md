# Análisis de Algoritmos

## TSP

\\\ Indicaciones Generales.

> El tiempo estimado para la realización de la tarea es de 3 horas.
> La tarea se debe realizar de forma individual.
> Se podrá hacer únicamente 1 entrega (upload) de su tarea.
En caso que se hagan varios uploads, se revisará únicamente la primera entrega realizada.
> Debe entregar su tarea en un archivo de texto de extensión .mac que sea reconocido para cargar en wxmaxima.
> Debe realizar su tarea en el lenguaje de wxmaxima, sin utilizar ninguna biblioteca adicional.
Es decir no puede usar el comando load(...) para subir una biblioteca adicional al lenguaje base.
Si se permite el uso del comando "sort", o cualquiera de sus variantes.
Debe utilizar el algoritmo Exhaustivo TSP con permutaciones visto en clase.
Debe utilizar el algoritmo Greedy TSP visto en clase.
No se permite el uso de ningún otro algoritmo.
Puede programar el algoritmo de cualquier forma, ya sea en iteración o en recursión.
> Todo el código que se presente debe ser completamente original y escrito por quienes realizaron la tarea.
No se permite copiar/cargar/descargar código de otros sitios.
> La respuesta a una pregunta teórico/práctica que no requiera programación debe ser original y propia.
Escrita por quienes realizaron la tarea.
No se permite copiar/cargar/descargar respuestas de otros sitios.
> Al inicio de la tarea, debe poner en comentarios la siguiente información:
Carné y nombre de quienes hicieron la tarea.
Documentación adicional que considere importante.
Respuesta a alguna pregunta planteada en la tarea
> Debe utilizar exactamente los nombres de las funciones, los parámetros y la impresión que se solicita.
Las funciones deben devolver exactamente lo que se solicita.
> El programa debe compilar correctamente.
> En caso que tenga que hacer un análisis del BigOh del programa,
deberá realizarlo utilizando la misma técnica que se usó en las clases.
Se debe presentar primero en programa, después del mismo entre comentarios, se copia de nuevo el programa y se hace el análisis con la indentación adecuada.
> Si no se siguen todas las indicaciones dada en la tarea, de no hacerlo tendrá una nota de 0.

\\\ Descripción de la Tarea.

El objetivo de la tarea es hacer dos programas:

1. Un programa que implemente el proceso de TSP Exhaustivo visto en clase.

2. Un programa que implemente el proceso de TSP Greedy visto en clase.

\\\ Primer Ejemplo.

Suponga que se tienen el siguiente grafo:

grafo:
[
[ c1, [ [c2,10], [c3,15], [c4,20] ] ],
[ c2, [ [c1,10], [c3,35], [c4,25] ] ],
[ c3, [ [c1,15], [c2,35], [c4,30] ] ],
[ c4, [ [c1,20], [c2,25], [c3,30] ] ]
];

(%i) tspPermu(c1,grafo);
(%o) [ [[c1,c2,c4,c3,c1],80],
[[c1,c3,c4,c2,c1],80]
]

(%i) tspGreedy(c1,grafo);
(%o) [[c1,c2,c4,c3,c1],80]

\\\ Segundo Ejemplo.

grafo:
[
[ c1, [ [c2, 1], [c3,15], [c4,90] ] ],
[ c2, [ [c1, 1], [c3, 1], [c4,25] ] ],
[ c3, [ [c1,15], [c2, 1], [c4, 1] ] ],
[ c4, [ [c1,90], [c2,25], [c3, 1] ] ]
];

(%i) tspPermu(c1,grafo);
(%o) [ [[c1,c2,c4,c3,c1],42],
[[c1,c3,c4,c2,c1],42]
]

(%i) tspGreedy(c1,grafo);
(%o) [[c1,c2,c3,c4,c1],93]

\\\ Tercer Ejemplo.

grafo:
[
[c1, [[c1,1000], [c2, 10], [c3, 20], [c4, 9], [c5, 7], [c6, 6]] ],
[c2, [[c1, 10], [c2,1000], [c3, 10], [c4, 5], [c5, 6], [c6, 4]] ],
[c3, [[c1, 20], [c2, 10], [c3,1000], [c4, 8], [c5, 9], [c6, 7]] ],
[c4, [[c1, 9], [c2, 5], [c3, 8], [c4,1000], [c5, 6], [c6, 5]] ],
[c5, [[c1, 7], [c2, 6], [c3, 9], [c4, 6], [c5,1000], [c6, 1]] ],
[c6, [[c1, 6], [c2, 4], [c3, 7], [c4, 5], [c5, 1], [c6,1000]] ]
];

(%i) tspPermu(c1,grafo);
(%o) [ [[c1,c2,c4,c3,c6,c5,c1],38],
[[c1,c5,c6,c3,c4,c2,c1],38]
]

(%i) tspGreedy(c1,grafo);
(%o) [[c1,c6,c5,c2,c4,c3,c1], 46]

\\\ Cuarto Ejemplo.

grafo:
[
[c1, [[c1,1000], [c2, 10], [c3, 20], [c4, 9], [c5, 7], [c6, 6]] ],
[c2, [[c1, 10], [c2,1000], [c3, 10], [c4, 5], [c5, 6], [c6, 4]] ],
[c3, [[c1, 20], [c2, 10], [c3,1000], [c4, 8], [c5, 9], [c6, 7]] ],
[c4, [[c1, 9], [c2, 5], [c3, 8], [c4,1000], [c5, 6], [c6, 5]] ],
[c5, [[c1, 7], [c2, 6], [c3, 9], [c4, 6], [c5,1000], [c6, 1]] ],
[c6, [[c1, 6], [c2, 4], [c3, 7], [c4, 5], [c5, 1], [c6,1000]] ]
];

(%i) tspPermu(c3,grafo);
(%o) [ [[c3,c4,c2,c1,c5,c6,c3],38],
      [[c3,c6,c5,c1,c2,c4,c3],38]
     ]

(%i) tspGreedy(c3,grafo);
(%o) [[c3,c6,c5,c2,c4,c1,c3],48]

\\\ Algunas Funciones de Máxima.

Puede utilizar las siguientes instrucciones:

(%i) per: permutations([a,b,c]);
(%o) {[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]}

(%i) listify(per);
(%o) [[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]]

\\\ Rúbrica de Calificación.

Criterios:

> Programa tspPermu................. 45pts
Programa no funciona 0pts
Programa no funciona correctamente 0pts
Programa funciona correctamente 45pts
> Programa tspGreedy................ 45pts
Programa no funciona 0pts
Programa no funciona correctamente 0pts
Programa funciona correctamente 45pts
> Desarrollo adecuado del programa...10pts*
Se revisa:
Salida solicitada para la revisión.
Buenas técnicas de programación.
Integración de las partes.
Seguimiento del algoritmo.
Otros elementos

No se tiene lo solicitado 0pts
Desarrollo no es completo 0pts
Desarrollo está completo 10pts

> Total............................ 100pts

* Solo se obtiene los puntos
si las secciones anteriores
funcionan correctamente.
