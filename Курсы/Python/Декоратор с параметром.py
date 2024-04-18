# from functools import wraps
#
#
# def bb(r = 5 ):
#     def aa(func):
#         def wrapper(*args):
#             res = r
#             res += func(*args)
#             return res
#         return wrapper
#     return aa
#
#
# @bb(r = 6)
# def get_lst(st, res = 5):
#     lst = [int(x) for x in st.split()]
#     res =sum(lst)
#     return res
#
#
#
#
# def sum_v(func):
#     @wraps(func)
#     def wrapper(*args):
#         res = sum(func(*args))
#         return res
#     return wrapper
# @sum
# def get_list(st):
#     '''Функция для формирования списка целых значений'''
#     lst = [int(x) for x in st.split()]
#     return lst

