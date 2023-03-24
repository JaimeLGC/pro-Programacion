# *******************
# EXTRACCIÓN DE PARES
# *******************


def run(values: list) -> list:
    evens = list(value for value in values if value % 2 == 0)
    return evens
