# s = input()
#
# lst = [int(x) for x in s.split()]
#
# tup = tuple(lst)
#
# lst.sort()
# tp_lst = tuple(sorted(tup))

# def get_sort(d):
#     dic = dict(sorted(d.items(), reverse=True))
#     lst = [x for x in dic.values()]
#
#     return lst
#
#
# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# print(get_sort(d))

s = [int(x) for x in input().split()]

se = set(s)

s = sorted(se, reverse=True)

print(*s[:4])


