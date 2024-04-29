from random import randint
class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)
    def __init__(self):
        self.pole = ((Cell(),Cell(),Cell()),
                     (Cell(),Cell(),Cell()),
                     (Cell(),Cell(),Cell()))

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0

    def check_win(self, who_is_it = 1):
        check_pole = []
        for row in self.pole:
            if all(map(lambda x: x.value == who_is_it ,row)):
                return True
            check_pole+=[*row]
        for i in range(3):
            if all(map(lambda x: x.value == who_is_it, check_pole[i::3])):
                return True

        if all(map(lambda x: x.value == who_is_it, check_pole[::4])):
            return True
        if all(map(lambda x: x.value == who_is_it, check_pole[3::2])):
            return True
        return False

    @property
    def is_human_win(self):
        return self.check_win(1)

    @property
    def is_computer_win(self):
        return self.check_win(2)

    @property
    def is_draw(self):
        for row in self.pole:
            for el in row:
                if el.value == 0:
                    return False
        if self.is_computer_win == False and self.is_human_win == False:
            return True
        else:
            return False


    def show(self):
        for row in self.pole:
            for cell in row:
                if cell.value == self.FREE_CELL:
                    print("*", end=" ")
                elif cell.value == self.HUMAN_X:
                    print("X", end=" ")
                elif cell.value == self.COMPUTER_O:
                    print("0", end=" ")
            print()
        print()

    def human_go(self):
        i, j = map(int, input("Введите индексы клетки через пробел:").split())
        if self.pole[i][j].value ==0:
            self.pole[i][j].value = 1
        else:
            print("Эта клетка занята")
            self.human_go()
    def computer_go(self):
        i = randint(0, 2)
        j = randint(0, 2)
        while self.pole[i][j].value != 0:
            i = randint(0, 2)
            j = randint(0, 2)

        self.pole[i][j].value = 2



    def check_index(self, item):
        if len(item) != 2:
            raise IndexError('некорректно указанные индексы')
        i, j = item
        if type(i) != int or type(j) != int:
            raise IndexError('некорректно указанные индексы')
        if i>2 or i<0 or j>2 or j<0:
            raise IndexError('некорректно указанные индексы')
    def __getitem__(self, item):
        self.check_index(item)
        i, j = item
        return self.pole[i][j].value

    def __setitem__(self, key, val):
        self.check_index(key)
        i, j = key
        self.pole[i][j].value = val
    def __bool__(self):
        for row in self.pole:
            for el in row:
                if el.value == 0 and self.is_computer_win == False and self.is_human_win == False:
                    return True
        return False



class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        if self.value == 0:
            return True
        else:
            return False


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
