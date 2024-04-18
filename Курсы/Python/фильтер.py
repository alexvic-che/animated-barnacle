import sys

# lst = input().split()
#
# b = filter(lambda x: len(x)>5,lst)
# print(next(b), end=" ")
# print(next(b), end=" ")
# print(next(b), end=" ")
#
# def is_dvy(x):
#     x = int(x)
#     if 9<x<100 or -100<x<-9:
#         return True
#     else:
#         return False
# a = list(filter(is_dvy, input().split()))
#
# print(*a)

lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]

set1 = set(lst1)
set2 = set(lst2)
setO = set2 & set1
lst = list(filter(lambda x: x % 2 == 0 , setO))
lst.sort()

print(*lst)