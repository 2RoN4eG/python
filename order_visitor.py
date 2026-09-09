class OrderVisitor:
    def visit(self, order):
        method_name = f'visit_{order["status"]}'
        method = getattr(self, method_name, self.visit_unknown)
        return method(order)
    
    def visit_pending(self, order):
        return "Заказ ожидает обработки"
    
    def visit_shipped(self, order):
        return "Заказ в пути"
    
    def visit_delivered(self, order):
        return "Заказ доставлен"
    
    def visit_unknown(self, order):
        return "Неизвестный статус"
