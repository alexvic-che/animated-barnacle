class FloatValidator:
    def __init__(self,min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
    def __call__(self, value):
        if type(value) != float:
            raise ValueError('значение не прошло валидацию')
        if not self.min_value<=value<=self.max_value:
            raise ValueError('значение не прошло валидацию')
        return True
class IntegerValidator:
    def __init__(self,min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
    def __call__(self, value):
        if type(value) != int:
            raise ValueError('значение не прошло валидацию')
        if not self.min_value<=value<=self.max_value:
            raise ValueError('значение не прошло валидацию')
        return True

def is_valid(lst, validators):
    valid_lst = []
    for el in lst:
        for v in validators:
            try:
                v(el)
                valid_lst.append(el)
                break
            except:
                continue
    return valid_lst

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])
print(lst_out)# [1, 4.5]