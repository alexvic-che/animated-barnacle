import sys


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        if not self.dict_db:
            self.dict_db[record] = [record]
            return
        for el in self.dict_db:
            if hash(el) == hash(record):
                self.dict_db[el].append(record)
                return
        self.dict_db[record] = [record]

    def read(self, pk):
        for value in self.dict_db.values():
            for el in value:
                if el.pk == pk:
                    return el
        return None




class Record:
    pk = 0
    def __init__(self,fio, descr, old):
        self.fio = fio if type(fio) == str else None
        self.descr =descr if type(descr) == str else None
        self.old = old if type(old) == int else None
        self.pk = self.__new_pk()
    @classmethod
    def __new_pk(cls):
        cls.pk += 1
        return cls.pk

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = list(map(str.strip, sys.stdin.readlines()))

db = DataBase("path")

for el in lst_in:
    fio, descr, old = el.split("; ")
    db.write(Record(fio, descr, old))


for key, value in db.dict_db.items():
    for v in value:
        print(f"{key.fio}, {v.descr}")
