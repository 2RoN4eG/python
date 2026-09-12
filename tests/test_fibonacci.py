"""Test cases for fibonacci sequence generator
"""

import pytest


@pytest.mark.parametrize("value,expected", [
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    (9, 21),
    (10, 34)
])
def test_round(value, expected):
    from fibonacci import fibonacci

    for _ in fibonacci(value):
        print(f'index: {value}, number: {_}')
        number = _

    assert(number == expected)
