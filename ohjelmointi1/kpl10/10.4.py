import random
import time



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
        self.change_speed()

        self.distance = (self.speed * time) + self.distance




class Kilpailu:
    def __init__(self, nimi, car_list):
        self.nimi = nimi
        self.distance = auto.distance
        self.car_list = car_list

    def tunti_kului(self, aika):
        for car in self.car_list:
            car.move(aika)

    def tulosta_tilanne(self, lap_counter):

        print("\x1b[2J")

        self.car_list.sort(key=lambda car: car.distance, reverse=True)
        print('\n'*25)
        print(f'Kierros {lap_counter}.\n'
              f'{"Sija":<5} {"Rekisteri":<10} {"Matka (km)":<15}{"Nopeus (km/h)":<20}{"Huippunopeus (km/h)":<30}')
        for i in range(amount):
            print(f'{i + 1:<5} {self.car_list[i].register:<10} {self.car_list[i].distance:<15}{self.car_list[i].speed:<20}{self.car_list[i].top_speed:<30}')

        return lap_counter+1

    def kilpailu_ohi(self, target):

        for car in self.car_list:
            if car.distance >= target:
                print('Kisa on päättynyt!\n'
                      f'Voittaja on {car.register}')
                return True

        return False

car_list = []
amount = 10
lap_time = 1
lap_counter=0
target = 8000
win = False

for i in range(amount):
    top_speed = random.randint(100, 200)
    auto = Car(f'ABC-{i+1}', top_speed)
    car_list.append(auto)
kilpailu = Kilpailu('Suuri romuralli', car_list)


input(f'Kisassa {kilpailu.nimi} on mukana {amount}. autoa!\n'
      f'Syötä mikätahansa merkki jatkaaksesi.')

while win is False:
    time.sleep(0.8)

    kilpailu.tunti_kului(lap_time)
    lap_counter = kilpailu.tulosta_tilanne(lap_counter)
    win = kilpailu.kilpailu_ohi(target)

