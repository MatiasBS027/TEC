from pymongo import MongoClient

cliente = MongoClient(host="127.0.0.1", port=27017)

db = cliente['app']
users = db['users']

# Inserta ejemplos (usa upsert para no duplicar en cada ejecución)
users.update_one(
    {"name": "Juan", "email": "juan@example.com"},
    {"$setOnInsert": {"name": "Juan", "age": 20, "email": "juan@example.com"}},
    upsert=True,
)
users.update_one(
    {"name": "Ado", "email": "ado@example.com"},
    {"$setOnInsert": {
        "name": "Ado",
        "age": 23,
        "email": "ado@example.com",
        "albums": [
            {"name": "Album 1", "year": 2020},
            {"name": "Album 2", "year": 2021},
            {"name": "Album 3", "year": 2022},
        ]
    }},
    upsert=True,
)

# Índice para consultas por albums.name
users.create_index({"albums.name": 1})

# find_one con proyección correcta: _id:0 es la única exclusión permitida con inclusiones
u = users.find_one({"name": "Ado"}, {"_id": 0, "name": 1, "age": 1, "albums": 1})
print("find_one:", u)

# aggregate correcto: $match con {campo: valor} y $project con _id:0 (no id:0)
result = list(users.aggregate([
    {"$match": {"name": "Ado"}},
    {"$project": {"_id": 0, "name": 1, "albums": 1}}
]))
print("aggregate:", result)

# Ejemplo $exists correcto (a nivel de campo, no top-level)
con_albums = users.find_one({"albums": {"$exists": True}}, {"_id": 0, "name": 1, "albums": 1})
print("con_albums ($exists):", con_albums)
