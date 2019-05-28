def atom(variable=None):

    def get_value():
        return variable

    def set_value(set_value=None):
        nonlocal variable
        variable = set_value
        return variable

    def process_value(*functions):
        nonlocal variable
        for function in functions:
            variable = function(variable)
        return variable

    def delete_value():
        nonlocal variable
        del variable

    return get_value, set_value, process_value, delete_value


if __name__ == '__main__':
    func = atom(123)
    func[1](100)
    func[2](chr, ord, chr)
    func[3]()
    print(func[0]())
