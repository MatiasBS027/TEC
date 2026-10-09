# Práctica de MongoDB — Sistema de Gestión de Películas (`cineDB`)

**Integrantes:** Matias Benavides Sandoval — 2025102376
**Curso:** Bases de Datos II (IC-4302)

> Base de datos: `cineDB` · Colección: `peliculas`. Cada ejercicio incluye un breve comentario de lo que hace el comando, el comando exacto utilizado y la respuesta obtenida (según lo pedido en las Notas de la guía).

---

## 1. Preparación del entorno

### Selección de la base de datos `cineDB`.

**Comentario:** Se selecciona (y crea si no existe) la base de datos `cineDB` para trabajar en ella.

**Comando de MongoDB:**

```js
use cineDB
```

---

## 2. Parte 1 — Inserción de datos

### Insertar documentos realistas en la colección `peliculas` (6 documentos: 2 de Peter Jackson, Matrix, Inception, Interstellar y Tenet).

**Comentario:** `insertMany` inserta varios documentos de una sola vez con el esquema `titulo, director, genero, año_estreno, rating, reparto[{nombre, rol}], ingresos`.

**Comando de MongoDB:**

```js
db.peliculas.insertMany([
  { titulo: "El Señor de los Anillos: La Comunidad del Anillo", director: "Peter Jackson", genero: "Fantasía", año_estreno: 2001, rating: 8.8, reparto: [{ nombre: "Elijah Wood", rol: "Frodo" }, { nombre: "Ian McKellen", rol: "Gandalf" }], ingresos: 870000000 },
  { titulo: "El Señor de los Anillos: Las Dos Torres", director: "Peter Jackson", genero: "Fantasía", año_estreno: 2002, rating: 8.8, reparto: [{ nombre: "Elijah Wood", rol: "Frodo" }, { nombre: "Ian McKellen", rol: "Gandalf" }], ingresos: 926000000 },
  { titulo: "Matrix", director: "Lana Wachowski", genero: "Ciencia Ficción", año_estreno: 1999, rating: 8.7, reparto: [{ nombre: "Keanu Reeves", rol: "Neo" }, { nombre: "Laurence Fishburne", rol: "Morfeo" }], ingresos: 467000000 },
  { titulo: "Inception", director: "Christopher Nolan", genero: "Ciencia Ficción", año_estreno: 2010, rating: 8.8, reparto: [{ nombre: "Leonardo DiCaprio", rol: "Cobb" }, { nombre: "Anne Hathaway", rol: "Ariadne" }], ingresos: 836000000 },
  { titulo: "Interstellar", director: "Christopher Nolan", genero: "Ciencia Ficción", año_estreno: 2014, rating: 8.6, reparto: [{ nombre: "Matthew McConaughey", rol: "Cooper" }, { nombre: "Anne Hathaway", rol: "Brand" }], ingresos: 677500000 },
  { titulo: "Tenet", director: "Christopher Nolan", genero: "Ciencia Ficción", año_estreno: 2020, rating: 7.4, reparto: [{ nombre: "Robert Pattinson", rol: "Neil" }], ingresos: 365000000 }
])
```

**Salida o resultado:**

```text
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ac82f6f7fe79043743a76a5'),
    '1': ObjectId('6ac82f6f7fe79043743a76a6'),
    '2': ObjectId('6ac82f6f7fe79043743a76a7'),
    '3': ObjectId('6ac82f6f7fe79043743a76a8'),
    '4': ObjectId('6ac82f6f7fe79043743a76a9'),
    '5': ObjectId('6ac82f6f7fe79043743a76aa')
  }
}
```

---

### Verificar la cantidad de documentos insertados.

**Comentario:** `countDocuments` cuenta los documentos de la colección para confirmar la inserción.

**Comando de MongoDB:**

```js
db.peliculas.countDocuments({})
```

**Salida o resultado:**

```text
6
```

---

## 3. Parte 2 — Actualización de documentos

### a. Actualizar el rating de la película "Matrix" a 9.0.

**Comentario:** `updateOne` con filtro `{ titulo: "Matrix" }` y operador `$set` modifica solo el campo `rating` del primer documento que coincida.

**Comando de MongoDB:**

```js
db.peliculas.updateOne({ titulo: "Matrix" }, { $set: { rating: 9.0 } })
```

**Salida o resultado:**

