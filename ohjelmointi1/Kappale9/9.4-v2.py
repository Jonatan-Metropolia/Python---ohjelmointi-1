import random

class Car:
    def __init__(self, register, top_speed):
        self.register = register
        self.top_speed = top_speed
        self.speed = 0
        self.distance = 0

    def change_speed(self):
        delta = random.randint(-10, 15)
        self.speed = self.speed + delta

        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.top_speed:
            self.speed = self.top_speed

    def move(self, time):
        self.distance = (self.speed * time) + self.distance

        if self.distance >= 10000:
            return True
        return None


car_list = []
amount = 10
time = 1
lap_counter=0
winner = None


for i in range(amount):
    top_speed = random.randint(100, 200)
    auto = Car(f'ABC-{i+1}', top_speed)

    car_list.append(auto)

input(f'Kisassa on mukana {amount}. autoa!\n'
      f'Syötä mikätahansa merkki jatkaaksesi.')

while winner == None:
    for i in range(amount):
        car_list[i].change_speed()

        win = car_list[i].move(time)

        if win == True and winner is None:
            winner = car_list[i]

    lap_counter += 1

car_list.sort(key=lambda car: car.distance, reverse=True)

print(f'Kisa on päättynyt, ja kesti {lap_counter} kierrosta.\n'
      f'{"Sija":<5} {"Rekisteri":<10} {"Matka (km)":<15}{"Huippunopeus":<20}')

for i in range(amount):
    print(f'{i+1:<5} {car_list[i].register:<10} {car_list[i].distance:<15} {car_list[i].top_speed:<20}')
