# ********************
# CALCULANDO MÚLTIPLOS
# ********************


def run(x: int, n: int) -> list:

    multiples = list(range(x, (n * x + 1), x))

    return multiples


if __name__ == "__main__":
    run(1, 10)
