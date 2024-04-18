stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

def delete_symbols(stich, chars = "–?!,.;"):
    new_stich = []
    for row in stich:
        a = row
        for el in chars:
            a = a.replace(el, '')
        new_stich.append(a)
    n_n_s = []
    for row in new_stich:
        while row.count("  ")!=0:
            row = row.replace("  ", " ")
        n_n_s.append(row)
    lst_words = []
    for el in n_n_s:
        lst_words.append(list(el.split()))

    return lst_words





class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __gt__(self, other):
        return len(self.lst_words) > len(other.lst_words)
    def __ge__(self, other):
        return len(self.lst_words) >= len(other.lst_words)

    

lst_text =[]
for st in delete_symbols(stich):
    lst_text.append(StringText(st))

lst_text_sorted = sorted(lst_text, reverse=True)

for i, el in enumerate(lst_text_sorted):
    a = " ".join(el.lst_words)
    lst_text_sorted[i] = a


print(lst_text_sorted)