import sys


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)

# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Python; Балакирев С.М.; 2020',
'Python ООП; Балакирев С.М.; 2021',
'Python ООП; Балакирев С.М.; 2022',
'Python; Балакирев С.М.; 2021']
print(lst_in)
lst_bs = []
for el in lst_in:
    name, author, year = el.split("; ")
    lst_bs.append(BookStudy(name, author, int(year)))


unique_books = len(set(lst_bs))
print(unique_books)