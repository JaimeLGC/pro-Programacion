from __future__ import annotations


class Fraction:
    @staticmethod
    def gcd(a: int, b: int):
        while b > 0:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(x: int, y: int) -> int:
        num = max(x, y)
        while True:
            if num % x == 0 and num % y == 0:
                return num
            num += 1

    def simplify(method):
        def wrapper(self, *args, **kwargs):
            print("Simplificando...")
            res = method(self, *args, **kwargs)  # Ojo llamada!
            gcd = self.gcd(self.num, self.den)
            self.num /= gcd
            self.den /= gcd
            return res

        return wrapper

    @simplify
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

    @simplify
    def __add__(self, other: Fraction):
        if self.den != other.den:
            lcm = self.lcm(self.den, other.den)
            new_self_num = self.num * (lcm / self.den)
            new_other_num = other.num * (lcm / other.den)
            num_add = new_self_num + new_other_num
            return Fraction(num_add, lcm)
        num_add = self.num + other.num
        return Fraction(num_add, self.den)

    @simplify
    def __sub__(self, other: Fraction):
        if self.den != other.den:
            lcm = self.lcm(self.den, other.den)
            new_self_num = self.num * (lcm / self.den)
            new_other_num = other.num * (lcm / other.den)
            num_sub = new_self_num - new_other_num
            return Fraction(num_sub, lcm)
        num_sub = self.num - other.num
        return Fraction(num_sub, self.den)

    @simplify
    def __mul__(self, other: Fraction):
        res_num = self.num * other.num
        res_den = self.den * other.den
        return Fraction(res_num, res_den)

    @simplify
    def __truediv__(self, other: Fraction):
        res_num = self.num * other.den
        res_den = self.den * other.num
        return Fraction(res_num, res_den)

    def __str__(self):
        return f" {int(self.num)}\n---\n {int(self.den)}"
