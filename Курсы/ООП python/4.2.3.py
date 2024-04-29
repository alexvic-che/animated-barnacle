class ListInteger(list):
    def __init__(self, lst):
        for el in lst:
            if type(el) != int:
                raise TypeError('можно передавать только целочисленные значения')
        super().__init__(lst)

    def __setitem__(self, key, value):
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

    def append(self, __object):
        if type(__object) != int:
            raise TypeError('можно передавать только целочисленные значения')
        super().append(__object)


s = ListInteger((1, 2, 3))
s[1] = 10

print(s)
s[0] = 10.5 # TypeError