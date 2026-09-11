import math

def round_(value: float) -> float:
    """Return rounded value, 0.5 is 1.0."""

    return math.floor(value + 0.5)


if __name__ == "__main__":
    print(round(1.5))           # Вернет 2
    print(round(2.5))           # Вернет 2
    print(round(3.5))           # Вернет 4
    print(round(4.5))           # Вернет 4
    print(round(5.5))           # Вернет 6
    print(round(3.14159, 3))    # Вернет 3.142

    print(round_(0.5))          # Вернет 1
    print(round_(1.5))          # Вернет 2
    print(round_(2.5))          # Вернет 3
    print(round_(3.5))          # Вернет 4
    print(round_(4.5))          # Вернет 5
    print(round_(5.5))          # Вернет 6
