# Análisis de Algoritmos

## DP Knapsack

\\\ Indicaciones Generales.

> El tiempo estimado para la realización de la tarea es de 3 horas.
> Esta tarea se debe realizar de forma individual.
> Se podrá hacer únicamente 1 entrega (upload) de su tarea.
  En caso de realizar más de 1 upload, se revisará únicamente la primera entrega realizada.
> Debe entregar su tarea en un archivo de texto (extensión .mac) que sea reconocido para cargar en wxmaxima.
> Debe realizar su tarea en el lenguaje de wxmaxima, sin utilizar ninguna biblioteca adicional.
Es decir no puede usar el comando load(...) para subir una biblioteca adicional al lenguaje base.
Debe utilizar el algoritmo DP, Dynamic Programming visto en clase, que tiene tiempo O(n*w).
No se permite el uso de memoization de wxmaxima.
No se permite el uso de ningún otro algoritmo.
> Todo el código que se presente debe ser completamente original y escrito por quienes realizaron la tarea.
No se permite copiar/cargar/descargar código de otros sitios.
Puede utilizar y modificar el código que les ha sido mostrado en clase.
> La respuesta a una pregunta teórico/práctica que no requiera programación debe ser original y propia.
Escrita por quienes realizaron la tarea.
No se permite copiar/cargar/descargar respuestas de otros sitios.
> Al inicio de la tarea, debe poner en comentarios la siguiente información:
Carné y nombre de quienes hicieron la tarea.
Documentación adicional que considere importante.
Respuesta a alguna pregunta planteada en la tarea.
> Se debe utilizar el algoritmo indicado en clase, no se puede utilizar otro.
> Debe utilizar exactamente los nombres de las funciones, los parámetros y la impresión que se solicita.
Las funciones deben devolver exactamente lo que se solicita.

El programa debe compilar correctamente.
> En caso que tenga que hacer un análisis del BigOh del programa, deberá realizarlo utilizando la misma técnica que se usó en las clases.
Se debe presentar primero en programa, después, se copia de nuevo el programa entre comentarios y se hace el análisis con la indentación adecuada. El programa no debe tener ningún análisis del BigOh y el análisis de BigOh no debe tener comentarios adicionales.
> Si no se siguen todas las indicaciones dada en la tarea, de no hacerlo tendrá una nota de 0.

\\\ Descripción de la Tarea.

El objetivo de la tarea es hacer un programa que implemente el proceso de la mochila utilizando programación dinámica de sobre una matriz.
Se desea aumentar la velocidad del algoritmo utilizando más memoria por medio de Programación Dinámica.

\\\ Descripción de los Funciones.

A continuación se muestran los datos y el resultado que se debe presentar.
Observe que debe construir una matriz, en la cual debe ir poniendo los datos respectivos.

\\\ Primer Ejemplo.

(%i) objetos:
[
[g, [1500,1]],
[s, [3000,4]],
[l, [2000,3]],
[i, [2000,1]]
]

(%i) ks(4,objetos):
[
[xx,  1,            2,              3,              4          ],
[g,  [1500,[g]],  [1500,[g]  ],  [1500,[g]  ],  [1500,[g]  ]],
[s,  [1500,[g]],  [1500,[g]  ],  [1500,[g]  ],  [3000,[s]  ]],
[l,  [1500,[g]],  [1500,[g]  ],  [2000,[l]  ],  [3500,[g,l]]],
[i,  [2000,[i]],  [3500,[g,i]],  [3500,[g,i]],  [4000,[l,i]]]
]

\\\ Segundo Ejemplo.

(%i) objetos:
[
[w, [70,1]],
[g, [60,1]],
[n, [90,2]],
[b, [90,4]],
[s, [80,1]]
]

(%i) ks(4,objetos);
[
[xx,  1,          2,            3,              4            ],
[w,  [70,[w]],  [70, [w]  ],  [70, [w]    ],  [70, [w]    ]],
[g,  [70,[w]],  [130,[w,g]],  [130,[w,g]  ],  [130,[w,g]  ]],
[n,  [70,[w]],  [130,[w,g]],  [160,[w,n]  ],  [220,[w,g,n]]],
[b,  [70,[w]],  [130,[w,g]],  [160,[w,n]  ],  [220,[w,g,n]]],
[s,  [80,[s]],  [150,[w,s]],  [210,[w,g,s]],  [240,[w,n,s]]]
]

\\\ Tercer Ejemplo.

(%i) objetos:
[
[a, [10, 2]],
[b, [20, 3]],
[c, [50, 4]],
[d, [60, 5]]
];

(%i3) ks(8,objetos);
[
[xx,  1,        2,          3,          4,          5,            6,            7,            8        ],
[a,  [0,[]],  [10,[a]],  [10,[a]],  [10,[a]],  [10,[a]  ],  [10,[a]  ],  [10,[a]  ],  [10,[a]  ]],
[b,  [0,[]],  [10,[a]],  [20,[b]],  [20,[b]],  [30,[a,b]],  [30,[a,b]],  [30,[a,b]],  [30,[a,b]]],
[c,  [0,[]],  [10,[a]],  [20,[b]],  [50,[c]],  [50,[c]  ],  [60,[a,c]],  [70,[b,c]],  [70,[b,c]]],
[d,  [0,[]],  [10,[a]],  [20,[b]],  [50,[c]],  [60,[d]  ],  [60,[a,c]],  [70,[b,c]],  [80,[b,d]]]
]

\\\ Rúbrica de Calificación.

Criterios:

> Matriz con valores correctos...... 30pts
  Programa no funciona                0pts
  Programa no funciona correctamente  0pts
  Programa funciona correctamente    30pts
> Programa ks....................... 60pts*
  Programa no funciona                0pts
  Programa no funciona correctamente  0pts
  Programa funciona correctamente    60pts
> Desarrollo adecuado del programa...10pts*
  (
    Impresión solicitada
    para la revisión, la matriz.
    Buenas técnicas de programación.
    Integración de las partes.
    Seguimiento del algoritmo.
    Otros elementos
  )
  No se tiene lo solicitado          0pts
  Desarrollo no es completo          0pts
  Desarrollo está completo          10pts
> Total............................ 100pts

* Solo se reciben puntos si la sección
    anterior funciona correctamente.
