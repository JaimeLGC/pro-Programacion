from __future__ import annotations


class DNA:
    ADENINE = "A"
    THYMINE = "T"
    CYTOSINE = "C"
    GUANINE = "G"

    def __init__(self, bases: str):
        self.bases = bases.upper()

    @property
    def total_adenine(self):
        counter = len(list(element for element in self.bases if element == "A"))
        return counter

    @property
    def total_thymine(self):
        counter = len(list(element for element in self.bases if element == "T"))
        return counter

    @property
    def total_cytosine(self):
        counter = len(list(element for element in self.bases if element == "C"))
        return counter

    @property
    def total_guanine(self):
        counter = len(list(element for element in self.bases if element == "G"))
        return counter

    def __add__(self, dna: DNA) -> int:
        total_adenine = self.total_adenine + dna.total_adenine
        total_thymine = self.total_thymine + dna.total_thymine
        total_cytosine = self.total_cytosine + dna.total_cytosine
        total_guanine = self.total_guanine + dna.total_guanine
        return max(total_adenine, total_thymine, total_cytosine, total_guanine)

    def stats(self) -> dict:
        percentages = {}
        percentages["Adenine"] = (self.total_adenine / len(self.bases)) * 100
        percentages["Thymine"] = (self.total_thymine / len(self.bases)) * 100
        percentages["Cytosine"] = (self.total_cytosine / len(self.bases)) * 100
        percentages["Guanine"] = (self.total_guanine / len(self.bases)) * 100
        return percentages

    def __mul__(self, dna: DNA) -> int:
        pass


dna1 = DNA("AGGACATATTACGCGGCATTAGATTACA")
dna2 = DNA("ACCCCCCCCCCCGT")
print(dna1.stats())
