class Auto:
    def __init__(self, tunnus, nopeus):
        self.tunnus = tunnus
        self.nopeus = nopeus


tunnus = str(input('Rekisterinumero:'))
nopeus = float(input('Nopeus:'))

auto = Auto(tunnus, nopeus)

print(f'Auton rekisterinumero on {auto.tunnus}, ja nopeus {auto.nopeus}km/h')

