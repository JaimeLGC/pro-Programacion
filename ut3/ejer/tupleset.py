# ***************
# TUPLA DE DUPLAS
# ***************


def run(input: tuple) -> set:
    primer_conjunto = set()
    segundo_conjunto = set()
    conjunto_final = (primer_conjunto, segundo_conjunto)
    for item in input:
        primer_conjunto.add(item[0])
        segundo_conjunto.add(item[1])
    output = (primer_conjunto, segundo_conjunto)

    return output


if __name__ == "__main__":
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))
