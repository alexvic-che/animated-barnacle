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
        self._length = length
        self._tp =tp
        self._is_move = True
        self._cells = [1 for i in range(self._length)]
    def __eq__(self, other):
        return self._x==other.x and self._y==other.y

    def check_coords(self,x,y):
        if type(x)!=int and x != None:
            raise ValueError
        if type(y)!=int and y != None:
            raise ValueError
    def set_start_coords(self,x,y):
        self.check_coords(x,y)
        self._x = x
        self._y = y
    def get_start_coords(self):
        return (self._x, self._y)

    def move(self,go):
        if self._is_move:
            pass

    def is_collide(self,ship):
        pass
    def is_out_pole(self,size=10):
        pass

class GamePole:
    def __init__(self,size=10):
        self._size = size
        self._ships = []
        self.__coords_reserv = [()]
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
        for i, ship in enumerate(self._ships):
            if i<4:
                while True:
                    x = randint(0, 10)
                    y = randint(0, 10)
                    if (x,y) not in self.__coords_reserv:
                        self.__coords_reserv.append((x,y))
                        ship.set_start_coords(x, y)
                        break
            elif 4<=i<7:
                if ship._tp == 1:
                    while True:
                        x = randint(0, 10)
                        y = randint(0, 10)
                        x_dep = randint(-1,1)
                        next_x = x+x_dep
                        if (x, y) not in self.__coords_reserv and (next_x,y) not in self.__coords_reserv and next_x<=self._size:
                            self.__coords_reserv.append((x, y))
                            self.__coords_reserv.append((next_x,y))
                            ship.set_start_coords(x, y)
                if ship._tp == 2:
                    while True:
                        x = randint(0, 10)
                        y = randint(0, 10)
                        y_dep = randint(-1, 1)
                        next_y = x + y_dep
                        if (x, y) not in self.__coords_reserv and (x,next_y) not in self.__coords_reserv and next_y<=self._size:
                            self.__coords_reserv.append((x, y))
                            self.__coords_reserv.append((x, next_y))
                            ship.set_start_coords(x, y)
            elif 7<=i<9:


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
        pole = [[0]*self._size for i in range(self._size)]
        return pole



f = GamePole()
f.init()
f.show()