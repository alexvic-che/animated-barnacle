class SoftList(list):
    def __init__(self,lst):
        self.lst = lst
        super().__init__(lst)

    def __getitem__(self, item):
        if self.lst:
            a = len(self.lst)
            b = 0 - a
            if item >= a or item < (-a):
                return False
            else:
                return self.lst[item]
        else:
            return False

a = SoftList([1,2,3,4,5])

print(a[-100])
