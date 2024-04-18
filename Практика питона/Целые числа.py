import sys
import math

# a =  11*2**2-13/4+7
# b = 3**9090001
# c = 1024
#print((sys.getsizeof(b))/(1024*1024))

def pas_add(a, b):
    res = a + b
    if res >= 0:
        return res


def foo(a,b):
    res = divmod(a,b)
    return res

def num_sum(a):
    if isinstance(a, int) and not isinstance(a, bool):
        a_to_str=str(abs(a))
        s=0
        for i in a_to_str:
            s+=int(i)
        return s
    return "Это не целое число"

print(num_sum(-5))
print(num_sum('-11'))
print(num_sum(True))













