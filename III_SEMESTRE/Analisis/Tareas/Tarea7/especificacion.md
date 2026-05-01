\\ Indicaciones Generales.

El tiempo estimado para la realización de la tarea es de 3 horas.

Puede realizar la tarea de forma individual o en grupos de 2 personas.

Se podrá hacer únicamente 1 entrega (upload) de su tarea.

Si trabaja en grupo, únicamente 1 de los dos miembros del grupo pueden hacer la entrega de la tarea.

Debe entregar su tarea en un archivo de texto de extensión .mac que sea reconocido para cargar en wxmaxima.

Debe realizar su tarea en el lenguaje de wxmaxima, sin utilizar ninguna biblioteca adicional.

Es decir no puede usar el comando load(...) para subir una biblioteca adicional al lenguaje base.

Todo el código que se presente debe ser completamente original y escrito por quienes realizaron la tarea.

No se permite copiar/cargar/descargar código de otros sitios.

La respuesta a una pregunta teórico/práctica que no requiera programación debe ser original y propia.

Escrita por quienes realizaron la tarea.

No se permite copiar/cargar/descargar respuestas de otros sitios.

Al inicio de la tarea, debe poner en comentarios la siguiente información:

Carné y nombre de quienes hicieron la tarea.

Documentación adicional que considere importante.

Respuesta a alguna pregunta planteada en la tarea

Se debe utilizar el algoritmo indicado en clase, no se puede utilizar otro.

Debe utilizar el algoritmo de vecinos/extender.

Todas las funciones deben programarse en recursión o con map.

Por lo tanto no se permite el uso de for, while, repeat, unless, makelist,

ni ninguna instrucción de iteración.

Debe utilizar exactamente los nombres de las funciones, los parámetros y la impresión que se solicita.

Las funciones deben devolver exactamente lo que se solicita.

El programa debe compilar correctamente.

Su programa debe resolver por lo menos hasta el caso de n=8,

en un tiempo menor a 30 segs en la computadora donde se hace la revisión.

En caso que tenga que hacer un análisis del BigOh del programa,

deberá realizarlo utilizando la misma técnica que se usó en las clases.

Se debe presentar primero en programa, después del mismo entre comentarios,

se copia de nuevo el programa y se hace el análisis con la indentación adecuada.

Si no se siguen todas las indicaciones dada en la tarea, de no hacerlo tendrá una nota de 0.

\\ Descripción de la Tarea.

Este problema apareció alrededor de 1848 y fue descrito por el jugador de ajedrez Max Bezzel utilizando el tablero del juego del ajedrez.

El objetivo de la tarea es hacer un programa que implemente el proceso de backtracking en la versión de vecino/extender, para resolver el problema de colocar "n" reinas sin que se ataquen en un tablero de dimensiones "nxn".

Dado un valor de n, por ejemplo n=4, se deben colocar 4 reinas, en un tablero con 4 filas y 4 columnas, de manera tal que ninguna de las reinas se encuentren en la misma fila, o en la misma columna o en la misma diagonal.

\\ Descripción de los Funciones.

A continuación vamos a explicar el proceso general, utilizando un tablero de dimensiones 4x4. El programa final debe funcionar para cualquier tamaño de tablero.

Se va a ir colocando una reina en cada fila. Una vez que se coloca una reina se sigue a la fila siguiente. Si en algún momento no es posible colocar una nueva reina, entonces se debe hacer backtracking con la reina anterior.

La función "vecinos".

Esta función muestra los posibles espacios disponibles en la siguiente fila.

(%i) vecinos(4,[1,1]);
(%o) [[2,1],[2,2],[2,3],[2,4]]

(%i) vecinos(4,[1,2]);
(%o) [[2,1],[2,2],[2,3],[2,4]]

La función "extender".

Dada una ruta, la función extender selecciona los vecinos que se pueden agregar a esa ruta. Generando un nuevo conjunto de rutas.

(%i) extender(4,[[1,1]]);
(%o) [ [[1,1],[2,3]], [[1,1],[2,4]] ]

(%i) extender(4,[[1,2],[2,4]]);
(%o) [[[1,2],[2,4],[3,1]]]

La función "prof"

La función "prof", utiliza las dos funciones anteriores para generar un proceso de forward/backtrack

(%i) prof(4);
(%o) [[1,2],[2,4],[3,1],[4,3]]

La función "profTodas".

Esta función continua el proceso de búsqueda para encontrar todas las soluciones.

(%i) profTodas(4);
(%o) [ [[1,2],[2,4],[3,1],[4,3]], [[1,3],[2,1],[3,4],[4,2]] ]

Para llegar a ese resultado, se realizan los siguientes pasos.
Estos pasos no se deben imprimir.
Solamente se muestran para que vean como debe funcionar el programa.

[ [[1,1]],
[[1,2]],
[[1,3]],
[[1,4]]
]

