import sys

import math
#a, b = map(int, input().split())

#print(round(math.sqrt(pow(a,2)+pow(b,2)), 2))

# n=5
# k=6
#
# res = int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
# # print(res)
#
# n = 40
# m = 45
# res = math.ceil((n+m)/20)
# print(res)
#
# x = 20
# x = x - x*0.1
# f = 500
# res = math.floor(f/x)
# print(res)

#
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
# lst_in = [[1, 1, 1, 0, 0],
#           [0, 0, 1, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 1, 0, 1 ,0],
#           [0, 0, 0, 0, 0]]

lst_in.append([0]*5)
lst_in.insert(0, [0]*5)
for i, row in enumerate(lst_in):
    row.append(0)
    row.insert(0, 0)



N = len(lst_in)
def verify(lst_in):
    for i,l in enumerate(lst_in):
        for j, el in enumerate(l):
            if el == 0:
                continue
            if el==1 and is_isolate(i, j, lst_in):
                continue
            else:
                return False
    return True
def is_isolate(i, j, lst_in):
     a = lst_in[i-1][j-1]+lst_in[i-1][j]+lst_in[i-1][j+1]
     a += lst_in[i][j+1]+lst_in[i+1][j+1]+lst_in[i+1][j]+lst_in[i+1][j-1]+lst_in[i][j-1]
     if a == 0:
        return True
     else:
        return False



print(verify(lst_in))