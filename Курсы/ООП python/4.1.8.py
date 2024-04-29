class Validator:

    def _is_valid(self, data):
        return True

    def __call__(self, data):
        if self._is_valid(data):
            return True
        else:
            raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    def __init__(self,min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, int) and self.min_value<=data<=self.max_value:
            return True
        else:
            return False


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) in (float, int) and self.min_value<=data<=self.max_value:
            return True
        else:
            return False


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(0.5)