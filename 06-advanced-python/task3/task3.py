"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""


class ShiftDescriptor:

    def __init__(self, shift):
        self.value = None
        self.shift = shift

    def modify(self, string):
        return ''.join(list(map(lambda x: chr(ord(x) + self.shift)
                            if (ord(x) + self.shift) < 124 else chr(97 + (ord(x) + self.shift) % 123), list(string))))

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = self.modify(value)


class CeasarSipher:

    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


if __name__ == '__main__':
    a = CeasarSipher()
    a.message = 'abc'
    a.another_message = 'hello'

    assert a.message == 'efg'
    assert a.another_message == 'olssv'
