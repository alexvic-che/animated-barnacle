# get_sq = lambda x : x**2
#
# get_div = lambda x, y : x/y if x/y !=0 else None
#
# get_abs = lambda  x : x if x >=0 else -x
#
# x = float(input())
#
# get_abs = lambda x : x if x >=0 else -1 * x
# print(get_abs(x))

# s = input()
#
# l = lambda st: "ra" in st
#
# print(l(s))

def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res
lst =[int(x) for x in input().split()]
print(*filter_lst(lst))
print(*filter_lst(lst, key = lambda x: x<0))
print(*filter_lst(lst, key = lambda x: x>=0))
print(*filter_lst(lst, key = lambda x: 3<=x<=5))

def create_global(x):
    global TOTAL
    TOTAL = x