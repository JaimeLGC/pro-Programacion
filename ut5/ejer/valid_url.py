import re

regex = r""

urls = ()


def check_mail(urls: tuple) -> None:
    for url in urls:
        if re.match(regex, url):
            print(f"{url} es una url válida")
        else:
            print(f"{url} no es una url válida")


check_mail(urls)