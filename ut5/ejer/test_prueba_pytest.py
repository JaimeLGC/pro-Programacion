import pytest
from prueba_pytest import calculator, suma


def test_calculator():
    assert (calculator(2, 2, "+")) == 4
    assert (calculator(4, 7, "-")) == -3
    assert (calculator(10, 5, "/")) == 2
    assert (calculator(3, 4, "*")) == 12
    assert (calculator(3, 3, "**")) == 27


@pytest.mark.parametrize(
    ("first_value", "second_value", "expected"),
    [(3, 2, 5), (2, 3, 5), (suma(12, 4), 2, 18)],
)
def test_suma(first_value, second_value, expected):
    assert suma(first_value, second_value) == expected

def test_accepted_values():
    assert isinstance(calculator(2, 3, "+"), int)
    assert isinstance(calculator(5, 2, "-"), int)
    assert isinstance(calculator(10, 2, "/"), float)
    assert isinstance(calculator(4, 3, "*"), int)
    assert isinstance(calculator(2, 5, "**"), int)
    assert isinstance(suma(10, 18), int)