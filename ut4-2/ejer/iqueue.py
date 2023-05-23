from __future__ import annotations


class IntegerQueue:
    """
    Cola de enteros:
    ╔══════╦═══╦═══╦═══╦═══╗
    ║ HEAD ║ 4 ║ 3 ║ 5 ║ 7 ║
    ╚══════╩═══╩═══╩═══╩═══╝
    """

    def __init__(self, *, max_size: int = 10):
        """Utilizar atributo items para guardar los elementos"""
        self.max_size = max_size
        self.items = []

    def enqueue(self, item: int) -> bool:
        """Añade item a la cola.
        Si la cola está llena retornar False, en otro caso retornar True"""
        if len(self.items) < self.max_size:
            self.items.append(item)
        return self.items[-1] == item

    def dequeue(self) -> int:
        """Extraer el elemento que está en el HEAD de la cola"""
        result = self.items[0]
        self.items.pop(0)
        return result

    def head(self) -> int:
        """Devolver el elemento que está en el HEAD de la cola (sin extracción)"""
        return self.items[0]

    def is_empty(self) -> bool:
        """Indica si la cola está vacía"""
        return not self.items

    def is_full(self) -> bool:
        """Indica si la cola está llena -> max_size"""
        return len(self.items) == self.max_size

    def expand(self, factor: int = 2) -> None:
        """Expande el tamaño máximo de la cola en el factor indicado"""
        self.max_size *= factor

    def dump_to_file(self, path: str) -> None:
        """Vuelca la cola a un fichero.
        - Todos los elementos en una misma línea separados por comas.
        - El primer elemento del fichero corresponde con el HEAD de la cola."""
        with open(path, "w") as f:
            f.write(str(self))

    @classmethod
    def load_from_file(cls, path: str) -> IntegerQueue:
        """Crea una cola desde un fichero.
        - Todos los elementos en una misma línea separados por comas.
        - El primer elemento del fichero corresponde con el HEAD de la cola.
        - Si la cola se llena al ir añadiendo elementos habrá que expandir con los valores
        por defecto"""
        with open(path, "r") as f:
            items = f.readline().split(",")
            queue = IntegerQueue()
            for item in items:
                if len(queue) == queue.max_size:
                    queue.expand()
                queue.enqueue(int(item))
            return queue

    def __getitem__(self, index: int) -> int:
        """Devuelve el elemento de la cola en el índice indicado"""
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        """Establece el valor de un elemento de la cola mediante el índice indicado"""
        self.items[index] = item

    def __len__(self):
        """Número de elementos que contiene la cola"""
        return len(self.items)

    def __str__(self):
        """Todos los elementos de la cola separados por coma empezando por el HEAD"""
        result = []
        for item in self.items:
            result.append(f"{item}")
        return ",".join(result)

    def __add__(self, other: IntegerQueue) -> IntegerQueue:
        """Sumar dos colas.
        - La segunda cola va "detrás" de la primera
        - El tamaño máximo de la cola resultante es la suma de los tamaños
        máximos de cada cola."""
        queue = IntegerQueue()
        queue.items = self.items
        for item in other.items:
            queue.items.append(item)
        queue.max_size = len(queue)
        return queue

    def __iter__(self) -> IntegerQueueIterator:
        return IntegerQueueIterator(self)


class IntegerQueueIterator:
    def __init__(self, queue: IntegerQueue):
        self.queue = queue
        self.pointer = 0

    def __next__(self) -> int:
        if self.pointer >= len(self.queue):
            raise StopIteration
        result = self.queue.items[self.pointer]
        self.pointer += 1
        return result
