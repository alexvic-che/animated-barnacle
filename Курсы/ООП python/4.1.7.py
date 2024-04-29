class Singleton:
    __is_instance =None
    name = ""

    def __new__(cls, *args, **kwargs):
        if cls.__is_instance == None:
            cls.__is_instance = super().__new__(cls)
        return cls.__is_instance

    def __del__(self):
        Singleton.__is_instance = None
        Singleton.name = ""

class Game(Singleton):
    def __init__(self, name):
        if not Singleton.name:
            Singleton.name = name
            self.name = name





