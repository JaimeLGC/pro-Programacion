def res2bin(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return bin(result)

    return wrapper
