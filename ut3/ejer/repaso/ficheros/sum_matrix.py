# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = "data/sum_matrix/result.dat"
    nums_1 = nums_2 = []

    with open(matrix1_path) as f:
        for line in f:
            for num in line.split():
                nums_1.append(int(num))
    with open(matrix2_path) as f:
        for line in f:
            line_lenght = len(line.split())
            for num in line.split():
                nums_2.append(int(num))

    suma = [n1 + n2 for n1, n2 in zip(nums_1, nums_2)]

    with open(result_path, "w") as f:
        s_count = 0
        for s in suma:
            if s_count == line_lenght - 1:
                f.write(f"{str(s)}\n")
                s_count = 0
            else:
                f.write(f"{str(s)} ")
                s_count += 1

    return filecmp.cmp(result_path, "data/sum_matrix/.expected", shallow=False)


if __name__ == "__main__":
    run("data/sum_matrix/matrix1.dat", "data/sum_matrix/matrix2.dat")
