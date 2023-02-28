# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:
    """xsum = []
    num_index = 0
    with open(data_path) as f:
        for line in f:
            for num in line.split():
                num_row_index = 0
                if num_row_index == num_index:
                    xsum.append(int(num))
                    num_index += 1
                num_row_index += 1"""

    num_index = 0
    num_lines = 0
    xsum = []
    zsum = []
    with open(data_path) as f:
        for line in f:
            num_lines += 1
            splitline = line.split()
            xsum.append(int(splitline[num_index]))
    if len(xsum) == num_lines:
        num_index += 1
        num_lines = 0
        zsum.append(sum(xsum))

    csum = zsum
    return csum


if __name__ == "__main__":
    run("data/sum_cols/data1.txt")
