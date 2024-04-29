class Triangle:
    def __init__(self,a, b, c):
        if not type(a) in (int, float):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if not type(b) in (int, float):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if not type(c) in (int, float):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if a<0 or b<0 or c<0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        if a+b<c or a+c<b or c+b<a:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')
        self._a = a
        self._b = b
        self._c = c
input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []

for el in input_data:
    try:
        lst_tr.append(Triangle(*el))
    except:
        continue
print(lst_tr)



