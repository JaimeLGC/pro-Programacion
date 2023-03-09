# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(n: int) -> bool:
    divs = list(num for num in range(1, n) if n % num == 0)
    if n == sum(divs):
        return True
    return False


# def is_perfect(n: int) -> bool:
# num = 1
# divs = []
# for num in range(1, n):
#     if n % num == 0:
#         divs.append(num)
#     num += 1
# if n == sum(divs):
#     return True
# return False
