# Práctica de Redis — Introducción a Redis

**Integrantes:** Matias Benavides Sandoval — 2025102376  
**Curso:** Bases de Datos II (IC-4302)

---

## 1. Strings

### 8. Añade el texto `" (IC-4302)"` al final del valor de `nombre_curso`.

**Comando de Redis:**

```redis
APPEND nombre_curso " (IC-4302)"
```

**Salida o resultado:**

```text
(integer) 26
```

---

### 9. Obtén el nuevo valor de `nombre_curso`.

**Comando de Redis:**

```redis
GET nombre_curso
```

**Salida o resultado:**

```text
"Bases de Datos II(IC-4302)"
```

---

### 10. Obtén la longitud del valor almacenado en `nombre_curso`.

**Comando de Redis:**

```redis
STRLEN nombre_curso
```

**Salida o resultado:**

```text
(integer) 26
```

---



### 11. Establece múltiples claves a la vez: `profesor` con valor `"Kenneth Obando"` y `semestre` con valor `"I"`.

**Comando de Redis:**

```redis
MSET profesor "Kenneth Obando" semestre "II"
```

**Salida o resultado:**

```text
OK
```

---



### 12. Obtén los valores de `profesor` y `semestre` en un solo comando.

**Comando de Redis:**

```redis
MGET profesor semestre
```

**Salida o resultado:**

```text
1) "Kenneth Obando"
2) "II"
```

---



## 2. Listas — `motores_db`



### 5. Obtén los elementos del índice 1 al 2.

**Comando de Redis:**

```redis
LRANGE motores_db 1 2
```

**Salida o resultado:**

```text
1) "PostgeSQL"
2) "Oracle"
```

---



### 6. Obtén y elimina el primer elemento (izquierda) de la lista `motores_db`. ¿Qué elemento se eliminó?

**Comando de Redis:**

```redis
LPOP motores_db
```

**Salida o resultado:**

```text
"SQL Server"
```

> **Elemento eliminado:** `SQL Server`.

---



### 7. Obtén y elimina el último elemento (derecha) de la lista `motores_db`. ¿Qué elemento se eliminó?

**Comando de Redis:**

```redis
RPOP motores_db
```

**Salida o resultado:**

```text
"MySQL"
```

> **Elemento eliminado:** `MySQL`.

---



### 8. Obtén la longitud actual de la lista `motores_db`.

**Comando de Redis:**

```redis
LLEN motores_db
```

**Salida o resultado:**

```text
(integer) 2
```

---



### 9. Obtén los elementos restantes de la lista `motores_db`.

**Comando de Redis:**

```redis
LRANGE motores_db 0 -1
```

**Salida o resultado:**

```text
1) "PostgeSQL"
2) "Oracle"
```

---



## 3. Sets — `temas_curso`



### 5. Verifica si `"Seguridad"` es miembro del set `temas_curso`.

**Comando de Redis:**

```redis
SISMEMBER temas_curso "Seguridad"
```

**Salida o resultado:**

```text
(integer) 1
```

---



### 6. Verifica si `"Big Data"` es miembro del set `temas_curso`.

**Comando de Redis:**

```redis
SISMEMBER temas_curso "Big Data"
```

**Salida o resultado:**

```text
(integer) 0
```

---



### 7. Elimina `"Transacciones"` del set `temas_curso`. (es que lo escribi mal profe)

**Comando de Redis:**

```redis
SREM temas_curso "Transacciones"
```

**Salida o resultado:**

```text
(integer) 0
```

**Verificación y corrección realizada:**

```redis
SMEMBERS temas_curso
```

```text
1) "Transcciones"
2) "Replicacion"
3) "Seguridad"
4) "Optimizacion"
```

```redis
SREM temas_curso "Transcciones"
```

```text
(integer) 1
```

```text
SMEMBERS temas_curso
```

```text
1) "Replicacion"
2) "Seguridad"
3) "Optimizacion"
```

---



### 8. Obtén la cantidad de elementos (cardinalidad) en el set `temas_curso`.

**Comando de Redis:**

```redis
SCARD temas_curso
```

**Salida o resultado:**

```text
(integer) 4
```

**Valor final después de la corrección:**

```redis
SCARD temas_curso
```

```text
(integer) 3
```

---



### 9. Obtén todos los miembros restantes del set `temas_curso`.

**Comando de Redis:**

```redis
SMEMBERS temas_curso
```

**Salida o resultado:**

```text
1) "Replicacion"
2) "Seguridad"
3) "Optimizacion"
```

---



## 4. Hashes — `estudiante:101`



### 5. Obtén solo los nombres de los campos (keys) del hash `estudiante:101`.

**Comando de Redis:**

```redis
HKEYS estudiante:101
```

**Salida o resultado:**

```text
1) "nombre"
2) "apellido"
3) "email"
```

