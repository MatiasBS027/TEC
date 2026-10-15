# Práctica Neo4j — Bases de Datos II

## Ambiente
- Neo4j Desktop 2.2.1 (instancia local `practica-neo4j`, DBMS Neo4j 2026.09.0, base `neo4j`, usuario `neo4j`)
- Alternativas válidas según la guía: Neo4j Desktop, AuraDB o Docker.

## Carga de datos
1. Crear instancia vacía en Neo4j Desktop.
2. Abrir la herramienta `Query` y ejecutar por bloques, en orden:
   - Bloque 1: `CREATE CONSTRAINT` de unicidad en `Movie.title` y `Person.name`.
   - Bloque 2: nodos `Movie` (12) y `Person` (24) con `MERGE`.
   - Bloque 3: relaciones `ACTED_IN` con propiedad `roles`.
   - Bloque 4: relaciones `DIRECTED`, `PRODUCED`, `WROTE`.
   - Bloque 5: relaciones `FOLLOWS` y `REVIEWED` con `summary` y `rating`.
3. Verificar con:
   ```cypher
   SHOW CONSTRAINTS;
   MATCH (n) RETURN labels(n) AS etiquetas, count(n) AS cantidad ORDER BY cantidad DESC;
   MATCH ()-[r]->() RETURN type(r) AS relacion, count(r) AS cantidad ORDER BY cantidad DESC;
   ```
   Esperado: 36 nodos (24 Person, 12 Movie), 48 relaciones
   (ACTED_IN, DIRECTED, PRODUCED, WROTE, REVIEWED, FOLLOWS).

## Ejecución de consultas
- Archivo `practica_neo4j.cypher` contiene Q1–Q18, cada una con comentario `// Qn`.
- Ejecutar Q1–Q15 **antes** de Q16, porque Q16 materializa `:COLLABORATED_WITH` y modifica el grafo.
- Q16 crea relaciones derivadas una sola vez por par (`WHERE a.name < b.name` + `MERGE`).
- Q18: anteponer `EXPLAIN` / `PROFILE` a la consulta elegida (Q4 media, Q11 difícil).

## Evidencias
- `evidencias/Qn.png`: captura de cada resultado en Neo4j Query.
- `Qn.csv`: tabla descargada desde Query (`Download CSV`).
- `Q18*.txt`: planes de ejecución en texto plano.

## Entregables (zip para TecDigital)
- `practica_neo4j.cypher`
- Informe PDF
- `README.md` (este archivo)
- Capturas de carga correcta
