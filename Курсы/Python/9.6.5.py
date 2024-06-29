lst1 = [int(el) for el in input().split()]
lst2 = [int(el) for el in input().split()]
lst1.sort()
lst2.sort(reverse=True)

lst = [sum(el) for el in zip(lst1, lst2)]
print(lst)