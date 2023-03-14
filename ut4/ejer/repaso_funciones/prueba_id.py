db = [
    {"id": 1, "lang": "English"},
    {"id": 3, "lang": "German"},
    {"id": 4, "lang": "Italian"},
    {"id": 5, "lang": "Portuguese"},
    {"id": 6, "lang": "Spanish"},
    {"id": 2, "lang": "French"},
]

ids = list(item.get("id") for item in db)
print(ids)
