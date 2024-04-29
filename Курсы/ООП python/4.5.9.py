import pytest
class Track:
    def __init__(self, *args):
        if len(args) == 2 and not (isinstance(args[0], PointTrack) and isinstance(args[1], PointTrack) ):
            start_x , start_y = args
            self.__points = [PointTrack(start_x , start_y)]
        else:
            for el in args:
                if isinstance(el, PointTrack):
                    continue
                else:
                    TypeError('координаты должны быть числами')
            self.__points = [*args] if args else []

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self,pt):
        self.__points.append(pt)
    def add_front(self,pt):
        self.__points.insert(0, pt)
    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)

class PointTrack:
    def __init__(self,x, y):
        if not type(x) in (int, float):
            raise TypeError('координаты должны быть числами')
        if not type(y) in (int, float):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"

@pytest.mark.parametrize('arguments', [
    (15, -12.3),
    (PointTrack(0.23, -54), PointTrack(-1, 101),),
    (PointTrack(0.23, -54),),
])
def test_track_class_structure(arguments):
    assert hasattr(Track, "points")
    assert type(getattr(Track, "points")) is property
    assert hasattr(Track, 'add_back')
    assert callable(getattr(Track, 'add_back'))
    assert hasattr(Track, 'add_front')
    assert callable(getattr(Track, 'add_front'))
    assert hasattr(Track, 'pop_back')
    assert callable(getattr(Track, 'pop_back'))
    assert hasattr(Track, 'pop_front')
    assert callable(getattr(Track, 'pop_front'))

    tr = Track(*arguments)
    assert hasattr(tr, "points")
    assert type(getattr(tr, "points")) is tuple

def test_point_track_class_structure():
    pt = PointTrack(-12, 22.43)
    assert hasattr(pt, 'x')
    assert hasattr(pt, 'y')
    with pytest.raises(TypeError) as ex:
        pt_error = PointTrack(-11, [22, 4, 7])
    assert 'координаты должны быть числами' in str(ex.value)
    assert str(pt) == f"PointTrack: -12, 22.43"

