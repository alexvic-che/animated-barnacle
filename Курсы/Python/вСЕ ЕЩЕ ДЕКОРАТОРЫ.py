t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def chars(chars = " !?"):
    def delet_defis(func):
        def wrapper(*args):
            new_st = ""

            for s in func(*args):

                if s in chars:
                    new_st += "-"
                else: new_st += s
            while "--" in new_st:
                new_st = new_st.replace("--", "-")
            return new_st
        return wrapper
    return delet_defis



@chars(chars="?!:;,. ")
def translate_to_lat(st):
    st = st.lower()
    new_st = ""
    for s in st:
        if s in t:
            new_st+=t[s]
        else:
            new_st+=s
    return new_st




print(translate_to_lat(input()))