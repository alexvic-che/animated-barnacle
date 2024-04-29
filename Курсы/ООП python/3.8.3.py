class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.speed = None
        self.marsh = []

    def add_point(self,x,y,speed):
        self.marsh.append([x,y,speed])

    def __getitem__(self, item):
        return tuple(self.marsh[item])

    def __setitem__(self, key, value):
        if 0<=key<len(self.marsh):
            self.marsh[key][1] = value
        else:
            raise IndexError('некорректный индекс')


