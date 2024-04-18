#a = 3 + 3.0 + 4
#print(type(a)).
import math

def to_float(num):
    if isinstance(num, (int, float)):
        return num
    return "Невозможно"

a=5.51231315351
b=6.13513513515135
c=7.13513513515
d=63.5344352251235
def avg_5(a,b,c,d):
    res = round((a+b+c+d)/2, 5)
    return res

def mul_to_int(a, b):
    res = a * b
    if float(res).is_integer():
        return int(res)
    return res

def radius_shara(V):
    radius = ((3*V/(4*math.pi))**(1/3))
    return radius


print(radius_shara(1000))







