# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    # TU CÓDIGO AQUÍ
    num_lines = num_words = num_bytes = 0
    with open(input_path) as f:
        for line in f:
            words = line.split(" ") if line.strip() else []
            num_words += len(words)
            num_bytes += sum(len(s.encode("utf-8")) for s in line)
            num_lines += 1
    return num_lines, num_words, num_bytes

    return num_lines, num_words, num_bytes


if __name__ == "__main__":
    run("data/wc/lorem.txt")
