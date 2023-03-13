def plusone(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return result + 1

    return wrapper


def mult(x: int, y: int) -> int:
    return x * y


mult_plusone = plusone(mult)

print(mult_plusone(3, 2))
