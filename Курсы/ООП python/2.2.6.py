class StackObj:
    def __init__(self, data):
        self.__next = None
        self.__data = data
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__next = data



class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        if self.last:
            self.last.next = obj
        self.last = obj

    def pop(self):
        h = self.top
        if h is None:
            return
        while h.next != self.last:
            h = h.next
        if h :
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        return []
