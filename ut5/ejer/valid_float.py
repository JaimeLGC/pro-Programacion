import re

regex = r"(^\d+[._e]\d+[._]?\d*$)"

numbers = ("4.0", "4.0", "04.0", "04.0", "4.000_000", "4e0")


def check_float(numbers: tuple) -> None:
    for num in numbers:
        if re.match(regex, num):
            print(f"{num} es un float válido")
        else:
            print(f"{num} no es un float válido")


check_float(numbers)
