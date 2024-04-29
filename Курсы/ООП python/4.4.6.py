class Furniture:

    def __init__(self,name, weight):
        self._name = name
        self._weight = weight

    def __verify_name(self, name):
        if type(name) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if weight <= 0:
            raise TypeError('вес должен быть положительным числом')


    def __setattr__(self, key, value):
        if key == "_name":
            self.__verify_name(value)
        if key == "_weight":
            self.__verify_weight(value)
        object.__setattr__(self, key, value)


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return (self._name, self._weight, self._tp, self._doors)


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


    def get_attrs(self):
        return (self._name, self._weight, self._height)


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return (self._name, self._weight, self._height, self._square)

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())