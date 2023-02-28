# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    first_item = items[0]
    for item in items:
        if item != first_item:
            all_same = False
            break
        else:
            all_same = True

    return all_same


if __name__ == "__main__":
    run([1, 1, 1, 1, 1, 1])
