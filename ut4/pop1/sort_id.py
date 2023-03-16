# **********************************
# ORDENANDO IDS EN UNA BASE DE DATOS
# **********************************


def sort_id(db: list) -> list:
    keys = list(key for key in db[0].keys)
    identifications = list(item.get("id") for item in db)
    second_value = list(item.get(keys[1]) for item in db)
    sorted_db = []
    sorted_db.copy(db)
    for identification in sorted(identifications):
        sorted_db.append(dict(id=identification))
        

    return sorted_db
