# *************
# SUMANDO FILAS
# *************
from pathlib import Path


def run(data_path: Path) -> tuple:
    tsum = []
    with open(data_path) as f:
        for line in f:
            line_sum = 0
            for num in line.split():
                line_sum += int(num)
            tsum.append(line_sum)

    rsum = tuple(tsum)
    print(line_sum)

    return rsum


if __name__ == "__main__":
    run("data/sum_rows/data1.txt")
