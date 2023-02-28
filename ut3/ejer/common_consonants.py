# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    # TU CÓDIGO AQUÍ
    
    cconst = {char for char in text1 if char in text2 and char not in "aeiou"}
    print(cconst)


if __name__ == "__main__":
    run("Flat is better than nested", "Readability counts")
