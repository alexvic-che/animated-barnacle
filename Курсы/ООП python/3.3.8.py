class DeltaClock:

    def __init__(self,clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        time = self.clock1.get_time() - self.clock2.get_time()
        if time < 0:
            return f"00: 00: 00"
        if time < 60:
            seconds = str(time).rjust(2, "0")
            return f"00: 00: {seconds}"
        if 60<=time<3600:
            minutes = str(int((time % 3600) / 60)).rjust(2, "0")
            seconds = str(time % 3600 % 60).rjust(2, "0")
            return f"00: {minutes}: {seconds}"
        if time >= 3600:
            hours = str(int(time/3600)).rjust(2, "0")
            minutes = str(int((time%3600)/60)).rjust(2, "0")
            seconds = str(time%3600%60).rjust(2, "0")
            return f"{hours}: {minutes}: {seconds}"

    def __len__(self):
        time = self.clock1.get_time() - self.clock2.get_time()
        if time<0:
            return 0
        else:
            return time



class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours =hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(1, 0, 0), Clock(2, 0, 0))
print(dt) # 01: 30: 00
a = str(dt)
print(a)
len_dt = len(dt) # 5400
print(dt) # 01: 30: 00

print(len_dt)

