# ****************************
# DECORANDO LA SUMA DE VALORES
# ****************************


def result_as_status(func):
    def wrapper(*args, **kwargs):
        rstatus = {}
        rstatus["status"], rstatus["result"] = func(*args, **kwargs)
        return rstatus

    return wrapper


@result_as_status
def is_instance(values: list) -> tuple:
    is_integer = True
    for value in values:
        if not isinstance(value, int):
            is_integer = False
    if is_integer:
        status = True
        result = sum(values)
    else:
        status = False
        result = "Not int value found"
    return status, result


def run(values: list) -> dict:
    rstatus = is_instance(values)
    return rstatus
