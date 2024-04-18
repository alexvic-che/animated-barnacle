import sys
# morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..',
#          'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..',
#          'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.',
#          'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-',
#          'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.',
#          'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-',
#          'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
#
# st = input().lower()
# kod = []
# for s in st:
#     kod.append(morze.get(s))
#
# print(*kod)

# lst = [int(x) for x in input().split()]
#
#
#
#
# di = dict.fromkeys(lst)
# lst.clear()
# for key in di:
#     lst.append(key)
#
# print(*lst)
# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# d = {}
# for l in lst_in:
#     a = l.split()
#     if int(a[0]) not in d:
#         d[int(a[0])] = [a[1]]
#     else:
#         d[int(a[0])].append(a[1])
#
#
# for key in d.keys():
#     b = d[key]
#     valuse = ", ".join(b)
#     print(f"{key}: {valuse}")

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

N = int(input())*1000
predmeti =[]
cena = []

for value in things.values():
    cena.append(value)

cena.sort(reverse=True)


for c in cena:
    if c <= N:
        N = N-c
        predmeti.append(c)


for key, value in things.items():
    for i, p in enumerate(predmeti):
        if value == p:
            predmeti[i] = key

print(*predmeti)