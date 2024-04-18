#
# a = 7
# b = -4
# c = 3
# print(a,'\n',b ,'\n', c, sep='')
# a, b = map(int, input().split())
# print(pow(a, b))
# import math
#
# # print(round(math.pi, 3))
# a = 78.50
#
# print((int(a)%3)==0)
# a = float(input())
#
# b = a % 100
# print(b > 50)

# a, b, c = map(int, input().split())
#
# print((a+b)<c and (b+c)<a and (c+a)<b)

# x = 1.2
#
# # print((x>= 0 and x<= 2) or (x>=10 and x<=20))
# X = float(input())
#
# a = round((X - int(X)) * 100)
# print(a>50)


# a, b = map(str, input().split())
# c = (a+' ') * 2
# g = (b+' ') * 3
# print(c,g, sep='')
#
# a = str(input())
# c =str(len(a))
#
# print('Строка: ' + a + '. Длина: ' + c)

a, b = map(str, input().split())
print(a in b, a==b, a>b, a<b)