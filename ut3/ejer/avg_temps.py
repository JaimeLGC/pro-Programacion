# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    # BLOQUE DE LECTURA
    avg_temps = []
    with open(input_path, "r") as f:
        for line in f:
            month_temps = [int(t) for t in line.strip().split(",")]
            avg_temp = sum(month_temps) / len(month_temps)
            avg_temps.append(avg_temp)

    # BLOQUE DE ESCRITURA
    output_path = "data/avg_temps/avg_temps.dat"
    with open(output_path, "w") as f:
        for avg_temp in avg_temps:
            f.write(f"{avg_temp:.2f}\n")

    return filecmp.cmp(output_path, "data/avg_temps/.expected", shallow=False)


if __name__ == "__main__":
    run("data/avg_temps/temperatures.dat")
