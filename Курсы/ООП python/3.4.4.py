class NewList:
    def __init__(self, lst=[]):
        self.lst = lst

    def __sub__(self, other):

        sc = other

        if type(other) is NewList:
            sc = other.lst
        new_ls = self.lst[:]
        for el in sc:
            if el in self.lst:
                new_ls.remove(el)
                if new_ls == []:
                    return NewList(new_ls)

        return NewList(new_ls)
    def __rsub__(self, other):
        sc = other

        if type(other) is NewList:
            sc = other.lst

        for el in self.lst:
            if el in sc and type(el) == :
                sc.remove(el)
                if sc == []:
                    return NewList(sc)
        return NewList(sc)

    def __isub__(self, other):
        sc = other

        if type(other) is NewList:
            sc = other.lst

        for el in sc:
            if el in self.lst:
                self.lst.remove(el)
        return self

    def get_list(self):
        return self.lst





lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]

lst = res_2.get_list() # [1, 2, 3]
print(res_2.lst)
