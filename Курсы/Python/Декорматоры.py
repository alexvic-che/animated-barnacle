
# def func_show(func):
#     def sad(*args, *kwargs):
#         print(f"Площадь прямоугольника: {func()}")
#
#     return sad
#
# @func_show
# def get_sq(width, height):
#     s = width*height
#     return s
#
# get_sq(4,5)







def get_sort(func):
    def wrapper(*args):
        lst = func(*args)
        lst.sort()
        return lst

    return wrapper

@get_sort
def get_list(st_di):
    lst = [int(x) for x in st_di.split()]
    return lst


def get_dict(func):
    def wrapper(*args):
        lst1, lst2 = func(*args)
        d = {}
        i = 0
        while i < len(lst1):
            d[lst1[i]] = lst2[i]
            i+=1
        return d

    return wrapper
@get_dict
def get2_list(st1, st2):
    lst1 = [x for x in st1.split()]
    lst2 = [x for x in st2.split()]
    return lst1, lst2

print(*sorted(get2_list(input(), input()).items()))


