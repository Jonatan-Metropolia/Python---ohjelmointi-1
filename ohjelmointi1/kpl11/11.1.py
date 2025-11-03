class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivu_määrä):
        self.kirjoittaja = kirjoittaja
        self.sivu_määrä = sivu_määrä

        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f'Nimi:{self.nimi}\n'
              f'Kirjailija:{self.kirjoittaja}\n'
              f'Sivu määrä:{self.sivu_määrä}')


class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}\n'
              f'Päätoimittaja: {self.päätoimittaja}')

julkaisut = []

julkaisut.append(Kirja('Hytti n:o 6', 'Rosa Liksom', 200))
julkaisut.append(Lehti('Aku Ankka', 'Aki Hyyppä'))

for julkaisu in julkaisut:
    julkaisu.tulosta_tiedot()

