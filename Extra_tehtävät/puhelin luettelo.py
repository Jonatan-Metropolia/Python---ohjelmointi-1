puhelinluettelo = {"Anna": "050 1476297",
                    "Pekka": "040 9873987",
                    "Jonatan": "030 7892723"}
def lisays():
        nimi = input("Henkilön nimi")
        puh = input("Puhelin numero")
        puhelinluettelo[nimi] = puh

def etsinta():
    nimi = input("Kenen numeron haluat tietää?")
    if nimi in puhelinluettelo:
        print(f"Henkilön {nimi} puh on {puhelinluettelo[nimi]}")
    else:
        print('Nimeä ei ole listalla, voit lisätä sen painamalla "2"')


loop = True
while loop==True:
    print("Valitse mitä haluat tehdä\n"
          "1. Lisää nimiä puhelin luetteloon\n"
          "2. Etsi puhelinnumeroita listalta\n"
          "3. Sulje ohjelma")

    valinta = int(input(""))

    if valinta == 1:
        lisays()
    elif valinta == 2:
        etsinta()
    elif valinta == 3:
        loop = False
    else:
        print('Wrong input, answer only with "1", "2" or "3"')

