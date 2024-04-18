# n, m = map(int, input().split())
# g = []
# while n<=m:
#     g.append(n**2)
#     n += 1
#
# print(*g)

# price = float(input())
# i = 2
# lst = []
# while i <= 10:
#     lst.append(round(price*i, 2))
#     i += 1
#
# print(*lst)

# n = int(input())
# i = 1
# res = 0
# while i <= n:
#     res = res + (1 / i)
#     i += 1
# print(round(res, 3))
# n = int(input())
# res = 0
# while n != 0:
#     res += n
#     n = int(input())
#
# print(res)

# a = input()
# while '--' in a:
#     a = a.replace('--', '-')
#
# print(a)

#
# n = int(input())
# i = 1
# lst = [1, 1]
# res = 0
# while i<=n-2:
#     res = lst[i] + lst[i-1]
#     lst.append(res)
#     i+=1
#
# print(*lst)

# n = int(input())
# i = 3
# cl = 1
# if n < 3:
#     print(1)
# else:
#     while i<=n:
#         cl *= 2
#         i += 3
#
# print(cl)

# n = int(input())
#
#
# res = 1000
# i = 1
#
# while i<=n:
#     res = res + (res*0.05)
#     i+=1
#
# print(round(res, 2))

# n, m = map(int, input().split())
#
# lst =[]
# while n<m:
#     lst.append(n+1)
#     n+=2
#
#
# print(*lst)

# a = 100
#
# lst=[]
# while a<=1000:
#     if a % 47 == 43 and a % 3 == 0:
#         lst.append(a)
#     a+=1
# print(*lst)
#
# p = [0] * 10
#
# s = p.count(1)
# while s < 5:
#     a = int(input())
#     if p[a] == 1:
#         continue
#     p[a] = 1
#     s = p.count(1)
# print(*p)
# a
#
# a = input().lower().split()
# i=0
# while i < len(a):
#     s = a[i]
#     if a[i][0] == a[i][-1]:
#         print("ДА")
#         break
#     i += 1
# else:print("НЕТ")

n = int(input())
i = 1
lst = []
if n<100:
    while i<=n:
        if i%3==0 and i%5==0:
            lst.append(i)
        i += 1
else: print("слишком большое значение n")
print(*lst)