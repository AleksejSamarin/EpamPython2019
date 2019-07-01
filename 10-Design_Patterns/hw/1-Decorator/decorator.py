"""
Используя паттерн "Декоратор" реализуйте возможность дополнительно добавлять к кофе
    маршмеллоу, взбитые сливки и сироп, а затем вычислить итоговую стоимость напитка.
"""


class Component:
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")


class BaseCoffee(Component):
    def get_cost(self):
        return 90


class Whip(Component):
    def __init__(self, product: Component):
        self.product = product

    def get_cost(self):
        return self.product.get_cost() + 50


class Marshmallow(Component):
    def __init__(self, product: Component):
        self.product = product

    def get_cost(self):
        return self.product.get_cost() + 40


class Syrup(Component):
    def __init__(self, product: Component):
        self.product = product

    def get_cost(self):
        return self.product.get_cost() + 30


if __name__ == "__main__":
    coffee = BaseCoffee()
    coffee = Whip(coffee)
    coffee = Marshmallow(coffee)
    coffee = Syrup(coffee)
    print("Итоговая стоимость за кофе: {}".format(str(coffee.get_cost())))
