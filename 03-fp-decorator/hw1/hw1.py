from functools import reduce


def problem_6_solver(data: list):
    return sum([i for i in data])**2 - sum([i**2 for i in data])


def problem_9_solver(val) -> tuple:
    return [(a, b, c) for a in range(0, val // 3) for b in range(0, val // 2) for c in range(val // 3, val)
            if ((a**2 + b**2) == c**2 and (a < b < c) and ((a + b + c) == val))][0]


def problem_40_solver(index_needs: list):
    # data = ''.join([str(i) for i in range(index_needs[-1])])
    # digits = [x for i, x in enumerate(data) if i in index_needs]
    # result = reduce(lambda x, y: int(x) * int(y), digits)

    return reduce(lambda x, y: int(x) * int(y),
                  [x for i, x in enumerate(''.join([str(i) for i in range(index_needs[-1])])) if i in index_needs])


def problem_48_solver(first: int, last: int) -> list:
    return list(str(reduce(lambda x, y: x + y, [x**x for x in range(first, last + 1)]))[-10:])


if __name__ == '__main__':
    result_6 = problem_6_solver([i for i in range(1, 101)])
    result_9 = problem_9_solver(1000)
    result_40 = problem_40_solver([10 ** i for i in range(0, 7)])
    result_48 = problem_48_solver(1, 1000)
    print(result_6, result_9, result_40, result_48, sep='\n')
