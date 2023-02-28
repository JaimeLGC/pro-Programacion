# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = "data/avg_temps/avg_temps.dat"
    avg_temps = []

    with open(input_path) as f:
        for line in f:
            monthly_temps = [int(t) for t in line.strip().split(",")]
            avg_temp = sum(monthly_temps) / len(monthly_temps)
            avg_temps.append(avg_temp)

    print(type(monthly_temps))

    with open(output_path, "w") as f:
        for avg_temp in avg_temps:
            f.write(f"{avg_temp:.2f}\n")
    return filecmp.cmp(output_path, "data/avg_temps/.expected", shallow=False)


if __name__ == "__main__":
    run("data/avg_temps/temperatures.dat")
