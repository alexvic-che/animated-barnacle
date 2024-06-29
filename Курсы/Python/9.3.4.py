s = input()
s_lst = s.split()
def convert(string):
    key , value = string.split("=")
    return (key, value)

tp = tuple((map(convert, s_lst)))



