# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text: str):
    VOWELS = "aeiou"
    num_vowels = len(list(char for char in text if char in VOWELS))
    return num_vowels
