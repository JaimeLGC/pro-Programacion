# ******************
# FIBONACCI ITERABLE
# ******************

# fib = 100

# n1 = 0
# print(n1)
# n2 = 1
# print(n2)

# for _ in range(fib - 2):
#     result = n1 + n2
#     n1 = n2
#     n2 = result
#     print(result)


class Fibonacci:
    def __init__(self, limit: int):
        self.limit = limit
        self.num1 = 0
        self.num2 = 1

    def __next__(self):
        if self.num2 >= self.limit - self.num1:
            raise StopIteration
        result = self.num1 + self.num2
        self.num1 = self.num2
        self.num2 = result
        return self.num2


def run(n: int):
    pass
