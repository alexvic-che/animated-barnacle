class Record:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value
        self.__atrs = tuple(kwargs.keys())

    def __getitem__(self, item):
        if item >= len(self.__dict__):
            raise IndexError('неверный индекс поля')
        else:
            return self.__dict__[self.__atrs[item]]
    def __setitem__(self, key, value):
        if key >= len(self.__dict__) and key<0:
            raise IndexError('неверный индекс поля')
        else:
            self.__dict__[self.__atrs[key]] = value



r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.__dict__)
print(r[0])
r[0] = 123123123
print(r[0])

