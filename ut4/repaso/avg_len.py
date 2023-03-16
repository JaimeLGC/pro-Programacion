# LONGITUD MEDIA DE LOS VALORES #

entrada1 = ["u", "y"]
entrada2 = ["aa", "bbb", "cccc"]
entrada3 = ["aa", "bb", "ddd", "eee"]


def avg_len(values: list) -> list:
    return len(values) / avg_len(values[+1])


print(avg_len(entrada1))
