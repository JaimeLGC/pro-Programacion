# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:

    replacements = replacements.split("|")
    buffer = []
    with open(input_path) as f:
        for line in f:
            for old_char, new_char in replacements:
                line = line.replace(old_char, new_char)
            buffer.append(line)

    output_path = "data/replace_chars/r_noticia.txt"
    with open(output_path, "w") as f:
        f.writelines(buffer)

    return filecmp.cmp(output_path, "data/replace_chars/.expected", shallow=False)


if __name__ == "__main__":
    run("data/replace_chars/noticia.txt", "áa|ée|íi|óo|úu")
