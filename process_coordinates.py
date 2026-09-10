def process_coordinates(point):
    match point:
        case (0, 0):
            print("Точка в начале координат")
        case (x, 0):
            print(f"Точка на оси X: {x}")
        case (0, y):
            print(f"Точка на оси Y: {y}")
        case (x, y):
            print(f"Точка в ({x}, {y})")
        case _:
            print("Не координаты")


if __name__ == "__main__":
    process_coordinates((0, 0))
    process_coordinates((0, 4))
    process_coordinates((5, 0))  # "Точка на оси X: 5"
    process_coordinates((5, 4))  # "Точка в (3, 4)"
