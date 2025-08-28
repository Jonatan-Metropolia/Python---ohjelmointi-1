import random
stop=0
piste=0

n = (input("Montako kierrosta haluat pelata?"))

while n != "":
    if n !="":
        N = int(n)
        while stop < N:
            if n !="":
                x=random.randint(1,10)
                y=random.randint(1,10)
                vastaus = x*y


                pelaaja = int(input(f"{x}*{y}=?"))

                if pelaaja == vastaus:
                    piste = piste +1
                    print("Oikein!")
                else:
                    print("Väärin :(")
                    print(f"{x}*{y}="+str(vastaus))

                stop = stop + 1

        if n !="":
            if piste !=N:
             print(f"Sait {piste} pistettä (max {n} pistettä)")
            else:
                print("Hurraa, sait kaikki oikein!")

        n = input('Jos haluat pelata uuden kierroksen niin kirjoita vain kierrosten luku määrä, sulkeaksesi ohjelma paina "ENTER"')
        stop=0
        piste=0
