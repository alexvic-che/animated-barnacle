lst_in = input().split()
def func(x):
    try:
        int(x)
        return int(x)
    except:
        try:
            float(x)
            return float(x)
        except:
            return x


lst_out = list(map(func,lst_in))
print(lst_out)
for el in lst_out:
    print(type(el))