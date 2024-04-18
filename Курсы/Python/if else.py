# lst = list(map(float,input().split()))
# s = input().lower()
# a = s[::-1]
# if s == a:
#     print("ДА")
# else:
#     print("НЕТ")

# a, b, c = list(map(int,input().split()))
#
# if m%n == 0:
#     print(int((m/n)))
# else:print(f"{m} на {n} нацело не делится")

# a, b, c = list(map(int,input().split()))
# if pow(c, 2) == pow(a, 2) + pow(b,2):
#     print("ДА")
# else:print("НЕТ")
#
# a = input()
#
# if a[-1] == '7':
#     print("ДА")
# else:print("НЕТ")

# a = input()
# if 't' in a and 'h' in a and 'o' in a:
#     print("ДА")
#
# else:print("НЕТ")

# a = input().split()
#
# if "Москва" in a:
#     a.remove("Москва")
# print(*a)

# a, b, c, d = list(map(int,input().split()))
# a = a - 2
# b = b - 2
#
# if (c<=a and d <= b) or (c<=b and d <= a):
#     print("ДА")
# else:print("НЕТ")

# lst = list(map(int,input()))
# if lst[0]+lst[1]+lst[2] == lst[-1]+lst[-2]+lst[-3]:
#     print("ДА")
# else:print("НЕТ")
#
# a = float(input())
# x = 0
# y = 3
# s_a = 0
# if a >= 10:
#     s_a += a
#     f = str(s_a)[0]
#     s_a = int(f) * 10
#     x = x + s_a
#     y = y + s_a
#
# if x <= a <= y or (x+5) <= a <= (y+5):
#     print('green')
# else:
#     print('red')

# m = int(input())
#
# if m == 1:
#     print("1. Введение в Python")
# elif m == 2:
#     print("2. Строки и списки")
# elif m == 3:
#     print("3. Условные операторы")
# elif m == 4:
#     print("4. Циклы")
# elif m == 5:
#     print("5. Словари, кортежи и множества")
# elif m == 6:
#     print("6. Выход")

# a, b, c = list(map(int, input().split()))
#
# if a < b:
#     if a < c:
#         print("a -> min")
#     else: print("c -> min")
#
# elif b < c:
#         print("b -> min")
# else: print("c -> min")

# lst = input().split()
#
# if lst[0] == "1":
#     if lst[1] == '1':
#         print("12.31", "01.02")
#     elif 2 <= int(lst[1]) <= 9:
#         print(f"0{lst[0]}.0{int(lst[1])-1}, 0{lst[0]}.0{int(lst[1])+1}")
#     elif lst[1] == '31':
#         print("01.30", "02.01")
# elif lst[0] == '2':
#     if lst[1] == '1':
#         print("01.31", "02.02")
#     elif 2 <= int(lst[1]) <= 9:
#         print(f"0{lst[0]}.0{int(lst[1])-1}, 0{lst[0]}.0{int(lst[1])+1}")
#     elif lst[1] == '28':
#         print("02.27", "03.01")
# elif lst[0] == '3':
#     if lst[1] == '1':
#         print("02.28", "03.02")
#     elif 2 <= int(lst[1]) <= 9:
#         print(f"0{lst[0]}.0{int(lst[1])-1}, 0{lst[0]}.0{int(lst[1])+1}")
#     elif lst[1] == '31':
#         print("03.30", "04.01")
# elif lst[0] == '4':
#     if lst[1] == '1':
#         print("03.31", "04.02")
#     elif 2 <= int(lst[1]) <= 9:
#         print(f"0{lst[0]}.0{int(lst[1])-1}, 0{lst[0]}.0{int(lst[1])+1}")
#     elif lst[1] == '30':
#         print("04.29", "05.01")
# elif lst[0] == '5':
#     if lst[1] == '1':
#         print("04.30", "05.02")
#     elif 2 <= int(lst[1]) <= 9:
#         print(f"0{lst[0]}.0{int(lst[1])-1}, 0{lst[0]}.0{int(lst[1])+1}")
#     elif lst[1] == '31':
#         print("05.30", "06.01")
# elif lst[0] == '6':
#     if lst[1] == '1':
#         print("05.31", "06.02")
#     elif 2 <= int(lst[1]) <= 9:
#         print(f"0{lst[0]}.0{int(lst[1])-1}, 0{lst[0]}.0{int(lst[1])+1}")
#     elif lst[1] == '30':
#         print("06.29", "07.01")
# elif lst[0] == '7':
#     if lst[1] == '1':
#         print("06.30", "07.02")
#     elif 2 <= int(lst[1]) <= 9:
#         print(f"0{lst[0]}.0{int(lst[1])-1}, 0{lst[0]}.0{int(lst[1])+1}")
#     elif lst[1] == '31':
#         print("07.30", "08.01")
#     else: print()
# elif lst[0] == '8':
#     if lst[1] == '1':
#         print("07.31", "08.02")
#     elif 2 <= int(lst[1]) <= 9:
#         print(f"0{lst[0]}.0{int(lst[1])-1}, 0{lst[0]}.0{int(lst[1])+1}")
#     elif lst[1] == '31':
#         print("08.30", "09.01")
# elif lst[0] == '9':
#     if lst[1] == '1':
#         print("08.31", "09.02")
#     elif 2 <= int(lst[1]) <= 9:
#         print(f"0{lst[0]}.0{int(lst[1])-1}, 0{lst[0]}.0{int(lst[1])+1}")
#     elif lst[1] == '30':
#         print("09.29", "10.01")


