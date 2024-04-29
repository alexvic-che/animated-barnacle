class Digit:
    def __init__(self, value):
        if not type(value) in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value

class Integer(Digit):
    def __init__(self, value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Float(Digit):
    def __init__(self, value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)
class Positive(Digit):
    def __init__(self, value):
        if value <=0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)
class Negative(Digit):
    def __init__(self, value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class PrimeNumber(Integer, Positive):
    pass

class FloatPositive(Float, Positive):
    pass

digits = [PrimeNumber(1),PrimeNumber(2),PrimeNumber(3),
          FloatPositive(2.2),FloatPositive(5.2),FloatPositive(6.2),FloatPositive(7.2),FloatPositive(8.2),]

lst_positive = list(filter(lambda x: isinstance(x, Positive),digits))
lst_float = list(filter(lambda x: isinstance(x, Float),digits))