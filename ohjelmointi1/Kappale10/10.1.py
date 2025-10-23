class Hissi:
    def __init__(self, alin, ylin):
        self.top = ylin
        self.bottom = alin
        self.floor= alin

    def siirry_kerrokseen(self, to_floor):

        if to_floor > self.top or to_floor < self.bottom:
            print(f'Voit mennä vain kerrokseen {self.bottom}-{self.top}')
            return None

        if self.floor < to_floor:
            self.kerros_ylös(to_floor)
        elif self.floor > to_floor:
            self.kerros_alas(to_floor)
        elif self.floor == to_floor:
            print('Olet haluamassasi kerroksessa!')


    def kerros_ylös(self, to_floor):

        while self.floor is not to_floor:
            new_floor = self.floor+1

            if new_floor <= self.top:
                self.floor +=1
                print(f'{self.floor}. kerros')

    def kerros_alas(self, to_floor):
        while self.floor is not to_floor:

            new_floor = self.floor-1

            if self.floor-1 >= self.bottom:
                self.floor -= 1
                print(f'{self.floor}. kerros')


h=Hissi(0,20)

while True:
    kerrokseen = input('Minne kerrokseen haluat mennä?  (Syötä tyhjä merkkijono pysäyttääksesi)')
    if kerrokseen == '':
        break

    try:
        kerrokseen = int(kerrokseen)
        h.siirry_kerrokseen(kerrokseen)
    except ValueError:
        print('syötä kokonaisluku')