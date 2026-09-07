def fibonacci(number):
    """Generator for the Fibonacci sequence."""
    lhs, rhs = 0, 1
    for _ in range(number):
        yield lhs
        lhs, rhs = rhs, lhs + rhs

if __name__ == "__main__":
    number = int(input("input nuber:"))

    for index, value in enumerate(fibonacci(number)):
        print(f"{index}: {value}")
