# ***********************
# SUMANDO CON ANIDAMIENTO
# ***********************


def sum_nested(items: list) -> int:
    _sum = 0
    for item in items:
        if isinstance(item, int):
            _sum += item
        else:
            _sum += sum_nested(item)
    return _sum
