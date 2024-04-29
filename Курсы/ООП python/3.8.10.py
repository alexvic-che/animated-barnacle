class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.db = []

    def add_data(self,row,col, data):
        while row >= len(self.db):
            self.db.append([None]*col)

        while col >= len(self.db[row]):
            self.db[row].append(None)
        self.db[row][col] = data
        self.rows = len(self.db)
        self.cols = len(self.db[row])
    def remove_data(self,row,col):

        del self.db[row][col]

class Cell:
    pass

sp = SparseTable()

sp.add_data(10,10,Cell())


print(sp.db)
print(sp.cols)
print(sp.rows)
