from __future__ import annotations

import sqlite3

DB_PATH = "todo.db"
TASK_DONE_SYMBOL = "✔"
TASK_PENDING_SYMBOL = "⎕"


class Task:
    """Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como diccionarios.
    - cur: para el cursor de manejo."""

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    def __init__(self, name: str, done: bool = False, id: int = -1):
        """Crea los atributos homónimos a los parámetros"""
        self.name = name
        self.done = done
        self.id = id

    def save(self):
        """Guarda esta tarea en la base de datos.
        El identificador asignado en la base de datos se debe usar para actualizar el
        atributo id de la tarea."""
        task = "INSERT INTO tasks(name, done) VALUES (?, ?)"
        self.cur.execute(task, (self.name, self.done))
        self.id = self.cur.lastrowid
        self.con.commit()

    def update(self):
        """Actualiza la tarea (nombre y estado) en la base de datos"""
        self.cur.execute(
            f'UPDATE tasks SET name="{self.name}", done={self.done} WHERE id={self.id}'
        )
        self.con.commit()

    def check(self):
        """Marca la tarea como completada. Haz uso también de .update()"""
        self.done = True
        self.update()

    def uncheck(self):
        """Marca la tarea como no completada. Haz uso también de .update()"""
        self.done = False
        self.update()

    def __repr__(self):
        """Muestra la tarea en formato:
        <SYMBOL> <name> (id=<id>)"""
        symbol = TASK_DONE_SYMBOL if self.done else TASK_PENDING_SYMBOL
        return f"{symbol} {self.name} (id={self.id})"

    # -------------------------------------------------------
    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        """Construye una nueva tarea a partir de una fila de consulta devuelta por execute()"""
        return cls(row["name"], row["done"], row["id"])

    @classmethod
    def get(cls, task_id: int) -> Task:
        """Devuelve un objeto Task desde la consulta a la base de datos"""
        sql = "SELECT * FROM tasks WHERE id=?"
        result = cls.cur.execute(sql, (task_id,))
        row = result.fetchone()
        return cls.from_db_row(row)


# -------------------------------------------------------


class ToDo:
    """Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como diccionarios.
    - cur: para el cursor de manejo."""

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    def create_db(self):
        '''Crea la base de datos con los campos "id", "name" y "done"'''
        self.cur.execute(
            """CREATE TABLE tasks (
        id INTEGER PRIMARY KEY,
        name CHAR,
        done INTEGER)"""
        )
        self.con.commit()

    def get_tasks(self, *, done: int = -1):
        """Devuelve todas las tareas como objetos de tipo Task consultando la BBDD.
        - Si done = 0 se devuelven las tareas pendientes.
        - Si done = 1 se devuelven las tareas completadas.
        Ojo! Esto es una función generadora."""
        result = self.cur.execute(f"select * from tasks where done = {done}")
        for row in result:
            yield Task.from_db_row(row)

    def add_task(self, name: str):
        '''Añade la tarea con nombre "name"'''
        task = Task(name)
        task.save()

    def complete_task(self, task_id: int):
        """Marca la tarea con identificador "task_id" como completada"""
        task = Task.get(task_id)
        task.check()

    def reopen_task(self, task_id: int):
        """Marca la tarea con identificador "task_id" como pendiente"""
        task = Task.get(task_id)
        task.uncheck()
