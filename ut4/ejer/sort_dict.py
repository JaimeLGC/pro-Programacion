# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    return sorted(unsorted_items, key=lambda t: t[1])


if __name__ == "__main__":
    run({"a": "two", "b": "one", "c": "three"})
