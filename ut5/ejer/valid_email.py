import re

regex = r""

mail = "welopeste1@gmailcom"


def check_mail(mail: str) -> None:
    if m := re.match(regex, mail):
        print(f"{mail} es un correo válido")
        print(m.span())
    else:
        print(f"{mail} no es un correo válido")


check_mail(mail)
