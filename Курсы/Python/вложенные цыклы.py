import sys

# N = int(input())
# l =[]
# for i in range(N):
#     r = []
#     for j in range(N):
#         if j == (N-1):
#             r.append(5)
#         else:
#             r.append(1)
#     l.append(r)
#
# for i, row in enumerate(l):
#     print(*row)



# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
#
# for i, line in enumerate(lst_in):
#     while line.count("  "):
#         line = line.replace("  ", ' ')
#     line = line.replace(" ", "-")
#     lst_in[i] = line
#     print(line)
#
# n = int(input())
#
# lst = [2]
# if n != 2:
#     for i in range(2, n):
#         if i == 2:
#             continue
#
#         for j in range(2, i):
#             if i % j == 0:
#                 b = False
#                 break
#             else:
#                 a = i
#                 b = True
#         if b == True:
#             lst.append(a)
# else:
#     print(*lst)
# print(*lst)
#
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# # print(lst_in)
# n = int(input())
# ls = [1, 2, 4, 8, 16, 32 , 64]
#
# lst = []
# a = n+1
#
# for i in range(a):

#
# import sys
#
#
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
#
# flag= True
# for i, row in enumerate(lst_in):
#     for j, x in enumerate(row):
#         if lst_in[i][j]==lst_in[j][i]:
#             continue
#         else:
#
#             flag = False
#             break
#     else: break
#
# if flag:
#     print("ДА")
# else:
#     print("НЕТ")

# lst = [int(x) for x in input().split()]
#
# for i in range(len(lst)):
#     for j in range(len(lst)-1):
#         if lst[j]>lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#
# print(*lst)

# a = int(input())
#
# lst = [64, 32, 16, 8, 4, 2, 1]
# b = lst[0]
# res = 0
# lst2 = []
#
# while True:
#     for l in range(len(lst)):
#         if a < b:
#             b = lst[l]
#         else:
#             break
#
#
#     res = a % b
#     h_m= (a - res)/b
#     i = 0
#     while  i < h_m:
#         lst2.append(b)
#         i+=1
#
#     if res == 0:
#         break
#     else:
#         a = res
#
# print(*lst2)

t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]

lst= [[j for j in x.split() if len(j)>3] for x in t ]

print(lst)