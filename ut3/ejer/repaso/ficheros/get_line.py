# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    line = ""
    with open(input_path) as f:
        line_count = 1
        for linea in f:
            if line_no > 0:
                if line_count == line_no:
                    line = linea.strip()
                    break
                line_count += 1
            line = None

    return line


if __name__ == "__main__":
    run("data/get_line/nasdaq.txt", 20)
