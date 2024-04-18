class String:
    is_empty = False

s1 = String()
s2 = String()

s2.is_empty = True
print(String.is_empty)
print(s1.is_empty)
print(s2.is_empty)

b = s2.is_empty
print(b)