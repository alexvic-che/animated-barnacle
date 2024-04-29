class StringDigit(str):
    def __init__(self, string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")

        self.string = string

    def check_string(self,string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        else:
            return string

    def __add__(self, other):
        self.check_string(other)
        new_str = self.string+other
        return StringDigit(new_str)

    def __radd__(self, other):
        self.check_string(other)
        new_str = other + self.string
        return StringDigit(new_str)


sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
print(sd)
sd = "789" + sd # StringDigit: 789123456
print(sd)

