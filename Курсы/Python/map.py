import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

lst2D = [[int(x)for x in st.split()] for st in lst_in ]
print(lst2D)