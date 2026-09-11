import pytest

@pytest.mark.parametrize("value,expected", [
    (0.4, 0),
    (0.5, 0),
    (0.6, 1),
    (1.4, 1),
    (1.5, 2),
    (1.6, 2),
    (2.4, 2),
    (2.5, 2),
    (2.6, 3),
    (3.4, 3),
    (3.5, 4)
])
def test_round(value, expected):
    assert round(value) == expected

@pytest.mark.parametrize("value,expected", [
    (0.4, 0),
    (0.5, 1),
    (0.6, 1),
    (1.4, 1),
    (1.5, 2),
    (1.6, 2),
    (2.4, 2),
    (2.5, 3),
    (2.6, 3),
    (3.4, 3)
])
def test_round_(value, expected):
    from round import round_

    assert round_(value) == expected
