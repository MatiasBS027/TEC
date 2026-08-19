from asyncio import tasks
from flask import Flask, request
#from app_service import AppService
#from db import DataBase

app = Flask(__name__)

class Tareas:
    def __init__(self):
        self.tasks = ["Tarea 1", "Tarea 2", "Tarea 3"]

    def compartir_tarea(self, id, email):
        # Implementar la logica para compartir la tarea
        tarea = self.tasks[id]
        # Enviar el correo electronico con la tarea compartida
        return f"Tarea {tarea} compartida con {email}"

tareas = Tareas()

@app.route('/')
def home():
    return {"msg": "La aplicacion esta funcionando"}

@app.route('/task')
def get_tasks():
    return str(tareas.tasks)

@app.route("/task/<int:id>")
def get_task(id):
    return str(tareas.tasks[id])

@app.route("/task", methods=["POST"])
def create_task():
    data = request.get_json()
    tasks.tasks.append(data["task"])
    return str(tasks.tasks)

@app.route("/task/<int:id>", methods=["DELETE"])
def delete_task(id):
    tareas.tasks.pop(id)
    return str(tareas.tasks)


@app.route("/task", methods=["UPDATE"])
def update_task(id):
    data = request.get_json()
    tareas.tasks.pop(id)
    tasks.tasks.append(data["task"])
    return str(tasks.tasks)

@app.route("/task/<int:id>/compartir", methods=["POST"])
def compartir_task(id):
    data = request.get_json()
    nombre_cliente = request.args.get('nombreCliente')
    respuesta = tareas.compartir_tarea(id, data["email"])
    return str(respuesta, nombre_cliente)

