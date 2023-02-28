# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items):
    sorted_items = []
    sorted_items += items
    while True:
        for i in range(len(items)):
            if i + 1 < len(items):
                if items[i] > items[i + 1]:
                    sorted_items[i + 1] = items[i]
                    sorted_items[i] = items[i + 1]
        return sorted_items
