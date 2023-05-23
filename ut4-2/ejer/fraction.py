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
        gcd = self.gcd(den, num)
        s_num = num / gcd
        s_den = den / gcd
        return s_num, s_den

    def __add__(self, fraction):
        n_num = self.num * fraction.den + self.den * fraction.num
        n_den = self.den * fraction.den
        s_num, s_den = self.simplify(n_num, n_den)
        return str(s_num + "/" + s_den)

    # def __sub__(self, fraction):
    #     n_den = self.gcd(self.den, fraction.den)
    #     if self.num >= fraction.num:
    #         n_num = self.num - fraction.num
    #     else:
    #         n_num = fraction.num - self.num
    #     return str(n_num + "/" + n_den)

    def __mul__(self, fraction):
        n_num = self.num * fraction.num
        n_den = self.den * fraction.den
        return str(n_num + "/" + n_den)
