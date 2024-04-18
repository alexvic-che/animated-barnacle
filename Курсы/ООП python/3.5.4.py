class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def get_v(self):
        v = self.a * self.b * self.c
        return v
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self,a):
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

    def __lt__(self, other):
        return self.get_v()<other.get_v()

    def __le__(self, other):
        return self.get_v() <= other.get_v()


    def __setattr__(self, key, value):
        if not self.MIN_DIMENSION<=value<=self.MAX_DIMENSION:
            return
        object.__setattr__(self, key, value)

class ShopItem:
    def __init__(self,name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

lst_shop = [ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
            ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
            ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
            ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200)),
            ]

def v(x):
    return x.dim.get_v()

lst_shop_sorted = sorted(lst_shop, key = v)

print(lst_shop_sorted[0].dim.get_v())
print(lst_shop_sorted[3].dim.get_v())

dim1 = Dimensions(10,10,10)
dim2 = Dimensions(10,10,10)

res = dim1>=dim2
print(res)