"""Main function for fibonacci function."""


from fibonacci import fibonacci
from order_visitor import OrderVisitor


if __name__ == "__main__":
    number = int(input("input nuber:"))

    for index, value in enumerate(fibonacci(number)):
        print(f"{index}: {value}")

    # Использование
    visitor = OrderVisitor()
    print(visitor.visit({"status": "pending", "id": 123}))      # "Заказ ожидает обработки"
    print(visitor.visit({"status": "shipped", "id": 123}))      # "Заказ в пути"
    print(visitor.visit({"status": "delivered", "id": 123}))    # "Заказ доставлен"
    print(visitor.visit({"status": "unknown", "id": 123}))      # "Неизвестный статус"
    print(visitor.visit({"status": "lost", "id": 123}))         # "Неизвестный статус"
