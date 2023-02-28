# ***********************
# PARTICIÓN POR EL NÚMERO
# ***********************


def run(values: list, ref_value: int) -> list:
    values_a = []
    values_b = []
    for value in values:
        if value >= ref_value:
            values_a.append(value)
        else:
            values_b.append(value)

    npartition = [values_b, values_a]

    return npartition


if __name__ == "__main__":
    run([4, 3, 2, 9, 8, 5], 4)
