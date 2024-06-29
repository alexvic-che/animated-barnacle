s = int(input())
n = int(input())
old_s = 0 + s
while n!= 0:

    if s == 0:
        s = old_s
    if s > n:
        break
    n = n - s
    s-=1
print(n)