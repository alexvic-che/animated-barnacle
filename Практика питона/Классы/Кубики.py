from random import randint
class Die():
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        number =  randint(1, self.sides)
        return number


die = Die()
di2 = Die(10)
di3 = Die(20)
x=1
while x<=10:
    print(di3.roll_die())


    x+=1

