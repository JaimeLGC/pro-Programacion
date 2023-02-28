# *****************
# DECIMAL A BINARIO
# *****************


def run(num: int) -> str:

    to_bin = bin(num).lstrip("0b")

    return to_bin


if __name__ == "__main__":
    run(1)
