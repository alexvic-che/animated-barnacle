class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        elif self.MIN_DIMENSION > value or value > self.MAX_DIMENSION:
            return
        else:
            super().__setattr__(key, value)
        # super().__setattr__(key, value)


d = Dimensions(10.5, 20.1, 30)
print(d.__dict__)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
print(a, b , c)
d.MAX_DIMENSION = 10  # исключение AttributeError
