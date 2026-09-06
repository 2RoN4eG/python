def fibonacci(number):
    """A generator for the Fibonacci sequence."""
    lhs, rhs = 0, 1
    for _ in range(number):
        yield lhs
        lhs, rhs = rhs, lhs + rhs
