# *******************************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO (CON RECURSIVIDAD)
# *******************************************************


def factorial(n: int, m: int = 1):
    if n == 0:
        return 1
    if n < 0:
        return None
    return n * factorial(n - 1)
