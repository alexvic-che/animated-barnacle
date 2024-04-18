class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        lst = [int(el) for el in self.func().split()]
        return lst

@InputDigits
def input_dg():
    return input()

res = input_dg()
print(res)