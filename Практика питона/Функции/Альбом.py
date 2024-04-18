def make_albom(ima_ispolnitela, name_albom, kolichestvo_dorozek = None):
    return {ima_ispolnitela: name_albom}

print(make_albom(input("isp"), input("albom")))
