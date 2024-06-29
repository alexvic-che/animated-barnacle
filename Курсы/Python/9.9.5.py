def is_free(lst):
    for row in lst:
        for el in row:
            if el == "#":
                return True
    return False