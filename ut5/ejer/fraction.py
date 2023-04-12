class Fraction:
    def __init__(self, num: int, den):
        self.num = num
        self.den = den

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Algoritmo de Euclides para el cálculo del Máximo Común Divisor."""
        while b > 0:
            a, b = b, a % b
        return a

    def simplify(self, num, den):
        max_common_divisor = self.gcd(den, num)
        s_num = num / max_common_divisor
        s_den = den / max_common_divisor
        return s_num, s_den

    def __add__(self, fraction):
        n_num = self.num * fraction.den + self.den * fraction.num
        n_den = self.den * fraction.den
        s_num, s_den = self.simplify(n_num, n_den)
        return str(n_num + "/" + n_den)

    def __sub__(self, fraction):
        max_common_divisor = self.gcd(self.den, fraction.den)
