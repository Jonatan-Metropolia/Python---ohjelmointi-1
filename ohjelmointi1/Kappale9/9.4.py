import random
class Auto:
    def __init__(self, speed, top_speed, distance, rg_number):
        self.speed = float(speed)
        self.top_speed = float(top_speed)
        self.distance = float(distance)
        self.rg_number = str(rg_number)


    def change_speed(self, delta_speed):
        self.speed = self.speed + delta_speed

        if self.speed > self.top_speed:
            self.speed = self.top_speed
        elif self.speed < 0:
            self.speed = 0

    def drive(self, time):
        self.distance = self.distance + self.speed * time
        return self.distance

    def parameter(self, cars):
        for i in range(len(cars)):
            cars[i].top_speed = random.randint(100, 200)
            return cars[i].top_speed

    def win(self, distance):
        if distance >= 10000:
            return True, self
        else:
            return False, self

    def speed_gain(self):
        speed = random.randint(-10, 15)
        return speed

    def score_add(self, cars):

        for i in range(10):
            cars.sort(key=lambda auto: auto.distance)
            print('Kuljettu matka:',cars[i].distance,'nopeus:',cars[i].speed,'Huippu nopeus:', cars[i].top_speed, 'rekisteri numero:',cars[i].rg_number)




top_speed = 147
speed = 0
distance = 0
lap = 0
score_board = {}
auto=Auto(speed, top_speed, distance, 'ABC-1')
cars = []

for i in range(1,11):
    rg_num = 'ABC-'+str(i)
    auto=Auto(speed, top_speed, distance, rg_num)
    cars.append(auto)

win= False
while win ==False:
    for i in range(10):
        top_speed = cars[i].parameter(cars)
        cars[i].top_speed = top_speed

        speed_delta = auto.speed_gain()

        cars[i].change_speed(speed_delta)
        distance = cars[i].drive(1)
        win, car= cars[i].win(distance)

        lap +=1
        if win == True:
            print(f'{cars[i].rg_number}, voitti kilpailun\n'
                  f'Saavuttamalla {cars[i].distance}km\n'
                  f'{lap}. Kierroksella')

            score_board = auto.score_add(cars)
            print(score_board)
            break

