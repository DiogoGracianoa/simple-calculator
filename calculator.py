class Calculator:
    """Uma calculadora com operações básicas e algumas funções extras."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

    def average(self, values):
        if not values:
            raise ValueError("Lista vazia não é permitida.")
        return sum(values) / len(values)
