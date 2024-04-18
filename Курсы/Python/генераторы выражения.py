from string import ascii_lowercase
import numpy as np
#
#
# a, b = map(int, input().split())
#
# gen = (abs(x) for x in range(a, b+1))
# i = 1
# for x in gen:
#     if i<=5:
#         print(x)
#         i+=1
#     else:break
#
# a = int(input())
#
#
# gen = (abs(x)**3 for x in range(-a, a+1))
# i = 1
# for x in gen:
#     if i <= 4:
#         print(x, end=' ')
#         i += 1
#     else: break

# i = 0
# for x in ascii_lowercase:
#     if i<50:
#         print(x+x)
#         print(x+1)
#         i+=1
#     else:break

#
# gen = (x+y for x in ascii_lowercase for y in ascii_lowercase)
# for i, x  in enumerate(gen):
#     if i > 50:
#         break
#     print(x, end = " ")

#
# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
#
# gen = (city for i in range(1000000) for city in cities)
#
# for i, x in enumerate(gen):
#     if i>19:
#         break
#     print(x, end=" ")


a, b = map(int, input().split())


gen = (0.5 * pow(x, 2) - 2.0 for x in np.arange(a, b+1, 0.01))

for i,x in enumerate(gen):
    if i >19:
        break
    print(round(x,2), end=" ")