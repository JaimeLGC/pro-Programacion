# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:

    inventory = {}
    for imove in imoves.split(","):
        article_id = imove[0]
        amount = int(imove[1:])
        inventory[article_id] = inventory.get(article_id, 0) + amount

    return inventory


if __name__ == "__main__":
    run("A1,B4,A-2,A7,B1,C4")
