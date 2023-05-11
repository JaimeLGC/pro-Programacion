from __future__ import annotations


def load_card_glyphs(path: str = "cards.dat") -> dict[str, str]:
    """Retorna un diccionario donde las claves serán los palos
    y los valores serán cadenas de texto con los glifos de las
    cartas sin ningún separador"""
    with open(path, "r") as f:
        cards = {}
        for line in f:
            stick, value = line.strip().split(":")
            cards[stick] = value.split(",")
    return cards


class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOLS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    A_VALUE = 1
    K_VALUE = 13
    GLYPHS = load_card_glyphs()
    SUITS = {CLUBS, DIAMONDS, HEARTS, SPADES}

    def __init__(self, value: int | str, suit: str):
        if isinstance(value, str) and value not in self.SYMBOLS:
            raise InvalidCardError(
                f"🃏 Invalid card: {repr(value)} is not a supported symbol"
            )
        if int(value) not in range(14) or int(value) <= 0:
            raise InvalidCardError(
                f"🃏 Invalid card: {repr(value)} is not a supported value"
            )
        if suit not in self.SUITS:
            raise InvalidCardError(
                f"🃏 Invalid card: {repr(suit)} is not a supported suit"
            )

        self.value = value
        self.suit = suit

    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS."""
        if self.value in list(self.SYMBOLS):
            self.value = list(self.SYMBOLS)[int(self.value) - 1]
        else:
            self.value = int(self.value)
        return self.value

    def __repr__(self):
        """Devuelve el glifo de la carta"""
        return self.GLYPHS[self.suit][self.cmp_value - 1]

    def __eq__(self, other: Card | object):
        """Indica si dos cartas son iguales"""
        return not self.value < other.value and not self.value > other.value

    def __lt__(self, other: Card):
        """Indica si una carta vale menos que otra"""
        return self.value > other.value

    def __gt__(self, other: Card):
        """Indica si una carta vale más que otra"""
        return self.value < other.value

    def __add__(self, other: Card) -> Card:
        """Suma de dos cartas"""
        if self.cmp_value >= other.cmp_value:
            suit = self.suit
        else:
            suit = other.suit
            
        result = self.cmp_value + other.cmp_value
        if result > self.K_VALUE:
            result = "A"
        else:
            result = self.SYMBOLS[result - 1]

        return Card(result, suit)

    def is_ace(self) -> bool:
        """Indica si una carta es un AS"""
        return self.value == "A"

    @classmethod
    def get_available_suits(cls) -> str:
        """Devuelve todos los palos como una cadena de texto"""
        return f"{cls.CLUBS}{cls.DIAMONDS}{cls.HEARTS}{cls.SPADES}"

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        """Función generadora que devuelve los glifos de las cartas por su palo"""
        return cls.GLYPHS[suit]


class InvalidCardError(Exception):
    def __init__(self, message="🃏 Invalid card"):
        super().__init__(message)
