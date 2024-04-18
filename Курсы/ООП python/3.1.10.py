import time


class GeyserClassic:
    slot_1 = None
    slot_2 = None
    slot_3 = None
    MAX_DATE_FILTER = 100

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and self.slot_1 is None and isinstance(filter, Mechanical):
            self.slot_1 = filter
        elif slot_num == 2 and self.slot_2 is None and isinstance(filter, Aragon):
            self.slot_2 = filter
        elif slot_num == 3 and self.slot_3 is None and isinstance(filter, Calcium):
            self.slot_3 = filter
    def remove_filter(self, slot_num):
        if int(slot_num) == 1:
            self.slot_1 = None
        elif slot_num == 2:
            self.slot_2 = None
        elif slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return (self.slot_1, self.slot_2, self.slot_3)

    def water_on(self):
        if not None in (self.slot_1, self.slot_2, self.slot_3):
            if 0<=abs(time.time() - self.slot_1.date)<=self.MAX_DATE_FILTER and 0<=abs(time.time() - self.slot_2.date)<=self.MAX_DATE_FILTER and 0<=abs(time.time() - self.slot_3.date)<=self.MAX_DATE_FILTER:
                return True
            else:
                return False
        else:
            return False



class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        else:
            object.__setattr__(self, key, value)

class Aragon:
    def __init__(self, date):
        self.date = date
    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        else:
            object.__setattr__(self, key, value)
class Calcium:
    def __init__(self, date):
        self.date = date
    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        else:
            object.__setattr__(self, key, value)
a = time.time()
print(a)
my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно