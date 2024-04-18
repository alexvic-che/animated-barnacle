class RadiusVector:
    def __init__(self, mer = 0, *args):
        if args:
            self.coords = [mer] + list(args)

        else:
            self.coords = [0]*mer

    def set_coords(self,*args):
        if len(args) == len(self.coords):
            for i, coord in enumerate(args):
                self.coords[i] = coord
        elif len(args) > len(self.coords):
            for i in range(len(self.coords)):
                self.coords[i] = args[i]
        elif len(args) < len(self.coords):
            for i in range(len(args)):
                self.coords[i] = args[i]
    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        sum_2_cord = 0
        len_rv = 0
        for coord in self.coords:
            sum_2_cord += coord**2
        len_rv = sum_2_cord**0.5
        return len_rv



vector3D = RadiusVector(3)
print(vector3D.coords)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.coords)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)
print(vector3D.coords)# ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)
print(vector3D.coords)# ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
print(res_len)
res_abs = abs(vector3D)
print(res_abs)

