

def counter_add(n):
    def ca(x):
        x += n
        return x

    return ca
#
# cnt = counter_add(2)

# k = int(input())
#
# print(cnt(k))

def asd(tag):
    def get_tag(s):
        tag_s = f"<{tag}>{s}</{tag}>"
        return tag_s
    return get_tag

def addd(tp):
    def convert_str_to_list_or_tuple(str):
        if tp == "list":
            return [int(x) for x in str.split()]
        else:
            tup = tuple([int(x) for x in str.split()])
            return tup
    return  convert_str_to_list_or_tuple

cnt = addd(input())

print(cnt(input()))