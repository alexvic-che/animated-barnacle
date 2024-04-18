from random import randint
class Line:
    def __init__(self, a,b,c,d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

i = 0
elements = []
while i<217:
    a = randint(1,3)

    if a == 1:
        p = Line(randint(1, 10000),randint(1, 10000),randint(1, 10000),randint(1, 10000))
        elements.append(p)
    elif a == 2:
        p = Rect(randint(1, 10000),randint(1, 10000),randint(1, 10000),randint(1, 10000))
        elements.append(p)
    elif a == 3:
        p = Ellipse(randint(1, 10000),randint(1, 10000),randint(1, 10000),randint(1, 10000))
        elements.append(p)
    i+=1

for el in elements:
    if Line == type(el):
        el.ep = (0, 0)
        el.sp = (0, 0)
    print(type(el))
    print(el.sp, el.ep)
