def get_add(a,b):
    if type(a)==int and type(b)==int:
        return a+b
    elif type(a)==float and type(b)==float:
        return a + b
    elif type(a)==str and type(b)==str:
        return a + b
    return None