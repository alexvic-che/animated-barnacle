class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self) == hash(other)
    def __lt__(self, other):
        return hash(self) < hash(other)


    def __setattr__(self, key, value):
        if value <= 0 :
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, key, value)

s_inp = input()

lst = list(map(str.strip,s_inp.split(";")))
lst_dims = []
for el in lst:
    a, b, c = el.split()
    lst_dims.append(Dimensions(float(a), float(b), float(c)))

lst_dims = sorted(lst_dims)

