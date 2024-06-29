from random import randint

class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def is_collide(self, ship):
        if self._x is None or self._y is None or ship._x is None or ship._y is None:
            return False
        if self._tp == 1 and ship._tp == 1:
            return self._y == ship._y and abs(self._x - ship._x) < self._length + ship._length
        elif self._tp == 2 and ship._tp == 2:
            return self._x == ship._x and abs(self._y - ship._y) < self._length + ship._length
        else:
            return abs(self._x - ship._x) < self._length and abs(self._y - ship._y) < ship._length

    def is_out_pole(self, size):
        return self._x is None or self._y is None or self._x < 0 or self._x >= size or self._y < 0 or self._y >= size


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        ship_counts = [4, 3, 2, 1]  # Number of ships of each length
        for length in range(1, 5):
            for _ in range(ship_counts[length - 1]):
                tp = randint(1, 2)
                ship = Ship(length, tp)
                self._ships.append(ship)
        for ship in self._ships:
            while True:
                x = randint(0, self._size - 1)
                y = randint(0, self._size - 1)
                ship.set_start_coords(x, y)
                collide = False
                for other_ship in self._ships:
                    if ship != other_ship and ship.is_collide(other_ship):
                        collide = True
                        break
                if not collide:
                    break

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            if ship._is_move:
                direction = randint(-1, 1)
                if direction == 0:
                    direction = 1
                ship.move(direction)
                if ship.is_out_pole(self._size) or any(
                        ship.is_collide(other_ship) for other_ship in self._ships if ship != other_ship):
                    ship.move(-direction)
                    # If ship is still out of bounds or collides after trying to move in the opposite direction,
                    # reset its position to None to indicate it's out of play
                    if ship.is_out_pole(self._size) or any(
                            ship.is_collide(other_ship) for other_ship in self._ships if ship != other_ship):
                        ship._x = None
                        ship._y = None

    def show(self):
        pole = self.get_pole()
        for row in pole:
            print(" ".join(map(str, row)))

    def get_pole(self):
        pole = [[0] * self._size for _ in range(self._size)]
        for ship in self._ships:
            if ship._x is not None and ship._y is not None:
                if ship._tp == 1:
                    for i in range(ship._length):
                        pole[ship._y][ship._x + i] = ship._cells[i]
                else:
                    for i in range(ship._length):
                        pole[ship._y + i][ship._x] = ship._cells[i]
        return pole

# Example Usage
SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()