```text
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

---

### b. Añadir un nuevo actor al reparto de "Matrix": Carrie-Anne Moss como Trinity.

**Comentario:** `updateOne` con operador `$push` agrega un subdocumento `{ nombre, rol }` al final del arreglo `reparto` sin tocar el resto del documento.

**Comando de MongoDB:**

```js
db.peliculas.updateOne({"titulo":"Matrix"}, {$push:{"reparto": {"nombre": "Carrie-Anne Moss", "rol": "Trinity"}}})
```

**Salida o resultado:**

```text
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

**Verificación:**

```js
db.peliculas.find({"titulo":"Matrix"})
```

```text
[
  {
    _id: ObjectId('6ac82f6f7fe79043743a76a7'),
    titulo: 'Matrix',
    director: 'Lana Wachowski',
    genero: 'Ciencia Ficción',
    'año_estreno': 1999,
    rating: 9,
    reparto: [
      { nombre: 'Keanu Reeves', rol: 'Neo' },
      { nombre: 'Laurence Fishburne', rol: 'Morfeo' },
      { nombre: 'Carrie-Anne Moss', rol: 'Trinity' }
    ],
    ingresos: 467000000
  }
]
```

---

## 4. Parte 3 — Consultas simples (`find`)

### a. Encontrar todas las películas dirigidas por "Peter Jackson".

**Comentario:** `find` con filtro de igualdad por `director` devuelve todos los documentos de ese director.

**Comando de MongoDB:**

```js
db.peliculas.find({"director":"Peter Jackson"})
```

**Salida o resultado:**

```text
[
  {
    _id: ObjectId('6ac82f6f7fe79043743a76a5'),
    titulo: 'El Señor de los Anillos: La Comunidad del Anillo',
    director: 'Peter Jackson',
    genero: 'Fantasía',
    'año_estreno': 2001,
    rating: 8.8,
    reparto: [
      { nombre: 'Elijah Wood', rol: 'Frodo' },
      { nombre: 'Ian McKellen', rol: 'Gandalf' }
    ],
    ingresos: 870000000
  },
  {
    _id: ObjectId('6ac82f6f7fe79043743a76a6'),
    titulo: 'El Señor de los Anillos: Las Dos Torres',
    director: 'Peter Jackson',
    genero: 'Fantasía',
    'año_estreno': 2002,
    rating: 8.8,
    reparto: [
      { nombre: 'Elijah Wood', rol: 'Frodo' },
      { nombre: 'Ian McKellen', rol: 'Gandalf' }
    ],
    ingresos: 926000000
  }
]
```

---

### b. Encontrar todas las películas de género "Ciencia Ficción" con rating mayor o igual a 8.5.

**Comentario:** `find` combina filtro de igualdad en `genero` con operador de comparación `$gte` en `rating` para exigir ambas condiciones a la vez; la proyección muestra solo los campos de interés.

**Comando de MongoDB:**

```js
db.peliculas.find({ genero: "Ciencia Ficción", rating: { $gte: 8.5 } }, { _id: 0, titulo: 1, genero: 1, rating: 1 }).toArray()
```

**Salida o resultado:**

```text
[
  { titulo: 'Matrix', genero: 'Ciencia Ficción', rating: 9 },
  { titulo: 'Inception', genero: 'Ciencia Ficción', rating: 8.8 },
  { titulo: 'Interstellar', genero: 'Ciencia Ficción', rating: 8.6 }
]
```


---

## 5. Parte 4 — Agregaciones avanzadas (`aggregate`)

### a. Mostrar el número total de películas por cada género.

**Comentario:** El pipeline agrupa con `$group` por `$genero` contando con `$sum: 1`.

**Comando de MongoDB:**

```js
db.peliculas.aggregate({$group:{_id: "$genero", total:{$sum:1}}})
```

**Salida o resultado:**

```text
[
  { _id: 'Ciencia Ficción', total: 4 },
  { _id: 'Fantasía', total: 2 }
]
```

---

### b. Mostrar el promedio de rating de todas las películas agrupadas por género.

**Comentario:** `$group` con acumulador `$avg: "$rating"` calcula el promedio por género.

**Comando de MongoDB:**

```js
db.peliculas.aggregate({$group:{_id: "$genero", promedio_rating :{$avg:"$rating"}}})
```

**Salida o resultado:**

```text
[
  { _id: 'Fantasía', promedio_rating: 8.8 },
  { _id: 'Ciencia Ficción', promedio_rating: 8.45 }
]
```

---

### c. Mostrar el título e ingresos de las 3 películas con mayores ingresos.

**Comentario:** `$sort: { ingresos: -1 }` ordena de mayor a menor ingreso, `$limit: 3` se queda con el top 3 y `$project` muestra solo `titulo` e `ingresos`.

**Comando de MongoDB:**

