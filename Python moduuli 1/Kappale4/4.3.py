pienin = 2147483647
suurin = -2147483647
tarkistus=1
while tarkistus == True:
    arvo = input("Anna luku")
    if arvo == "":
        tarkistus = False
    if arvo != "":

        luku = float(arvo)

        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

if pienin != 2147483647 or suurin != -2147483647:
    print(f"Pienin luku = {pienin}")
    print(f"Suurin luku = {suurin}")
else:
    print("Et antanut lukua, kokeile uudelleen.")

