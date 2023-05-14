class Fibonacci:
    def __init__(self, max: int):
        self.last = 0
        self.current = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        self.next = self.last + self.current
        if self.next >= self.max:
            raise StopIteration
        self.last = self.current
        self.current = self.next

        return self.current


for fib in Fibonacci(100):
    print(fib)
