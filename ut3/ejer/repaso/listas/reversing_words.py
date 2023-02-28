# *************************
# PALABRAS EN ORDEN INVERSO
# *************************


def run(text: str) -> str:
    reversed = text.lower().split()
    reversing = " ".join(reversed[::-1])

    return reversing


if __name__ == "__main__":
    run("Hello World")
