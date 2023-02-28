# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:

    merch_stock = stock[merch]
    available = merch_stock >= amount

    return available


if __name__ == "__main__":
    run({"pen": 20, "cup": 11, "keyring": 40}, "cup", 9)

#    for item, number in stock.items():
#        if item == merch:
#            if number >= amount:
#                available = True
#            else:
#                available = False
