import time
class Hissi:
    def __init__(self, alin, ylin):
        self.bottom= alin
        self.top = ylin
        self.floor = alin


    def move(self, to_floor):

        if self.bottom > to_floor or to_floor > self.top:
            print(f'syöttämäsi kerros tulee olla {self.bottom}-{self.top}')
            return

        while self.floor is not to_floor:
            if self.floor < to_floor:
                self.up(to_floor)
            elif self.floor > to_floor:
                self.down(to_floor)

        print(f'Olet kerroksessa {self.floor}')

    def up(self, to_floor):
        self.floor +=1
        print(f'Kerros {self.floor}.')

    def down(self, to_floor):
        self.floor -=1
        print(f'Kerros {self.floor}.')


class Talo:
    def __init__(self, alin, ylin, hissi_määrä):
        self.hissit = []

        for i in range(hissi_määrä):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissi, to_floor):
        if hissi < 1 or hissi > len(self.hissit):
            print(f'Valitse hissi väliltä 1-{len(self.hissit)}')
            return

        chosen_elevator = self.hissit[hissi-1]
        chosen_elevator.move(to_floor)
        print(f'Liikkunut hissi: {hissi}')

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.move(1)






bottom = 1
top = 10

hissien_määrä=5

talo = Talo(bottom, top, hissien_määrä)

for i in range(3):
    valittu_hissi = input(f'Aja hissiä 1-{hissien_määrä}')
    kerros = input(f'Minne kerrokseen haluat mennä? ({bottom}-{top})')

    try:
        valittu_hissi = int(valittu_hissi)
        kerros = int(kerros)
    except ValueError:
        print('Syötä kokonais luku!')
        continue

    talo.aja_hissiä(valittu_hissi, kerros)

print('Tulipalo!!!!')
for i in range (3):
    print(i+1,'.')
    time.sleep(1)

talo.palohälytys()

for i, hissi in enumerate(talo.hissit, start=1):
    print(f'{i}. Hissin kerros:',hissi.floor)