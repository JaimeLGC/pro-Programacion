# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    money_back = {}
    available_currencies = sorted(available_currencies, reverse=True)
    money = to_give_back

    for currency in available_currencies:
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
    run(20, [5, 2, 1])
