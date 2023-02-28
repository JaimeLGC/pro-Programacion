# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:

    available = True
    if merch not in stock or amount > stock[merch]:
        available = False

    return available


if __name__ == "__main__":
    run({"pen": 20, "cup": 11, "keyring": 40}, "cup", 9)
