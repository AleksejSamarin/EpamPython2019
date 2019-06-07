from typing import Optional
from .homework import Homework


class Student:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework) -> Optional[Homework]:
        if homework.is_active():
            return homework
        print('You are late')
