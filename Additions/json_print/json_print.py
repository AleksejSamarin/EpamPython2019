"""
Реализовать функцию:

def json_pretty_print(s: str) -> Iterable[str]:
    pass

На вход ей подаётся строка, на выходе - итерируемый объект из строк отформатированного json.
Пользоваться библиотечной реализацией prettyprint запрещено.
"""

import json
from typing import Iterable


def json_pretty_print(s: str) -> Iterable[str]:
    return json.dumps(json.loads(s), indent=4).split('\n')


if __name__ == '__main__':
    example = '{"A": [1, null, 22.0, 6, "hello", "{ ,} "], "B": 17}'
    for line in json_pretty_print(example):
        print(line)
