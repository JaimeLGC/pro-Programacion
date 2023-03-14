# ***************
# CUADRADO MÁGICO
# ***************


def is_magic_square(values: list):
    target = sum(values[0])
    num_ammount = len(values[0])
    n = 0
    items = []

    for value in values:
        items.append(value[n])
