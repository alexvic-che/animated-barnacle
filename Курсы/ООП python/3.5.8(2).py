class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls

class Money:
    type_money = None
    EPS = 0.1
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def get_volums(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("sdad")
        v1 = self.volume/self.cb.rates[self.type_money]
        v2 = other.volume/other.cb.rates[other.type_money]
        return v1, v2
    def __eq__(self, other):
        v1, v2 =self.get_volums(other)
        return abs(v1 - v2) < self.EPS
    def __lt__(self, other):
        v1, v2 = self.get_volums(other)
        return v1 < v2
    def __le__(self, other):
        v1, v2 = self.get_volums(other)
        return v1 <= v2

class MoneyR(Money):
    type_money = 'rub'

class MoneyD(Money):
    type_money = 'dollar'

class MoneyE(Money):
    type_money = 'euro'