---



### 6. Obtén solo los valores de los campos del hash `estudiante:101`.

**Comando de Redis:**

```redis
HVALS estudiante:101
```

**Salida o resultado:**

```text
1) "Ana"
2) "Solano"
3) "ana.solano@email.com"
```

---



### 7. Elimina el campo `carnet` del hash `estudiante:101`.

**Comando de Redis:**

```redis
HDEL estudiante:101 carnet
```

**Salida o resultado:**

```text
(integer) 1
```

---



### 8. Obtén el número de campos en el hash `estudiante:101`.

**Comando de Redis:**

```redis
HLEN estudiante:101
```

**Salida o resultado:**

```text
(integer) 3
```

---



### 9. Obtén todos los campos y valores restantes de `estudiante:101`.

**Comando de Redis:**

```redis
HGETALL estudiante:101
```

**Salida o resultado:**

```text
1) "nombre"
2) "Ana"
3) "apellido"
4) "Solano"
5) "email"
6) "ana.solano@email.com"
```



## 5. Sorted Sets — `ranking_proyectos`



### 6. Obtén el ranking (posición, basada en 0) de `"Proyecto Gama"` (ordenado de menor a mayor score).

**Comando de Redis:**

```redis
ZRANK ranking_proyectos "Proyecto Gama"
```

**Salida o resultado:**

```text
(integer) 2
```

**Intento previo con clave en singular:**

```redis
ZRANK ranking_proyecto "Proyecto Gama"
```

```text
(nil)
```

---



### 7. Obtén el score de `"Proyecto Alfa"`.

**Comando de Redis:**

```redis
ZSCORE ranking_proyectos "Proyecto Alfa"
```

**Salida o resultado:**

```text
"95"
```

---



### 8. Obtén la cantidad de miembros en `ranking_proyectos`.

**Comando de Redis:**

```redis
ZCARD ranking_proyectos
```

**Salida o resultado:**

```text
(integer) 4
```

**Verificación adicional — orden de mayor a menor con scores:**

```redis
ZREVRANGE ranking_proyectos 0 -1 WITHSCORES
```

```text
1) "Proyecto Alfa"
2) "95"
3) "Proyecto Gama"
4) "92"
5) "Proyecto Delta"
6) "88"
7) "Proyecto Beta"
8) "88"
```



## 6. Administración de Claves



### 8. Establece un tiempo de expiración de 60 segundos para la clave `temas_curso`.

**Comando de Redis:**

```redis
EXPIRE temas_curso 60
```

**Salida o resultado:**

```text
(integer) 1
```

---



### 9. Consulta el tiempo restante (en segundos) antes de que la clave `temas_curso` expire. Ejecútalo varias veces para ver cómo disminuye.

**Comando de Redis (ejecutado varias veces):**

```redis
TTL temas_curso
```

**Salida o resultado (disminuye con cada ejecución):**

```text
(integer) 53
(integer) 52
(integer) 51
(integer) 50
(integer) 49
(integer) 48
...
(integer) 22
...
(integer) 3
(integer) 1
(integer) -2
```

> La clave expiró al llegar a `-2` (no existe).

---



### 10. Consulta el tiempo de expiración de una clave que no tiene expiración, como `nombre_curso`. ¿Qué devuelve?

**Comando de Redis:**

```redis
TTL nombre_curso
```

**Salida o resultado:**

```text
(integer) -1
```

> Devuelve `-1`: la clave existe pero no tiene expiración.

---



### 11. Consulta el tiempo de expiración de una clave que no existe, como `creditos`. ¿Qué devuelve?

**Comando de Redis:**

```redis
TTL creditos
```

**Salida o resultado:**

```text
(integer) -2
```

> Devuelve `-2`: la clave no existe.

---



### 12. Elimina todas las claves de la base de datos actual.

**Comando de Redis:**

```redis
FLUSHDB
```

**Salida o resultado:**

```text
OK
```

---



### 13. Verifica que no queden claves.

**Comando de Redis:**

```redis
KEYS *
```

**Salida o resultado:**

```text
(empty array)
```

---



## 7. Capturas de pantalla — RedisInsight



### Captura 1 — Strings (`nombre_curso`)

![Vista de claves String en RedisInsight](./Captura%201%20de%20Redis.png)

### Captura 2 — Hash (`estudiante:101`)

![Vista del hash estudiante:101 en RedisInsight](./Captura%202%20de%20Redis.png)

### Captura 3 — Sorted Set (`ranking_proyectos`)

![Vista del sorted set ranking_proyectos en RedisInsight](./Captura%203%20de%20Redis.png)

### Captura 4 — Base vacía tras `FLUSHDB`

![Vista de RedisInsight sin claves tras FLUSHDB](./Captura 4 de Redis (Tras es FLUSHDB).png)