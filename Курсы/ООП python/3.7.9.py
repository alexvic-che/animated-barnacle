class Vector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        if isinstance(other, Vector) and not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        sc = other
        new_coords = []
        if isinstance(sc, Vector):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] + other.coords[i])
            return Vector(*new_coords)
        elif type(sc) in (int, float):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] + sc)
            return Vector(*new_coords)



    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        sc = other
        new_coords = []
        if isinstance(sc, Vector):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] * other.coords[i])
            return Vector(*new_coords)
        elif type(sc) in (int, float):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] * sc)
            return Vector(*new_coords)

    def __rmul__(self, other):
        if not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        sc = other
        new_coords = []
        if isinstance(sc, Vector):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] * other.coords[i])
            return Vector(*new_coords)
        elif type(sc) in (int, float):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] * sc)
            return Vector(*new_coords)

    def __sub__(self, other):
        if not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        sc = other
        new_coords = []
        if isinstance(sc, Vector):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - other.coords[i])
            return Vector(*new_coords)
        elif type(sc) in (int, float):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - sc)
            return Vector(*new_coords)
    def __rsub__(self, other):
        if not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        sc = other
        new_coords = []
        if isinstance(sc, Vector):
            for i in range(len(self.coords)):
                new_coords.append(other.coords[i] - self.coords[i])
            return Vector(*new_coords)
        elif type(sc) in (int, float):
            for i in range(len(self.coords)):
                new_coords.append(sc - self.coords[i])
            return Vector(*new_coords)

    def __iadd__(self, other):
        if isinstance(other, Vector) and not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        sc = other
        new_coords = []
        if isinstance(sc, Vector):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] + other.coords[i])
            self.coords = new_coords
            return self
        elif type(sc) in (int, float):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] + sc)
            self.coords = new_coords
            return self
    def __imul__(self, other):
        if isinstance(other, Vector) and not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        sc = other
        new_coords = []
        if isinstance(sc, Vector):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] * other.coords[i])
            self.coords = new_coords
            return self
        elif type(sc) in (int, float):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] * sc)
            self.coords = new_coords
            return self

    def __isub__(self, other):
        if isinstance(other, Vector) and not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        sc = other
        new_coords = []
        if isinstance(sc, Vector):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - other.coords[i])
            self.coords = new_coords
            return self
        elif type(sc) in (int, float):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - sc)
            self.coords = new_coords
            return self
    def __eq__(self, other):
        if isinstance(other, Vector) and not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        for i in range(len(self.coords)):
            if self.coords[i] == other.coords[i]:
                continue
            else:
                return False
        return True

v1 = Vector(1,1,1,1)
v2 = Vector(2,2,2,2)

v1 + v2 # суммирование соответствующих координат векторов

v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает



