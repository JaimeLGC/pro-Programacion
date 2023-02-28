# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int:
    diagonal = 0
    sum_diagonal = 0
    for item in matrix:
        sum_diagonal += item[diagonal]
        diagonal += 1

    return sum_diagonal


if __name__ == "__main__":
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])
