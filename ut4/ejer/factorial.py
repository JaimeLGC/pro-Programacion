# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    if n > 0:
        mult = 1
        for n in range(1, n + 1):
            mult *= n
        return mult
    elif n == 0:
        return 1
