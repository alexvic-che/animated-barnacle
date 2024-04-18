class Cart:
    goods = []

    def add(self,gd):
        self.goods.append(gd)
    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        lst = []
        for el in self.goods:
            lst.append(f"{el.name}: {el.price}")
        return lst


class Table:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:

    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
cart.add(TV("lg", 1444))
cart.add(TV("samsung", 144124))
cart.add(Table("asd", 144))
cart.add(Notebook("asus", 1222))
cart.add(Notebook("asus", 1222))
cart.add(Cup("gr", 55))

print(cart.get_list())

