from cmath import sqrt


class PathLines:
    def __init__(self,*args):
        if args:
            self.path =[LineTo(0,0),*args]
        else:
            self.path =[]
    def get_path(self):
        return self.path

    def add_line(self, line):
        if not self.path:
            self.path.append(LineTo(0, 0))
            self.path.append(line)
        self.path.append(line)

    def get_length(self):
        res = 0
        back_line = 0
        for line in self.path:
            if self.path[0] == line:
                back_line = line
                continue
            L = (((line.x - back_line.x)**2) + ((line.y-back_line.y)**2))**0.5
            back_line = line
            res += L
        return res
class LineTo:

    def __init__(self,x,y):
        self.x = x
        self.y = y

p = PathLines(LineTo(10, 20), LineTo(10, 30))
print(p.get_path())
p.add_line(LineTo(20, -10))
print(p.get_path()[3].x, end=" ")
print(p.get_path()[3].y)
dist = p.get_length()
print(dist)