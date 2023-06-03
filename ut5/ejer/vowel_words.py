import re

regex = r"(\b[aeiou]\w*\s)"

text = "Esta función admite un uso más avanzado ya que podemos pasar una función en vez de una cadena de texto de reemplazo, lo que nos abre un mayor rango de posibilidades. Siguiendo con el caso anterior, supongamos que queremos hacer la misma transformación pero convirtiendo el apellido a mayúsculas, y asegurarnos de que el nombre queda como título:"


def check_text(text: tuple) -> None:
    print(re.findall(regex, text))


check_text(text)
