nested = {"a": {"b": {"c": 12, "d": "Hello World"}, "e": [1, 2, 3]}}


def flatten_nest(nested: dict) -> dict:
    flattened_nest = {}
    for key in nested.keys():
        if isinstance(nested.get(key), dict):
            flattened_nest[key] = nested.get(key)
    print(flattened_nest)


flatten_nest(nested)
