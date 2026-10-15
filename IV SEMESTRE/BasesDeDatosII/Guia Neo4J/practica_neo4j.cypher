// Practica Neo4j - Bases de Datos II
// Archivo acumulativo: aqui se guardan Q1 a Q18 conforme las vayamos resolviendo.
// Cada bloque lleva comentario con numero de ejercicio.
// NO pegar aqui el script de creacion de datos, solo las consultas Q1-Q18.

// Q1. Peliculas por decada
MATCH (m:Movie)
WHERE m.released >= 1990 AND m.released <= 1999
RETURN m.title AS titulo, m.released AS anno, m.tagline AS tag
ORDER BY anno ASC, titulo ASC;

// Q2. Reparto de The Matrix
MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
WHERE m.title = 'The Matrix'
RETURN p.name AS actor, r.roles AS roles;

// Q3. Peliculas con sus directores
MATCH (m:Movie)
OPTIONAL MATCH (p:Person)-[:DIRECTED]->(m)
RETURN m.title AS pelicula, collect(p.name) AS directores;

// Q4. Actores nacidos despues de 1965
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE p.born > 1965
RETURN p.name AS actor, p.born AS nacido, count(DISTINCT m) AS cantidadPeliculas
ORDER BY cantidadPeliculas DESC, nacido ASC;

// Q5. Colaboradores de Keanu Reeves
MATCH (keanu:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(colega:Person)
WHERE keanu.name = 'Keanu Reeves' AND colega <> keanu
RETURN colega.name AS colaborador, collect(m.title) AS peliculas;

// Q6. Personas con más de un tipo de participación en películas
MATCH (p:Person)-[r:ACTED_IN|DIRECTED|PRODUCED|WROTE]->(m:Movie)
WITH p,
     collect(DISTINCT type(r)) AS conexiones,
     collect(DISTINCT m.title) AS peliculas
WHERE size(conexiones) > 1
RETURN p.name AS persona, conexiones AS tipos, peliculas AS peliculas, size(peliculas) AS cantidadPeliculas;

// Q7. Peliculas con reparto amplio
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WITH m, collect(p.name) AS actores
WHERE size(actores) >= 5
RETURN m.title AS pelicula, m.released AS anno, size(actores) AS cantidadActores, actores AS actores;

// Q8. Relacion entre usuarios que siguen y resenas
MATCH (seguidor:Person)-[:FOLLOWS]->(seguido:Person)-[r:REVIEWED]->(m:Movie)
OPTIONAL MATCH (seguidor)-[r2:REVIEWED]->(m)
RETURN seguidor.name AS quienSigue,
       seguido.name AS aQuienSigue,
       m.title AS pelicula,
       r.rating AS calificacion,
       r2 IS NOT NULL AS seguidorTambienReseno;

// Q9. Ruta mas corta entre Keanu Reeves y Tom Hanks
MATCH (a:Person {name: 'Keanu Reeves'}), (b:Person {name: 'Tom Hanks'})
MATCH ruta = shortestPath((a)-[:ACTED_IN|DIRECTED|PRODUCED|WROTE*]-(b))
RETURN [n IN nodes(ruta) | coalesce(n.name, n.title)] AS nodosDeLaRuta,
       length(ruta) AS saltos;

// Q10. Recomendacion basada en personas seguidas (James Thompson)
MATCH (james:Person {name: 'James Thompson'})-[:FOLLOWS]->(seguido:Person)-[r:REVIEWED]->(m:Movie)
WHERE NOT (james)-[:REVIEWED]->(m)
RETURN m.title AS peliculaRecomendada,
       collect(DISTINCT seguido.name) AS recomendadaPor,
       avg(r.rating) AS calificacionPromedio
ORDER BY calificacionPromedio DESC;

// Q11. Actores con mayor red de colaboracion
MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(colega:Person)
WHERE actor <> colega
RETURN actor.name AS actor,
       count(DISTINCT colega) AS colaboradoresDistintos
ORDER BY colaboradoresDistintos DESC
LIMIT 10;

// Q12. Numero de Bacon
MATCH (bacon:Person {name: 'Kevin Bacon'}), (p:Person)
WHERE p <> bacon
MATCH ruta = shortestPath((bacon)-[:ACTED_IN*]-(p))
RETURN p.name AS persona,
       length(ruta) / 2 AS numeroDeBacon
ORDER BY numeroDeBacon ASC, persona ASC
LIMIT 20;

// Q13. Personas que actuaron y dirigieron
MATCH (p:Person)-[:ACTED_IN]->(peliActuada:Movie)
WITH p, collect(DISTINCT peliActuada.title) AS peliculasActuadas
MATCH (p)-[:DIRECTED]->(peliDirigida:Movie)
RETURN p.name AS persona,
       peliculasActuadas,
       collect(DISTINCT peliDirigida.title) AS peliculasDirigidas;

// Q14. Actores con multiples roles en una misma pelicula
MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
WHERE size(r.roles) > 1
RETURN p.name AS actor,
       m.title AS pelicula,
       r.roles AS roles,
       size(r.roles) AS cantidadRoles;

// Q15. Peliculas similares por actores compartidos
MATCH (m1:Movie)<-[:ACTED_IN]-(p:Person)-[:ACTED_IN]->(m2:Movie)
WHERE m1.title < m2.title
WITH m1, m2, collect(DISTINCT p.name) AS actoresCompartidos
WHERE size(actoresCompartidos) >= 2
RETURN m1.title AS pelicula1,
       m2.title AS pelicula2,
       actoresCompartidos,
       size(actoresCompartidos) AS similitud
ORDER BY similitud DESC;

// Q16. Crear relaciones de colaboracion COLLABORATED_WITH
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(b:Person)
WHERE a.name < b.name
WITH a, b, collect(DISTINCT m.title) AS peliculasCompartidas
MERGE (a)-[c:COLLABORATED_WITH]->(b)
SET c.movies = peliculasCompartidas,
    c.count = size(peliculasCompartidas);

// Q17. Consultar las colaboraciones materializadas
MATCH (a:Person)-[c:COLLABORATED_WITH]->(b:Person)
RETURN a.name AS persona1,
       b.name AS persona2,
       c.count AS peliculasCompartidas,
       c.movies AS peliculas
ORDER BY c.count DESC
LIMIT 10;

// Q18. Comparacion con EXPLAIN y PROFILE
// Q18a media (Q4) EXPLAIN
EXPLAIN
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE p.born > 1965
RETURN p.name AS actor, p.born AS nacido, count(DISTINCT m) AS cantidadPeliculas
ORDER BY cantidadPeliculas DESC, nacido ASC;
// Q18a media (Q4) PROFILE
PROFILE
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE p.born > 1965
RETURN p.name AS actor, p.born AS nacido, count(DISTINCT m) AS cantidadPeliculas
ORDER BY cantidadPeliculas DESC, nacido ASC;
// Q18b dificil con agregacion (Q11) EXPLAIN
EXPLAIN
MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(colega:Person)
WHERE actor <> colega
RETURN actor.name AS actor,
       count(DISTINCT colega) AS colaboradoresDistintos
ORDER BY colaboradoresDistintos DESC
LIMIT 10;
// Q18b dificil con agregacion (Q11) PROFILE
PROFILE
MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(colega:Person)
WHERE actor <> colega
RETURN actor.name AS actor,
       count(DISTINCT colega) AS colaboradoresDistintos
ORDER BY colaboradoresDistintos DESC
LIMIT 10;
