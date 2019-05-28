counter_name = 0


def make_it_count(func, global_variable_name):
    def new_function():
        globals()[global_variable_name] += 1
        func()
    return new_function


def dummy_function():
    print('dummy function')


if __name__ == '__main__':
    new_func = make_it_count(dummy_function, 'counter_name')
    new_func()
