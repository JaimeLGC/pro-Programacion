# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    money_back = {}
    money = to_give_back

    for currency in sorted(available_currencies, reverse=True):
        if money % currency >= 0:
            ammount = money // currency
            if ammount > 0:
                money_back[currency] = ammount
            money -= currency * ammount

    if money == 0:
        return money_back
    else:
        return None


if __name__ == "__main__":
    run(20, {5: 3, 2: 7, 1: 3})
