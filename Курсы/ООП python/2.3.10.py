class TVProgram:
    def __init__(self,name):
        self.name = name
        self.items = []
    def add_telecast(self,ti):
        self.items.append(ti)

    def remove_telecast(self, indx):
        for telecast in self.items:
            if telecast.uid == indx:
                self.items.remove(telecast)


class Telecast:
    def __init__(self,id,name,duration):
        self.uid = id
        self.name = name
        self.duration = duration

    @property
    def uid(self):
        return self.__id
    @uid.setter
    def uid(self,id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration
pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
print(pr.items[0].__dict__)
pr.remove_telecast(2)
