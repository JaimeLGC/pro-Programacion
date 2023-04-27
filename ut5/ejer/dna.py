from __future__ import annotations


class DNA:
    ADENINE = "A"
    THYMINE = "T"
    CYTOSINE = "C"
    GUANINE = "G"

    def __init__(self, sequence: str):
        self.sequence = sequence.upper()
        self.adenines = self.total_adenine
        self.thymines = self.total_thymine
        self.cytosines = self.total_cytosine
        self.guanines = self.total_guanine

    def __len__(self):
        return len(self.sequence)

    @property
    def total_adenine(self):
        return len(list(element for element in self.sequence if element == "A"))

    @property
    def total_thymine(self):
        return len(list(element for element in self.sequence if element == "T"))

    @property
    def total_cytosine(self):
        return len(list(element for element in self.sequence if element == "C"))

    @property
    def total_guanine(self):
        return len(list(element for element in self.sequence if element == "G"))

    def __add__(self, dna: DNA) -> str:
        addition = ""
        for a, b in zip(self.sequence, dna.sequence):
            addition += max(a, b)
        if len(self) > len(dna):
            addition += self.sequence[len(dna) : len(self)]
        elif len(self) < len(dna):
            addition += dna.sequence[len(self) : len(dna)]
        return DNA(addition)

    def stats(self) -> dict:
        percentages = {}
        percentages["A"] = (self.total_adenine / len(self.sequence)) * 100
        percentages["T"] = (self.total_thymine / len(self.sequence)) * 100
        percentages["C"] = (self.total_cytosine / len(self.sequence)) * 100
        percentages["G"] = (self.total_guanine / len(self.sequence)) * 100
        return percentages

    def __mul__(self, dna: DNA) -> int:
        multiplication = ""
        for a, b in zip(self.sequence, dna.sequence):
            if a == b:
                multiplication += a
        return DNA(multiplication)

    def __str__(self) -> str:
        return f"{self.sequence}"

    def dump_to_file(self, path: str):
        with open(path, "w") as f:
            f.write(self.sequence)

    @classmethod
    def build_from_file(self, path: str):
        with open(path, "r") as f:
            for line in f:
                return DNA(line)

    def __getitem__(self, index: int):
        return self.sequence[index]

    def __setitem__(self, index: int, base: str):
        bases = ("A", "T", "G", "C")
        split_sequence = list(self.sequence)
        if base in bases:
            split_sequence[index] = base
        else:
            split_sequence[index] = "A"
        self.sequence = "".join(split_sequence)
