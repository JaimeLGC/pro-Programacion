from __future__ import annotations


class IntegerStack:
    def __init__(self, *, max_size: int = 10):
        self.max_size = max_size
        self.items = []

    def push(self, item: int) -> bool:
        if len(self.items) < self.max_size:
            self.items.insert(0, item)
            return True
        else:
            return False

    def pop(self) -> int:
        if self.items[0]:
            result = self.items[0]
            self.items.pop(0)
        return result

    def top(self) -> int:
        if self.items[0]:
            return self.items[0]

    def is_empty(self) -> bool:
        if not self.items:
            return True
        return False

    def is_full(self) -> bool:
        if len(self.items) == self.max_size:
            return True
        return False

    def expand(self, factor: int = 2) -> None:
        self.max_size = self.max_size * factor

    def dump_to_file(self, path: str) -> None:
        with open(path, "w") as f:
            for item in self.items:
                f.write(f"{item}\n")

    @classmethod
    def load_from_file(cls, path: str) -> IntegerStack:
        """Crea una pila desde un fichero. Si la pila se llena al ir añadiendo elementos
        habrá que expandir con los valores por defecto"""
        with open(path, "r") as f:
            stack = IntegerStack(max_size=len(f.readlines()))
            stack.items = f.readlines()
            return stack

    load_from_file

    def __getitem__(self, index: int) -> int:
        """Devuelve el elemento de la pila en el índice indicado"""
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        """Establece el valor de un elemento de la pila mediante el índice indicado"""
        if index > len(self.items):
            self.items.append(item)
        else:
            self.items[index] = item

    def __len__(self):
        """Número de elementos que contiene la pila"""
        return len(self.items)

    def __str__(self):
        return "\n".join(list(str(item for item in self.items)))
        ...

    def __add__(self, other: IntegerStack) -> IntegerStack:
        """La segunda pila va "encima" de la primera"""
        result = IntegerStack(max_size=(len(self.items) + len(other.items)))
        result.items += other.items
        result.items += self.items

    def __iter__(self) -> IntegerStackIterator:
        ...


class IntegerStackIterator:
    def __init__(self, stack: IntegerStack):
        ...

    def __next__(self) -> int:
        ...
