import random
arvoitus= (random.randint(1,10))
oikein=1
pelaajan_arvaus = input("Arvaa lukuni väliltä 1-10")
while oikein==1:

    arvoitus2 = int(arvoitus)
    if int(pelaajan_arvaus) < int(arvoitus2):
        pelaajan_arvaus = input("Lukuni on suurempi")
    elif int(pelaajan_arvaus) > int(arvoitus2):
        pelaajan_arvaus = input("Lukuni on pienempi")
    elif int(pelaajan_arvaus) == arvoitus2:
        print("Oikein!")
        oikein=0

