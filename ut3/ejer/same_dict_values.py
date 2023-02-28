# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    first_value = ""
    all_same = True
    for word, value in items.items():
        if value == first_value or first_value == "":
            all_same = True
            first_value = value
        else:
            all_same = False
            break

    return all_same


if __name__ == "__main__":
    run({"a": 1, "b": 1, "c": 1, "d": 1})
