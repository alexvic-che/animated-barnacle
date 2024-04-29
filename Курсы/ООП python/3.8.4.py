class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.__array = [self.__cell() for i in range(max_length)]



    def __getitem__(self, item):
        if item<0 or item>=self.__max_length or type(item) != int:
            raise IndexError('неверный индекс для доступа к элементам массива')
        a = self.__array[item].value
        return a

    def __setitem__(self, key, val):
        if key<0 or key>=self.__max_length or type(key) != int:
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.__array[key].value = val

    def __repr__(self):
        return " ".join(map(str, self.__array))


class Integer:
    def __init__(self, start_value = 0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return str(self.__value)


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10


