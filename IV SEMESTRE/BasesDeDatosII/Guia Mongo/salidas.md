cineDB> db.peliculas.find({"director":"Peter Jackson"})
[
  {
    _id: ObjectId('6ac826ebd956e32f036ad371'),
    titulo: 'El Señor de los Anillos: La Comunidad del Anillo',
    director: 'Peter Jackson',
  {
    _id: ObjectId('6ac826ebd956e32f036ad371'),
    titulo: 'El Señor de los Anillos: La Comunidad del Anillo',
    director: 'Peter Jackson',
    genero: 'Fantasía',
    'año_estreno': 2001,
    rating: 8.8,
    genero: 'Fantasía',
    'año_estreno': 2001,
    rating: 8.8,
    reparto: [
    'año_estreno': 2001,
    rating: 8.8,
    reparto: [
      { nombre: 'Elijah Wood', rol: 'Frodo' },
    reparto: [
      { nombre: 'Elijah Wood', rol: 'Frodo' },
      { nombre: 'Ian McKellen', rol: 'Gandalf' }
      { nombre: 'Elijah Wood', rol: 'Frodo' },
      { nombre: 'Ian McKellen', rol: 'Gandalf' }
    ],
      { nombre: 'Ian McKellen', rol: 'Gandalf' }
    ],
    ingresos: 870000000
    ],
    ingresos: 870000000
    ingresos: 870000000
  },
  },
  {
    _id: ObjectId('6ac826ebd956e32f036ad372'),
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


cineDB> db.peliculas.updateOne({"titulo":"Matrix"}, {$push:{"reparto": {"nombre": "Carrie-Anne Moss", "rol": "Trinity"}}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
cineDB> db.peliculas.find({"titulo":"Matrix"})
[
  {
    _id: ObjectId('6ac826ebd956e32f036ad373'),
    titulo: 'Matrix',
    director: 'Lana Wachowski',
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
cineDB> db.peliculas.find({"titulo":"Matrix"})
[
  {
    _id: ObjectId('6ac826ebd956e32f036ad373'),
    titulo: 'Matrix',
    director: 'Lana Wachowski',
  modifiedCount: 1,
  upsertedCount: 0
}
cineDB> db.peliculas.find({"titulo":"Matrix"})
[
  {
    _id: ObjectId('6ac826ebd956e32f036ad373'),
    titulo: 'Matrix',
    director: 'Lana Wachowski',
  upsertedCount: 0
}
cineDB> db.peliculas.find({"titulo":"Matrix"})
[
  {
    _id: ObjectId('6ac826ebd956e32f036ad373'),
    titulo: 'Matrix',
    director: 'Lana Wachowski',
cineDB> db.peliculas.find({"titulo":"Matrix"})
[
  {
    _id: ObjectId('6ac826ebd956e32f036ad373'),
    titulo: 'Matrix',
    director: 'Lana Wachowski',
[
  {
    _id: ObjectId('6ac826ebd956e32f036ad373'),
    titulo: 'Matrix',
    director: 'Lana Wachowski',
    genero: 'Ciencia Ficción',
    'año_estreno': 1999,
    rating: 9,
    reparto: [
    _id: ObjectId('6ac826ebd956e32f036ad373'),
    titulo: 'Matrix',
    director: 'Lana Wachowski',
    genero: 'Ciencia Ficción',
    'año_estreno': 1999,
    rating: 9,
    reparto: [
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
      { nombre: 'Keanu Reeves', rol: 'Neo' },
      { nombre: 'Laurence Fishburne', rol: 'Morfeo' },
      { nombre: 'Carrie-Anne Moss', rol: 'Trinity' }
    ],
    ingresos: 467000000
  }
]
cineDB> db.peliculas.find({"director":"Peter Jackson"})
[
    ],
    ingresos: 467000000
  }
]
cineDB> db.peliculas.find({"director":"Peter Jackson"})
[
  {
    _id: ObjectId('6ac826ebd956e32f036ad371'),
    titulo: 'El Señor de los Anillos: La Comunidad del Anillo',
    director: 'Peter Jackson',
]



cineDB> db.peliculas.aggregate({$group:{_id: "$genero", total:{$sum:1}}})
[ { _id: 'Fantasía', total: 2 }, { _id: 'Ciencia Ficción', total: 4 } ]



cineDB> db.peliculas.aggregate({$group:{_id: "$genero", promedio_rating :{$avg:"$rating"}}})
[
  { _id: 'Ciencia Ficción', promedio_rating: 8.45 },
  { _id: 'Fantasía', promedio_rating: 8.8 }
]



cineDB> db.peliculas.aggregate([{ $sort: { "ingresos": -1 } },{ $limit: 3 },{ $project: { _id: 0, "titulo": 1, "ingresos": 1 } }])
[
  {
    titulo: 'El Señor de los Anillos: Las Dos Torres',
    ingresos: 926000000
  },
  {
    titulo: 'El Señor de los Anillos: La Comunidad del Anillo',
    ingresos: 870000000
  },
  { titulo: 'Inception', ingresos: 836000000 }
]


cineDB> db.peliculas.aggregate([{ $match: { "director": "Peter Jackson" } },{ $group: { _id: "$director", total_ingresos: { $sum: "$ingresos" } } }])
[ { _id: 'Peter Jackson', total_ingresos: 1796000000 } ]


cineDB> db.peliculas.aggregate([{ $unwind: "$reparto" },{ $group: { _id: "$reparto.nombre", apariciones: { $sum: 1 } } },{ $sort: { apariciones: -1 } },{ $limit: 1 },{ $project: { _id: 0, actor: "$_id", apariciones: 1 } }])
[ { apariciones: 2, actor: 'Ian McKellen' } ]

cineDB> db.peliculas.aggregate([{ $unwind: "$reparto" },{ $group: { _id: "$reparto.nombre", apariciones: { $sum: 1 } } },{ $sort: { apariciones: -1 } },{ $project: { _id: 0, actor: "$_id", apariciones: 1 } }])
[
  { apariciones: 2, actor: 'Elijah Wood' },
  { apariciones: 2, actor: 'Ian McKellen' },
  { apariciones: 2, actor: 'Anne Hathaway' },
  { apariciones: 1, actor: 'Leonardo DiCaprio' },
  { apariciones: 1, actor: 'Laurence Fishburne' },
  { apariciones: 1, actor: 'Keanu Reeves' },
  { apariciones: 1, actor: 'Carrie-Anne Moss' },
  { apariciones: 1, actor: 'Matthew McConaughey' },
  { apariciones: 1, actor: 'Robert Pattinson' }
]
cineDB>


cineDB> db.peliculas.insertOne({
|   "titulo": "Dragon Ball Evolution",
|   "director": "James Wong",
|   "genero": "Acción",
|   "año_estreno": 2009,
|   "rating": 2.7,
|   "reparto": [
|     { "nombre": "Justin Chatwin", "rol": "Goku" },
|     { "nombre": "Emmy Rossum", "rol": "Bulma" },
|     { "nombre": "Chow Yun-fat", "rol": "Maestro Roshi" }
|   ],
|   "ingresos": 56000000
| })
{
  acknowledged: true,
  insertedId: ObjectId('6ac82cce7e67b91a602b9a2e')
}
cineDB>

cineDB> db.peliculas.deleteMany({ "rating": { $lt: 6.0 } })
{ acknowledged: true, deletedCount: 1 }db.peliculas.deleteOne({ "titulo": "Matrix" })
cineDB> db.peliculas.deleteOne({ "titulo": "Matrix" })
{ acknowledged: true, deletedCount: 1 }