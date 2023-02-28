def find_item(values: tuple, target: int) -> int:
    """Returns the ammount of values in the tuple that match
    the given target

    :param items: Numeric items to look for in
    :type items: tuple

    :param target: Value to be counted
    :type target: int"""

    return len([value for value in values if value == target])


print(find_item((1, 2, 3, 3, 3, 4, 5, 3, 6), 3))
