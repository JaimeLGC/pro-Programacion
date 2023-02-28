# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:

    data = []
    with open(datafile) as f:
        fields = f.readline().strip().split(",")
        for line in f:
            values = line.strip().split(",")
            pokemon = {}
            for field, value in zip(fields, values):
                if value == "True":
                    value = True
                elif value == "False":
                    value = False
                elif value.isnumeric():
                    value = int(value)
                pokemon[field] = value
            data.append(pokemon)

    return data


if __name__ == "__main__":
    run("data/read_csv/pokemon.csv")
