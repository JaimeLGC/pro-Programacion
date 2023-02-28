# *******************
# NO ERES CONSECUTIVO
# *******************


def run(values: list) -> int:
    target = None
    if values != []:
        last_num = values[0]
    for value in values:
        if value == last_num:
            last_num += 1
        elif value != last_num:
            target = value
            break

    return target


if __name__ == "__main__":
    run([1, 2, 3, 4, 6, 7, 8])
