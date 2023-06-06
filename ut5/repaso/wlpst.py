import re

pswd = "W3l0P3st31234"
pwd1 = "Azzzzz1112222"


def check_passwd(passwd: int) -> bool:
    regex = r"^[A-Z][A-Za-z]{5,8}[1-9]{3,5}[1-9]{1,4}$"
    if re.match(regex, passwd):
        return True
    else:
        return False


print(check_passwd(pswd))

print(check_passwd(pwd1))
