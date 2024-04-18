def tag(tag = "div"):
    def in_tag(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"
        return wrapper
    return in_tag



@tag()
def lower(sst):
    return sst.lower()

print(lower(input()))


