# Análisis de Algoritmos

## KNN

\\\ Indicaciones Generales.

> El tiempo estimado para la realización de la tarea es de 3 horas.
> Esta tarea se debe realizar de forma individual.
> Se podrá hacer únicamente 1 entrega (upload) de su tarea.
> Debe entregar su tarea en un archivo de texto (extensión .mac) que sea reconocido para cargar en wxmaxima.
> Debe realizar su tarea en el lenguaje de wxmaxima, sin utilizar ninguna biblioteca adicional.
Es decir no puede usar el comando load(...) para subir una biblioteca adicional al lenguaje base.
Debe utilizar el algoritmo KNN.
No debe normalizar los datos.
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
Respuesta a alguna pregunta planteada en la tarea
> Se debe utilizar el algoritmo indicado en clase, no se puede utilizar otro.
> Debe utilizar exactamente los nombres de las funciones, los parámetros y la impresión que se solicita.
Las funciones deben devolver exactamente lo que se solicita.
> El programa debe compilar correctamente.
> En caso que tenga que hacer un análisis del BigOh del programa, deberá realizarlo utilizando la misma técnica que se usó en las clases.
Se debe presentar primero en programa, después del mismo entre comentarios, se copia de nuevo el programa y se hace el análisis con la indentación adecuada.
> Si no se siguen todas las indicaciones dada en la tarea, de no hacerlo tendrá una nota de 0.

\\\ Descripción de la Tarea.

El objetivo de la tarea es hacer un programa que implemente el algoritmo de KNN, sin normalizar los datos.

\\\ Descripción de los Funciones.

A continuación se muestran los datos y el resultado que se debe presentar.

\\\ Primer Ejemplo.

(%i) datos;
(%o) [  [a,[5,1,0,300]],
        [b,[3,1,1,225]],
        [c,[1,1,0, 75]],
        [d,[3,0,1,200]],
        [e,[4,0,0,150]],
        [f,[2,0,0, 50]]
        ]

(%i) dat:first(datos);
(%o) [a,[5,1,0,300]]

(%i) ide(dat);
(%o) a

(%i) xs(dat);
(%o) [5,1,0]

(%i) ys(dat);
(%o) 300

(%i) distancia
    (
        [5,1,0],
        [3,1,1]
        );
(%o) 2.23606797749979

(%i) knn(
            [4,1,0],
            3,
        datos
        );
(%o) 225

(%i) knn(
            [4,1,0],
            5,
            datos
        );
(%o) 185

\\\ Segundo Ejemplo.

datos:

[ [a, [ 1,1,1,1,1,
        1,0,0,0,1,
        1,1,1,1,1,
        1,0,0,0,1,
        1,0,0,0,1,
        100]],

  [b, [ 1,1,1,1,0,
        1,0,0,0,1,
        1,1,1,1,0,
        1,0,0,0,1,
        1,1,1,1,0,
        200]],

  [c, [ 1,1,1,1,1,
        1,0,0,0,0,
        1,0,0,0,0,
        1,0,0,0,0,
        1,1,1,1,1,
        300]]

];

(%i) knn( [ 0,0,1,0,0,
            0,1,0,1,0,
            0,1,1,1,0,
            0,1,0,1,0,
            1,0,0,0,1
            ],
            1,
            datos
            );
(%o) 100

\\\ Rúbrica de Calificación.

Criterios:

> Encontrar los K vecinos .......... 30pts
Programa no funciona                0pts
Programa no funciona correctamente  0pts
Programa funciona correctamente    30pts
> Realizar la regresión ............ 60pts*
Programa no funciona                0pts
Programa no funciona correctamente  0pts
Programa funciona correctamente    60pts
> Desarrollo adecuado del programa...10pts*
(
Impresión solicitada
para la revisión.
Buenas técnicas de programación.
Integración de las partes.
Seguimiento del algoritmo.
Otros elementos
)
No se tiene lo solicitado          0pts
Desarrollo no es completo          0pts
Desarrollo está completo          10pts
> Total............................ 100pts

* Solo se obtienen los puntos
si funciona correctamente
la parte anterior.
