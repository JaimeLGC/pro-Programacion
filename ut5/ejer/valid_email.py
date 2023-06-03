import re

regex = r"(\w+@\D+.(?:com|es))"

mails = (
    "welopeste1@gmail.com",
    "welopeste1gmail.com",
    "gmail.com",
    "@gmail.com",
    "welo@12.com",
)


def check_mail(mails: tuple) -> None:
    for mail in mails:
        if re.match(regex, mail):
            print(f"{mail} es un correo válido")
        else:
            print(f"{mail} no es un correo válido")


check_mail(mails)
