def plusone(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return result + 1

    return wrapper


@plusone
@plusone
def mult(x: int, y: int) -> int:
    return x * y


mult_plusone = plusone(mult)

# aplica plusone dos veces (lineas 11 y 16)
print(mult_plusone(3, 2))
