class Auto:
    def __init__(self, num, speed, top_speed, distance):
        self.num = tunnus
        self.speed = nopeus
        self.top_speed = huippu
        self.distance = distance


tunnus = input('Rekisterinumero:')
nopeus = input('Nopeus:')
huippu = input('Huippu nopeus:')
matka = input('Kuljettu matka:')


auto = Auto(tunnus, nopeus, huippu, matka)

print(f'Autontiedot:\n{tunnus}\n{nopeus}\n{huippu}\n{matka}')

