import re

num = r"(\b\d+\s)"
op = r"(\b\W)"

text = ("1+1", "1-1", "1*1", "1/1", "1  +   1", "1 degdgdg + 1")


def check_op(text: tuple) -> None:
    for item in text:
        number = re.findall(num, item)
        operand = re.search(op, item)[0]
        n1 = int(number[1])
        n2 = int(number[2])

        match operand:
            case "+":
                return n1 + n2
            case "-":
                return n1 - n2
            case "*":
                return n1 * n2
            case "/":
                return n1 / n2


check_op(text)
