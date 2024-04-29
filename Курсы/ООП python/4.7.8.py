class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias * other
        return obj



class Linear(Function):
    def __init__(self,*args):
        super().__init__()
        if len(args) == 2:
            k,b = args
            self._k = k
            self._b = b
        if len(args)== 1:
            obj = args[0]
            if isinstance(obj, Linear):
                self._k = obj._k
                self._b = obj._b
    def _get_function(self, x):
        y = self._k * x + self._b
        return y