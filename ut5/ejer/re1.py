import re

text = "Estaré disponible el Lunes por la Tarde"

regex = r"[A-Z]"

print(re.findall(regex, text))
