
1

Automatic Zoom
"Análisis de Algoritmos"
José Helo Guzmán
 __
/ _   _  __  __  _|         /\  |  _   _   _ . |_  |_   _   _
\__) |  (-_ (-_ (_| \/     /--\ | (_) (_) |  | |_  | ) ||| _)
                    /             _/
               
 _   _   _|    
(_| | ) (_|    
               
____            ____
 |   |_   __     |    _  _       __ | .  _   _
 |   | ) (-_     |   |  (_| \/  (-_ | | | ) (_)
                                            _/
 ___                                          __
(__   _  |  __  _   _   __  _  _   _   _     |__)  _  _  |_  |  __  _
___) (_| | (-_ _)  |_) (-_ |  _)  (_) | )    |    |  (_) |_) | (-_ |||
                   |
Contenido
▬▬▬ 1. Introducción.
▬▬▬ 2. Descripción del Problema.
▬▬▬ 3. Estructura del Problema.
▬▬▬ 4. Solución de Forma Exhaustiva.
▬▬▬ 5. Análisis de Complejidad Algoritmo Exhaustivo.
▬▬▬ 6. Solución con un Algoritmo Greedy.
▬▬▬ 7. El Algoritmo Greedy es Aproximado.
▬▬▬ 8. Análisis de Complejidad del Algoritmo Greedy.
▬▬▬ 9. Resumen.
▬▬▬ 10. Ejercicios.
▬▬▬ 1. Introducción.
El problema del “traveling salesperson problem”, conocido por sus siglas TSP, es
un problema clásico y difícil de resolver.
▬▬▬ 2. Descripción del Problema.
Tenemos un conjunto de ciudades, y las distancias que conectan cada una de estas
ciudades. El problema consiste en encontrar la ruta más corta que visita cada
ciudad una única vez y regresa al punto de inicio.
El grafo está completamente conectado, para cada ciudad existe una ruta hacia las
demás ciudades. Existe lo que se conoce como un “ciclo de Hamilton” en el grafo.
Tiene que existir un recorrido completo que pase por todas las ciudades. De los
posibles recorridos, deseamos encontrar el de menor distancia.
▬▬▬ 3. Estructura del Problema.
Supongamos que tenemos el siguiente grafo no dirigido.
        10
(c1)─────────(c2)
  │ ╲        ╱│
  │  ╲20    ╱ │ 
  │   ╲    ╱  │
  │    ╲  ╱   │
15│     ╲╱    │25
  │     ╱╲    │
  │    ╱  ╲   │
  │   ╱    ╲  │
  │  ╱35    ╲ │ 
  │ ╱        ╲│
(c3)─────────(c4)
        30
El grafo suele representarse en diferentes libros de texo mediante una matriz.
Observe que se pone un valor muy alto, denominado “M” en la diagonal, pues no
deseamos que la ruta contenga la misma ciudad más de una vez.
──────────────────────
     c1   c2   c3   c4
──────────────────────
c1    M   10   15   20     
c2   10    M   35   25
c3   15   35    M   30 
c4   20   25   30    M
──────────────────────
De la misma forma, podemos representar el problema por medio de una lista de nodos
adyacentes. Se pueden utilizar estas dos representaciones.
grafo:
[
[ c1, [ [c1,1000], [c2,  10], [c3,  15], [c4,  20] ],
