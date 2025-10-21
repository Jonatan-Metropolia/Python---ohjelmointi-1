class Auto:
    def __init__(self, number, speed, top, dist):
        self.number = number
        self.speed = speed
        self.top = top
        self.dist = dist

    def kiihdyta(self, muutos):
        self.speed = self.speed + muutos

        if self.speed > self.top:
            self.speed = self.top
        elif self.speed <= 0:
            self.speed = 0


auto = Auto('ABC-123', 90, 142, 0)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(auto.speed)


auto.kiihdyta(-200)
print(auto.speed)
