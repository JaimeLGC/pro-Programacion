# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    fitems = {}
    for item in items.keys():
        fitword = ""
        for char in item:
            if char != " ":
                fitword += char
        fitems[fitword] = items.get(item)

    return fitems


if __name__ == "__main__":
    run({"S  001": ["Math", "Science"], "S    002": ["Math", "English"]})
