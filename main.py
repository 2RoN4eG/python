"""Main function for fibonacci function."""


from fibonacci import fibonacci


if __name__ == "__main__":
    number = int(input("input nuber:"))

    for index, value in enumerate(fibonacci(number)):
        print(f"{index}: {value}")
