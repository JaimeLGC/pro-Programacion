# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> set:

    a = set()
    b = set()
    for va1, va2 in input:
        a.add(va1)
        b.add(va2)
    output = (a, b)

    return output


if __name__ == "__main__":
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))
