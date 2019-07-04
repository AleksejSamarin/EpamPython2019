"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.

"""

from __future__ import annotations
import yaml
import os
from abc import ABC, abstractmethod
from datetime import datetime as date


class AbstractDishFactory(ABC):
    @abstractmethod
    def create_first_course(self, menu: dict) -> AbstractFirstCourse:
        pass

    @abstractmethod
    def create_second_course(self, menu: dict) -> AbstractSecondCourse:
        pass

    @abstractmethod
    def create_third_course(self, menu: dict) -> AbstractThirdCourse:
        pass

    def get_day(self) -> str:
        return date.today().strftime("%A")


class VeganDishFactory(AbstractDishFactory):
    def __init__(self):
        self.type = 'vegan'

    def create_first_course(self, menu: dict) -> FirstCourseVeganDish:
        dish = menu[self.get_day()]['first_courses'][self.type]
        return FirstCourseVeganDish(dish)

    def create_second_course(self, menu: dict) -> SecondCourseVeganDish:
        dish = menu[self.get_day()]['second_courses'][self.type]
        return SecondCourseVeganDish(dish)

    def create_third_course(self, menu: dict) -> ThirdCourseVeganDish:
        dish = menu[self.get_day()]['third_courses'][self.type]
        return ThirdCourseVeganDish(dish)


class ChildDishFactory(AbstractDishFactory):
    def __init__(self):
        self.type = 'child'

    def create_first_course(self, menu: dict) -> FirstCourseChildDish:
        dish = menu[self.get_day()]['first_courses'][self.type]
        return FirstCourseChildDish(dish)

    def create_second_course(self, menu: dict) -> SecondCourseChildDish:
        dish = menu[self.get_day()]['second_courses'][self.type]
        return SecondCourseChildDish(dish)

    def create_third_course(self, menu: dict) -> ThirdCourseChildDish:
        dish = menu[self.get_day()]['third_courses'][self.type]
        return ThirdCourseChildDish(dish)


class ChinaDishFactory(AbstractDishFactory):
    def __init__(self):
        self.type = 'china'

    def create_first_course(self, menu: dict) -> FirstCourseChinaDish:
        dish = menu[self.get_day()]['first_courses'][self.type]
        return FirstCourseChinaDish(dish)

    def create_second_course(self, menu: dict) -> SecondCourseChinaDish:
        dish = menu[self.get_day()]['second_courses'][self.type]
        return SecondCourseChinaDish(dish)

    def create_third_course(self, menu: dict) -> ThirdCourseChinaDish:
        dish = menu[self.get_day()]['third_courses'][self.type]
        return ThirdCourseChinaDish(dish)


class AbstractFirstCourse(ABC):
    def __init__(self, name: str):
        self.name = name
        print(f"Here's your first course dish '{self.name}'")

    @abstractmethod
    def get_first_course_full_type_name(self) -> str:
        pass


class AbstractSecondCourse(ABC):
    def __init__(self, name: str):
        self.name = name
        print(f"Here's your second course dish '{self.name}'")

    @abstractmethod
    def get_second_course_full_type_name(self) -> str:
        pass


class AbstractThirdCourse(ABC):
    def __init__(self, name: str):
        self.name = name
        print(f"Here's your third course dish '{self.name}'")

    @abstractmethod
    def get_third_course_full_type_name(self) -> str:
        pass


class FirstCourseVeganDish(AbstractFirstCourse):
    def get_first_course_full_type_name(self) -> str:
        return 'First course vegan dish'


class FirstCourseChildDish(AbstractFirstCourse):
    def get_first_course_full_type_name(self) -> str:
        return 'First course child dish'


class FirstCourseChinaDish(AbstractFirstCourse):
    def get_first_course_full_type_name(self) -> str:
        return 'First course china dish'


class SecondCourseVeganDish(AbstractSecondCourse):
    def get_second_course_full_type_name(self) -> str:
        return 'Second course vegan dish'


class SecondCourseChildDish(AbstractSecondCourse):
    def get_second_course_full_type_name(self) -> str:
        return 'Second course child dish'


class SecondCourseChinaDish(AbstractSecondCourse):
    def get_second_course_full_type_name(self) -> str:
        return 'Second course china dish'


class ThirdCourseVeganDish(AbstractThirdCourse):
    def get_third_course_full_type_name(self) -> str:
        return 'Third course vegan dish'


class ThirdCourseChildDish(AbstractThirdCourse):
    def get_third_course_full_type_name(self) -> str:
        return 'Third course child dish'


class ThirdCourseChinaDish(AbstractThirdCourse):
    def get_third_course_full_type_name(self) -> str:
        return 'Third course china dish'


def get_data_from_yaml_file(file):
    with open(file, 'r', encoding='utf-8') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def client_code(factory: AbstractDishFactory, menu: dict):
    product_a = factory.create_first_course(menu)
    print(product_a.get_first_course_full_type_name())
    product_b = factory.create_second_course(menu)
    print(product_b.get_second_course_full_type_name())


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))
    yaml_file = os.path.join(current_path, './menu.yml')
    menu = get_data_from_yaml_file(yaml_file)
    client_code(ChinaDishFactory(), menu)
