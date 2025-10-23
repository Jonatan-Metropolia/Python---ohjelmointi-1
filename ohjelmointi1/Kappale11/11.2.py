import random

class Auto:
    def __init__(self, rekisteri_tunnus, top_speed):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.top_speed = top_speed
        self.distance = 0
        self.speed = 0


    def change_speed(self):
        delta = random.randint(-10, 30)
        self.speed += delta

        if self.speed > self.top_speed:
            self.speed = self.top_speed
        elif self.speed < 0:
            self.speed = 0


    def kulutus(self, old_distance):
        delta = self.distance - old_distance
        consumed = (delta/100*self.consumption)
        self.capacity = self.capacity - consumed

        if self.capacity < 0:
            over = -self.capacity
            self.capacity = 0

            adjustment = over / consumed

            self.distance -= delta * adjustment


    def move(self, time):
        if self.capacity > 0:
            self.change_speed()

            old_distance = self.distance

            self.distance = self.distance + (self.speed * time)

            self.kulutus(old_distance)



class Ev(Auto):
    def __init__(self, rekisteri_tunnus, top_speed, capacity, consumption):
        super().__init__(rekisteri_tunnus, top_speed)

        self.capacity = capacity
        self.consumption = consumption



class Petrol(Auto):
     def __init__(self, rekisteri_tunnus, top_speed, capacity, consumption):
         super().__init__(rekisteri_tunnus, top_speed)
         self.capacity = capacity
         self.consumption = consumption


aika = 10

auto1 = Ev('ABC-15', 180, 52.5, 7)
auto2 = Petrol('ADC-123', 165, 32.3, 6)

for i in range(aika):
    auto1.move(1)
    auto2.move(1)

print(f'Etäisyys, sähköauto: {auto1.distance}, Virtaa: {auto1.capacity}\n'
      f'Etäisyys bensa auto: {auto2.distance} Bensaa: {auto2.capacity}')

