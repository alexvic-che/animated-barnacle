class Tuple(tuple):
    def __init__(self, tup):
        self.tup = tuple(tup)

    def __add__(self, other):
        new_tup = self.tup + tuple(other)
        return Tuple(new_tup)


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"