from random import randint, choice
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        psw = ""
        length = randint(self.min_length, self.max_length)
        while len(psw) != length:
            psw += choice(self.psw_chars)
        return psw

rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)

lst_pass = [rnd() for i in range(3)]
print(*lst_pass)

def RanPas(psw_chars, min_length, max_length):
    def rndd():
        psw = ""
        length = randint(min_length, max_length)
        while len(psw) != length:
            psw += choice(psw_chars)
        return psw
    return rndd


rn = RanPas("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)

lst_pass = [rn() for i in range(3)]
print(*lst_pass)