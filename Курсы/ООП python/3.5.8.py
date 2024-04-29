class MoneyR:
    def __init__(self,money=0):
        self.__volume = money
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

    def __lt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(other, MoneyR):
            return self.volume < other.volume
        if isinstance(other, MoneyD):
            return self.volume < other.volume * self.cb.rates["rub"]
        if isinstance(other, MoneyE):
            return round((self.volume * self.cb.rates["euro"])/self.cb.rates["rub"], 5) < other.volume
    def __le__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(other, MoneyR):
            return self.volume <= other.volume
        if isinstance(other, MoneyD):
            return self.volume <= other.volume * self.cb.rates["rub"]
        if isinstance(other, MoneyE):
            return round((self.volume * self.cb.rates["euro"])/self.cb.rates["rub"], 5) <= other.volume
    def __eq__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(other, MoneyR):
            return self.volume == other.volume
        if isinstance(other, MoneyD):
            return self.volume == other.volume * self.cb.rates["rub"]
        if isinstance(other, MoneyE):
            return round((self.volume * self.cb.rates["euro"])/self.cb.rates["rub"], 5) == other.volume
class MoneyD:
    def __init__(self, money=0):
        self.__volume = money
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

    def __lt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(other, MoneyD):
            return self.volume < other.volume
        if isinstance(other, MoneyR):
            return self.volume * self.cb.rates["rub"] < other.volume
        if isinstance(other, MoneyE):
            return self.volume * self.cb.rates["euro"] < other.volume
    def __le__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(other, MoneyD):
            return self.volume <= other.volume
        if isinstance(other, MoneyR):
            return self.volume * self.cb.rates["rub"] <= other.volume
        if isinstance(other, MoneyE):
            return self.volume * self.cb.rates["euro"] <= other.volume
    def __eq__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(other, MoneyD):
            return self.volume == other.volume
        if isinstance(other, MoneyR):
            return self.volume * self.cb.rates["rub"] == other.volume
        if isinstance(other, MoneyE):
            return self.volume * self.cb.rates["euro"] == other.volume
class MoneyE:
    def __init__(self, money=0):
        self.__volume = money
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

    def __lt__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(other, MoneyE):
            return self.volume < other.volume
        if isinstance(other, MoneyD):
            return self.volume < other.volume * self.cb.rates["euro"]
        if isinstance(other, MoneyR):
            return self.volume  < round((other.volume * self.cb.rates["euro"])/self.cb.rates["rub"], 2)
    def __le__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(other, MoneyE):
            return self.volume <= other.volume
        if isinstance(other, MoneyD):
            return self.volume <= other.volume * self.cb.rates["euro"]
        if isinstance(other, MoneyR):
            return self.volume <= round((other.volume * self.cb.rates["euro"]) / self.cb.rates["rub"], 2)
    def __eq__(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(other, MoneyE):
            return self.volume == other.volume
        if isinstance(other, MoneyD):
            return self.volume == other.volume * self.cb.rates["euro"]
        if isinstance(other, MoneyR):
            return self.volume == round((other.volume * self.cb.rates["euro"]) / self.cb.rates["rub"], 2)
class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(450)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")