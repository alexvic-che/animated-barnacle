class StringValue:

    def __init__(self,min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length


    def check_string(self, string):
        if type(string) == str and self.min_length<= len(string)<=self.max_length:
            return True
        return False
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        if self.check_string(value):
            setattr(instance,self.name,value)

class PriceValue:

    def __init__(self,max_value = 10000):
        self.min_value = 0
        self.max_value = max_value
    def check_price(self, value):
        if type(value) in (int, float) and  self.min_value<= value<=self.max_value:
            return True
        return False
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        if self.check_price(value):
            setattr(instance,self.name,value)

class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self,product):
        self.goods.append(product)

    def remove_product(self,product):
        self.goods.remove(product)

class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self,name,price):
        self.name = name
        self.price = price




shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")