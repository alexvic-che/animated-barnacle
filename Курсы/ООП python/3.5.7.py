class Body:
    def __init__(self,name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.m = ro * volume

    def __eq__(self, other):
        sc = other if type(other) in (int, float) else other.m
        return self.m == sc
    def __lt__(self, other):
        sc = other if type(other) in (int, float) else other.m
        return self.m < sc