# *****************
# SUMA DE COCIENTES
# *****************


def sum_quot(n: int) -> float:
    if n == 2:
        return 1 / (n - 1)
    return sum_quot(n - 1) + sum_quot(n - 2)
