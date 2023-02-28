# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    INVALID_CHARS = ".,:;()'¡!-"
    target_word = target_word.lower()
    matches = []
    f = open(data_path)

    for num_line, line in enumerate(f, start=1):
        words = line.strip().lower().split()
        char_pos = 1
        for word in words:
            if word.strip(INVALID_CHARS) == target_word:
                clean_word_len = len(word.lstrip(INVALID_CHARS))
                whole_word_len = len(word)
                delta = whole_word_len - clean_word_len
                matches.append((num_line, char_pos + delta))
            char_pos += len(word) + 1
    return matches


if __name__ == "__main__":
    run("data/find_words/bzrp.txt", "persona")
