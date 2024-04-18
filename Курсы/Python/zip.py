import sys

# lst1 = [int(x) for x in input().split()]
# lst2 = [int(x) for x in input().split()]
# def ymnz(tup):
#     return int(tup[0])*int(tup[1])
#
# z = map(ymnz,zip(lst1, lst2))
#
# print(next(z))
# print(next(z))
# print(next(z))

lst_in = list(map(str.strip, sys.stdin.readlines()))


lst = [[int(el) for el in x.split() ] for x in lst_in]

z = list(zip(*lst))
z = list(zip(*z))
for el in z:
    print(*el)