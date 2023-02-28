# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:

    inventory = {"output"}
    for move in imoves.split(","):
        letter = move[0]
        number = int(move[1:])
        if letter in inventory:
            inventory[letter] += number
            continue
        else:
            inventory[letter] = number
    return inventory


if __name__ == "__main__":
    run("A1,B4,A-2,A7,B1,C4")
