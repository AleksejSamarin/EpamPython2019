from functools import reduce


def is_armstrong(number):
    string = str(number)
    length = len(string)
    result = reduce(lambda x, y: x + y, [int(x)**length for x in string]) == number
    return result


assert is_armstrong(153), 'Armstrong number'
assert is_armstrong(10), 'Not Armstrong number'
