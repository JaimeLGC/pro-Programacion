# *******************
# CONTANDO SIN CONTAR
# *******************


def mcount(items: tuple, target: int):
    count = 0
    for i in items:
        if i == target:
            count += 1
    return count
