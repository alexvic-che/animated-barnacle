

#
# lst = input().split()
#
# mark = {1: 'ужасно', 2: 'неудовлетворительно', 3: 'удовлетворительно', 4: 'прилично', 5: 'отлично'}
#
# d = {i+int(lst[0]) : l for i, l in enumerate(lst[1:]) }
#
# print(d)
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# se1 = set(lst_in)
#
# print(len(se1))

# se1 = {x for x in input().lower().split() if len(x) >= 3}
#
# print(len(se1))
# lst = input().lower().split()
# dic = {key : lst.count(key) for key in lst}
# if "и" in dic:
#     print(dic.get('и'))
# else :
#     print(0)
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Пушкин: Сказака о рыбаке и рыбке',
          'Есенин: Письмо к женщине',
          'Тургенев: Муму',
          'Пушкин: Евгений Онегин',
          'Есенин: Русь'
          ]
# lst = [[key, valeu] for key, value in lst_in[1].split()]
# for l in lst_in:
#     lst.append(l.split(": "))
#
# d = {}
# for l in lst:
#     if l[0] not in d:
#         d[l[0]] = [l[1]]
#     else:
#         d[l[0]].append(l[1])
#
# print(d)
# d ={l for l in lst for i, a in enumerate(l)}


d = {author: {book.split(": ")[1] for book in lst_in if book.startswith(author)} for author in
     {book.split(":")[0] for book in lst_in}}

print(d)
