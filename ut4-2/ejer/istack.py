from __future__ import annotations


class IntegerStack:
    def __init__(self, *, max_size: int = 10):
        self.max_size = max_size
        self.items = []

    def push(self, item: int) -> bool:
        if not self.is_full():
            self.items.insert(0, item)
        return self.items[0] == item

    def pop(self) -> int:
        return self.items.pop(0)

    def top(self) -> int:
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) == self.max_size

    def expand(self, factor: int = 2) -> None:
        self.max_size *= factor

    def dump_to_file(self, path: str) -> None:
        with open(path, "w") as f:
            f.write(str(self))

    @classmethod
    def load_from_file(cls, path: str) -> IntegerStack:
        """Crea una pila desde un fichero. Si la pila se llena al ir añadiendo elementos
        habrá que expandir con los valores por defecto"""
        with open(path, "r") as f:
            stack = IntegerStack()
            for item in f.readlines():
                stack.items.append(int(item.strip("\n")))
                if len(stack) == stack.max_size:
                    stack.expand()
            return stack

    def __getitem__(self, index: int) -> int:
        """Devuelve el elemento de la pila en el índice indicado"""
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        """Establece el valor de un elemento de la pila mediante el índice indicado"""
        self.items[index] = item

    def __len__(self):
        """Número de elementos que contiene la pila"""
        return len(self.items)

    def __str__(self):
        return "\n".join(str(item) for item in self.items)

    def __add__(self, other: IntegerStack) -> IntegerStack:
        """La segunda pila va "encima" de la primera"""
        stack = IntegerStack()
        stack.items += list(item for item in other.items)
        stack.items += list(item for item in self.items)
        stack.max_size = self.max_size + other.max_size
        return stack

    def __iter__(self) -> IntegerStackIterator:
        return IntegerStackIterator(self)


class IntegerStackIterator:
    def __init__(self, stack: IntegerStack):
        self.stack = stack
        self.pointer = 0

    def __next__(self) -> int:
        if self.pointer >= len(self.stack):
            raise StopIteration
        result = self.stack.items[self.pointer]
        self.pointer += 1
        return result
