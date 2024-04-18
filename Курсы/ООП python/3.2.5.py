class DigitRetrieve:
    def __call__(self,number, *args, **kwargs):
        if number.isdigit():
            return int(number)
        elif number[0] == '-' and number[1:].isdigit():
            return -int(number[1:])
        else:
            return None



dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)

