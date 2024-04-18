class WordString:
    def __init__(self, stri =""):
        self.stri = stri

    def __len__(self):
        while "  " in self.string:
            a = self.string.replace("  ", " ")
            self.string = a
        lst = [el for el in self.string.split()]
        return len(lst)

    def __call__(self, indx,*args, **kwargs):
        while "  " in self.string:
            a = self.string.replace("  ", " ")
            self.string = a

        lst = [el for el in self.string.split()]
        return lst[indx]

    @property
    def string(self):
        return self.stri

    @string.setter
    def string(self, string):
        self.stri = string

words = WordString()
words.string = "Курс                      по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")


