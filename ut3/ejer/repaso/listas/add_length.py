# *********************
# PALABRAS CON LONGITUD
# *********************


def run(text: str) -> list:
    words_length = []
    for word in text.split(" "):
        char_counter = 0
        for char in word:
            char_counter += 1
        words_length.append(f"{word} {char_counter}")

    return words_length


if __name__ == "__main__":
    run("todo se transforma")
