class SingletonFive:
    __is_instance = None
    a = 0
    def __new__(cls, *args, **kwargs):
        if cls.a < 5:
            cls.__is_instance = super().__new__(cls)
            cls.a += 1
        return cls.__is_instance
    def __init__(self,name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]

print(objs)