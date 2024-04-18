class Translator:

    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if eng in self.tr:
            if rus not in self.tr[eng]:
                self.tr[eng].append(rus)
        else:
            self.tr[eng] = [rus]


    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]

tr = Translator()

tr.add('tree' , 'дерево')
tr.add('car' , 'машина')
tr.add('car' , 'автомобиль')
tr.add('river' , 'река')
tr.add('go' , 'идти')
tr.add('go' , 'ехать')
tr.add('go' , 'ходить')

tr.add('milk' , 'молоко')

tr.remove("car")


print(*tr.translate("go"))
