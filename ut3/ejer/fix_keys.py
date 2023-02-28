# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    # TU CÓDIGO AQUÍ
    fitems = dict()
    for words, meaning in items.items():
        fitword = ""
        for char in words:
            if char != " ":
                fitword += char
        fitems[fitword] = meaning

    return fitems


if __name__ == "__main__":
    run({"S  001": ["Math", "Science"], "S    002": ["Math", "English"]})
