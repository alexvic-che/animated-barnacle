class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.track = []

    def add_track(self, tr):
        self.track.append(tr)

    def get_tracks(self):
        return self.track

    def __len__(self):
        if not self.track:
            return 0
        length = 0
        xa = self.start_x
        ya = self.start_y
        for i in range(len(self.track)):
            ab = (((self.track[i].to_x - xa)**2)+((self.track[i].to_y - ya)**2))**0.5
            xa = self.track[i].to_x
            ya = self.track[i].to_y
            length += ab
        return int(length)


    def __eq__(self, other):
        sc = other if type(other) == int else len(other)
        return self.__len__() == sc

    def __lt__(self, other):
        sc = other if type(other) == int else len(other)
        return self.__len__() < sc
class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 100))
print(len(track1))
print(len(track2))
res_eq = (track1 != track2)
print(res_eq)



