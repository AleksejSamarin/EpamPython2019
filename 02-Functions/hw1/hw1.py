def letters_range(*args, **kwargs) -> list:
    length = len(args)
    if not length or length > 3:
        raise Exception(f"Incorrect args length: {len(args)}")
    letters = [chr(code) for code in range(97, 123)]
    if length == 1:
        stop = letters.index(args[0])
        result = letters[:stop]
    else:
        ordered_args = map(lambda i: letters.index(i), (args[:2]))
        if length == 3:
            ordered_args = (*ordered_args, args[2])
        result = letters[slice(*ordered_args)]
    return list(map(lambda i: kwargs[i] if i in kwargs.keys() else i, result))


if __name__ == '__main__':
    test_args = (('b', 'w', 2), 'g', ('g', 'p'), ('p', 'g', -2), 'a')
    print(letters_range('g', 'p', **{'l': 7, 'o': 0}))
    for args in test_args:
        print(letters_range(*args))
