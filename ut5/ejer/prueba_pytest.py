def calculator(x, y, operator: str) -> int:
    match operator:
        case "+":
            return x + y
        case "-":
            return x - y
        case "/":
            return x / y
        case "*":
            return x * y
        case "**":
            return x**y
    return None


def suma(x: int, y: int):
    return x + y