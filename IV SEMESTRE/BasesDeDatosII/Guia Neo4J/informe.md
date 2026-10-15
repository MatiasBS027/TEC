# Informe — Práctica de Laboratorio Neo4j
## Bases de Datos II — Prof. Kenneth Obando Rodríguez

## 1. Portada
- Curso: Bases de Datos II, Sede Central Cartago
- Práctica: construcción, consulta y análisis de base de datos orientada a grafos en Neo4j con Cypher
- Entregables: `practica_neo4j.cypher`, informe PDF, `README.md`, evidencias de carga

## 2. Ambiente utilizado
- Neo4j Desktop 2.2.1, instancia local `practica-neo4j`, base `neo4j`, usuario `neo4j`
- Versión DBMS 2026.09.0, lenguaje Cypher 25
- La ventana de PowerShell del DBMS se minimiza (no se cierra) para mantener la instancia en ejecución
- Datos generados con IA según autorización del docente (el script original no fue provisto)

## 3. Evidencia de carga de datos
- Restricciones: `movie_title_unique` sobre `Movie.title`, `person_name_unique` sobre `Person.name` (`SHOW CONSTRAINTS`)
- Nodos: 36 (24 `Person`, 12 `Movie`) — ver `evidencias/Q16a.png` y conteo `MATCH (n)`
- Relaciones: 48 (`ACTED_IN` 27, `DIRECTED` 6, `PRODUCED` 4, `WROTE` 4, `REVIEWED` 5, `FOLLOWS` 2)
- Propiedades: `title, released, tagline, name, born, roles, rating, summary`
- Modelo: `(Person)-[:ACTED_IN {roles}]->(Movie)`, `(Person)-[:DIRECTED|PRODUCED|WROTE]->(Movie)`, `(Person)-[:REVIEWED {summary, rating}]->(Movie)`, `(Person)-[:FOLLOWS]->(Person)`

## 4. Resultados Q1–Q18

### Q1. Películas por década (media)
- Propósito: listar películas 1990–1999 con título, año y lema
- Patrón: `MATCH (m:Movie) WHERE m.released >= 1990 AND <= 1999 RETURN ... ORDER BY anno, titulo`
- Resultado: 7 filas (`A Few Good Men` 1992 … `The Matrix` 1999). Evidencia `evidencias/Q1.png`, `Q1.csv`
- Utilidad real: catálogos y filtros por rango en streaming

### Q2. Reparto de The Matrix (media)
- Propósito: actores y roles de una película específica
- Patrón: `(p:Person)-[r:ACTED_IN]->(m:Movie)` + filtro por título; `r.roles` es lista
- Resultado: 6 actores (Keanu/Neo, Laurence/Morpheus, Carrie/Trinity, Hugo/Smith, Joe/Cypher, Alice/extra)
- Utilidad: ficha de reparto

### Q3. Películas con sus directores (media)
- Propósito: todas las películas con directores agrupados
- Patrón: `MATCH (m)` + `OPTIONAL MATCH (p)-[:DIRECTED]->(m)` + `collect(p.name)` para no perder películas sin director
- Resultado: 12 películas; ej. The Matrix [Lana, Lilly]; varias con lista vacía (John Wick, Speed…)
- Utilidad: vista completa aunque falten relaciones

### Q4. Actores nacidos después de 1965 (media)
- Propósito: personas jóvenes con conteo de películas
- Patrón: `(p)-[:ACTED_IN]->(m)` + `WHERE p.born > 1965` + `count(DISTINCT m)` (el MATCH ya garantiza ≥1)
- Resultado: 3 (Carrie-Anne Moss 1967, Robin Wright 1966, Alice Johnson 1990, 1 c/u)
- Utilidad: segmentación por edad y actividad

### Q5. Colaboradores de Keanu Reeves (media-alta)
- Propósito: quiénes actuaron con Keanu y en qué películas
- Patrón: `(keanu)-[:ACTED_IN]->(m)<-[:ACTED_IN]-(colega)` + `colega <> keanu` + `collect(m.title)`
- Resultado: 6 colaboradores; Laurence Fishburne [Matrix, John Wick]; resto 1 película
- Utilidad: red de co-actuación

### Q6. Personas con múltiples funciones (media-alta)
- Propósito: ≥2 tipos de relación entre ACTED_IN/DIRECTED/PRODUCED/WROTE
- Patrón: `[r:ACTED_IN|DIRECTED|PRODUCED|WROTE]` + `collect(DISTINCT type(r))` + `size(...) > 1`
- Resultado: 5; ej. Keanu [ACTED_IN, PRODUCED, DIRECTED] 4 películas; Lana/Lilly [DIRECTED, WROTE]
- Utilidad: detectar perfiles multifuncionales

### Q7. Películas con reparto amplio (media-alta)
- Propósito: películas con ≥5 actores
- Patrón: agrupar por película `collect(p.name)` + `size(...) >= 5`
- Resultado: 1 (The Matrix, 6 actores)
- Utilidad: detectar producciones de elenco grande

### Q8. Seguidos y reseñas (media-alta)
- Propósito: reseñas de personas seguidas + si el seguidor también la reseñó
- Patrón: `(seguidor)-[:FOLLOWS]->(seguido)-[r:REVIEWED]->(m)` + `OPTIONAL MATCH (seguidor)-[r2:REVIEWED]->(m)` + `r2 IS NOT NULL`
- Resultado: 4 filas (James→Alice→Matrix/Forrest, James→Bob→Forrest/Apollo)
- Utilidad: feed social de reseñas

