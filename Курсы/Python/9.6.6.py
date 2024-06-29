import sys

def get_lower_price(dic):
    d = dict(sorted(dic.items()))
    print(d)
    s = list(d.values())
    return s[:3]

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = list(el.split(":") for el in lst_in)
d = {int(key):value for value, key in lst}
print(*get_lower_price(d))




