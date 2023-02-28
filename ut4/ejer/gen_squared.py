# *******************
# GENERANDO CUADRADOS
# *******************


def gen_sq(i: int) -> list:
    square_gen = (l for l in range(i))
    square = []
    for i in square_gen:
        square.append(i**2)
    return square
