# **********
# PALÍNDROMO
# **********


def is_palindrome(text: str) -> bool:
    text_join = "".join(text.lower().split())
    backwards_text = "".join(reversed(text.lower().split()))
    if text_join == backwards_text:
        return True
    return False
