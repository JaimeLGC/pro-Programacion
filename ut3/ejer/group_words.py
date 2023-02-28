# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    group_words = {}
    
    for word in words:
        if word[0] not in group_words:
            group = []
        group_words = {word[0]: word}
        print(group_words)


if __name__ == "__main__":
    run(
        [
            "mesa",
            "móvil",
            "barco",
            "coche",
            "avión",
            "bandeja",
            "casa",
            "monitor",
            "carretera",
            "arco",
        ]
    )


