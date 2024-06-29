class FloatValue:
    @classmethod
    def verify_value(cls,value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance,self.name,value)

class Cell:
    value = FloatValue()
    def __init__(self,start_coord):
        self.value = start_coord

class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell(0.0) for j in range(M)]for i in range(N)]

table = TableSheet(5,3)

i = 0.0
for row in table.cells:
    for cell in row:
        i+=1
        cell.value = i



