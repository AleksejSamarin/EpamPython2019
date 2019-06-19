"""
Реализовать функцию:

def json_pretty_print(s: str) -> Iterable[str]:
    pass

На вход ей подаётся строка, на выходе - итерируемый объект из строк отформатированного json.
Пользоваться библиотечной реализацией prettyprint запрещено.
"""

import json
import re
from typing import Iterable


# def json_pretty_print(s: str) -> Iterable[str]:
#     return json.dumps(json.loads(s), indent=4).split('\n')


def json_pretty_print(s: str) -> Iterable[str]:
    string_tuples = [(*match.span(), match.group()) for match in re.finditer(r'".+?"', s)]
    for string in string_tuples:
        s = s.replace(string[2], '|'.join([str(string[idx]) for idx in range(2)]))

    replaces = ((' ', ''), ('[', '[\n'), ('{', '{\n'), (',', ',\n'),
                ('}', '\n}'), (']', '\n]'), (':', ': '))
    for replace in replaces:
        s = s.replace(*replace)
    tabs_count = 0
    result_list = s.split('\n')
    for idx, string in enumerate(result_list):
        if '}' in string or ']' in string:
            tabs_count -= 1
        result_list[idx] = '\t' * tabs_count + string
        if '[' in string or '{' in string or string.endswith(': '):
            tabs_count += 1
        for string in string_tuples:
            result_list[idx] = result_list[idx].replace('|'.join([str(string[idx]) for idx in range(2)]), string[2])
    return result_list


if __name__ == '__main__':
    example = '{"A": [1, null, 22.0, 6, "he  ds", ", llo", "{ [, } "], "B": 17}'
    for line in json_pretty_print(example):
        print(line)
