from collections import defaultdict
from .homework import Homework
from .homework_result import HomeworkResult
from .person import Person


class Teacher(Person):

    homework_done = defaultdict(list)

    @classmethod
    def check_homework(cls, result: HomeworkResult) -> bool:
        condition_length = len(result.solution) > 5
        key = result.homework
        if condition_length and key not in cls.homework_done:
            cls.homework_done[key].append(result)
        return condition_length

    @classmethod
    def reset_results(cls, homework: Homework = None):
        if homework:
            cls.homework_done.pop(homework)
        else:
            cls.homework_done.clear()

    @staticmethod
    def create_homework(text: str, days: int) -> Homework:
        return Homework(text, days)
