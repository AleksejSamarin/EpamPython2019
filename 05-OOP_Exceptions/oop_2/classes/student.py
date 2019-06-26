from .exceptions import DeadlineError
from .homework import Homework
from .homework_result import HomeworkResult
from .person import Person


class Student(Person):

    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError('You are late')
