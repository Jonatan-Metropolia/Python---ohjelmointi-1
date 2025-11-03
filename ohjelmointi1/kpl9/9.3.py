class Auto:
    def __init__(self, speed, top_speed, distance, rg_number):
        self.speed = float(speed)
        self.top_speed = float(top_speed)
        self.distance = float(distance)
        self.rg_number = str(rg_number)


    def change_speed(self, delta_speed):
        self.speed = self.speed + delta_speed

        if self.speed > top_speed:
            self.speed = top_speed
        elif self.speed < 0:
            self.speed = 0

    def drive(self, time):
        self.distance = self.distance + self.speed * time

top_speed = 147
speed = 0
distance = 0
rg_num = "ABC-123"

auto = Auto(speed, top_speed, distance, rg_num)

auto.change_speed(60)



auto.drive(1.5)
print(auto.speed, "km/h")
print(auto.distance, "km")