"""Generator for the Fibonacci sequence."""

def fibonacci(number: int) -> int:
    """Return Fibonacci number."""
    lhs, rhs = 0, 1
    for _ in range(number):
        yield lhs
        lhs, rhs = rhs, lhs + rhs
