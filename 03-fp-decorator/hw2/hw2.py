from functools import reduce


def is_armstrong(number):
    # string = str(number)
    # length = len(string)
    return reduce(lambda x, y: x + y, [int(x)**len(str(number)) for x in str(number)]) == number


assert is_armstrong(153), 'Armstrong number'
assert is_armstrong(10), 'Not Armstrong number'
