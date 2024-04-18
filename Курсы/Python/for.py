# n = int(input())
#
# for i in range(1, n+1):
#     if n%i == 0:
#         print(i)

# n = int(input())
#
# for i in range(2, n):
#     if n%i == 0:
#         print("НЕТ")
#         break
# else: print("ДА")

# lst = input().lower().split()
# i = 0
# a = ""
# b = ""
# c = ""
# for l in lst:
#     a = l[0]
#     if b == a:
#         c = "ДА"
#         break
#     b = l[-1] if l[-1] != 'ь' and l[-1] != 'ъ' and l[-1] != 'ы' else l[-2]
#
# print(c if c else "НЕТ")
#
# st = input()
#
# a = ""
# if len(st) == 16:
#     for i, d in enumerate(st):
#         if i == 0 and d == "+":
#             continue
#         elif i == 1 and d != "7":
#             a = "НЕТ"
#             break
#         elif i == 2 and d == "(":
#             continue
#         elif i == 6 and d == ")":
#             continue
#         elif i == 10 and d == "-":
#             continue
#         elif i == 13 and d == "-":
#             continue
#         elif d.isdigit():
#             continue
#         else:
#             a = "НЕТ"
#             break
# else:
#     a = "НЕТ"
#
# print(a if a else "ДА")


#
# lts = list(map(float, input().split()))
#
# a = lts[0]
# for i, d  in enumerate(lts):
#     if a > d:
#         a = d
#

lst = input()

a = iter(lst)
b = []

b.append(int(next(a)))
b.append(int(next(a)))
b.append(int(next(a)))
b.append(int(next(a)))

print(*b)
