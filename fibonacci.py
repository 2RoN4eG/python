"""Generator for the Fibonacci sequence."""

def fibonacci(number: int) -> int:
    """Return Fibonacci number."""

    lhs, rhs = 0, 1
    for _ in range(number):
        yield lhs
        lhs, rhs = rhs, lhs + rhs


if __name__ == "__main__":
    """Main function for fibonacci function."""
    number = int(input("input nuber:"))

    for index, value in enumerate(fibonacci(number)):
        print(f"{index}: {value}")
