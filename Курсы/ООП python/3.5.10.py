class Box:

    def __init__(self):
        self.box = []

    def add_thing(self, obj):
        self.box.append(obj)
    def get_things(self):
        return self.box

    def __eq__(self, other):
        if len(self.box) != len(other.box):
            return False
        return all(map(lambda x: x in other.box,self.box))
class Thing:
    def __init__(self,name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.mass == other.mass and self.name.lower() == other.name.lower()

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)