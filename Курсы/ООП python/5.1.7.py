lst_in = input().split()

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

a = sum(map(int, filter(is_integer, lst_in)))
print(a)

a = "7.6"
int(a)