class Box:
    def __init__(self,name, max_weight):
        self._name= name
        self._max_weight = max_weight
        self._things = []

    def add_thing(self, obj):
        self._things.append(obj)
        new_weight = 0
        for tup in self._things:
            new_weight+= tup[1]
        if new_weight>self._max_weight:
            raise ValueError('превышен суммарный вес вещей')

class BoxDefender:
    def __init__(self, box):
        self._box = box
        self._things = box._things[:]

    def __enter__(self):
        return self._box
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._box._things = self._things
        return False




