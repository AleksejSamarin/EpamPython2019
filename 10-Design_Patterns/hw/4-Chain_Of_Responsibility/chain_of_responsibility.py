"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""

from abc import ABC, abstractmethod


class Fridge:
    def __init__(self):
        self.eggs_count = 0
        self.flour_grams = 240
        self.milk_liters = 0.3
        self.sugar_grams = 310
        self.sunflower_oil_milliliters = 5
        self.butter_grams = 55


class DishComponentsHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, storage, needs):
        pass


class PancakeComponentsHandler(DishComponentsHandler):
    def __init__(self):
        self.next = None

    def set_next(self, handler: DishComponentsHandler):
        self.next = handler

    def handle(self, storage: Fridge, needs: dict):
        if self.next:
            self.next.handle(storage, needs)


class EggsCountCheckHandler(PancakeComponentsHandler):
    def handle(self, storage: Fridge, needs: dict):
        if storage.eggs_count < needs['eggs_count']:
            print(f"Eggs: {needs['eggs_count'] - storage.eggs_count} (items)")
        super().handle(storage, needs)


class FlourGramsCountCheckHandler(PancakeComponentsHandler):
    def handle(self, storage: Fridge, needs: dict):
        if storage.flour_grams < needs['flour_grams']:
            print(f"Flour: {needs['flour_grams'] - storage.flour_grams} (grams)")
        super().handle(storage, needs)


class MilkLitersCheckHandler(PancakeComponentsHandler):
    def handle(self, storage: Fridge, needs: dict):
        if storage.milk_liters < needs['milk_liters']:
            print(f"Milk: {needs['milk_liters'] - storage.milk_liters} (liters)")
        super().handle(storage, needs)


class SugarGramsCheckHandler(PancakeComponentsHandler):
    def handle(self, storage: Fridge, needs: dict):
        if storage.sugar_grams < needs['sugar_grams']:
            print(f"Sugar: {needs['sugar_grams'] - storage.sugar_grams} (grams)")
        super().handle(storage, needs)


class SunflowerOilMillilitersCountCheckHandler(PancakeComponentsHandler):
    def handle(self, storage: Fridge, needs: dict):
        if storage.sunflower_oil_milliliters < needs['sunflower_oil_milliliters']:
            print(f"Sunflower oil: {needs['sunflower_oil_milliliters'] - storage.sunflower_oil_milliliters} (milliliters)")
        super().handle(storage, needs)


class ButterGramsCountCheckHandler(PancakeComponentsHandler):
    def handle(self, storage: Fridge, needs: dict):
        if storage.butter_grams < needs['butter_grams']:
            print(f"Butter: {needs['butter_grams'] - storage.butter_grams} (grams)")
        super().handle(storage, needs)


if __name__ == '__main__':
    pancake_needs = {
        'eggs_count': 2,
        'flour_grams': 300,
        'milk_liters': 0.5,
        'sugar_grams': 100,
        'sunflower_oil_milliliters': 10,
        'butter_grams': 120
    }

    eggs_count_handler = EggsCountCheckHandler()
    flour_grams_count_handler = FlourGramsCountCheckHandler()
    milk_liters_handler = MilkLitersCheckHandler()
    sugar_grams_handler = SugarGramsCheckHandler()
    sunflower_oil_milliliters_count_handler = SunflowerOilMillilitersCountCheckHandler()
    butter_grams_count_handler = ButterGramsCountCheckHandler()

    eggs_count_handler.set_next(flour_grams_count_handler)
    flour_grams_count_handler.set_next(milk_liters_handler)
    milk_liters_handler.set_next(sugar_grams_handler)
    sugar_grams_handler.set_next(sunflower_oil_milliliters_count_handler)
    sunflower_oil_milliliters_count_handler.set_next(butter_grams_count_handler)

    fridge = Fridge()
    print('Accurate shopping list:')
    eggs_count_handler.handle(fridge, pancake_needs)
