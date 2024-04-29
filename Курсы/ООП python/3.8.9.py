class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []




    def add_thing(self, thing):
        if self.things:
            res = sum(self.things) + thing
            if res <= self.max_weight:
                    self.things.append(thing)
            else:
                raise ValueError('превышен суммарный вес предметов')
        elif not self.things:
            if thing <= self.max_weight:
                self.things.append(thing)
            else:
                raise ValueError('превышен суммарный вес предметов')
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __getitem__(self, item):
        if item < len(self.things):
            return self.things[item]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if key < len(self.things):
            value_old = self.things[key]
            self.things[key] = value
            if not sum(self.things)<=self.max_weight:
                self.things[key] = value_old
                raise ValueError('превышен суммарный вес предметов')
        else:
            raise IndexError('неверный индекс')

    def __delitem__(self, key):
        if key < len(self.things):
            del self.things[key]
        else:
            raise IndexError('неверный индекс')

class Thing:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        sc = other
        if isinstance(other, Thing):
            res = self.weight + other.weight
        else:
            res = self.weight + sc
        return res
    def __radd__(self, other):
        return self + other

    def __le__(self, other):
        return self.weight <= other

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))

print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок


