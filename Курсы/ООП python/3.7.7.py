class Ellipse:
    def __init__(self,x1=None, y1=None, x2=None, y2=None):
        if None not in (x1,x2,y1,y2):
            self.x1 = x1
            self.y1 = y1
            self.y2 = y2
            self.x2 = x2
            self.coords = (self.x1,self.y1,self.x2, self.y2)
        else:
            self.coords = ()

    def __bool__(self):
        return bool(self.coords)

    def get_coords(self):
        if not bool(self):
            raise AttributeError('нет координат для извлечения')
        return self.coords

lst_geom = [Ellipse(),Ellipse(),Ellipse(1,1,1,1), Ellipse(1,1,1,1)]

for el in lst_geom:
    if bool(el):
        el.get_coords()