import sys

class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for i, value in enumerate(fields):
                setattr(self, value, lst_values[i])
            return True
        else:
            return False





class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


a = StreamReader()
print(a.readlines())