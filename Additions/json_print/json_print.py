"""
Реализовать функцию:

def json_pretty_print(s: str) -> Iterable[str]:
    pass

На вход ей подаётся строка, на выходе - итерируемый объект из строк отформатированного json.
Пользоваться библиотечной реализацией prettyprint запрещено.
"""

from typing import Iterable


def json_pretty_print(s: str) -> Iterable[str]:
    replaces = ((' ', ''), ('[', '[\n'), ('{', '{\n'), (',', ',\n'),
                ('}', '\n}'), (']', '\n]'), (':', ': '))
    for replace in replaces:
        s = s.replace(*replace)
    tabs_count = 0
    result_list = s.split('\n')
    for idx, string in enumerate(result_list):
        if string.count('}') or string.count(']'):
            tabs_count -= 1
        result_list[idx] = '\t' * tabs_count + string
        if string.count('[') or string.count('{') or string.endswith(': '):
            tabs_count += 1
    return result_list


if __name__ == '__main__':
    example = '{"A": [1, null, 22.0, 6, "hello"], "B": 17}'
    for line in json_pretty_print(example):
        print(line)
