class TicTacToe:
    def __init__(self):
        self.pole = ((Cell(), Cell(),Cell()),(Cell(), Cell(),Cell()),(Cell(), Cell(),Cell()))

    def clear(self):
        for tup in self.pole:
            for cell in tup:
                cell.value = 0
                cell.is_free = True
    def __getitem__(self, item):
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(len(self.pole)))
        if type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(len(self.pole)))
        else:
            return self.pole[r][c].value


    def __setitem__(self, key, value):
        if key[0]>2 or key[0]<0:
            raise IndexError('неверный индекс клетки')
        if key[1]>2 or key[1]<0:
            raise IndexError('неверный индекс клетки')
        if self.pole[key[0]][key[1]].is_free == False:
            raise ValueError('клетка уже занята')
        if self.pole[key[0]][key[1]]:
            self.pole[key[0]][key[1]].value = value
            self.pole[key[0]][key[1]].is_free = False
class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free

game = TicTacToe()
print(game[0, 0])
game[0, 0] = 1 # установка нового значения, если поле закрыто
print(game[0, 0])
res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)
print(res)
slice_1 = game[:, 1] # выбираются все элементы (кортеж) столбца с индексом indx
slice_2 = game[1, :] # выбираются все элементы (кортеж) строки с индексом indx
