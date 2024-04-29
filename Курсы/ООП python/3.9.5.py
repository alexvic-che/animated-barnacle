class Person:
    def __init__(self,fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.info = [fio, job, old, salary, year_job]
        self.i = 0

    def __getitem__(self, item):
        if 0<=item<len(self.info):
            return self.info[item]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if 0<=key<len(self.info):
            self.info[key] = value
        else:
            raise IndexError('неверный индекс')

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        if self.i < len(self.info)-1:
            self.i+=1
            return self.info[self.i]

        raise StopIteration

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
