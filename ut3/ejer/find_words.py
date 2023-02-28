# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    line_count = 0
    matches = []
    with open(data_path, "r") as f1:
        for line in f1:
            char_count = 1
            line_count += 1
            for word in line.lower().split(" "):
                if word.strip(' .,:;()"¡!-') == target_word:
                    matches.append((line_count, char_count))
                    char_count = 1
                else:
                    char_count += len(word) + 1

    return matches


if __name__ == "__main__":
    run("data/find_words/bzrp.txt", "persona")
