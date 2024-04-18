class NewList:
    def __init__(self,lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._lst
    def __sub__(self, other):
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst, other_list))

    @staticmethod
    def __diff_list(lst_1, lst_2):
        if len(lst_2)==0:
            return lst_1
        sub = lst_2[:]
        n_l = [x for x in lst_1 if not NewList.__is_elem(x, sub)]
        return n_l if n_l else sub

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x)==type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res

    def __rsub__(self, other):
        return NewList(self.__diff_list(self._lst, other))

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]

print(res_3.get_list())