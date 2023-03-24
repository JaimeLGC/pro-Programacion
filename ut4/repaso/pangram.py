# ********
# PANGRAMA
# ********


def is_pangram(text: str):
    chars = set("abcdefghijklmnopqrstuvwxyz")
    text_chars = set(text.lower())
    if chars < text_chars:
        return True
    return False