[ [[1,1],[2,3]], ---> No se puede extender!
[[1,1],[2,4]],
[[1,2]],
[[1,3]],
[[1,4]]
]

[ [[1,1],[2,4]],
[[1,2]],
[[1,3]],
[[1,4]]
]

[ [[1,1],[2,4],[3,2]], --> No se puede extender!
[[1,2]],
[[1,3]],
[[1,4]]
]

[ [[1,2]],
[[1,3]],
[[1,4]]
]

[ [[1,2],[2,4]],
[[1,3]],
[[1,4]]
]

[ [[1,2],[2,4],[3,1]],
[[1,3]],
[[1,4]]
]

[ [[1,2],[2,4],[3,1],[4,3]], --> Se tiene una solución
[[1,3]],
[[1,4]]
]

[[[1,3]],
[[1,4]]
]

[[[1,3],[2,1]],
[[1,4]]
]

[ [[1,3],[2,1],[3,4]],
[[1,4]]]

[ [[1,3],[2,1],[3,4],[4,2]], --> Se tiene una solución
[[1,4]]
]

[ [[1,4]]
]

[ [[1,4],[2,1]],
[[1,4],[2,2]]
]

[ [[1,4],[2,1],[3,3]], --> No se puede extender!
[[1,4],[2,2]]
]

[ [[1,4],[2,2]] --> No se puede extender!
]

[]

(%o) [ [[1,2],[2,4],[3,1],[4,3]],
[[1,3],[2,1],[3,4],[4,2]]
]

Observe las soluciones que brinda:

Primera solución:

[[1,2],[2,4],[3,1],[4,3]]

[x, R, x, x]
[x, x, x, R]
[R, x, x, x]
[x, x, R, x]

Segunda solución:

[[1,3],[2,1],[3,4],[4,2]]

[x, x, R, x]
[R, x, x, x]
[x, x, x, R]
[x, R, x, x]

\\ Un Tablero de Tamaño 8.

Aquí damos una solución para un tablero de tamaño 8:

[[1,1],[2,5],[3,8],[4,6],[5,3],[6,7],[7,2],[8,4]]

[R, x, x, x, x, x, x,x],
[x, x, x, x, R, x, x,x],
[x, x, x, x, x, x, x,R],
[x, x, x, x, x, R, x,x],
[x, x, R, x, x, x, x,x],
[x, x, x, x, x, x, R,x],
[x, R, x, x, x, x, x,x],
[x, x, x, R, x, x, x,x]

\\ Cómo debe funcionar la tarea?

La tarea debe tener la siguientes funciones.

Y debe producir los siguientes resultados.

(%i) vecinos(4,[1,2]);
(%o) [[2,1],[2,2],[2,3],[2,4]]

(%i) extender(4,[[1,2],[2,4]]);
(%o) [[[1,2],[2,4],[3,1]]]

(%i) prof(4);
(%o) [[1,2],[2,4],[3,1],[4,3]]

(%i) profTodas(4);
(%o) [ [[1,2],[2,4],[3,1],[4,3]], [[1,3],[2,1],[3,4],[4,2]] ]

\\ Número de Soluciones.

Para 1 reina : 1 solución.
Para 2 reinas: 0 soluciones.
Para 3 reinas: 0 soluciones.
Para 4 reinas: 2 soluciones.
Para 5 reinas: 10 soluciones.
Para 6 reinas: 4 soluciones.
Para 7 reinas: 40 soluciones.
Para 8 reinas: 92 soluciones.
Para 9 reinas: 352 soluciones.()
Para 10 reinas: 724 soluciones.()
Para 11 reinas: 2680 soluciones.()
Para 12 reinas: 14200 soluciones.()

(*) Este programa de backtracking,
con vecinos/extender probablemente no puede
resolver este tamaño de problema.
Su tarea debe resolver el problema por lo menos
hasta un tablero de tamaño 8, en menos de 30segs

\\ Rúbrica de Calificación.

Criterios:

Programa vecinos................ 10pts
Programa no funciona 0pts
Programa no funciona correctamente 0pts
Programa funciona correctamente 10pts

Programa extender................. 30pts*
Programa no funciona 0pts
Programa no funciona correctamente 0pts
Programa funciona correctamente 30pts

Programa prof..................... 30pts*
Programa no funciona 0pts
Programa no funciona correctamente 0pts
Programa funciona correctamente 30pts

Programa profTodas................ 30pts*
Programa no funciona 0pts
Programa no funciona correctamente 0pts
Programa funciona correctamente 25pts

Total............................ 100pts

Solo se obtienen estos puntos
si los elementos anteriores funcionan
correctamente.

Además, para que los elementos mencionados anteriormente
estén correctos debe cumplir con:
Programación en recursión correcta.
Adecuado uso del algoritmo.
Integración de las funciones.
Resultados correctos hasta n=8
El resultado debe permitir que se aplique la función length(profTodas(n)).