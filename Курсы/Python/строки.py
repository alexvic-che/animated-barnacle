# a, b = map(str, input().split())
# # print("Коды: "+a+" = "+str(ord(a))+", "+b+" = "+str(ord(b)))
# a = input()
# b = input()
# print(a[1::2], b[::2])
#
# a = input()
# print(a[-7::-1])
# a, b = map(str, input().split())
#
# s = len(b)
# n_a = a[:s]
# # print(n_a[1:]>=b[1:])
# a = input()
# print(a.split())
# # print(len(a.split()))
# a = input()
# s = a.replace(' ', '\'')
# print(s)
# print(s.replace(' ', '\"', 1))
#
# lst =  input().split()
#
# print(lst)
# #print(max(lst), min(lst), sum(lst))
#
# lst = list(map(int,input().split()))
#
# print(*sorted(lst,reverse=True))

# cities = ["Москва", "Тверь", "Вологда"]
#
# add_cities = input().split()
# res = cities+ add_cities
# print(res)

# a = list(map(int,input().split()))
# a.append(a[0]!=a[-1])
# print(*a)

# cities = ["Москва", "Казань", "Ярославль"]
#
# cities.insert(1, "Ульяновск")
# print(*cities)
# lst = list(input())
# lst.remove('+')
# lst.remove('7')
# lst.insert(0, '8')
# lst.remove('-')
# lst.remove('-')
# print("".join(lst))
# fio = input().split()
#
# familia = fio.pop()
# otch = list(fio.pop())
# name = list(fio.pop())
# new_fio = f"{familia} {name[0]}.{otch[0]}."
# print(new_fio)


# b=[]
# b.append(a.pop(a.index(max(a))))
# b.append(a.pop(a.index(max(a))))
# b.append(a.pop(a.index(max(a))))
# b.sort()
# print(b)

# lst = list(map(int,input().split()))
#
# lst.append((lst.pop()%2) != 0)
#
# print(*lst)
# lst = list(map(int,input().split()))
#
# print(lst.count(2))

# lst = input().split()
# lst.sort()
# lst.pop(0)
# print(*lst)

# a1 = input().split()
# a2 = input().split()
# a3 = input().split()
# lst = [a1, a2, a3]
# print(lst[0][-1], lst[1][-1], lst[2][-1])
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]


a = 'дядя'

print(a in t[0] or a in t[1] or a in t[2])