from random import randint
class Ship:
    def __init__(self, length , tp=1 ,x=None, y=None):
        if not 1<=length<=4:
            raise ValueError
        if type(x)!=int and x != None:
            raise ValueError
        if type(y)!=int and y != None:
            raise ValueError
        if not 1<=tp<=2:
            raise ValueError
        self._x = x
        self._y = y
        self._y_f = None
        self._x_f = None
        self._length = length
        self._tp =tp
        self._is_move = True
        self._cells = [1 for i in range(self._length)]
    def __eq__(self, other):
        return self._x==other.x and self._y==other.y
    def check_item(self,item):
        if type(item)!=int:
            raise ValueError("Некоректный индекс")
        if item<0 or item >self._length-1:
            raise ValueError
    def __getitem__(self, item):
        self.check_item(item)
        return self._cells[item]
    def __setitem__(self, key, value):
        self.check_item(key)
        if value not in (1,2):
            raise ValueError("Некоректное волюме")
        self._cells[key] = value


    def check_coords(self,x,y):
        if type(x)!=int and x != None:
            raise ValueError
        if type(y)!=int and y != None:
            raise ValueError
    def set_start_coords(self,x,y):
        self.check_coords(x,y)
        self._x = x
        self._y = y
        if self._length == 1:
            self._x_f = x
            self._y_f = y
        elif self._tp ==1:
            self._y_f = self._y
        elif self._tp == 2:
            self._x_f = self._x
    def get_start_coords(self):
        return (self._x, self._y)

    def move(self,go):
        if self._is_move:
            pass

    def is_collide(self, ship):
        x1 = self._x
        y1 = self._y
        width1 = None
        height1 = None
        if self._tp == 1:
            height1 = 3
            width1 = self._length
        if self._tp == 2:
            height1 = self._length
            width1 = 3
        x2 = ship._x
        y2 = ship._y
        width2 = None
        height2 = None
        if ship._tp == 1:
            height2 = 3
            width2 = ship._length
        if ship._tp == 2:
            height2 = ship._length
            width2 = 3
        if (x1 < x2 + width2 and x1 + width1 > x2 and y1 < y2 + height2 and y1 + height1 > y2):
            return True
        else:
            return False



    def is_out_pole(self,size=10):
        if self._x>size-1 or self._y>size-1 or self._y<0 or self._x<0:
            return True
        if self._x_f>size-1 or self._y_f>size-1 or self._x_f<0 or self._y_f<0:
            return True
        return False

class GamePole:
    def __init__(self,size=10):
        self._size = size
        self._ships = []
        self._pole = [[0]*self._size for i in range(self._size)]
    def init(self):
        i = 0
        while i < 4:
            t = randint(1,2)
            self._ships.append(Ship(1, tp = t))
            i+=1
        i = 0
        while i < 3:
            t = randint(1, 2)
            self._ships.append(Ship(2,tp = t))
            i += 1
        i = 0
        while i < 2:
            t = randint(1, 2)
            self._ships.append(Ship(3,tp = t))
            i += 1
        t = randint(1, 2)
        self._ships.append(Ship(4,tp = t))
        pole = self._pole[:]
        ships_good = []
        for i, ship in enumerate(self._ships):
            if i == 0:
                x = randint(0, 9)
                y = randint(0, 9)
                ship.set_start_coords(x, y)
                pole[y][x] = 1
                ships_good.append(ship)
                continue
            elif 0 < i < 4:
                x = randint(0, 9)
                y = randint(0, 9)
                ship.set_start_coords(x, y)
                while any(map(ship.is_collide,ships_good)):
                    x = randint(0, 9)
                    y = randint(0, 9)
                    ship.set_start_coords(x, y)
                ships_good.append(ship)
                pole[y][x] = 1
                continue
            elif 4 <= i < 7:
                x = randint(0, 9)
                y = randint(0, 9)
                ship.set_start_coords(x, y)
                if ship._tp == 1:
                    ship._x_f = x + 1
                elif ship._tp == 2:
                    ship._y_f = y + 1
                while any(map(ship.is_collide,ships_good)):
                    x = randint(0, 9)
                    y = randint(0, 9)
                    ship.set_start_coords(x, y)
                    if ship._tp == 1:
                        ship._x_f = x - 1

                    elif ship._tp == 2:
                        ship._y_f = y - 1


                ships_good.append(ship)
                pole[ship._y][ship._x] = 1
                pole[ship._y_f][ship._x_f] = 1



    def clear_pole(self):
        self._pole = [[0]*self._size for i in range(self._size)]

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            go = randint(-1,1)
            ship.move(go)
    def show(self):
        for row in self.get_pole():
            print(*row)

    def get_pole(self):
        return self._pole



f = GamePole()

f.init()
f.show()
print()
f.clear_pole()