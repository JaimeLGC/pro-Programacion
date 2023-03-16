entrada1 = [1, 2, 3]
entrada2 = [1, 2, [2, 4], [10, 4, [6, 10]]]


def recursive_average(values: list) -> int:
    to_be_checked = []
    for value in values:
        if isinstance(value, int):
            to_be_checked.append(value)
        elif isinstance(value, list):
            to_be_checked.append(recursive_average(value))
    return sum(to_be_checked) // len(to_be_checked)


print(recursive_average(entrada2))
