from .homework import Homework


class Teacher:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def create_homework(cls, text: str, days: int) -> Homework:
        return Homework(text, days)
