class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Ошибка: нельзя создавать объекты абстрактного класса"


class SingletonFive:
    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = super().__new__(cls)

        return cls.__isinstance
    
    def __del__(self):
        SingletonFive.__isinstance = None

    def __init__(self, name):
        self.name = name



