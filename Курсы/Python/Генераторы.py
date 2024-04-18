# lst = [abs(float(x)) for x in input().split()]
# print(lst)
# lst = [int(x) for x in input()]
# print(lst)
# N = int(input())
# lst = [[1 if j==i else 0 for j in range(N)] for i in range(N)]
# for i in lst:
#     print(*i)

# lst = [x for x in input().split() if len(x)>5]
# print(*lst)


# lst = [x for x in range(1, n+1) if n%x == 0]
# print(*lst)


# N = int(input())
# lst = [[i for j in range(N)] for i in range(N)]
#
# for x in lst:
#     print(*x)

# lst = [float(x) for x in input().split()]
#
# lst2 = [lst[i]  for i in range(len(lst)) if i%2 == 0]
# print(lst2)

# lst = [int(x) for x in input().split()]
# lst2 = [int(x) for x in input().split()]
# lst3= [lst[i]+lst2[i] for i in range(len(lst))]
# print(*lst3)

l_f = [i for i in input().split()]

lst = [[l_f[j-1], int(l_f[j])] for j in range(len(l_f)) if j%2!=0]
print(lst)