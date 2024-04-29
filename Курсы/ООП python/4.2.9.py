class IteratorAttrs:
    __lst = None
    __i = -1
    def __iter__(self):
        IteratorAttrs.__i = -1
        lst = []
        for key, value in self.__dict__.items():
            lst.append((key, value))
        IteratorAttrs.__lst = tuple(lst)
        return iter(IteratorAttrs.__lst)

    def __next__(self):
        if not IteratorAttrs.__lst is None:
            IteratorAttrs.__i+=1
            return IteratorAttrs.__lst[IteratorAttrs.__i]

class SmartPhone(IteratorAttrs):
    def __init__(self,model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory
phone = SmartPhone('model', 'siasdae', 'memory')

for attr, value in phone:
    print(attr, value)