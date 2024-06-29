import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = dict(el.split("=") for el in lst_in)
def asd(items):
    key, value = items
    return value
lst = sorted(d.items(), key=asd, reverse=True)
print(lst)