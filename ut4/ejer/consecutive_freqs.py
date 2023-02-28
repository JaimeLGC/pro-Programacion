# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


# def cfreq(items, /, as_string=False):
# known_items = []
# freqs_list = []
# item_counter = 0
# last_item = items[0]
# for item in items:
#     if item not in known_items:
#         known_items.append[item, 1]
#     elif item in known_items:
#         known_items[item, 1]


def cfreq(items, /, as_string=False):
    item_counter = 0
    freqs_list = []
    ifreqs = []
    freqs = ""
    if not items:
        if as_string:
            return freqs
        else:
            return freqs_list
    else:
        last_item = items[0]
        for item in items:
            if item == last_item:
                item_counter += 1
            elif item != last_item:
                freqs_list.append((last_item, item_counter))
                last_item = item
                item_counter = 1
        freqs_list.append((last_item, item_counter))

    if as_string:
        for i in freqs_list:
            a, b = i
            ifreqs.append(f"{a}:{b}")
        freqs = ",".join(ifreqs)
        return freqs
    else:
        return freqs_list


cfreq([0, 0, 9, 5, 5, 5, 1, 1, 1])
