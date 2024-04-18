class Money:
    def __init__(self,money):
        self.money = money

class Point:
    def __init__(self, x, y, color = "black"):
        self.x = x
        self.y = y
        self.color = color

i = 1
j = 1
points = []
while i < 1001:
    if j == 3:
        p = Point(j, j, color="yellow")
        points.append(p)
    else:
        p = Point(j, j)
        points.append(p)
    i+=1
    j+=2

print(points[1].color)