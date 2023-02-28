# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    known_words = {}
    freq = {}
    with open(input_path) as f:
        for line in f:
            for word in line.lower().strip(".,:;'-_").split(" "):
                known_words[word] = known_words.get(word, 0) + 1

    for item in known_words.keys():
        if known_words.get(item) >= lower_bound:
            freq[item] = known_words.get(item)

    return freq


if __name__ == "__main__":
    run("data/word_freq/cistercian.txt", 9)
