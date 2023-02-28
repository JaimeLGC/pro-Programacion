# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    max_length = 0
    longest_word = ""
    with open(input_path) as f:
        for line in f:
            for word in line.strip().split():
                word_lenght = 0
                clean_word = word.strip(".,:;'-_")
                for char in clean_word:
                    word_lenght += 1
                if word_lenght >= max_length:
                    max_length = word_lenght
                    longest_word = clean_word

    return longest_word


if __name__ == "__main__":
    run("data/longest_word/python.txt")
