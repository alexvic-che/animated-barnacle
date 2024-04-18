lst = input().split()

s = sorted(lst, key=len, reverse=True)

print(*s)