import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# print(lst_in)
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):

        for d in data:
            dic = dict()
            for i, el in enumerate(d.split()):
                dic[self.FIELDS[i]] = el
            self.lst_data.append(dic)


    def select(self,a,b):
        return self.lst_data[a:b+1]


db = DataBase()
db.insert(lst_in)
print(db.select(0, 3))


