from typing import Union
from .homework import Homework


class Student:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def do_homework(cls, homework: Homework) -> Union[Homework, None]:
        if homework.is_active():
            return homework
        print('You are late')
        return None
