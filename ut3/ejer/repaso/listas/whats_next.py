# *********************
# ¿QUÉ ES LO SIGUIENTE?
# *********************


def run(items: list, ref_item: object) -> object:
    if ref_item in items and ref_item != items[-1]:
        target_item = items[items.index(ref_item) + 1]
    else:
        target_item = None

    return target_item


if __name__ == "__main__":
    run([1, 2, 3, 4, 5, 6, 7], 3)