```js
db.peliculas.aggregate([{ $sort: { "ingresos": -1 } },{ $limit: 3 },{ $project: { _id: 0, "titulo": 1, "ingresos": 1 } }])
```

**Salida o resultado:**

```text
[
  { titulo: 'El Señor de los Anillos: Las Dos Torres', ingresos: 926000000 },
  { titulo: 'El Señor de los Anillos: La Comunidad del Anillo', ingresos: 870000000 },
  { titulo: 'Inception', ingresos: 836000000 }
]
```

---

### d. Mostrar el total de ingresos generados por todas las películas dirigidas por "Peter Jackson".

**Comentario:** `$match` filtra solo las de Peter Jackson y `$group` con `$sum: "$ingresos"` acumula el total.

**Comando de MongoDB:**

```js
db.peliculas.aggregate([{ $match: { "director": "Peter Jackson" } },{ $group: { _id: "$director", total_ingresos: { $sum: "$ingresos" } } }])
```

**Salida o resultado:**

```text
[
  { _id: 'Peter Jackson', total_ingresos: 1796000000 }
]
```


---

### e. Encontrar el actor que más veces ha aparecido en películas y la cantidad de apariciones.

**Comentario:** `$unwind: "$reparto"` crea un documento por cada actor del arreglo, `$group` cuenta apariciones por nombre, `$sort` ordena de mayor a menor, `$limit: 1` se queda con el primero y `$project` le da el formato `{ actor, apariciones }`.

**Comando de MongoDB:**

```js
db.peliculas.aggregate([{ $unwind: "$reparto" },{ $group: { _id: "$reparto.nombre", apariciones: { $sum: 1 } } },{ $sort: { apariciones: -1 } },{ $limit: 1 },{ $project: { _id: 0, actor: "$_id", apariciones: 1 } }])
```

**Salida o resultado:**

```text
[
  { apariciones: 2, actor: 'Ian McKellen' }
]
```

**Tabla completa (mismo pipeline sin `$limit`):**

```text
[
  { apariciones: 2, actor: 'Elijah Wood' },
  { apariciones: 2, actor: 'Ian McKellen' },
  { apariciones: 2, actor: 'Anne Hathaway' },
  { apariciones: 1, actor: 'Matthew McConaughey' },
  { apariciones: 1, actor: 'Carrie-Anne Moss' },
  { apariciones: 1, actor: 'Keanu Reeves' },
  { apariciones: 1, actor: 'Leonardo DiCaprio' },
  { apariciones: 1, actor: 'Laurence Fishburne' },
  { apariciones: 1, actor: 'Robert Pattinson' }
]
```

---

## 6. Parte 5 — Eliminación de documentos

### a. Eliminar todas las películas con un rating menor a 6.0 (se inserta antes "Dragon Ball Evolution" con rating 2.7 para demostrar el borrado).

**Comentario:** `insertOne` agrega la película de rating bajo y luego `deleteMany` con filtro `{ rating: { $lt: 6.0 } }` borra todos los documentos con rating menor a 6.0.

**Comando de MongoDB:**

```js
db.peliculas.insertOne({
  "titulo": "Dragon Ball Evolution",
  "director": "James Wong",
  "genero": "Acción",
  "año_estreno": 2009,
  "rating": 2.7,
  "reparto": [
    { "nombre": "Justin Chatwin", "rol": "Goku" },
    { "nombre": "Emmy Rossum", "rol": "Bulma" },
    { "nombre": "Chow Yun-fat", "rol": "Maestro Roshi" }
  ],
  "ingresos": 56000000
})
```

**Salida o resultado:**

```text
{
  acknowledged: true,
  insertedId: ObjectId('6ac82f8003b42cd0f437be3b')
}
```

```js
db.peliculas.deleteMany({ "rating": { $lt: 6.0 } })
```

```text
{
  acknowledged: true,
  deletedCount: 1
}
```

---

### b. Eliminar la película cuyo título sea "Matrix".

**Comentario:** `deleteOne` con filtro de igualdad `{ titulo: "Matrix" }` borra únicamente ese documento.

**Comando de MongoDB:**

```js
db.peliculas.deleteOne({ "titulo": "Matrix" })
```

**Salida o resultado:**

```text
{
  acknowledged: true,
  deletedCount: 1
}
```

---

### Verificación final — documentos restantes.

**Comentario:** `countDocuments` confirma el estado final: de 6 documentos (+1 insertado para la prueba) se eliminaron 2, quedan 5.

**Comando de MongoDB:**

```js
db.peliculas.countDocuments({})
```

**Salida o resultado:**

```text
COUNT FINAL=5
```
