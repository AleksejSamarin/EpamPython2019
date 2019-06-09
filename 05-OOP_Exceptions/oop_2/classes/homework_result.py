from datetime import datetime
from .homework import Homework


class HomeworkResult:

    def __init__(self, author, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.now()
