class Hissi:
    def __init__(self, alin, ylin):
        self.bottom = alin
        self.top = ylin
        self.floor = alin

    def move(self, to_floor):
        if self.bottom > to_floor or to_floor > self.top:
            print(f'Syöttämäsi kerros tulee olla {self.bottom}-{self.top}')
            return

        while self.floor != to_floor:
            if self.floor < to_floor:
                self.up()
            elif self.floor > to_floor:
                self.down()

        print(f'Olet kerroksessa {self.floor}')

    def up(self):
        self.floor += 1
        print(f'Kerros {self.floor}.')

    def down(self):
        self.floor -= 1
        print(f'Kerros {self.floor}.')


class Talo:
    def __init__(self, alin, ylin, hissi_määrä):
        self.hissit = []
        for i in range(hissi_määrä):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissi, to_floor):
        if hissi < 1 or hissi > len(self.hissit):
            print(f'Virhe: hissin numeron tulee olla välillä 1–{len(self.hissit)}!')
            return

        chosen_elevator = self.hissit[hissi - 1]
        chosen_elevator.move(to_floor)
        print(f'Liikkunut hissi: {hissi}')


bottom = 0
top = 10
hissien_määrä = 5
talo = Talo(bottom, top, hissien_määrä)

print('Tyhjä merkkijono lopettaa ohjelman!')
while True:
    valittu_hissi = input(f'Aja hissiä 1–{hissien_määrä}: ')
    if valittu_hissi == "":
        break
    kerros = input(f'Mihin kerrokseen haluat mennä? ({bottom}–{top}): ')
    if kerros == "":
        break

    try:
        valittu_hissi = int(valittu_hissi)
        kerros = int(kerros)
    except ValueError:
        print('Syötä kokonaisluku!')
        continue

    talo.aja_hissiä(valittu_hissi, kerros)
