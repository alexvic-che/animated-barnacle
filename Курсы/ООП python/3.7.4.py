import sys


class Player:
    def __init__(self,name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return bool(self.score)

lst_in = list(map(str.strip, sys.stdin.readlines()))

players = []

for el in lst_in:
    name, old, score = el.split("; ")
    players.append(Player(name, old, int(score)))

players_filtered = list(filter(bool, players))

