import inspect


def modified_func(func, *fixated_args, **fixated_kwargs):
    def func_print_args_kwargs(*fixed_args, **fixed_kwargs):
        """
        > A func implementation of print_args_kwargs
        with pre-applied arguments being:
        > fixated_args values: {fixated_args}
        > fixated_kwargs values: {fixated_kwargs}
        > source_code: {code}
        """
        frame = inspect.currentframe()
        args_dict = inspect.getargvalues(frame)[3]
        code = inspect.getsource(func_print_args_kwargs)
        replaces = (('{fixated_args}', str(args_dict['fixated_args'])),
                    ('{fixated_kwargs}', str(args_dict['fixated_kwargs'])),
                    ('{code}', code[code.rfind('\"\"\"') + 3:]))
        for replace in replaces:
            new_func.__doc__ = new_func.__doc__.replace(*replace)

        summary_args = (*fixated_args, *fixed_args)
        summary_kwargs = {**fixated_kwargs, **fixed_kwargs}
        func(*summary_args, **summary_kwargs)
    return func_print_args_kwargs


def print_args_kwargs(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    new_func = modified_func(print_args_kwargs, 1, 2, a=3, b=4)
    new_func(5, 6, c=7, b=8)
    print(new_func.__doc__)
