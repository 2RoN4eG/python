class OrderVisitor:
    """Order visitor class"""

    def visit(self, order: dict) -> str:
        method_name = f'visit_{order["status"]}'
        method = getattr(self, method_name, self.visit_unknown)
        return method(order)

    def visit_pending(self, order: dict) -> str:
        """Return order string with pending status"""
        return f'Заказ {order["id"]} ожидает обработки'

    def visit_shipped(self, order: dict) -> str:
        """Return order string with shipped status"""
        return f'Заказ {order["id"]} в пути'

    def visit_delivered(self, order: dict) -> str:
        """Return order string with delivered status"""
        return f'Заказ {order["id"]} доставлен'

    def visit_unknown(self, order: dict) -> str:
        """Return order string with unknown status"""
        return 'Неизвестный статус'


if __name__ == "__main__":
    visitor = OrderVisitor()
    print(visitor.visit({"status": "pending", "id": 123}))      # "Заказ ожидает обработки"
    print(visitor.visit({"status": "shipped", "id": 123}))      # "Заказ в пути"
    print(visitor.visit({"status": "delivered", "id": 123}))    # "Заказ доставлен"
    print(visitor.visit({"status": "unknown", "id": 123}))      # "Неизвестный статус"
    print(visitor.visit({"status": "lost", "id": 123}))         # "Неизвестный статус"