### Q9. Ruta más corta Keanu–Tom Hanks (difícil)
- Propósito: distancia en el grafo de participación
- Patrón: `shortestPath((a)-[:ACTED_IN|DIRECTED|PRODUCED|WROTE*]-(b))` sin dirección + `coalesce(n.name, n.title)` + `length(p)`
- Resultado: [Keanu, Matrix, Hugo Weaving, Cloud Atlas, Tom Hanks], 4 saltos
- Utilidad: grados de separación en redes

### Q10. Recomendación para James Thompson (difícil)
- Propósito: recomendar por seguidos excluyendo ya vistas
- Patrón: `(j)-[:FOLLOWS]->(s)-[r:REVIEWED]->(m)` + `WHERE NOT (j)-[:REVIEWED]->(m)` + `collect(s.name), avg(r.rating)`
- Resultado: Forrest Gump [Alice, Bob] 4.5; Apollo 13 [Bob] 4.0 (Matrix excluida, ya la vio)
- Utilidad: recomendador colaborativo simple

### Q11. Mayor red de colaboración (difícil)
- Propósito: top 10 por co-actores distintos
- Patrón: `(a1)-[:ACTED_IN]->(m)<-[:ACTED_IN]-(a2)` + `a1 <> a2` + `count(DISTINCT a2)` + `ORDER BY DESC LIMIT 10`
- Resultado: 10 filas (ver `Q11.csv`)
- Utilidad: centralidad en red de colaboración

### Q12. Número de Bacon (difícil)
- Propósito: distancia en películas desde Kevin Bacon solo con ACTED_IN
- Patrón: `shortestPath((p)-[:ACTED_IN*]-(kb))` + `length/2` (2 saltos = 1 película)
- Resultado: 12 alcanzables (Bill Paxton y Tom Hanks = 1 … Keanu = 3); resto aislado (Pulp Fiction) sin ruta. Por eso salen 12 y no 20
- Utilidad: métrica de cercanía en redes

### Q13. Actuaron y dirigieron (difícil)
- Propósito: ambas funciones aunque sea en distintas películas
- Patrón: dos MATCH separados sobre `p`: uno `ACTED_IN`, otro `DIRECTED` + `collect`
- Resultado: 1 (Keanu: actuó en Matrix/John Wick/Speed; dirigió Man of Tai Chi)
- Utilidad: separar condiciones que no deben ir en el mismo patrón

### Q14. Múltiples roles en una película (difícil)
- Propósito: actores con >1 rol en el mismo filme
- Patrón: `(p)-[r:ACTED_IN]->(m)` + `WHERE size(r.roles) > 1`
- Resultado: 2 (Tom Hanks en Cloud Atlas 3 roles; Hugo Weaving en Cloud Atlas 2 roles)
- Utilidad: explotar propiedades lista

### Q15. Películas similares por actores (difícil)
- Propósito: pares con ≥2 actores en común + puntaje
- Patrón: `(m1)<-[:ACTED_IN]-(p)-[:ACTED_IN]->(m2)` + `m1.title < m2.title` (evita duplicados sin usar IDs internos) + `collect` + `size >= 2`
- Resultado: 1 par (John Wick–The Matrix [Keanu, Laurence], similitud 2)
- Utilidad: similitud por solapamiento

### Q16. Materializar COLLABORATED_WITH (actualización)
- Propósito: relación derivada entre co-actores con `movies` y `count`, una sola vez por par
- Patrón: `MATCH (a)-[:ACTED_IN]->(m)<-[:ACTED_IN]-(b) WHERE a.name < b.name WITH ... collect MERGE (a)-[c:COLLABORATED_WITH]->(b) SET ...`
- Resultado: `Created 30 relationships, set 60 properties` (`evidencias/Q16.png`)
- Cambio en el grafo: 30 aristas nuevas persona→persona con lista y conteo; se ejecuta después de Q1–Q15 para no contaminar

### Q17. Colaboraciones materializadas (actualización)
- Propósito: top 10 por `c.count`
- Patrón: `MATCH (a)-[c:COLLABORATED_WITH]->(b) RETURN ... ORDER BY c.count DESC LIMIT 10`
- Resultado: 10 filas (ver `Q17.csv`)
- Utilidad: leer conocimiento derivado sin recalcular

### Q18. EXPLAIN y PROFILE (análisis)
- Q4 (media): plan con `NodeByLabelScan`/`Filter`/`Expand` + agregación; pocas filas, bajo costo
- Q11 (difícil con agregación): doble `Expand` por el patrón triangular + `count(DISTINCT)` + `Sort` + `Limit`; muchas filas intermedias, costo mayor
- Mejoras: apoyarse en constraints (índices en `name/title`), evitar cartesiano separando MATCH por nombre único, acotar `*` con límite superior, filtrar `<>` temprano
- Evidencias: `Q18a–d.txt`, `evidencias/Q18A–D.png`

## 5. Análisis de consultas complejas
- Las rutas (`shortestPath`, longitud variable) generan avisos O3N90 (producto cartesiano por `(a),(b)` desconectados — inofensivo con nombres únicos) y O3N91 (patrón `*` sin cota — conviene `*..10` en grafos grandes)
- Las agregaciones (`collect`, `count(DISTINCT)`, `avg`) obligan a agrupar y ordenar; el `WHERE` de pares (`m1.title < m2.title`, `a.name < b.name`) evita duplicados sin depender de IDs internos
- Materializar (`MERGE` + `SET`) traslada cómputo a escritura para lecturas rápidas posteriores

## 6. Conclusiones técnicas
- Cypher expresa recorridos que en SQL requerirían múltiples joins recursivos
- `OPTIONAL MATCH` preserva nodos sin relación; `collect` ignora nulos
- El isomorfismo de relaciones evita auto-matches accidentales, pero se deja el filtro `<>` por seguridad
- El orden de ejecución importa: derivar conocimiento (Q16) al final preserva la reproducibilidad de Q1–Q15
