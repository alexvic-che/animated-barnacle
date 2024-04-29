class Vector:
    def __init__(self,*args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def get_coords(self):
        return self.coords

    def __add__(self, other):
        if len(self) != len(other):
            raise TypeError('размерности векторов не совпадают')

        for i in range(len(self)):
            if type(self.coords[i])==float or type(other.coords[i]) ==float:
                new_coords = tuple((self.coords[i] + other.coords[i] for i in range(len(self))))
                return Vector(*new_coords)

        new_coords = tuple((self.coords[i] + other.coords[i] for i in range(len(self))))
        return VectorInt(*new_coords)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if len(self) != len(other):
            raise TypeError('размерности векторов не совпадают')

        for i in range(len(self)):
            if type(self.coords[i]) == float or type(other.coords[i]) == float:
                new_coords = tuple((self.coords[i] - other.coords[i] for i in range(len(self))))
                return Vector(*new_coords)

        new_coords = tuple((self.coords[i] - other.coords[i] for i in range(len(self))))
        return VectorInt(*new_coords)

    def __rsub__(self, other):
        if len(self) != len(other):
            raise TypeError('размерности векторов не совпадают')

        for i in range(len(self)):
            if type(self.coords[i]) == float or type(other.coords[i]) == float:
                new_coords = tuple((other.coords[i] - self.coords[i] for i in range(len(self))))
                return Vector(*new_coords)

        new_coords = tuple((other.coords[i] - self.coords[i]  for i in range(len(self))))
        return VectorInt(*new_coords)



class VectorInt(Vector):
    def __init__(self, *args):
        for el in args:
            if type(el) != int:
               raise ValueError('координаты должны быть целыми числами')

        super().__init__(*args)



v = VectorInt(1, 2, 3, 4)
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v_1 = v1 + v2  # v1 - объект класса VectorInt
v_2 = v1 - v2  # v1 - объект класса VectorInt
print(v_1, v_2)