class TriangleChecker:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if int(self.a) <=0 or int(self.c)<=0 or int(self.b)<=0 or type(self.a) not in (int, float) or type(self.b) not in (int, float) or type(self.c) not in (int, float):
            return 1
        elif self.a+self.b>self.c and self.a+self.c>self.b and self.c+self.b>self.a:
            return 3
        else:
            return 2

a, b, c = map(int, input().split())

tr = TriangleChecker(a,b,c)

print(tr.is_triangle())