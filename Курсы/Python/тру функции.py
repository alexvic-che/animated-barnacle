def perimetr(width, height):
    p = (int(width) + int(height))*2
    print(f"Периметр прямоугольника, равен {p}")

# a, b = input().split()
# perimetr(a, b)

def correct_email(email):
    set_A = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
             'S', 'T', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e',
             'i', 'o', 'u', 'y', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
             'v', 'w', 'x', 'y', 'z', '@', '.'}

    if email - set_A == set():
        print("ДА")
    else:
        print("НЕТ")

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
def covert(st, sep="-"):
    st = st.lower().replace(" ", sep)
    slug=""
    for s in st:
        if s == sep:
            slug+=sep
            continue
        slug += t[s] if s in t else s
    return slug




def get_data_fig(*args, **kwargs):
    p=0
    t=[]
    for x in args:
        p +=int(x)
    t.append(p)
    if kwargs:
        if "type" in kwargs:
            t.append(kwargs["type"])
        if "color" in kwargs:
            t.append(kwargs["color"])
        if "closed" in kwargs:
            t.append(kwargs["closed"])
        if "width" in kwargs:
            t.append(kwargs["width"])
    t = tuple(t)
    return t

print(get_data_fig(1,23,4,5,5,7, width=2, type=True, color=1, closed=False))