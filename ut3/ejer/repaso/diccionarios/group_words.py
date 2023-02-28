# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    group_words = {}
    for word in words:
        first_letter = word[0]
        if first_letter in group_words:
            words_with_letter = group_words[first_letter]
            words_with_letter.append(word)
        else:
            group_words[first_letter] = [word]

    return group_words


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
