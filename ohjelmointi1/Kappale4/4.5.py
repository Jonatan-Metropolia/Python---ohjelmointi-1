yritykset = 0
while yritykset<5:
    sala_sana_tarkistus = 0
    käyttäjä_tunnus_tarkistus = 0
    sala_sana = input(str("Anna sala sana:"))
    käyttäjä_tunnus = input(str("Anna käyttäjä tunnus:"))
    if sala_sana == str("jonatan"):
        sala_sana_tarkistus = 1
    if käyttäjä_tunnus == str("gomes"):
        käyttäjä_tunnus_tarkistus = 1
    pääsy_oikeus = sala_sana_tarkistus+käyttäjä_tunnus_tarkistus
    if pääsy_oikeus == 2:
        yritykset = yritykset + 5
        print("Tervetuloa")
    yritykset = yritykset + 1

if pääsy_oikeus !=2:
    print("Pääsy evätty")
